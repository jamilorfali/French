# FrenchFlow Architecture Documentation

## System Design Philosophy

### Core Principles
1. **Simplicity First** - Easy to understand, maintain, and extend
2. **Offline-Capable** - Works without internet (except initial setup)
3. **Mobile-Friendly** - Responsive design, touch-friendly UI
4. **Spanish Leverage** - Maximize existing Spanish knowledge
5. **Spaced Repetition** - Science-backed retention methodology

## Database Schema

### Entity Relationship Diagram

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│     Users       │     │   CEFRLevels    │     │    Lessons      │
├─────────────────┤     ├─────────────────┤     ├─────────────────┤
│ id (PK)         │     │ id (PK)         │     │ id (PK)         │
│ name            │     │ code (A1-C2)    │     │ cefr_level_id   │──┐
│ native_lang     │     │ name            │     │ unit_number     │  │
│ secondary_lang  │     │ description     │     │ title           │  │
│ current_level   │──┐  │ order           │     │ description     │  │
│ created_at      │  │  └────────┬────────┘     │ objectives      │  │
└─────────────────┘  │           │              └─────────────────┘  │
                     │           │                       │           │
                     └───────────┴───────────────────────┘           │
                                                                     │
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐  │
│   Vocabulary    │     │    Grammar      │     │   Exercises     │  │
├─────────────────┤     ├─────────────────┤     ├─────────────────┤  │
│ id (PK)         │     │ id (PK)         │     │ id (PK)         │  │
│ french          │     │ cefr_level_id   │──┐  │ lesson_id       │──┘
│ english         │     │ topic           │  │  │ type            │
│ spanish         │     │ title           │  │  │ difficulty      │
│ gender (m/f/-)  │     │ explanation_en  │  │  │ content (JSON)  │
│ part_of_speech  │     │ explanation_es  │  │  │ answer (JSON)   │
│ phonetic        │     │ examples        │  │  │ hints           │
│ is_cognate      │     │ spanish_compare │  │  └─────────────────┘
│ cognate_note    │     └─────────────────┘  │
│ cefr_level_id   │──────────────────────────┘
│ category        │
│ example_fr      │     ┌─────────────────┐
│ example_en      │     │  UserProgress   │
│ example_es      │     ├─────────────────┤
└─────────────────┘     │ id (PK)         │
                        │ user_id (FK)    │
┌─────────────────┐     │ item_type       │  (vocabulary/grammar/exercise)
│     Verbs       │     │ item_id         │
├─────────────────┤     │ ease_factor     │  (SM-2 algorithm)
│ id (PK)         │     │ interval        │
│ infinitive      │     │ repetitions     │
│ english         │     │ next_review     │
│ spanish         │     │ last_reviewed   │
│ group (1/2/3)   │     │ correct_count   │
│ is_irregular    │     │ incorrect_count │
│ cefr_level_id   │     └─────────────────┘
│ auxiliary       │
└────────┬────────┘     ┌─────────────────┐
         │              │ PracticeSession │
         ▼              ├─────────────────┤
