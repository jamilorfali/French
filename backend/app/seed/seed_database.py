#!/usr/bin/env python3
"""
Database seeding script.
Populates the database with French learning content for all CEFR levels.
"""
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from sqlalchemy.orm import Session
from app.database import SessionLocal, init_db
from app.models import (
    CEFRLevel, Vocabulary, Grammar, Verb, VerbConjugation, Lesson, User
)
from app.models.vocabulary import Gender, PartOfSpeech
from app.models.verb import VerbGroup, Auxiliary

from app.seed.cefr_levels import CEFR_LEVELS
from app.seed.vocabulary_a1 import VOCABULARY_A1
from app.seed.vocabulary_a2 import VOCABULARY_A2
from app.seed.vocabulary_b1 import VOCABULARY_B1
from app.seed.vocabulary_b2 import VOCABULARY_B2
from app.seed.vocabulary_c1 import VOCABULARY_C1
from app.seed.vocabulary_c2 import VOCABULARY_C2
from app.seed.verbs_a1 import VERBS_A1
from app.seed.verbs_a2 import VERBS_A2
from app.seed.verbs_b1 import VERBS_B1
from app.seed.verbs_b2 import VERBS_B2
from app.seed.verbs_c1 import VERBS_C1
from app.seed.verbs_c2 import VERBS_C2
from app.seed.grammar_a1 import GRAMMAR_A1
from app.seed.grammar_a2 import GRAMMAR_A2
from app.seed.grammar_b1 import GRAMMAR_B1
from app.seed.grammar_b2 import GRAMMAR_B2
from app.seed.grammar_c1 import GRAMMAR_C1
from app.seed.grammar_c2 import GRAMMAR_C2
from app.seed.vocabulary_colloquial import COLLOQUIAL_BY_LEVEL


# All vocabulary by level (includes regular + colloquial)
VOCABULARY_BY_LEVEL = {
    "A1": VOCABULARY_A1 + COLLOQUIAL_BY_LEVEL.get("A1", []),
    "A2": VOCABULARY_A2 + COLLOQUIAL_BY_LEVEL.get("A2", []),
    "B1": VOCABULARY_B1 + COLLOQUIAL_BY_LEVEL.get("B1", []),
    "B2": VOCABULARY_B2 + COLLOQUIAL_BY_LEVEL.get("B2", []),
    "C1": VOCABULARY_C1 + COLLOQUIAL_BY_LEVEL.get("C1", []),
    "C2": VOCABULARY_C2 + COLLOQUIAL_BY_LEVEL.get("C2", []),
}

# All verbs by level
VERBS_BY_LEVEL = {
    "A1": VERBS_A1,
    "A2": VERBS_A2,
    "B1": VERBS_B1,
    "B2": VERBS_B2,
    "C1": VERBS_C1,
    "C2": VERBS_C2,
}

# All grammar by level
GRAMMAR_BY_LEVEL = {
    "A1": GRAMMAR_A1,
    "A2": GRAMMAR_A2,
    "B1": GRAMMAR_B1,
    "B2": GRAMMAR_B2,
    "C1": GRAMMAR_C1,
    "C2": GRAMMAR_C2,
}

