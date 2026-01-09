"""
Exercise Generator Service.

Generates varied exercises based on content and user progress.
"""
import random
from typing import Optional, Any
from sqlalchemy.orm import Session

from ..models import Vocabulary, Grammar, Verb, VerbConjugation, Exercise
from ..models.vocabulary import Gender, PartOfSpeech
from ..models.exercise import ExerciseType, Difficulty


class ExerciseGenerator:
    """Generates exercises dynamically from content."""

    def __init__(self, db: Session):
        self.db = db

    def generate_vocabulary_flashcard(
        self,
        vocabulary: Vocabulary,
        direction: str = "fr_to_en",
        show_spanish: bool = True
    ) -> dict:
        """
        Generate a vocabulary flashcard exercise.

        Args:
            vocabulary: Vocabulary item
            direction: Translation direction (fr_to_en, en_to_fr, es_to_fr)
            show_spanish: Whether to show Spanish hint

        Returns:
            Exercise content dictionary
        """
        content = {
            "type": "vocabulary_flashcard",
            "vocabulary_id": vocabulary.id,
            "direction": direction,
        }

        if direction == "fr_to_en":
            content["prompt"] = vocabulary.french
            content["prompt_phonetic"] = vocabulary.phonetic
            if vocabulary.gender and vocabulary.gender != Gender.NONE:
                article = "le" if vocabulary.gender == Gender.MASCULINE else "la"
                content["prompt"] = f"{article} {vocabulary.french}"
        elif direction == "en_to_fr":
            content["prompt"] = vocabulary.english
        else:  # es_to_fr
            content["prompt"] = vocabulary.spanish

        if show_spanish and vocabulary.is_cognate:
            content["spanish_hint"] = f"Similar to Spanish: {vocabulary.cognate_spanish}"
            if vocabulary.cognate_note:
                content["cognate_note"] = vocabulary.cognate_note

        answer = {
            "french": vocabulary.french,
            "english": vocabulary.english,
            "spanish": vocabulary.spanish,
            "gender": vocabulary.gender.value if vocabulary.gender else None,
        }

        return {"content": content, "answer": answer}

    def generate_multiple_choice(
        self,
        vocabulary: Vocabulary,
        all_vocabulary: list[Vocabulary],
        direction: str = "en_to_fr"
    ) -> dict:
        """
        Generate a multiple choice exercise.

        Args:
            vocabulary: Target vocabulary item
            all_vocabulary: List of all vocabulary for distractors
            direction: Translation direction

        Returns:
            Exercise content dictionary
        """
        # Get distractors (same part of speech, different words)
        distractors = [
            v for v in all_vocabulary
            if v.id != vocabulary.id and v.part_of_speech == vocabulary.part_of_speech
        ]
        random.shuffle(distractors)
        distractors = distractors[:3]

        if direction == "en_to_fr":
            question = f"What is the French word for '{vocabulary.english}'?"
            correct = vocabulary.french
            options = [correct] + [d.french for d in distractors]
        else:
            question = f"What does '{vocabulary.french}' mean?"
            correct = vocabulary.english
            options = [correct] + [d.english for d in distractors]

        random.shuffle(options)
        correct_index = options.index(correct)

        content = {
            "type": "multiple_choice",
            "question": question,
            "options": options,
            "vocabulary_id": vocabulary.id,
        }

        if vocabulary.is_cognate and vocabulary.spanish:
            content["spanish_hint"] = f"Think of Spanish: {vocabulary.spanish}"

        answer = {
            "correct_index": correct_index,
            "correct_answer": correct,
            "explanation": vocabulary.notes,
        }

        return {"content": content, "answer": answer}

    def generate_listening_exercise(
        self,
        vocabulary: Vocabulary
    ) -> dict:
        """
        Generate a listening comprehension exercise.
        The frontend will use TTS to read the French text.

        Args:
            vocabulary: Vocabulary item

        Returns:
            Exercise content dictionary
        """
        content = {
            "type": "listening",
            "french_text": vocabulary.example_french or vocabulary.french,
            "question": "What did you hear? Select the correct translation.",
            "vocabulary_id": vocabulary.id,
            "play_speed": 1.0,
        }

        answer = {
            "french": vocabulary.french,
            "english": vocabulary.english,
            "phonetic": vocabulary.phonetic,
        }

        return {"content": content, "answer": answer}

    def generate_speaking_exercise(
        self,
        vocabulary: Vocabulary
    ) -> dict:
        """
        Generate a speaking practice exercise.
        The frontend will use speech recognition.

        Args:
            vocabulary: Vocabulary item

        Returns:
            Exercise content dictionary
        """
        text_to_say = vocabulary.example_french or vocabulary.french

        content = {
            "type": "speaking",
            "prompt": f"Say: '{text_to_say}'",
            "expected_text": text_to_say,
            "vocabulary_id": vocabulary.id,
            "english": vocabulary.example_english or vocabulary.english,
            "spanish": vocabulary.example_spanish or vocabulary.spanish,
        }

        if vocabulary.phonetic:
            content["phonetic"] = vocabulary.phonetic

        answer = {
            "expected_text": text_to_say,
            "phonetic": vocabulary.phonetic,
        }

        return {"content": content, "answer": answer}

    def generate_conjugation_drill(
        self,
        verb: Verb,
        tense: str = "present",
        subject: Optional[str] = None
    ) -> dict:
        """
        Generate a verb conjugation exercise.

        Args:
            verb: Verb to conjugate
            tense: Tense to practice
            subject: Specific subject pronoun, or random if None

        Returns:
            Exercise content dictionary
        """
        # Get conjugation for this tense
        conjugation = self.db.query(VerbConjugation).filter(
            VerbConjugation.verb_id == verb.id,
            VerbConjugation.tense == tense
        ).first()

        if not conjugation:
            return None

        subjects = {
            "je": conjugation.je,
            "tu": conjugation.tu,
            "il/elle": conjugation.il_elle,
            "nous": conjugation.nous,
            "vous": conjugation.vous,
            "ils/elles": conjugation.ils_elles,
        }

        if subject is None:
            subject = random.choice(list(subjects.keys()))

        correct_answer = subjects.get(subject)
        if not correct_answer:
            return None

        content = {
            "type": "conjugation",
            "verb_id": verb.id,
            "infinitive": verb.infinitive,
            "english": verb.english,
            "tense": tense,
            "subject": subject,
            "prompt": f"Conjugate '{verb.infinitive}' ({verb.english}) for '{subject}' in {tense} tense",
        }

        if verb.spanish:
            content["spanish_verb"] = verb.spanish

        answer = {
            "correct_answer": correct_answer,
            "full_conjugation": subjects,
            "spanish_equivalent": conjugation.spanish_equivalent,
        }

        return {"content": content, "answer": answer}

    def generate_gender_exercise(
        self,
        vocabulary: Vocabulary
    ) -> dict:
        """
        Generate a gender identification exercise.

        Args:
            vocabulary: Noun to identify gender

        Returns:
            Exercise content dictionary
        """
        if vocabulary.part_of_speech != PartOfSpeech.NOUN:
            return None

        if vocabulary.gender in (Gender.NONE, None):
            return None

        correct_article = "le" if vocabulary.gender == Gender.MASCULINE else "la"

        content = {
            "type": "gender",
            "noun": vocabulary.french,
            "english": vocabulary.english,
            "prompt": f"Is it 'le' or 'la' {vocabulary.french}?",
            "options": ["le", "la"],
            "vocabulary_id": vocabulary.id,
        }

        # Add Spanish comparison if helpful
        if vocabulary.spanish:
            spanish_article = "el" if vocabulary.gender == Gender.MASCULINE else "la"
            content["spanish_hint"] = f"In Spanish: {spanish_article} {vocabulary.spanish}"

        # Add pattern hints based on word ending
        ending = vocabulary.french[-2:] if len(vocabulary.french) > 2 else vocabulary.french
        ending_hints = {
            "masculine": ["-age", "-ment", "-eau", "-isme", "-oir"],
            "feminine": ["-tion", "-sion", "-té", "-ure", "-ence", "-ance", "-ie", "-ée"]
        }

        hint = None
        for endings in ending_hints.get("masculine" if vocabulary.gender == Gender.MASCULINE else "feminine", []):
            if vocabulary.french.endswith(endings.replace("-", "")):
                hint = f"Words ending in '{endings}' are usually {'masculine' if vocabulary.gender == Gender.MASCULINE else 'feminine'}"
                break

        if hint:
            content["pattern_hint"] = hint

        answer = {
            "correct_article": correct_article,
            "gender": "masculine" if vocabulary.gender == Gender.MASCULINE else "feminine",
        }

        return {"content": content, "answer": answer}

    def generate_sentence_builder(
        self,
        vocabulary_items: list[Vocabulary],
        sentence_template: Optional[dict] = None
    ) -> dict:
        """
        Generate a sentence building exercise.

        Args:
            vocabulary_items: Vocabulary to use in sentence
            sentence_template: Optional template with sentence structure

        Returns:
            Exercise content dictionary
        """
        # Simple sentence templates
        templates = [
            {
                "french": ["Je", "mange", "une", "pomme"],
                "english": "I eat an apple",
                "spanish": "Yo como una manzana",
            },
            {
                "french": ["Il", "parle", "français"],
                "english": "He speaks French",
                "spanish": "Él habla francés",
            },
        ]

        template = sentence_template or random.choice(templates)

        # Add distractors
        word_bank = template["french"].copy()
        distractors = ["un", "la", "nous", "très", "bien"]
        word_bank.extend(random.sample(distractors, min(2, len(distractors))))
        random.shuffle(word_bank)

        content = {
            "type": "sentence_builder",
            "english": template["english"],
            "spanish": template["spanish"],
            "word_bank": word_bank,
            "prompt": f"Build the sentence: '{template['english']}'",
        }

        answer = {
            "correct_order": template["french"],
            "sentence": " ".join(template["french"]),
        }

        return {"content": content, "answer": answer}

    def generate_exercise_set(
        self,
        user_id: int,
        count: int = 10,
        exercise_types: Optional[list[ExerciseType]] = None,
        cefr_level: str = "A1",
        focus_areas: Optional[list[str]] = None
    ) -> list[dict]:
        """
        Generate a set of varied exercises for a practice session.

        Args:
            user_id: User ID
            count: Number of exercises to generate
            exercise_types: Specific types to include, or all if None
            cefr_level: CEFR level to draw content from
            focus_areas: Specific areas to focus on

        Returns:
            List of exercise dictionaries
        """
        from ..models import CEFRLevel

        # Get CEFR level
        level = self.db.query(CEFRLevel).filter(CEFRLevel.code == cefr_level).first()
        if not level:
            return []

        # Get vocabulary for this level
        vocabulary = self.db.query(Vocabulary).filter(
            Vocabulary.cefr_level_id == level.id
        ).all()

        # Get verbs for this level
        verbs = self.db.query(Verb).filter(
            Verb.cefr_level_id == level.id
        ).all()

        exercises = []

        # Default exercise type distribution
        if exercise_types is None:
            exercise_types = [
                ExerciseType.VOCABULARY_FLASHCARD,
                ExerciseType.MULTIPLE_CHOICE,
                ExerciseType.LISTENING,
                ExerciseType.SPEAKING,
                ExerciseType.CONJUGATION,
                ExerciseType.GENDER,
            ]

        # Adjust based on focus areas
        if focus_areas:
            if "listening" in focus_areas:
                exercise_types.extend([ExerciseType.LISTENING] * 2)
            if "conjugation" in focus_areas:
                exercise_types.extend([ExerciseType.CONJUGATION] * 2)
            if "gender" in focus_areas:
                exercise_types.extend([ExerciseType.GENDER] * 2)
            if "pronunciation" in focus_areas:
                exercise_types.extend([ExerciseType.SPEAKING] * 2)

        for _ in range(count):
            exercise_type = random.choice(exercise_types)
            exercise = None

            if exercise_type == ExerciseType.VOCABULARY_FLASHCARD and vocabulary:
                vocab = random.choice(vocabulary)
                exercise = self.generate_vocabulary_flashcard(vocab)

            elif exercise_type == ExerciseType.MULTIPLE_CHOICE and vocabulary:
                vocab = random.choice(vocabulary)
                exercise = self.generate_multiple_choice(vocab, vocabulary)

            elif exercise_type == ExerciseType.LISTENING and vocabulary:
                vocab = random.choice(vocabulary)
                exercise = self.generate_listening_exercise(vocab)

            elif exercise_type == ExerciseType.SPEAKING and vocabulary:
                vocab = random.choice(vocabulary)
                exercise = self.generate_speaking_exercise(vocab)

            elif exercise_type == ExerciseType.CONJUGATION and verbs:
                verb = random.choice(verbs)
                exercise = self.generate_conjugation_drill(verb)

            elif exercise_type == ExerciseType.GENDER and vocabulary:
                nouns = [v for v in vocabulary if v.part_of_speech == PartOfSpeech.NOUN]
                if nouns:
                    vocab = random.choice(nouns)
                    exercise = self.generate_gender_exercise(vocab)

            if exercise:
                exercise["type"] = exercise_type.value
                exercises.append(exercise)

        return exercises