┌─────────────────┐     │ id (PK)         │
│ VerbConjugation │     │ user_id (FK)    │
├─────────────────┤     │ session_type    │
│ id (PK)         │     │ duration_mins   │
│ verb_id (FK)    │     │ items_practiced │
│ tense           │     │ correct_count   │
│ mood            │     │ started_at      │
│ je              │     │ completed_at    │
│ tu              │     │ focus_areas     │
│ il_elle         │     └─────────────────┘
│ nous            │
│ vous            │
│ ils_elles       │
└─────────────────┘
```

## API Endpoints

### Lessons & Content
```
GET    /api/levels                    # List all CEFR levels
GET    /api/levels/{level_id}/lessons # Get lessons for a level
GET    /api/lessons/{lesson_id}       # Get lesson details
GET    /api/vocabulary                # List vocabulary (filterable)
GET    /api/vocabulary/{id}           # Get vocabulary item
GET    /api/grammar                   # List grammar topics
GET    /api/grammar/{id}              # Get grammar details
GET    /api/verbs                     # List verbs
GET    /api/verbs/{id}/conjugations   # Get verb conjugations
```

### Practice & Exercises
```
POST   /api/practice/start            # Start a practice session
GET    /api/practice/next             # Get next exercise
POST   /api/practice/answer           # Submit answer
POST   /api/practice/complete         # End session
GET    /api/exercises/types           # List exercise types
```

### Progress & Statistics
```
GET    /api/progress                  # Overall progress
GET    /api/progress/level/{level}    # Progress for specific level
GET    /api/progress/weak-areas       # Items needing review
GET    /api/statistics                # Learning statistics
POST   /api/progress/review           # Mark item for review
```

### User
```
GET    /api/user/profile              # Get user profile
PUT    /api/user/profile              # Update profile
PUT    /api/user/settings             # Update settings
```

## Exercise Content Structures (JSON)

### Vocabulary Flashcard
```json
{
  "type": "vocabulary_flashcard",
  "vocabulary_id": 123,
  "show_spanish_hint": true,
  "direction": "fr_to_en"  // or "en_to_fr", "es_to_fr"
}
```

### Multiple Choice
```json
{
  "type": "multiple_choice",
  "question": "What is the French word for 'house'?",
  "options": ["maison", "maçon", "raison", "saison"],
  "correct_index": 0,
  "spanish_hint": "Similar to Spanish 'mansión'"
}
```

### Listening Exercise
```json
{
  "type": "listening",
  "french_text": "Je voudrais un café, s'il vous plaît.",
  "question": "What does the speaker want?",
  "options": ["coffee", "tea", "water", "juice"],
  "correct_index": 0,
  "play_speed": 1.0
}
```

### Speaking Exercise
```json
{
  "type": "speaking",
  "prompt": "Say: 'Bonjour, comment allez-vous?'",
  "expected_text": "Bonjour, comment allez-vous?",
  "phonetic": "bɔ̃.ʒuʁ kɔ.mɑ̃.t‿a.le.vu",
  "english": "Hello, how are you?",
  "spanish": "Hola, ¿cómo está usted?"
}
```

### Conjugation Drill
```json
{
  "type": "conjugation",
  "verb_id": 45,
  "tense": "present",
  "subject": "nous",
  "infinitive": "parler",
  "correct_answer": "parlons",
  "spanish_equivalent": "hablamos"
}
```

### Gender Practice
```json
{
  "type": "gender",
  "noun": "table",
  "correct_article": "la",
  "hint": "Most nouns ending in -e are feminine",
  "spanish_gender": "la mesa (feminine in Spanish too)"
}
```

### Sentence Builder
```json
{
  "type": "sentence_builder",
  "english": "I eat an apple",
  "spanish": "Yo como una manzana",
  "word_bank": ["je", "mange", "une", "pomme", "un", "tu"],
  "correct_order": ["je", "mange", "une", "pomme"]
}
```

## Spaced Repetition Algorithm (SM-2)

The app uses a modified SM-2 algorithm for optimal retention:

```python
def calculate_next_review(quality, repetitions, ease_factor, interval):
    """
    quality: 0-5 (0-2 = incorrect, 3-5 = correct with varying ease)
    """
    if quality < 3:
        # Reset on incorrect
        repetitions = 0
        interval = 1
    else:
        if repetitions == 0:
            interval = 1
        elif repetitions == 1:
            interval = 6
        else:
            interval = round(interval * ease_factor)
        repetitions += 1

    # Adjust ease factor
    ease_factor = max(1.3, ease_factor + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)))

    return {
        'interval': interval,  # days until next review
        'repetitions': repetitions,
        'ease_factor': ease_factor
    }