# Lessons by level
LESSONS_BY_LEVEL = {
    "A1": [
        {
            "unit_number": 1,
            "title": "Bonjour! Introductions",
            "description": "Learn to greet people and introduce yourself in French.",
            "objectives": [
                "Say hello and goodbye",
                "Introduce yourself",
                "Ask and answer simple questions about identity",
                "Use subject pronouns je, tu, il, elle"
            ],
            "themes": ["greetings", "introductions", "identity"],
            "grammar_topics": ["subject_pronouns", "etre_avoir"],
            "estimated_duration": 45
        },
        {
            "unit_number": 2,
            "title": "Ma famille et moi",
            "description": "Talk about your family and describe people.",
            "objectives": [
                "Name family members",
                "Describe people using basic adjectives",
                "Use possessive adjectives (mon, ma, mes)",
                "Count from 1-20"
            ],
            "themes": ["family", "descriptions", "numbers"],
            "grammar_topics": ["possessive_adjectives", "noun_gender"],
            "estimated_duration": 45
        },
        {
            "unit_number": 3,
            "title": "Les jours et les mois",
            "description": "Learn days of the week, months, and talk about time.",
            "objectives": [
                "Name days of the week",
                "Name months of the year",
                "Talk about dates and schedules",
                "Use time expressions"
            ],
            "themes": ["days", "months", "time"],
            "grammar_topics": ["definite_articles"],
            "estimated_duration": 45
        },
        {
            "unit_number": 4,
            "title": "J'aime, je n'aime pas",
            "description": "Express likes, dislikes, and preferences.",
            "objectives": [
                "Express what you like and don't like",
                "Use -ER verbs in present tense",
                "Form negative sentences with ne...pas",
                "Talk about food and activities"
            ],
            "themes": ["preferences", "food", "activities"],
            "grammar_topics": ["present_tense_er_verbs", "negation", "indefinite_articles"],
            "estimated_duration": 45
        },
        {
            "unit_number": 5,
            "title": "Ou habites-tu?",
            "description": "Talk about where you live and describe places.",
            "objectives": [
                "Describe your home and neighborhood",
                "Use prepositions of place",
                "Talk about cities and countries",
                "Ask and answer questions about location"
            ],
            "themes": ["home", "places", "location"],
            "grammar_topics": ["prepositions_place", "asking_questions"],
            "estimated_duration": 45
        },
        {
            "unit_number": 6,
            "title": "Francais familier - Les bases",
            "description": "Introduction to informal French expressions used in everyday conversation.",
            "objectives": [
                "Understand common filler words (ben, bof, ouais)",
                "Use informal greetings (coucou, salut, bisous)",
                "Recognize the difference between formal and informal French",
                "Respond naturally in casual conversations"
            ],
            "themes": ["colloquial", "greetings", "informal"],
            "grammar_topics": [],
            "estimated_duration": 40,
            "is_colloquial": True
        },
    ],
    "A2": [
        {
            "unit_number": 1,
            "title": "Ma routine quotidienne",
            "description": "Describe your daily routine and activities.",
            "objectives": [
                "Talk about daily activities",
                "Use reflexive verbs",
                "Tell time precisely",
                "Use time expressions (d'abord, ensuite, puis)"
            ],
            "themes": ["daily_routines", "time", "activities"],
            "grammar_topics": ["reflexive_verbs", "time_expressions"],
            "estimated_duration": 45
        },
        {
            "unit_number": 2,
            "title": "Faire les courses",
            "description": "Learn to shop and make purchases in French.",
            "objectives": [
                "Ask for prices and quantities",
                "Use partitive articles (du, de la, des)",
                "Express quantities with numbers",
                "Describe food and products"
            ],
            "themes": ["shopping", "food", "quantities"],
            "grammar_topics": ["partitive_articles", "quantities"],
            "estimated_duration": 45
        },
        {
            "unit_number": 3,
            "title": "Les transports",
            "description": "Navigate transportation and give directions.",
            "objectives": [
                "Ask for and give directions",
                "Talk about different modes of transport",
                "Use the imperative mood",
                "Understand travel vocabulary"
            ],
            "themes": ["transportation", "directions", "travel"],
            "grammar_topics": ["imperative", "prepositions_place"],
            "estimated_duration": 45
        },
        {
            "unit_number": 4,
            "title": "Hier et aujourd'hui",
            "description": "Talk about past events using passe compose.",
            "objectives": [
                "Narrate past events",
                "Use passe compose with avoir",
                "Form past participles",
                "Use time markers for past"
            ],
            "themes": ["past", "events", "time"],
            "grammar_topics": ["passe_compose_avoir", "past_participles"],
            "estimated_duration": 45
        },
        {
            "unit_number": 5,
            "title": "Aller et venir",
            "description": "Master movement verbs and passe compose with etre.",
            "objectives": [
                "Use movement verbs correctly",
                "Apply passe compose with etre",
                "Understand agreement rules",
                "Describe trips and journeys"
            ],
            "themes": ["movement", "travel", "past"],
            "grammar_topics": ["passe_compose_etre", "agreement"],
            "estimated_duration": 45
        },
        {
            "unit_number": 6,
            "title": "Francais familier - La vie quotidienne",
            "description": "Everyday slang for work, food, and social situations.",
            "objectives": [
                "Use informal vocabulary for work (bosser, le boulot)",
                "Learn slang for food and eating (bouffer, la bouffe)",
                "Understand common expressions (un truc, un mec, une meuf)",
                "Express opinions casually (kiffer, nickel, grave)"
            ],
            "themes": ["colloquial", "work", "food", "social"],
            "grammar_topics": [],
            "estimated_duration": 40,
            "is_colloquial": True
        },
    ],
    "B1": [
        {
            "unit_number": 1,
            "title": "Le monde du travail",
            "description": "Discuss work, careers, and professional life.",
            "objectives": [
                "Talk about jobs and careers",
                "Use professional vocabulary",
                "Write a simple CV or cover letter",
                "Discuss work preferences and conditions"
            ],
            "themes": ["work", "career", "professional"],
            "grammar_topics": ["futur_simple", "conditionnel_present"],
            "estimated_duration": 50
        },
        {
            "unit_number": 2,
            "title": "Raconter des souvenirs",
            "description": "Master the imperfect tense for memories and descriptions.",
            "objectives": [
                "Describe past habits and states",
                "Use imparfait for descriptions",
                "Contrast passe compose and imparfait",
                "Tell childhood memories"
            ],
            "themes": ["memories", "past", "descriptions"],
            "grammar_topics": ["imparfait", "passe_compose_vs_imparfait"],
            "estimated_duration": 50
        },
        {
            "unit_number": 3,
            "title": "Exprimer des hypotheses",
            "description": "Make hypotheses and express conditions.",
            "objectives": [
                "Form conditional sentences",
                "Express wishes and regrets",
                "Make polite requests",
                "Use si + imparfait constructions"
            ],
            "themes": ["hypotheses", "conditions", "wishes"],
            "grammar_topics": ["conditionnel_present", "si_clauses"],
            "estimated_duration": 50
        },
        {
            "unit_number": 4,
            "title": "Relier ses idees",
            "description": "Connect ideas using relative pronouns.",
            "objectives": [
                "Use qui, que, ou, dont correctly",
                "Build complex sentences",
                "Avoid repetition in speech",
                "Describe people and things precisely"
            ],
            "themes": ["descriptions", "complex_sentences"],
            "grammar_topics": ["pronoms_relatifs"],
            "estimated_duration": 50
        },
        {
            "unit_number": 5,
            "title": "Exprimer la necessite",
            "description": "Introduction to the subjunctive mood.",
            "objectives": [
                "Use il faut que + subjunctive",
                "Express necessity and desire",
                "Form basic subjunctive conjugations",
                "Recognize subjunctive triggers"
            ],
            "themes": ["obligation", "necessity", "desire"],
            "grammar_topics": ["subjonctif_introduction"],
            "estimated_duration": 50
        },
        {
            "unit_number": 6,
            "title": "Francais familier - Exprimer ses emotions",
            "description": "Express frustration, boredom, and stress like a native speaker.",
            "objectives": [
                "Express frustration (j'en ai marre, ca craint)",
                "Describe difficult situations (la galere, se planter)",
                "Talk about time pressure (etre a la bourre)",
                "Use emphatic expressions (peter un cable, n'importe quoi)"
            ],
            "themes": ["colloquial", "emotions", "frustration", "stress"],
            "grammar_topics": [],
            "estimated_duration": 45,
            "is_colloquial": True
        },
    ],
    "B2": [
        {
            "unit_number": 1,
            "title": "Debattre et convaincre",
            "description": "Present arguments and participate in debates.",
            "objectives": [
                "Express opinions strongly",
                "Use advanced subjunctive triggers",
                "Structure an argument",
                "Respond to opposing viewpoints"
            ],
            "themes": ["debate", "opinion", "argumentation"],
            "grammar_topics": ["subjonctif_advanced"],
            "estimated_duration": 55
        },
        {
            "unit_number": 2,
            "title": "Le monde hypothetique",
            "description": "Master past conditional and complex hypotheses.",
            "objectives": [
                "Express unreal past situations",
                "Use si + plus-que-parfait",
                "Express regret and criticism",
                "Form complex conditional sentences"
            ],
            "themes": ["hypotheses", "regret", "past"],
            "grammar_topics": ["conditionnel_passe", "plus_que_parfait"],
            "estimated_duration": 55
        },
        {
            "unit_number": 3,
            "title": "La voix passive et causative",
            "description": "Use passive voice and causative constructions.",
            "objectives": [
                "Transform active to passive",
                "Use faire + infinitive",
                "Describe processes",
                "Discuss news and events objectively"
            ],
            "themes": ["media", "processes", "formal"],
            "grammar_topics": ["passive_voice", "faire_causatif"],
            "estimated_duration": 55
        },
        {
            "unit_number": 4,
            "title": "Nuancer son discours",
            "description": "Add nuance and precision to your French.",
            "objectives": [
                "Use concession structures",
                "Express opposition and contrast",
                "Master discourse connectors",
                "Write more sophisticated texts"
            ],
            "themes": ["nuance", "writing", "formal"],
            "grammar_topics": ["mise_en_relief", "nominalisation"],
            "estimated_duration": 55
        },
        {
            "unit_number": 5,
            "title": "Actions simultanees",
            "description": "Express simultaneous actions with the gerondif.",
            "objectives": [
                "Form and use the gerondif",
                "Express manner and condition",
                "Describe processes",
                "Use tout en + gerondif"
            ],
            "themes": ["actions", "processes", "manner"],
            "grammar_topics": ["gerondif"],
            "estimated_duration": 55
        },
        {
            "unit_number": 6,
            "title": "Francais familier - La vie sociale",
            "description": "Navigate social situations with authentic informal French.",
            "objectives": [
                "Discuss relationships (draguer, se la peter)",
                "Express moods and states (avoir le cafard, bourre)",
                "Talk about problems (arnaque, se faire arnaquer)",
                "Use emphatic speech (prendre la tete, se casser)"
            ],
            "themes": ["colloquial", "social", "relationships", "emotions"],
            "grammar_topics": [],
            "estimated_duration": 50,
            "is_colloquial": True
        },
    ],
    "C1": [
        {
            "unit_number": 1,
            "title": "Le francais litteraire",
            "description": "Understand and appreciate literary French.",
            "objectives": [
                "Recognize passe simple in texts",
                "Understand literary tenses",
                "Analyze literary style",
                "Read classic French literature excerpts"
            ],
            "themes": ["literature", "style", "reading"],
            "grammar_topics": ["passe_simple"],
            "estimated_duration": 60
        },
        {
            "unit_number": 2,
            "title": "Subjonctif avance",
            "description": "Master all subjunctive tenses and uses.",
            "objectives": [
                "Use subjonctif passe fluently",
                "Recognize subjonctif imparfait",
                "Apply subjunctive in complex contexts",
                "Express subtle emotions and doubts"
            ],
            "themes": ["emotions", "doubt", "formal"],
            "grammar_topics": ["subjonctif_passe", "subjonctif_imparfait"],
            "estimated_duration": 60
        },
        {
            "unit_number": 3,
            "title": "Le discours rapporte",
            "description": "Master advanced reported speech.",
            "objectives": [
                "Report complex statements",
                "Transform questions and commands",
                "Apply all tense shifts",
                "Summarize spoken content accurately"
            ],
            "themes": ["reporting", "media", "formal"],
            "grammar_topics": ["discours_indirect_advanced"],
            "estimated_duration": 60
        },
        {
            "unit_number": 4,
            "title": "Subtilites de la negation",
            "description": "Use nuanced negative expressions.",
            "objectives": [
                "Use ne...guere, ne...nullement",
                "Understand expletive ne",
                "Express subtle negation",
                "Write in elevated style"
            ],
            "themes": ["nuance", "style", "formal"],
            "grammar_topics": ["negation_avancee"],
            "estimated_duration": 60
        },
        {
            "unit_number": 5,
            "title": "L'argumentation ecrite",
            "description": "Write sophisticated argumentative texts.",
            "objectives": [
                "Structure complex arguments",
                "Use all concession structures",
                "Master infinitif passe",
                "Distinguish participle vs adjective"
            ],
            "themes": ["writing", "argumentation", "academic"],
            "grammar_topics": ["concession_opposition", "infinitif_passe", "participe_present_adjectif_verbal"],
            "estimated_duration": 60
        },
        {
            "unit_number": 6,
            "title": "Francais familier - Le langage colore",
            "description": "Master expressive and colorful French expressions.",
            "objectives": [
                "Express annoyance eloquently (ca me saoule, c'est du n'importe quoi)",
                "Discuss laziness and motivation (avoir la flemme, etre au taquet)",
                "Use vivid expressions (foutre le bordel, laisser tomber)",
                "Recognize subtle nuances (se faire des films, prise de tete)"
            ],
            "themes": ["colloquial", "expressions", "emotions", "advanced"],
            "grammar_topics": [],
            "estimated_duration": 55,
            "is_colloquial": True
        },
    ],
    "C2": [
        {
            "unit_number": 1,
            "title": "Les temps littéraires",
            "description": "Master the literary past tenses used in formal writing and literature.",
            "objectives": [
                "Recognize and understand passé antérieur",
                "Identify subjonctif plus-que-parfait in texts",
                "Analyze classic French literature excerpts",
                "Understand the relationship between literary tenses"
            ],
            "themes": ["literature", "literary", "reading", "style"],
            "grammar_topics": ["passe_anterieur", "subjonctif_plus_que_parfait"],
            "estimated_duration": 65
        },
        {
            "unit_number": 2,
            "title": "L'élégance stylistique",
            "description": "Develop sophisticated stylistic techniques in French.",
            "objectives": [
                "Use stylistic inversion appropriately",
                "Master the expletive 'ne' in all contexts",
                "Write in elevated register",
                "Identify stylistic devices in authentic texts"
            ],
            "themes": ["style", "formal", "writing", "stylistics"],
            "grammar_topics": ["inversion_stylistique", "ne_explétif_complet"],
            "estimated_duration": 65
        },
        {
            "unit_number": 3,
            "title": "Les constructions complexes",
            "description": "Master complex grammatical structures for advanced expression.",
            "objectives": [
                "Use advanced impersonal constructions",
                "Apply strict sequence of tenses",
                "Navigate between different registers",
                "Express nuanced ideas precisely"
            ],
            "themes": ["rhetoric", "academic", "connectors", "formal"],
            "grammar_topics": ["constructions_impersonnelles", "concordance_des_temps"],
            "estimated_duration": 65
        },
        {
            "unit_number": 4,
            "title": "Maîtriser les registres",
            "description": "Navigate fluidly between different language registers.",
            "objectives": [
                "Distinguish soutenu, standard, and familier registers",
                "Adapt speech to context appropriately",
                "Understand colloquial and argot expressions",
                "Write effectively in formal academic French"
            ],
            "themes": ["idioms", "verbs", "literary", "philosophy"],
            "grammar_topics": ["registres_de_langue"],
            "estimated_duration": 65
        },
        {
            "unit_number": 5,
            "title": "L'expression idiomatique",
            "description": "Master idiomatic structures unique to French.",
            "objectives": [
                "Use all gallicisms naturally",
                "Recognize and employ literary expressions",
                "Master rare verbs and their usage",
                "Achieve native-like fluency in expression"
            ],
            "themes": ["idioms", "legal", "connectors", "rhetoric"],
            "grammar_topics": ["gallicismes"],
            "estimated_duration": 65
        },
        {
            "unit_number": 6,
            "title": "Francais familier - Parler comme un natif",
            "description": "Master native-level idiomatic and colloquial expressions.",
            "objectives": [
                "Use sophisticated idioms (couper les cheveux en quatre, rouler dans la farine)",
                "Express opinions like a native (c'est du flan, etre a cote de la plaque)",
                "Navigate delicate situations (mettre les pieds dans le plat, retourner sa veste)",
                "Master vulgar but essential expressions appropriately (peter plus haut que son cul)"
            ],
            "themes": ["colloquial", "idioms", "native", "advanced"],
            "grammar_topics": [],
            "estimated_duration": 60,
            "is_colloquial": True
        },
    ],
}


