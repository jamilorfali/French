"""
A2 Level Grammar - Elementary
Alliance Française A200-A205 equivalent
"""

GRAMMAR_A2 = [
    {
        "topic": "passe_compose_avoir",
        "title": "Passé Composé with Avoir",
        "order": 1,
        "explanation_en": "The passé composé is a past tense used to describe completed actions. Most verbs use 'avoir' as the auxiliary verb, followed by the past participle. For regular -ER verbs, replace -er with -é. For -IR verbs, replace -ir with -i. For -RE verbs, replace -re with -u.",
        "explanation_es": "El passé composé es un tiempo pasado usado para describir acciones completadas. Similar al pretérito perfecto español (he comido), pero se usa más frecuentemente.",
        "spanish_comparison": "Like Spanish 'he hablado', but French uses it more broadly where Spanish might use pretérito indefinido.",
        "examples": [
            {"french": "J'ai mangé une pomme.", "english": "I ate an apple.", "spanish": "He comido / Comí una manzana."},
            {"french": "Elle a fini ses devoirs.", "english": "She finished her homework.", "spanish": "Ha terminado / Terminó sus deberes."},
            {"french": "Nous avons vendu la voiture.", "english": "We sold the car.", "spanish": "Hemos vendido / Vendimos el coche."}
        ],
        "common_mistakes": [
            "Forgetting to use the auxiliary 'avoir'",
            "Using incorrect past participle endings",
            "Placing negation incorrectly (ne...pas goes around avoir)"
        ],
        "tips": [
            "Most verbs use avoir - memorize the être verbs separately",
            "Past participle agrees with preceding direct object (advanced)"
        ],
        "related_topics": ["passe_compose_etre", "past_participles"]
    },
    {
        "topic": "passe_compose_etre",
        "title": "Passé Composé with Être",
        "order": 2,
        "explanation_en": "Certain verbs use 'être' as their auxiliary in passé composé. These are primarily verbs of motion and reflexive verbs. When using être, the past participle must agree in gender and number with the subject.",
        "explanation_es": "Algunos verbos usan 'être' (ser/estar) como auxiliar. El participio pasado debe concordar con el sujeto en género y número.",
        "spanish_comparison": "Unlike Spanish, French requires agreement of past participle with subject when using être.",
        "examples": [
            {"french": "Je suis allé(e) au cinéma.", "english": "I went to the cinema.", "spanish": "Fui al cine."},
            {"french": "Elle est partie hier.", "english": "She left yesterday.", "spanish": "Ella se fue ayer."},
            {"french": "Nous sommes arrivés en retard.", "english": "We arrived late.", "spanish": "Llegamos tarde."}
        ],
        "common_mistakes": [
            "Forgetting to make the past participle agree with subject",
            "Using avoir instead of être",
            "DR MRS VANDERTRAMP verbs: Devenir, Revenir, Monter, Rester, Sortir, Venir, Aller, Naître, Descendre, Entrer, Retourner, Tomber, Rentrer, Arriver, Mourir, Partir"
        ],
        "tips": [
            "Learn DR MRS VANDERTRAMP to remember être verbs",
            "All reflexive verbs also use être"
        ],
        "related_topics": ["passe_compose_avoir", "reflexive_verbs"]
    },
    {
        "topic": "reflexive_verbs",
        "title": "Reflexive Verbs (Les verbes pronominaux)",
        "order": 3,
        "explanation_en": "Reflexive verbs indicate that the subject performs an action on itself. They use reflexive pronouns: me, te, se, nous, vous, se. In passé composé, reflexive verbs always use être as auxiliary.",
        "explanation_es": "Los verbos reflexivos en francés funcionan de manera similar al español (me lavo, te levantas). Siempre usan être en passé composé.",
        "spanish_comparison": "Very similar to Spanish reflexive verbs (lavarse, levantarse). Pronoun placement is the same.",
        "examples": [
            {"french": "Je me lève à sept heures.", "english": "I get up at seven o'clock.", "spanish": "Me levanto a las siete."},
            {"french": "Elle s'est habillée rapidement.", "english": "She got dressed quickly.", "spanish": "Se vistió rápidamente."},
            {"french": "Nous nous sommes rencontrés hier.", "english": "We met yesterday.", "spanish": "Nos conocimos ayer."}
        ],
        "common_mistakes": [
            "Forgetting the reflexive pronoun",
            "Using avoir instead of être in passé composé",
            "Not making agreement with reflexive verbs in passé composé"
        ],
        "tips": [
            "Always conjugate the reflexive pronoun to match the subject",
            "In questions, keep the pronoun before the verb"
        ],
        "related_topics": ["passe_compose_etre", "pronouns"]
    },
    {
        "topic": "imparfait_introduction",
        "title": "Introduction to Imparfait",
        "order": 4,
        "explanation_en": "The imparfait is used to describe ongoing past actions, habitual actions, or states in the past. Form it by taking the nous form of the present tense, dropping -ons, and adding: -ais, -ais, -ait, -ions, -iez, -aient.",
        "explanation_es": "El imparfait corresponde al imperfecto español (hablaba, comía). Se usa de manera muy similar.",
        "spanish_comparison": "Almost identical usage to Spanish imperfecto. Same concept of ongoing/habitual past actions.",
        "examples": [
            {"french": "Quand j'étais jeune, j'habitais à Paris.", "english": "When I was young, I lived in Paris.", "spanish": "Cuando era joven, vivía en París."},
            {"french": "Il faisait beau hier.", "english": "The weather was nice yesterday.", "spanish": "Hacía buen tiempo ayer."},
            {"french": "Nous mangions toujours ensemble.", "english": "We always ate together.", "spanish": "Siempre comíamos juntos."}
        ],
        "common_mistakes": [
            "Confusing imparfait with passé composé",
            "Irregular stem of être: ét- (j'étais)",
            "Forgetting the -i- in nous/vous forms (-ions, -iez)"
        ],
        "tips": [
            "Use imparfait for descriptions, habits, and ongoing states",
            "Use passé composé for completed, specific actions",
            "Only être has an irregular stem in imparfait"
        ],
        "related_topics": ["passe_compose_avoir", "passe_compose_etre"]
    },
    {
        "topic": "comparative_superlative",
        "title": "Comparatives and Superlatives",
        "order": 5,
        "explanation_en": "To compare things: plus + adjective + que (more...than), moins + adjective + que (less...than), aussi + adjective + que (as...as). For superlatives: le/la/les plus + adjective (the most), le/la/les moins + adjective (the least).",
        "explanation_es": "Similar al español: más...que, menos...que, tan...como. Para superlativos: el/la más...",
        "spanish_comparison": "Very similar structure to Spanish comparatives and superlatives.",
        "examples": [
            {"french": "Paris est plus grand que Lyon.", "english": "Paris is bigger than Lyon.", "spanish": "París es más grande que Lyon."},
            {"french": "Ce livre est moins intéressant.", "english": "This book is less interesting.", "spanish": "Este libro es menos interesante."},
            {"french": "C'est la plus belle ville.", "english": "It's the most beautiful city.", "spanish": "Es la ciudad más bella."}
        ],
        "common_mistakes": [
            "Irregular forms: bon → meilleur (not plus bon), bien → mieux",
            "Forgetting que in comparisons",
            "Article agreement in superlatives"
        ],
        "tips": [
            "Meilleur (better) and mieux (better - adverb) are irregular",
            "Superlative article agrees with noun gender"
        ],
        "related_topics": ["adjective_agreement", "adverbs"]
    },
    {
        "topic": "direct_object_pronouns",
        "title": "Direct Object Pronouns",
        "order": 6,
        "explanation_en": "Direct object pronouns replace nouns that receive the action directly: me, te, le/la, nous, vous, les. They are placed before the conjugated verb (or before the infinitive if there is one).",
        "explanation_es": "Los pronombres de objeto directo (me, te, lo/la, nos, os, los/las) funcionan de manera similar en francés.",
        "spanish_comparison": "Similar to Spanish but always placed before the verb in French (never attached to infinitives as in Spanish).",
        "examples": [
            {"french": "Je le vois.", "english": "I see him/it.", "spanish": "Lo veo."},
            {"french": "Elle les aime.", "english": "She loves them.", "spanish": "Los/Las quiere."},
            {"french": "Je vais le faire.", "english": "I'm going to do it.", "spanish": "Voy a hacerlo."}
        ],
        "common_mistakes": [
            "Placing pronoun after the verb (wrong position)",
            "Confusing le/la with lui (indirect object)",
            "In passé composé, pronoun goes before avoir/être"
        ],
        "tips": [
            "Le/la/les replace things and people",
            "In negative sentences: ne + pronoun + verb + pas"
        ],
        "related_topics": ["indirect_object_pronouns", "pronouns"]
    },
]