```

## Frontend Component Architecture

```
App
├── Layout
│   ├── Header (navigation, current level indicator)
│   ├── MobileNav (bottom navigation for iPhone)
│   └── MainContent
│
├── Pages
│   ├── Home
│   │   ├── DailyGoal
│   │   ├── QuickPractice (5/15/30 min options)
│   │   ├── WeakAreasWidget
│   │   └── RecentProgress
│   │
│   ├── Practice
│   │   ├── SessionConfig (duration, focus areas)
│   │   ├── ExerciseContainer
│   │   │   ├── VocabularyCard
│   │   │   ├── MultipleChoice
│   │   │   ├── ListeningExercise
│   │   │   ├── SpeakingExercise
│   │   │   ├── ConjugationDrill
│   │   │   ├── GenderPractice
│   │   │   └── SentenceBuilder
│   │   ├── ProgressBar
│   │   └── SessionSummary
│   │
│   ├── Lessons
│   │   ├── LevelSelector
│   │   ├── LessonList
│   │   └── LessonDetail
│   │
│   ├── Vocabulary
│   │   ├── VocabularyBrowser
│   │   ├── SearchFilter
│   │   └── VocabularyDetail
│   │
│   ├── Grammar
│   │   ├── GrammarTopics
│   │   └── GrammarDetail
│   │
│   └── Progress
│       ├── OverallStats
│       ├── LevelProgress
│       ├── WeakAreas
│       └── History
│
└── Shared Components
    ├── Button
    ├── Card
    ├── Modal
    ├── AudioPlayer
    ├── SpeechButton
    └── LoadingSpinner
```

## Speech Integration

### Text-to-Speech (Web Speech API)
```typescript
const speak = (text: string, lang: 'fr-FR' | 'es-ES' | 'en-US') => {
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = lang;
  utterance.rate = 0.9;  // Slightly slower for learning
  speechSynthesis.speak(utterance);
};
```

### Speech Recognition (Web Speech API)
```typescript
const recognition = new webkitSpeechRecognition();
recognition.lang = 'fr-FR';
recognition.continuous = false;
recognition.interimResults = false;

recognition.onresult = (event) => {
  const transcript = event.results[0][0].transcript;
  const confidence = event.results[0][0].confidence;
  // Compare with expected text
};
```

## Session Flow

### Quick Practice (5-30 minutes)
1. User selects duration (5, 15, or 30 minutes)
2. System calculates ~number of exercises
3. Mix of exercise types based on:
   - Items due for review (spaced repetition)
   - Weak areas (listening, conjugation, gender, pronunciation)
   - New content (20% of session)
4. Progress saved after each answer
5. Summary shown at end

### Focused Practice
1. User selects specific focus:
   - Vocabulary only
   - Conjugation drills
   - Listening practice
   - Speaking practice
   - Gender practice
2. Exercises tailored to focus area
3. Deeper dive into specific weakness

## Content Organization by CEFR Level

### A1 (Beginner) - ~500 vocabulary items
- Basic greetings and introductions
- Numbers 1-100
- Days, months, seasons
- Family members
- Common objects
- Basic adjectives (colors, sizes)
- Present tense verbs (être, avoir, aller, faire, etc.)
- Basic questions (qui, que, où, quand)

### A2 (Elementary) - ~1000 vocabulary items
- Daily routines
- Food and dining
- Shopping
- Transportation
- Weather
- Past tense (passé composé)
- Imperfect tense
- Future simple

### B1 (Intermediate) - ~2000 vocabulary items
- Work and career
- Health and body
- Travel and culture
- Opinions and feelings
- Conditional tense
- Subjunctive (basic)
- Relative pronouns

### B2 (Upper Intermediate) - ~4000 vocabulary items
- Abstract concepts
- News and media
- Environment
- Politics (basic)
- Advanced subjunctive
- Past subjunctive
- Nuanced expressions

### C1 (Advanced) - ~8000 vocabulary items
- Professional contexts
- Literature and arts
- Idiomatic expressions
- Formal vs informal register
- Complex sentence structures
- Nuanced argumentation

### C2 (Mastery) - ~16000 vocabulary items
- Near-native vocabulary
- Rare/literary words
- Regional variations
- Slang and colloquialisms
- Stylistic mastery