def seed_cefr_levels(db: Session) -> dict[str, CEFRLevel]:
    """Seed CEFR levels and return a mapping of code to level."""
    print("Seeding CEFR levels...")
    levels = {}

    for level_data in CEFR_LEVELS:
        existing = db.query(CEFRLevel).filter(CEFRLevel.code == level_data["code"]).first()
        if existing:
            levels[level_data["code"]] = existing
            continue

        level = CEFRLevel(
            code=level_data["code"],
            name=level_data["name"],
            order=level_data["order"],
            af_levels=level_data["af_levels"],
            vocabulary_target=level_data["vocabulary_target"],
            description=level_data["description"]
        )
        db.add(level)
        levels[level_data["code"]] = level

    db.commit()
    print(f"  ✓ Seeded {len(CEFR_LEVELS)} CEFR levels")
    return levels


def seed_vocabulary(db: Session, levels: dict[str, CEFRLevel]):
    """Seed vocabulary items for all levels."""
    print("Seeding vocabulary...")
    total_count = 0

    # Map gender string to enum
    gender_map = {"m": Gender.MASCULINE, "f": Gender.FEMININE, "-": Gender.NONE, "mf": Gender.BOTH}

    # Map part of speech string to enum
    pos_map = {
        "noun": PartOfSpeech.NOUN,
        "verb": PartOfSpeech.VERB,
        "adjective": PartOfSpeech.ADJECTIVE,
        "adverb": PartOfSpeech.ADVERB,
        "pronoun": PartOfSpeech.PRONOUN,
        "preposition": PartOfSpeech.PREPOSITION,
        "conjunction": PartOfSpeech.CONJUNCTION,
        "interjection": PartOfSpeech.INTERJECTION,
        "article": PartOfSpeech.ARTICLE,
        "phrase": PartOfSpeech.PHRASE,
    }

    for level_code, vocab_list in VOCABULARY_BY_LEVEL.items():
        level = levels.get(level_code)
        if not level:
            print(f"  ✗ {level_code} level not found!")
            continue

        count = 0
        for vocab_data in vocab_list:
            existing = db.query(Vocabulary).filter(
                Vocabulary.french == vocab_data["french"],
                Vocabulary.cefr_level_id == level.id
            ).first()

            if existing:
                continue

            gender = gender_map.get(vocab_data.get("gender", "-"), Gender.NONE)
            part_of_speech = pos_map.get(vocab_data.get("part_of_speech", "noun"), PartOfSpeech.NOUN)

            vocab = Vocabulary(
                cefr_level_id=level.id,
                french=vocab_data["french"],
                english=vocab_data["english"],
                spanish=vocab_data.get("spanish"),
                gender=gender,
                part_of_speech=part_of_speech,
                phonetic=vocab_data.get("phonetic"),
                is_cognate=vocab_data.get("is_cognate", False),
                cognate_spanish=vocab_data.get("cognate_spanish"),
                cognate_note=vocab_data.get("cognate_note"),
                is_false_friend=vocab_data.get("is_false_friend", False),
                category=vocab_data.get("category"),
                example_french=vocab_data.get("example_french"),
                example_english=vocab_data.get("example_english"),
                example_spanish=vocab_data.get("example_spanish"),
                notes=vocab_data.get("notes"),
            )
            db.add(vocab)
            count += 1

        total_count += count
        print(f"    - {level_code}: {count} items")

    db.commit()
    print(f"  ✓ Seeded {total_count} vocabulary items total")


