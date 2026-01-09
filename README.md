# FrenchFlow - Personal French Language Learning Application

A comprehensive, self-hosted French language learning application designed for a native English speaker with fluent Spanish skills, progressing from CEFR A1 to C2.

## Overview

FrenchFlow is a personal language learning platform that:
- Follows the CEFR framework (A1 → A2 → B1 → B2 → C1 → C2)
- Leverages Spanish-French cognates and similarities to accelerate learning
- Provides varied exercises: vocabulary, grammar, listening, speaking, reading
- Runs locally on your home network (Mac Mini server)
- Accessible from any device on your LAN (MacBook, iPhone, etc.)

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         Client Devices                          │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐   │
│  │   iPhone     │  │   MacBook    │  │      Mac Mini        │   │
│  │   Safari     │  │   Safari     │  │   Safari/Chrome      │   │
│  └──────┬───────┘  └──────┬───────┘  └──────────┬───────────┘   │
│         │                 │                      │               │
│         └─────────────────┼──────────────────────┘               │
│                           │ HTTP (LAN)                           │
│                           ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                    Mac Mini Server                          │ │
│  │  ┌───────────────────────────────────────────────────────┐  │ │
│  │  │              React Frontend (Port 3000)               │  │ │
│  │  │  - Responsive design (mobile + desktop)               │  │ │
│  │  │  - Web Speech API (TTS + Speech Recognition)          │  │ │
│  │  │  - PWA support for iPhone home screen                 │  │ │
│  │  └───────────────────────────────────────────────────────┘  │ │
│  │                           │                                  │ │
│  │                           ▼ REST API                         │ │
│  │  ┌───────────────────────────────────────────────────────┐  │ │
│  │  │            FastAPI Backend (Port 8000)                │  │ │
│  │  │  - User progress tracking                             │  │ │
│  │  │  - Lesson & exercise management                       │  │ │
│  │  │  - Spaced repetition algorithm                        │  │ │
│  │  │  - Content serving                                    │  │ │
│  │  └───────────────────────────────────────────────────────┘  │ │
│  │                           │                                  │ │
│  │                           ▼                                  │ │
│  │  ┌───────────────────────────────────────────────────────┐  │ │
│  │  │              SQLite Database                          │  │ │
│  │  │  - Vocabulary, Grammar, Exercises                     │  │ │
│  │  │  - User progress & statistics                         │  │ │
│  │  │  - Spaced repetition schedules                        │  │ │
│  │  └───────────────────────────────────────────────────────┘  │ │
│  └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

## Tech Stack

### Backend
- **Python 3.11+** - Main programming language
- **FastAPI** - Modern, fast web framework with automatic API docs
- **SQLAlchemy** - Database ORM
- **SQLite** - Lightweight, file-based database
- **Pydantic** - Data validation

### Frontend
- **React 18** - UI framework
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first CSS framework
- **Vite** - Fast build tool
- **Web Speech API** - Browser-native TTS and speech recognition

## Project Structure

