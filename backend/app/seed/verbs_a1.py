"""
A1 Level Verbs - Essential French verbs with conjugations.
"""

VERBS_A1 = [
    # ============ ÊTRE (to be) - IRREGULAR ============
    {
        "infinitive": "être",
        "english": "to be",
        "spanish": "ser/estar",
        "group": 3,
        "is_irregular": True,
        "auxiliary": "avoir",
        "past_participle": "été",
        "present_participle": "étant",
        "spanish_comparison": "French 'être' combines both Spanish 'ser' (permanent) and 'estar' (temporary). Context determines meaning.",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicatif",
                "je": "suis",
                "tu": "es",
                "il_elle": "est",
                "nous": "sommes",
                "vous": "êtes",
                "ils_elles": "sont",
                "spanish_equivalent": "soy/estoy, eres/estás, es/está, somos/estamos, sois/estáis, son/están"
            },
            {
                "tense": "passé_composé",
                "mood": "indicatif",
                "je": "ai été",
                "tu": "as été",
                "il_elle": "a été",
                "nous": "avons été",
                "vous": "avez été",
                "ils_elles": "ont été",
                "spanish_equivalent": "he sido/estado, has sido/estado..."
            },
            {
                "tense": "imparfait",
                "mood": "indicatif",
                "je": "étais",
                "tu": "étais",
                "il_elle": "était",
                "nous": "étions",
                "vous": "étiez",
                "ils_elles": "étaient",
                "spanish_equivalent": "era/estaba, eras/estabas..."
            },
            {
                "tense": "futur_simple",
                "mood": "indicatif",
                "je": "serai",
                "tu": "seras",
                "il_elle": "sera",
                "nous": "serons",
                "vous": "serez",
                "ils_elles": "seront",
                "spanish_equivalent": "seré/estaré, serás/estarás..."
            },
        ]
    },

    # ============ AVOIR (to have) - IRREGULAR ============
    {
        "infinitive": "avoir",
        "english": "to have",
        "spanish": "tener/haber",
        "group": 3,
        "is_irregular": True,
        "auxiliary": "avoir",
        "past_participle": "eu",
        "present_participle": "ayant",
        "spanish_comparison": "French 'avoir' combines Spanish 'tener' (possession) and 'haber' (auxiliary). Used in many expressions like 'avoir faim' (to be hungry).",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicatif",
                "je": "ai",
                "tu": "as",
                "il_elle": "a",
                "nous": "avons",
                "vous": "avez",
                "ils_elles": "ont",
                "spanish_equivalent": "tengo/he, tienes/has, tiene/ha..."
            },
            {
                "tense": "passé_composé",
                "mood": "indicatif",
                "je": "ai eu",
                "tu": "as eu",
                "il_elle": "a eu",
                "nous": "avons eu",
                "vous": "avez eu",
                "ils_elles": "ont eu",
                "spanish_equivalent": "he tenido, has tenido..."
            },
            {
                "tense": "imparfait",
                "mood": "indicatif",
                "je": "avais",
                "tu": "avais",
                "il_elle": "avait",
                "nous": "avions",
                "vous": "aviez",
                "ils_elles": "avaient",
                "spanish_equivalent": "tenía/había, tenías/habías..."
            },
            {
                "tense": "futur_simple",
                "mood": "indicatif",
                "je": "aurai",
                "tu": "auras",
                "il_elle": "aura",
                "nous": "aurons",
                "vous": "aurez",
                "ils_elles": "auront",
                "spanish_equivalent": "tendré/habré, tendrás/habrás..."
            },
        ]
    },

    # ============ ALLER (to go) - IRREGULAR ============
    {
        "infinitive": "aller",
        "english": "to go",
        "spanish": "ir",
        "group": 3,
        "is_irregular": True,
        "auxiliary": "être",
        "past_participle": "allé",
        "present_participle": "allant",
        "spanish_comparison": "Like Spanish 'ir', this verb is highly irregular and essential for expressing movement and future actions.",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicatif",
                "je": "vais",
                "tu": "vas",
                "il_elle": "va",
                "nous": "allons",
                "vous": "allez",
                "ils_elles": "vont",
                "spanish_equivalent": "voy, vas, va, vamos, vais, van"
            },
            {
                "tense": "passé_composé",
                "mood": "indicatif",
                "je": "suis allé(e)",
                "tu": "es allé(e)",
                "il_elle": "est allé(e)",
                "nous": "sommes allé(e)s",
                "vous": "êtes allé(e)(s)",
                "ils_elles": "sont allé(e)s",
                "spanish_equivalent": "he ido, has ido, ha ido..."
            },
            {
                "tense": "imparfait",
                "mood": "indicatif",
                "je": "allais",
                "tu": "allais",
                "il_elle": "allait",
                "nous": "allions",
                "vous": "alliez",
                "ils_elles": "allaient",
                "spanish_equivalent": "iba, ibas, iba, íbamos, ibais, iban"
            },
            {
                "tense": "futur_simple",
                "mood": "indicatif",
                "je": "irai",
                "tu": "iras",
                "il_elle": "ira",
                "nous": "irons",
                "vous": "irez",
                "ils_elles": "iront",
                "spanish_equivalent": "iré, irás, irá, iremos, iréis, irán"
            },
        ]
    },

    # ============ FAIRE (to do/make) - IRREGULAR ============
    {
        "infinitive": "faire",
        "english": "to do / to make",
        "spanish": "hacer",
        "group": 3,
        "is_irregular": True,
        "auxiliary": "avoir",
        "past_participle": "fait",
        "present_participle": "faisant",
        "spanish_comparison": "Similar to Spanish 'hacer'. Used in weather expressions: 'il fait chaud' (it's hot) like 'hace calor'.",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicatif",
                "je": "fais",
                "tu": "fais",
                "il_elle": "fait",
                "nous": "faisons",
                "vous": "faites",
                "ils_elles": "font",
                "spanish_equivalent": "hago, haces, hace, hacemos, hacéis, hacen"
            },
            {
                "tense": "passé_composé",
                "mood": "indicatif",
                "je": "ai fait",
                "tu": "as fait",
                "il_elle": "a fait",
                "nous": "avons fait",
                "vous": "avez fait",
                "ils_elles": "ont fait",
                "spanish_equivalent": "he hecho, has hecho..."
            },
            {
                "tense": "imparfait",
                "mood": "indicatif",
                "je": "faisais",
                "tu": "faisais",
                "il_elle": "faisait",
                "nous": "faisions",
                "vous": "faisiez",
                "ils_elles": "faisaient",
                "spanish_equivalent": "hacía, hacías, hacía..."
            },
            {
                "tense": "futur_simple",
                "mood": "indicatif",
                "je": "ferai",
                "tu": "feras",
                "il_elle": "fera",
                "nous": "ferons",
                "vous": "ferez",
                "ils_elles": "feront",
                "spanish_equivalent": "haré, harás, hará..."
            },
        ]
    },

    # ============ PARLER (to speak) - REGULAR -ER ============
    {
        "infinitive": "parler",
        "english": "to speak",
        "spanish": "hablar",
        "group": 1,
        "is_irregular": False,
        "auxiliary": "avoir",
        "past_participle": "parlé",
        "present_participle": "parlant",
        "spanish_comparison": "Regular -ER verb, similar pattern to Spanish -AR verbs. Note: French 'parler' is cognate with 'parlamento'.",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicatif",
                "je": "parle",
                "tu": "parles",
                "il_elle": "parle",
                "nous": "parlons",
                "vous": "parlez",
                "ils_elles": "parlent",
                "spanish_equivalent": "hablo, hablas, habla, hablamos, habláis, hablan"
            },
            {
                "tense": "passé_composé",
                "mood": "indicatif",
                "je": "ai parlé",
                "tu": "as parlé",
                "il_elle": "a parlé",
                "nous": "avons parlé",
                "vous": "avez parlé",
                "ils_elles": "ont parlé",
                "spanish_equivalent": "he hablado, has hablado..."
            },
            {
                "tense": "imparfait",
                "mood": "indicatif",
                "je": "parlais",
                "tu": "parlais",
                "il_elle": "parlait",
                "nous": "parlions",
                "vous": "parliez",
                "ils_elles": "parlaient",
                "spanish_equivalent": "hablaba, hablabas..."
            },
            {
                "tense": "futur_simple",
                "mood": "indicatif",
                "je": "parlerai",
                "tu": "parleras",
                "il_elle": "parlera",
                "nous": "parlerons",
                "vous": "parlerez",
                "ils_elles": "parleront",
                "spanish_equivalent": "hablaré, hablarás..."
            },
        ]
    },

    # ============ MANGER (to eat) - REGULAR -ER (with spelling change) ============
    {
        "infinitive": "manger",
        "english": "to eat",
        "spanish": "comer",
        "group": 1,
        "is_irregular": False,
        "auxiliary": "avoir",
        "past_participle": "mangé",
        "present_participle": "mangeant",
        "spanish_comparison": "Note the 'e' added before 'a/o' to keep soft 'g' sound: 'nous mangeons'.",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicatif",
                "je": "mange",
                "tu": "manges",
                "il_elle": "mange",
                "nous": "mangeons",
                "vous": "mangez",
                "ils_elles": "mangent",
                "spanish_equivalent": "como, comes, come, comemos, coméis, comen"
            },
            {
                "tense": "passé_composé",
                "mood": "indicatif",
                "je": "ai mangé",
                "tu": "as mangé",
                "il_elle": "a mangé",
                "nous": "avons mangé",
                "vous": "avez mangé",
                "ils_elles": "ont mangé",
                "spanish_equivalent": "he comido, has comido..."
            },
        ]
    },

    # ============ AIMER (to like/love) - REGULAR -ER ============
    {
        "infinitive": "aimer",
        "english": "to like / to love",
        "spanish": "amar / gustar",
        "group": 1,
        "is_irregular": False,
        "auxiliary": "avoir",
        "past_participle": "aimé",
        "present_participle": "aimant",
        "spanish_comparison": "Unlike Spanish 'gustar', French 'aimer' follows normal subject-verb order: 'J'aime le café' (I like coffee).",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicatif",
                "je": "aime",
                "tu": "aimes",
                "il_elle": "aime",
                "nous": "aimons",
                "vous": "aimez",
                "ils_elles": "aiment",
                "spanish_equivalent": "amo/me gusta, amas/te gusta..."
            },
        ]
    },

    # ============ VOULOIR (to want) - IRREGULAR ============
    {
        "infinitive": "vouloir",
        "english": "to want",
        "spanish": "querer",
        "group": 3,
        "is_irregular": True,
        "auxiliary": "avoir",
        "past_participle": "voulu",
        "present_participle": "voulant",
        "spanish_comparison": "Similar to Spanish 'querer' for wanting things. 'Je voudrais' (I would like) is very polite.",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicatif",
                "je": "veux",
                "tu": "veux",
                "il_elle": "veut",
                "nous": "voulons",
                "vous": "voulez",
                "ils_elles": "veulent",
                "spanish_equivalent": "quiero, quieres, quiere, queremos, queréis, quieren"
            },
            {
                "tense": "conditionnel",
                "mood": "conditionnel",
                "je": "voudrais",
                "tu": "voudrais",
                "il_elle": "voudrait",
                "nous": "voudrions",
                "vous": "voudriez",
                "ils_elles": "voudraient",
                "spanish_equivalent": "querría, querrías..."
            },
        ]
    },

    # ============ POUVOIR (can/to be able) - IRREGULAR ============
    {
        "infinitive": "pouvoir",
        "english": "can / to be able to",
        "spanish": "poder",
        "group": 3,
        "is_irregular": True,
        "auxiliary": "avoir",
        "past_participle": "pu",
        "present_participle": "pouvant",
        "spanish_comparison": "Very similar to Spanish 'poder'. Note the stem change in present tense.",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicatif",
                "je": "peux",
                "tu": "peux",
                "il_elle": "peut",
                "nous": "pouvons",
                "vous": "pouvez",
                "ils_elles": "peuvent",
                "spanish_equivalent": "puedo, puedes, puede, podemos, podéis, pueden"
            },
        ]
    },

    # ============ DEVOIR (must/to have to) - IRREGULAR ============
    {
        "infinitive": "devoir",
        "english": "must / to have to",
        "spanish": "deber",
        "group": 3,
        "is_irregular": True,
        "auxiliary": "avoir",
        "past_participle": "dû",
        "present_participle": "devant",
        "spanish_comparison": "Very similar to Spanish 'deber'. Expresses obligation.",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicatif",
                "je": "dois",
                "tu": "dois",
                "il_elle": "doit",
                "nous": "devons",
                "vous": "devez",
                "ils_elles": "doivent",
                "spanish_equivalent": "debo, debes, debe, debemos, debéis, deben"
            },
        ]
    },

    # ============ SAVOIR (to know facts) - IRREGULAR ============
    {
        "infinitive": "savoir",
        "english": "to know (facts/how to)",
        "spanish": "saber",
        "group": 3,
        "is_irregular": True,
        "auxiliary": "avoir",
        "past_participle": "su",
        "present_participle": "sachant",
        "spanish_comparison": "Like Spanish 'saber' vs 'conocer'. Use 'savoir' for facts/skills, 'connaître' for familiarity.",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicatif",
                "je": "sais",
                "tu": "sais",
                "il_elle": "sait",
                "nous": "savons",
                "vous": "savez",
                "ils_elles": "savent",
                "spanish_equivalent": "sé, sabes, sabe, sabemos, sabéis, saben"
            },
        ]
    },

    # ============ VENIR (to come) - IRREGULAR ============
    {
        "infinitive": "venir",
        "english": "to come",
        "spanish": "venir",
        "group": 3,
        "is_irregular": True,
        "auxiliary": "être",
        "past_participle": "venu",
        "present_participle": "venant",
        "spanish_comparison": "Identical infinitive! Very similar conjugation pattern to Spanish 'venir'.",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicatif",
                "je": "viens",
                "tu": "viens",
                "il_elle": "vient",
                "nous": "venons",
                "vous": "venez",
                "ils_elles": "viennent",
                "spanish_equivalent": "vengo, vienes, viene, venimos, venís, vienen"
            },
        ]
    },

    # ============ PRENDRE (to take) - IRREGULAR ============
    {
        "infinitive": "prendre",
        "english": "to take",
        "spanish": "tomar / coger",
        "group": 3,
        "is_irregular": True,
        "auxiliary": "avoir",
        "past_participle": "pris",
        "present_participle": "prenant",
        "spanish_comparison": "Like Spanish 'tomar' or 'coger' (careful: 'coger' is vulgar in Latin America!).",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicatif",
                "je": "prends",
                "tu": "prends",
                "il_elle": "prend",
                "nous": "prenons",
                "vous": "prenez",
                "ils_elles": "prennent",
                "spanish_equivalent": "tomo, tomas, toma, tomamos, tomáis, toman"
            },
        ]
    },

    # ============ FINIR (to finish) - REGULAR -IR ============
    {
        "infinitive": "finir",
        "english": "to finish",
        "spanish": "terminar / acabar",
        "group": 2,
        "is_irregular": False,
        "auxiliary": "avoir",
        "past_participle": "fini",
        "present_participle": "finissant",
        "spanish_comparison": "Regular -IR verb. Note the -iss- infix in plural forms.",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicatif",
                "je": "finis",
                "tu": "finis",
                "il_elle": "finit",
                "nous": "finissons",
                "vous": "finissez",
                "ils_elles": "finissent",
                "spanish_equivalent": "termino, terminas, termina, terminamos, termináis, terminan"
            },
        ]
    },

    # ============ COMPRENDRE (to understand) - IRREGULAR ============
    {
        "infinitive": "comprendre",
        "english": "to understand",
        "spanish": "comprender / entender",
        "group": 3,
        "is_irregular": True,
        "auxiliary": "avoir",
        "past_participle": "compris",
        "present_participle": "comprenant",
        "spanish_comparison": "Cognate with Spanish 'comprender'. Conjugates like 'prendre'.",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicatif",
                "je": "comprends",
                "tu": "comprends",
                "il_elle": "comprend",
                "nous": "comprenons",
                "vous": "comprenez",
                "ils_elles": "comprennent",
                "spanish_equivalent": "comprendo, comprendes, comprende..."
            },
        ]
    },

    # ============ ATTENDRE (to wait) - REGULAR -RE ============
    {
        "infinitive": "attendre",
        "english": "to wait (for)",
        "spanish": "esperar",
        "group": 3,
        "is_irregular": False,
        "auxiliary": "avoir",
        "past_participle": "attendu",
        "present_participle": "attendant",
        "spanish_comparison": "No preposition needed: 'J'attends le bus' (I wait for the bus).",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicatif",
                "je": "attends",
                "tu": "attends",
                "il_elle": "attend",
                "nous": "attendons",
                "vous": "attendez",
                "ils_elles": "attendent",
                "spanish_equivalent": "espero, esperas, espera..."
            },
        ]
    },

    # ============ HABITER (to live) - REGULAR -ER ============
    {
        "infinitive": "habiter",
        "english": "to live (reside)",
        "spanish": "vivir / habitar",
        "group": 1,
        "is_irregular": False,
        "auxiliary": "avoir",
        "past_participle": "habité",
        "present_participle": "habitant",
        "spanish_comparison": "Cognate with Spanish 'habitar'. Regular -ER verb.",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicatif",
                "je": "habite",
                "tu": "habites",
                "il_elle": "habite",
                "nous": "habitons",
                "vous": "habitez",
                "ils_elles": "habitent",
                "spanish_equivalent": "vivo/habito, vives/habitas..."
            },
        ]
    },

    # ============ TRAVAILLER (to work) - REGULAR -ER ============
    {
        "infinitive": "travailler",
        "english": "to work",
        "spanish": "trabajar",
        "group": 1,
        "is_irregular": False,
        "auxiliary": "avoir",
        "past_participle": "travaillé",
        "present_participle": "travaillant",
        "spanish_comparison": "Very similar to Spanish 'trabajar'. Regular -ER verb.",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicatif",
                "je": "travaille",
                "tu": "travailles",
                "il_elle": "travaille",
                "nous": "travaillons",
                "vous": "travaillez",
                "ils_elles": "travaillent",
                "spanish_equivalent": "trabajo, trabajas, trabaja..."
            },
        ]
    },

    # ============ ÉCOUTER (to listen) - REGULAR -ER ============
    {
        "infinitive": "écouter",
        "english": "to listen (to)",
        "spanish": "escuchar",
        "group": 1,
        "is_irregular": False,
        "auxiliary": "avoir",
        "past_participle": "écouté",
        "present_participle": "écoutant",
        "spanish_comparison": "Very similar to Spanish 'escuchar'. No preposition needed in French.",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicatif",
                "je": "écoute",
                "tu": "écoutes",
                "il_elle": "écoute",
                "nous": "écoutons",
                "vous": "écoutez",
                "ils_elles": "écoutent",
                "spanish_equivalent": "escucho, escuchas, escucha..."
            },
        ]
    },

    # ============ REGARDER (to watch/look at) - REGULAR -ER ============
    {
        "infinitive": "regarder",
        "english": "to watch / to look at",
        "spanish": "mirar",
        "group": 1,
        "is_irregular": False,
        "auxiliary": "avoir",
        "past_participle": "regardé",
        "present_participle": "regardant",
        "spanish_comparison": "Cognate with Spanish 'resguardar'. No preposition needed.",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicatif",
                "je": "regarde",
                "tu": "regardes",
                "il_elle": "regarde",
                "nous": "regardons",
                "vous": "regardez",
                "ils_elles": "regardent",
                "spanish_equivalent": "miro, miras, mira..."
            },
        ]
    },

    # ============ LIRE (to read) - IRREGULAR ============
    {
        "infinitive": "lire",
        "english": "to read",
        "spanish": "leer",
        "group": 3,
        "is_irregular": True,
        "auxiliary": "avoir",
        "past_participle": "lu",
        "present_participle": "lisant",
        "spanish_comparison": "Similar to Spanish 'leer'. Note the irregular past participle 'lu'.",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicatif",
                "je": "lis",
                "tu": "lis",
                "il_elle": "lit",
                "nous": "lisons",
                "vous": "lisez",
                "ils_elles": "lisent",
                "spanish_equivalent": "leo, lees, lee, leemos, leéis, leen"
            },
        ]
    },

    # ============ ÉCRIRE (to write) - IRREGULAR ============
    {
        "infinitive": "écrire",
        "english": "to write",
        "spanish": "escribir",
        "group": 3,
        "is_irregular": True,
        "auxiliary": "avoir",
        "past_participle": "écrit",
        "present_participle": "écrivant",
        "spanish_comparison": "Cognate with Spanish 'escribir'. Note spelling changes.",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicatif",
                "je": "écris",
                "tu": "écris",
                "il_elle": "écrit",
                "nous": "écrivons",
                "vous": "écrivez",
                "ils_elles": "écrivent",
                "spanish_equivalent": "escribo, escribes, escribe..."
            },
        ]
    },
]