def seed_verbs(db: Session, levels: dict[str, CEFRLevel]):
    """Seed verbs and their conjugations for all levels."""
    print("Seeding verbs...")
    total_verb_count = 0
    total_conj_count = 0

    # Map group and auxiliary to enums
    group_map = {1: VerbGroup.FIRST, 2: VerbGroup.SECOND, 3: VerbGroup.THIRD}
    aux_map = {"avoir": Auxiliary.AVOIR, "être": Auxiliary.ETRE}

    for level_code, verb_list in VERBS_BY_LEVEL.items():
        level = levels.get(level_code)
        if not level:
            print(f"  ✗ {level_code} level not found!")
            continue

        verb_count = 0
        conj_count = 0

        for verb_data in verb_list:
            # Check by infinitive only (UNIQUE constraint is on infinitive alone)
            existing = db.query(Verb).filter(
                Verb.infinitive == verb_data["infinitive"]
            ).first()

            if existing:
                continue

            verb = Verb(
                cefr_level_id=level.id,
                infinitive=verb_data["infinitive"],
                english=verb_data["english"],
                spanish=verb_data.get("spanish"),
                group=group_map.get(verb_data["group"], VerbGroup.FIRST),
                is_irregular=verb_data.get("is_irregular", False),
                auxiliary=aux_map.get(verb_data.get("auxiliary", "avoir"), Auxiliary.AVOIR),
                past_participle=verb_data.get("past_participle"),
                present_participle=verb_data.get("present_participle"),
                notes=verb_data.get("notes"),
                spanish_comparison=verb_data.get("spanish_comparison"),
            )
            db.add(verb)
            db.flush()  # Get the verb ID
            verb_count += 1

            # Add conjugations
            for conj_data in verb_data.get("conjugations", []):
                conjugation = VerbConjugation(
                    verb_id=verb.id,
                    tense=conj_data["tense"],
                    mood=conj_data.get("mood", "indicatif"),
                    je=conj_data.get("je"),
                    tu=conj_data.get("tu"),
                    il_elle=conj_data.get("il_elle"),
                    nous=conj_data.get("nous"),
                    vous=conj_data.get("vous"),
                    ils_elles=conj_data.get("ils_elles"),
                    spanish_equivalent=conj_data.get("spanish_equivalent"),
                )
                db.add(conjugation)
                conj_count += 1

        total_verb_count += verb_count
        total_conj_count += conj_count
        print(f"    - {level_code}: {verb_count} verbs, {conj_count} conjugations")

    db.commit()
    print(f"  ✓ Seeded {total_verb_count} verbs with {total_conj_count} conjugations total")


