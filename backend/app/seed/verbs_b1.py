"""
B1 Level Verbs - Intermediate
Alliance Française B100-B105 equivalent
Focus on more complex tenses: imparfait, futur simple, conditionnel
"""

VERBS_B1 = [
    # Professional/Work verbs
    {
        "infinitive": "travailler",
        "english": "to work",
        "spanish": "trabajar",
        "group": 1,
        "is_irregular": False,
        "spanish_comparison": "Very similar conjugation pattern to Spanish 'trabajar'",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicative",
                "je": "travaille",
                "tu": "travailles",
                "il_elle": "travaille",
                "nous": "travaillons",
                "vous": "travaillez",
                "ils_elles": "travaillent",
                "spanish_equivalent": "trabajo, trabajas, trabaja, trabajamos, trabajáis, trabajan"
            },
            {
                "tense": "imparfait",
                "mood": "indicative",
                "je": "travaillais",
                "tu": "travaillais",
                "il_elle": "travaillait",
                "nous": "travaillions",
                "vous": "travailliez",
                "ils_elles": "travaillaient",
                "spanish_equivalent": "trabajaba, trabajabas, trabajaba, trabajábamos, trabajabais, trabajaban"
            },
            {
                "tense": "futur_simple",
                "mood": "indicative",
                "je": "travaillerai",
                "tu": "travailleras",
                "il_elle": "travaillera",
                "nous": "travaillerons",
                "vous": "travaillerez",
                "ils_elles": "travailleront",
                "spanish_equivalent": "trabajaré, trabajarás, trabajará, trabajaremos, trabajaréis, trabajarán"
            }
        ]
    },
    {
        "infinitive": "réussir",
        "english": "to succeed/pass",
        "spanish": "tener éxito/aprobar",
        "group": 2,
        "is_irregular": False,
        "spanish_comparison": "No direct cognate, but regular -ir verb pattern",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicative",
                "je": "réussis",
                "tu": "réussis",
                "il_elle": "réussit",
                "nous": "réussissons",
                "vous": "réussissez",
                "ils_elles": "réussissent",
                "spanish_equivalent": "tengo éxito, tienes éxito, tiene éxito..."
            },
            {
                "tense": "passé_composé",
                "mood": "indicative",
                "je": "ai réussi",
                "tu": "as réussi",
                "il_elle": "a réussi",
                "nous": "avons réussi",
                "vous": "avez réussi",
                "ils_elles": "ont réussi",
                "spanish_equivalent": "he tenido éxito, has tenido éxito..."
            },
            {
                "tense": "futur_simple",
                "mood": "indicative",
                "je": "réussirai",
                "tu": "réussiras",
                "il_elle": "réussira",
                "nous": "réussirons",
                "vous": "réussirez",
                "ils_elles": "réussiront",
                "spanish_equivalent": "tendré éxito, tendrás éxito..."
            }
        ]
    },
    {
        "infinitive": "croire",
        "english": "to believe",
        "spanish": "creer",
        "group": 3,
        "is_irregular": True,
        "spanish_comparison": "Cognate with Spanish 'creer'. Both have irregular forms.",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicative",
                "je": "crois",
                "tu": "crois",
                "il_elle": "croit",
                "nous": "croyons",
                "vous": "croyez",
                "ils_elles": "croient",
                "spanish_equivalent": "creo, crees, cree, creemos, creéis, creen"
            },
            {
                "tense": "imparfait",
                "mood": "indicative",
                "je": "croyais",
                "tu": "croyais",
                "il_elle": "croyait",
                "nous": "croyions",
                "vous": "croyiez",
                "ils_elles": "croyaient",
                "spanish_equivalent": "creía, creías, creía, creíamos, creíais, creían"
            },
            {
                "tense": "futur_simple",
                "mood": "indicative",
                "je": "croirai",
                "tu": "croiras",
                "il_elle": "croira",
                "nous": "croirons",
                "vous": "croirez",
                "ils_elles": "croiront",
                "spanish_equivalent": "creeré, creerás, creerá, creeremos, creeréis, creerán"
            }
        ]
    },
    {
        "infinitive": "recevoir",
        "english": "to receive",
        "spanish": "recibir",
        "group": 3,
        "is_irregular": True,
        "spanish_comparison": "Cognate with Spanish 'recibir'. Note the ç before o/u in French.",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicative",
                "je": "reçois",
                "tu": "reçois",
                "il_elle": "reçoit",
                "nous": "recevons",
                "vous": "recevez",
                "ils_elles": "reçoivent",
                "spanish_equivalent": "recibo, recibes, recibe, recibimos, recibís, reciben"
            },
            {
                "tense": "passé_composé",
                "mood": "indicative",
                "je": "ai reçu",
                "tu": "as reçu",
                "il_elle": "a reçu",
                "nous": "avons reçu",
                "vous": "avez reçu",
                "ils_elles": "ont reçu",
                "spanish_equivalent": "he recibido, has recibido, ha recibido..."
            },
            {
                "tense": "futur_simple",
                "mood": "indicative",
                "je": "recevrai",
                "tu": "recevras",
                "il_elle": "recevra",
                "nous": "recevrons",
                "vous": "recevrez",
                "ils_elles": "recevront",
                "spanish_equivalent": "recibiré, recibirás, recibirá..."
            }
        ]
    },
    {
        "infinitive": "suivre",
        "english": "to follow",
        "spanish": "seguir",
        "group": 3,
        "is_irregular": True,
        "spanish_comparison": "Related to Spanish 'seguir'. Both have stem changes.",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicative",
                "je": "suis",
                "tu": "suis",
                "il_elle": "suit",
                "nous": "suivons",
                "vous": "suivez",
                "ils_elles": "suivent",
                "spanish_equivalent": "sigo, sigues, sigue, seguimos, seguís, siguen"
            },
            {
                "tense": "imparfait",
                "mood": "indicative",
                "je": "suivais",
                "tu": "suivais",
                "il_elle": "suivait",
                "nous": "suivions",
                "vous": "suiviez",
                "ils_elles": "suivaient",
                "spanish_equivalent": "seguía, seguías, seguía, seguíamos, seguíais, seguían"
            },
            {
                "tense": "passé_composé",
                "mood": "indicative",
                "je": "ai suivi",
                "tu": "as suivi",
                "il_elle": "a suivi",
                "nous": "avons suivi",
                "vous": "avez suivi",
                "ils_elles": "ont suivi",
                "spanish_equivalent": "he seguido, has seguido, ha seguido..."
            }
        ]
    },
    {
        "infinitive": "vivre",
        "english": "to live",
        "spanish": "vivir",
        "group": 3,
        "is_irregular": True,
        "spanish_comparison": "Direct cognate with Spanish 'vivir'. Similar meaning and usage.",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicative",
                "je": "vis",
                "tu": "vis",
                "il_elle": "vit",
                "nous": "vivons",
                "vous": "vivez",
                "ils_elles": "vivent",
                "spanish_equivalent": "vivo, vives, vive, vivimos, vivís, viven"
            },
            {
                "tense": "imparfait",
                "mood": "indicative",
                "je": "vivais",
                "tu": "vivais",
                "il_elle": "vivait",
                "nous": "vivions",
                "vous": "viviez",
                "ils_elles": "vivaient",
                "spanish_equivalent": "vivía, vivías, vivía, vivíamos, vivíais, vivían"
            },
            {
                "tense": "passé_composé",
                "mood": "indicative",
                "je": "ai vécu",
                "tu": "as vécu",
                "il_elle": "a vécu",
                "nous": "avons vécu",
                "vous": "avez vécu",
                "ils_elles": "ont vécu",
                "spanish_equivalent": "he vivido, has vivido, ha vivido..."
            }
        ]
    },
    {
        "infinitive": "produire",
        "english": "to produce",
        "spanish": "producir",
        "group": 3,
        "is_irregular": True,
        "spanish_comparison": "Direct cognate with Spanish 'producir'. Similar irregular patterns.",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicative",
                "je": "produis",
                "tu": "produis",
                "il_elle": "produit",
                "nous": "produisons",
                "vous": "produisez",
                "ils_elles": "produisent",
                "spanish_equivalent": "produzco, produces, produce, producimos, producís, producen"
            },
            {
                "tense": "passé_composé",
                "mood": "indicative",
                "je": "ai produit",
                "tu": "as produit",
                "il_elle": "a produit",
                "nous": "avons produit",
                "vous": "avez produit",
                "ils_elles": "ont produit",
                "spanish_equivalent": "he producido, has producido, ha producido..."
            },
            {
                "tense": "futur_simple",
                "mood": "indicative",
                "je": "produirai",
                "tu": "produiras",
                "il_elle": "produira",
                "nous": "produirons",
                "vous": "produirez",
                "ils_elles": "produiront",
                "spanish_equivalent": "produciré, producirás, producirá..."
            }
        ]
    },
    {
        "infinitive": "permettre",
        "english": "to allow/permit",
        "spanish": "permitir",
        "group": 3,
        "is_irregular": True,
        "spanish_comparison": "Direct cognate with Spanish 'permitir'. Conjugates like 'mettre'.",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicative",
                "je": "permets",
                "tu": "permets",
                "il_elle": "permet",
                "nous": "permettons",
                "vous": "permettez",
                "ils_elles": "permettent",
                "spanish_equivalent": "permito, permites, permite, permitimos, permitís, permiten"
            },
            {
                "tense": "passé_composé",
                "mood": "indicative",
                "je": "ai permis",
                "tu": "as permis",
                "il_elle": "a permis",
                "nous": "avons permis",
                "vous": "avez permis",
                "ils_elles": "ont permis",
                "spanish_equivalent": "he permitido, has permitido, ha permitido..."
            },
            {
                "tense": "conditionnel",
                "mood": "conditionnel",
                "je": "permettrais",
                "tu": "permettrais",
                "il_elle": "permettrait",
                "nous": "permettrions",
                "vous": "permettriez",
                "ils_elles": "permettraient",
                "spanish_equivalent": "permitiría, permitirías, permitiría..."
            }
        ]
    },
    {
        "infinitive": "conduire",
        "english": "to drive/lead",
        "spanish": "conducir",
        "group": 3,
        "is_irregular": True,
        "spanish_comparison": "Direct cognate with Spanish 'conducir'. Both have irregular yo/je forms.",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicative",
                "je": "conduis",
                "tu": "conduis",
                "il_elle": "conduit",
                "nous": "conduisons",
                "vous": "conduisez",
                "ils_elles": "conduisent",
                "spanish_equivalent": "conduzco, conduces, conduce, conducimos, conducís, conducen"
            },
            {
                "tense": "imparfait",
                "mood": "indicative",
                "je": "conduisais",
                "tu": "conduisais",
                "il_elle": "conduisait",
                "nous": "conduisions",
                "vous": "conduisiez",
                "ils_elles": "conduisaient",
                "spanish_equivalent": "conducía, conducías, conducía, conducíamos, conducíais, conducían"
            },
            {
                "tense": "passé_composé",
                "mood": "indicative",
                "je": "ai conduit",
                "tu": "as conduit",
                "il_elle": "a conduit",
                "nous": "avons conduit",
                "vous": "avez conduit",
                "ils_elles": "ont conduit",
                "spanish_equivalent": "he conducido, has conducido, ha conducido..."
            }
        ]
    },
    {
        "infinitive": "offrir",
        "english": "to offer/give (gift)",
        "spanish": "ofrecer",
        "group": 3,
        "is_irregular": True,
        "spanish_comparison": "Cognate with Spanish 'ofrecer'. Conjugates like -er verbs in present.",
        "conjugations": [
            {
                "tense": "present",
                "mood": "indicative",
                "je": "offre",
                "tu": "offres",
                "il_elle": "offre",
                "nous": "offrons",
                "vous": "offrez",
                "ils_elles": "offrent",
                "spanish_equivalent": "ofrezco, ofreces, ofrece, ofrecemos, ofrecéis, ofrecen"
            },
            {
                "tense": "passé_composé",
                "mood": "indicative",
                "je": "ai offert",
                "tu": "as offert",
                "il_elle": "a offert",
                "nous": "avons offert",
                "vous": "avez offert",
                "ils_elles": "ont offert",
                "spanish_equivalent": "he ofrecido, has ofrecido, ha ofrecido..."
            },
            {
                "tense": "conditionnel",
                "mood": "conditionnel",
                "je": "offrirais",
                "tu": "offrirais",
                "il_elle": "offrirait",
                "nous": "offririons",
                "vous": "offririez",
                "ils_elles": "offriraient",
                "spanish_equivalent": "ofrecería, ofrecerías, ofrecería..."
            }
        ]
    }
]
