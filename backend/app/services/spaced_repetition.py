"""
Spaced Repetition Service using SM-2 algorithm.

The SM-2 algorithm calculates optimal review intervals based on:
- Quality of response (0-5 scale)
- Ease factor (difficulty multiplier)
- Number of successful repetitions
"""
from datetime import datetime, timedelta
from typing import Optional
from sqlalchemy.orm import Session

from ..models.progress import UserProgress, ItemType


class SpacedRepetitionService:
    """
    Implements the SM-2 spaced repetition algorithm.

    Quality ratings:
    0 - Complete blackout, no recall
    1 - Incorrect, but upon seeing answer, remembered
    2 - Incorrect, but answer seemed easy to recall
    3 - Correct with serious difficulty
    4 - Correct after hesitation
    5 - Perfect response
    """

    MIN_EASE_FACTOR = 1.3
    DEFAULT_EASE_FACTOR = 2.5

    @staticmethod
    def calculate_quality(correct: bool, time_taken_seconds: int, used_hint: bool = False) -> int:
        """
        Calculate quality rating based on response.

        Args:
            correct: Whether the answer was correct
            time_taken_seconds: Time taken to answer
            used_hint: Whether user requested a hint

        Returns:
            Quality rating 0-5
        """
        if not correct:
            # Incorrect answers
            if time_taken_seconds < 5:
                return 0  # Quick wrong = complete blackout
            elif time_taken_seconds < 15:
                return 1  # Thought about it but wrong
            else:
                return 2  # Took time but still wrong

        # Correct answers
        if used_hint:
            return 3  # Needed help

        if time_taken_seconds < 3:
            return 5  # Instant recall = perfect
        elif time_taken_seconds < 10:
            return 4  # Quick but not instant
        else:
            return 3  # Correct but slow

    @classmethod
    def calculate_next_review(
        cls,
        quality: int,
        repetitions: int,
        ease_factor: float,
        interval: int
    ) -> dict:
        """
        Calculate the next review parameters using SM-2 algorithm.

        Args:
            quality: Quality of response (0-5)
            repetitions: Number of successful reviews
            ease_factor: Current ease factor
            interval: Current interval in days

        Returns:
            Dictionary with new interval, repetitions, and ease_factor
        """
        if quality < 3:
            # Failed - reset to beginning
            new_repetitions = 0
            new_interval = 1
        else:
            # Success - calculate new interval
            if repetitions == 0:
                new_interval = 1
            elif repetitions == 1:
                new_interval = 6
            else:
                new_interval = round(interval * ease_factor)

            new_repetitions = repetitions + 1

        # Update ease factor based on quality
        new_ease_factor = ease_factor + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
        new_ease_factor = max(cls.MIN_EASE_FACTOR, new_ease_factor)

        return {
            "interval": new_interval,
            "repetitions": new_repetitions,
            "ease_factor": new_ease_factor,
            "next_review": datetime.now() + timedelta(days=new_interval)
        }

    @classmethod
    def update_progress(
        cls,
        db: Session,
        user_id: int,
        item_type: ItemType,
        item_id: int,
        correct: bool,
        time_taken_seconds: int = 0,
        used_hint: bool = False
    ) -> UserProgress:
        """
        Update user progress for an item after a review.

        Args:
            db: Database session
            user_id: User ID
            item_type: Type of item (vocabulary, grammar, etc.)
            item_id: ID of the item
            correct: Whether the answer was correct
            time_taken_seconds: Time taken to answer
            used_hint: Whether user used a hint

        Returns:
            Updated UserProgress object
        """
        # Find or create progress record
        progress = db.query(UserProgress).filter(
            UserProgress.user_id == user_id,
            UserProgress.item_type == item_type,
            UserProgress.item_id == item_id
        ).first()

        if not progress:
            progress = UserProgress(
                user_id=user_id,
                item_type=item_type,
                item_id=item_id,
                ease_factor=cls.DEFAULT_EASE_FACTOR,
                interval=1,
                repetitions=0,
                correct_count=0,
                incorrect_count=0
            )
            db.add(progress)

        # Calculate quality
        quality = cls.calculate_quality(correct, time_taken_seconds, used_hint)

        # Calculate new spaced repetition values
        result = cls.calculate_next_review(
            quality=quality,
            repetitions=progress.repetitions,
            ease_factor=progress.ease_factor,
            interval=progress.interval
        )

        # Update progress
        progress.ease_factor = result["ease_factor"]
        progress.interval = result["interval"]
        progress.repetitions = result["repetitions"]
        progress.next_review = result["next_review"]
        progress.last_reviewed = datetime.now()
        progress.last_quality = quality
        progress.total_time_seconds += time_taken_seconds

        if correct:
            progress.correct_count += 1
        else:
            progress.incorrect_count += 1

        db.commit()
        db.refresh(progress)

        return progress

    @staticmethod
    def get_items_due_for_review(
        db: Session,
        user_id: int,
        item_type: Optional[ItemType] = None,
        limit: int = 50
    ) -> list[UserProgress]:
        """
        Get items that are due for review.

        Args:
            db: Database session
            user_id: User ID
            item_type: Optional filter by item type
            limit: Maximum number of items to return

        Returns:
            List of UserProgress items due for review
        """
        query = db.query(UserProgress).filter(
            UserProgress.user_id == user_id,
            UserProgress.next_review <= datetime.now()
        )

        if item_type:
            query = query.filter(UserProgress.item_type == item_type)

        return query.order_by(UserProgress.next_review).limit(limit).all()

    @staticmethod
    def get_weak_items(
        db: Session,
        user_id: int,
        threshold_accuracy: float = 60.0,
        limit: int = 20
    ) -> list[UserProgress]:
        """
        Get items where user has low accuracy (weak areas).

        Args:
            db: Database session
            user_id: User ID
            threshold_accuracy: Accuracy below this is considered weak
            limit: Maximum number of items to return

        Returns:
            List of weak UserProgress items
        """
        items = db.query(UserProgress).filter(
            UserProgress.user_id == user_id,
            (UserProgress.correct_count + UserProgress.incorrect_count) >= 3  # At least 3 attempts
        ).all()

        # Filter by accuracy (can't do this in SQL easily)
        weak_items = [
            item for item in items
            if item.accuracy < threshold_accuracy
        ]

        # Sort by accuracy (lowest first)
        weak_items.sort(key=lambda x: x.accuracy)

        return weak_items[:limit]