def seed_grammar(db: Session, levels: dict[str, CEFRLevel]):
    """Seed grammar topics for all levels."""
    print("Seeding grammar...")
    total_count = 0

    for level_code, grammar_list in GRAMMAR_BY_LEVEL.items():
        level = levels.get(level_code)
        if not level:
            print(f"  ✗ {level_code} level not found!")
            continue

        count = 0
        for grammar_data in grammar_list:
            existing = db.query(Grammar).filter(
                Grammar.topic == grammar_data["topic"],
                Grammar.cefr_level_id == level.id
            ).first()

            if existing:
                continue

            grammar = Grammar(
                cefr_level_id=level.id,
                topic=grammar_data["topic"],
                title=grammar_data["title"],
                order=grammar_data.get("order", 0),
                explanation_en=grammar_data["explanation_en"],
                explanation_es=grammar_data.get("explanation_es"),
                spanish_comparison=grammar_data.get("spanish_comparison"),
                examples=grammar_data.get("examples", []),
                common_mistakes=grammar_data.get("common_mistakes", []),
                tips=grammar_data.get("tips", []),
                related_topics=grammar_data.get("related_topics", []),
            )
            db.add(grammar)
            count += 1

        total_count += count
        print(f"    - {level_code}: {count} topics")

    db.commit()
    print(f"  ✓ Seeded {total_count} grammar topics total")