```
French/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI application entry
│   │   ├── config.py            # Configuration settings
│   │   ├── database.py          # Database connection
│   │   ├── models/              # SQLAlchemy models
│   │   │   ├── __init__.py
│   │   │   ├── user.py
│   │   │   ├── vocabulary.py
│   │   │   ├── grammar.py
│   │   │   ├── lesson.py
│   │   │   ├── exercise.py
│   │   │   └── progress.py
│   │   ├── schemas/             # Pydantic schemas
│   │   │   ├── __init__.py
│   │   │   └── ...
│   │   ├── routers/             # API endpoints
│   │   │   ├── __init__.py
│   │   │   ├── lessons.py
│   │   │   ├── exercises.py
│   │   │   ├── vocabulary.py
│   │   │   ├── grammar.py
│   │   │   ├── progress.py
│   │   │   └── practice.py
│   │   ├── services/            # Business logic
│   │   │   ├── __init__.py
│   │   │   ├── spaced_repetition.py
│   │   │   └── exercise_generator.py
│   │   └── seed/                # Initial content data
│   │       ├── __init__.py
│   │       ├── vocabulary_a1.py
│   │       ├── vocabulary_a2.py
│   │       ├── vocabulary_b1.py
│   │       ├── vocabulary_b2.py
│   │       ├── vocabulary_c1.py
│   │       ├── vocabulary_c2.py
│   │       ├── grammar_all.py
│   │       └── seed_database.py
│   ├── requirements.txt
│   └── run.py
│
├── frontend/
│   ├── public/
│   │   ├── manifest.json        # PWA manifest
│   │   └── icons/
│   ├── src/
│   │   ├── components/
│   │   │   ├── common/          # Shared components
│   │   │   ├── exercises/       # Exercise type components
│   │   │   │   ├── VocabularyCard.tsx
│   │   │   │   ├── MultipleChoice.tsx
│   │   │   │   ├── ListeningExercise.tsx
│   │   │   │   ├── SpeakingExercise.tsx
│   │   │   │   ├── ConjugationDrill.tsx
│   │   │   │   ├── GenderPractice.tsx
│   │   │   │   └── SentenceBuilder.tsx
│   │   │   ├── layout/
│   │   │   └── progress/
│   │   ├── hooks/
│   │   │   ├── useSpeechSynthesis.ts
│   │   │   ├── useSpeechRecognition.ts
│   │   │   └── useApi.ts
│   │   ├── pages/
│   │   │   ├── Home.tsx
│   │   │   ├── Practice.tsx
│   │   │   ├── Lessons.tsx
│   │   │   ├── Vocabulary.tsx
│   │   │   ├── Grammar.tsx
│   │   │   └── Progress.tsx
│   │   ├── services/
│   │   │   └── api.ts
│   │   ├── types/
│   │   │   └── index.ts
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   └── index.css
│   ├── package.json
│   ├── tsconfig.json
│   ├── tailwind.config.js
│   └── vite.config.ts
│
├── scripts/
│   ├── start.sh                 # Start both servers
│   ├── setup.sh                 # Initial setup script
│   └── seed.sh                  # Seed database with content
│
├── docker-compose.yml           # Optional: containerized deployment
├── .env.example
└── README.md
```

## CEFR Level Mapping

| Alliance Française | CEFR Level | Description |
|-------------------|------------|-------------|
| A100 - A105 | A1 | Beginner - Basic phrases, introductions |
| A200 - A205 | A2 | Elementary - Simple conversations, daily life |
| B100 - B105 | B1 | Intermediate - Independent speaker |
| B200 - B205 | B2 | Upper Intermediate - Complex texts, fluent |
| C100 - C105 | C1 | Advanced - Proficient, nuanced expression |
| C200 - C205 | C2 | Mastery - Near-native fluency |

## Exercise Types

1. **Vocabulary Flashcards** - Word learning with Spanish cognates highlighted
2. **Multiple Choice** - Translation and fill-in-the-blank
3. **Listening Comprehension** - TTS reads French, user answers questions
4. **Speaking Practice** - User speaks, speech recognition evaluates
5. **Conjugation Drills** - Verb conjugation practice by tense
6. **Gender Practice** - Le/La article identification
7. **Sentence Construction** - Build sentences from word banks
8. **Reading Comprehension** - Read passages, answer questions

## Spanish-French Connection Feature

Since you're fluent in Spanish, the app highlights:
- **Cognates**: Words similar in Spanish and French (e.g., importante/important)
- **False Friends**: Words that look similar but differ (e.g., embarazada ≠ embarrassé)
- **Grammar Parallels**: Similar structures (subjunctive, gendered nouns)
- **Pronunciation Differences**: Key sound differences between Spanish/French

## Quick Start

### Prerequisites
- Python 3.11 or higher
- Node.js 18 or higher
- npm or yarn

### Installation

```bash
# Clone and enter directory
cd French

# Run setup script
chmod +x scripts/setup.sh
./scripts/setup.sh

# Seed the database with French content
./scripts/seed.sh

# Start the application
./scripts/start.sh
```

### Access
- **From Mac Mini**: http://localhost:3000
- **From other devices on LAN**: http://[mac-mini-ip]:3000

## User Profile Configuration

The app is pre-configured for your learning profile:
- **Native Language**: English (US - Minnesota)
- **Secondary Language**: Spanish (Spain - Castilian)
- **Target Language**: French
- **Current Level**: A1 (A100-A105)
- **Focus Areas**: Listening, verb conjugations, gendered nouns, pronunciation

## License

Personal use only. Content sourced from open educational resources.