def seed_lessons(db: Session, levels: dict[str, CEFRLevel]):
    """Seed lessons for all levels."""
    print("Seeding lessons...")
    total_count = 0

    for level_code, lessons_list in LESSONS_BY_LEVEL.items():
        level = levels.get(level_code)
        if not level:
            print(f"  ✗ {level_code} level not found!")
            continue

        count = 0
        for lesson_data in lessons_list:
            existing = db.query(Lesson).filter(
                Lesson.unit_number == lesson_data["unit_number"],
                Lesson.cefr_level_id == level.id
            ).first()

            if existing:
                continue

            lesson = Lesson(
                cefr_level_id=level.id,
                unit_number=lesson_data["unit_number"],
                title=lesson_data["title"],
                description=lesson_data["description"],
                objectives=lesson_data["objectives"],
                themes=lesson_data["themes"],
                grammar_topics=lesson_data["grammar_topics"],
                estimated_duration=lesson_data["estimated_duration"]
            )
            db.add(lesson)
            count += 1

        total_count += count
        print(f"    - {level_code}: {count} lessons")

    db.commit()
    print(f"  ✓ Seeded {total_count} lessons total")


def seed_default_user(db: Session):
    """Create the default user profile."""
    print("Creating default user...")

    existing = db.query(User).first()
    if existing:
        print("  ✓ User already exists")
        return

    user = User(
        name="French Learner",
        native_language="en-US",
        secondary_language="es-ES",
        target_language="fr-FR",
        current_cefr_level="A1",
        settings={
            "session_duration": 15,
            "speech_rate": 0.9,
            "show_spanish_hints": True,
            "show_phonetic": True,
            "daily_goal": 20,
            "focus_areas": ["listening", "conjugation", "gender", "pronunciation"]
        }
    )
    db.add(user)
    db.commit()
    print("  ✓ Created default user")


def main():
    """Main seeding function."""
    print("\n" + "=" * 50)
    print("FrenchFlow Database Seeding")
    print("=" * 50 + "\n")

    # Initialize database
    print("Initializing database...")
    init_db()
    print("  ✓ Database initialized\n")

    # Create session
    db = SessionLocal()

    try:
        # Seed all content
        levels = seed_cefr_levels(db)
        seed_vocabulary(db, levels)
        seed_verbs(db, levels)
        seed_grammar(db, levels)
        seed_lessons(db, levels)
        seed_default_user(db)

        print("\n" + "=" * 50)
        print("Database seeding complete!")
        print("=" * 50 + "\n")

        # Print summary
        print("Summary:")
        print(f"  - CEFR Levels: {db.query(CEFRLevel).count()}")
        print(f"  - Vocabulary: {db.query(Vocabulary).count()}")
        print(f"  - Verbs: {db.query(Verb).count()}")
        print(f"  - Conjugations: {db.query(VerbConjugation).count()}")
        print(f"  - Grammar Topics: {db.query(Grammar).count()}")
        print(f"  - Lessons: {db.query(Lesson).count()}")
        print(f"  - Users: {db.query(User).count()}")
        print()

    except Exception as e:
        print(f"\n Error during seeding: {e}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
