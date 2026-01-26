"""
A2 Level Verbs - Elementary
Alliance Française A200-A205 equivalent
Focus on passé composé, imparfait introduction, and more irregular verbs
"""

VERBS_A2 = [
    {
        "infinitive": "venir",
        "english": "to come",
        "spanish": "venir",
        "group": 3,
        "is_irregular": True,
        "auxiliary": "être",
        "past_participle": "venu",
        "present_participle": "venant",
        "spanish_comparison": "Like Spanish 'venir', uses être as auxiliary in passé composé",
        "conjugations": [
            {"tense": "présent", "mood": "indicatif", "je": "viens", "tu": "viens", "il_elle": "vient", "nous": "venons", "vous": "venez", "ils_elles": "viennent", "spanish_equivalent": "vengo, vienes, viene..."},
            {"tense": "passé_composé", "mood": "indicatif", "je": "suis venu(e)", "tu": "es venu(e)", "il_elle": "est venu(e)", "nous": "sommes venu(e)s", "vous": "êtes venu(e)(s)", "ils_elles": "sont venu(e)s"},
        ]
    },
    {
        "infinitive": "prendre",
        "english": "to take",
        "spanish": "tomar/coger",
        "group": 3,
        "is_irregular": True,
        "auxiliary": "avoir",
        "past_participle": "pris",
        "present_participle": "prenant",
        "spanish_comparison": "Unlike Spanish 'tomar', prendre has an irregular conjugation pattern",
        "conjugations": [
            {"tense": "présent", "mood": "indicatif", "je": "prends", "tu": "prends", "il_elle": "prend", "nous": "prenons", "vous": "prenez", "ils_elles": "prennent"},
            {"tense": "passé_composé", "mood": "indicatif", "je": "ai pris", "tu": "as pris", "il_elle": "a pris", "nous": "avons pris", "vous": "avez pris", "ils_elles": "ont pris"},
        ]
    },
    {
        "infinitive": "mettre",
        "english": "to put/to wear",
        "spanish": "poner/ponerse",
        "group": 3,
        "is_irregular": True,
        "auxiliary": "avoir",
        "past_participle": "mis",
        "present_participle": "mettant",
        "spanish_comparison": "Similar to Spanish 'poner' - irregular in both languages",
        "conjugations": [
            {"tense": "présent", "mood": "indicatif", "je": "mets", "tu": "mets", "il_elle": "met", "nous": "mettons", "vous": "mettez", "ils_elles": "mettent"},
            {"tense": "passé_composé", "mood": "indicatif", "je": "ai mis", "tu": "as mis", "il_elle": "a mis", "nous": "avons mis", "vous": "avez mis", "ils_elles": "ont mis"},
        ]
    },
    {
        "infinitive": "partir",
        "english": "to leave/depart",
        "spanish": "partir/irse",
        "group": 3,
        "is_irregular": True,
        "auxiliary": "être",
        "past_participle": "parti",
        "present_participle": "partant",
        "spanish_comparison": "Unlike Spanish 'partir', French uses être as auxiliary",
        "conjugations": [
            {"tense": "présent", "mood": "indicatif", "je": "pars", "tu": "pars", "il_elle": "part", "nous": "partons", "vous": "partez", "ils_elles": "partent"},
            {"tense": "passé_composé", "mood": "indicatif", "je": "suis parti(e)", "tu": "es parti(e)", "il_elle": "est parti(e)", "nous": "sommes parti(e)s", "vous": "êtes parti(e)(s)", "ils_elles": "sont parti(e)s"},
        ]
    },
    {
        "infinitive": "sortir",
        "english": "to go out/exit",
        "spanish": "salir",
        "group": 3,
        "is_irregular": True,
        "auxiliary": "être",
        "past_participle": "sorti",
        "present_participle": "sortant",
        "spanish_comparison": "Like Spanish 'salir', but uses être in passé composé",
        "conjugations": [
            {"tense": "présent", "mood": "indicatif", "je": "sors", "tu": "sors", "il_elle": "sort", "nous": "sortons", "vous": "sortez", "ils_elles": "sortent"},
            {"tense": "passé_composé", "mood": "indicatif", "je": "suis sorti(e)", "tu": "es sorti(e)", "il_elle": "est sorti(e)", "nous": "sommes sorti(e)s", "vous": "êtes sorti(e)(s)", "ils_elles": "sont sorti(e)s"},
        ]
    },
    {
        "infinitive": "dormir",
        "english": "to sleep",
        "spanish": "dormir",
        "group": 3,
        "is_irregular": True,
        "auxiliary": "avoir",
        "past_participle": "dormi",
        "present_participle": "dormant",
        "spanish_comparison": "Same infinitive as Spanish 'dormir' - cognate!",
        "conjugations": [
            {"tense": "présent", "mood": "indicatif", "je": "dors", "tu": "dors", "il_elle": "dort", "nous": "dormons", "vous": "dormez", "ils_elles": "dorment"},
            {"tense": "passé_composé", "mood": "indicatif", "je": "ai dormi", "tu": "as dormi", "il_elle": "a dormi", "nous": "avons dormi", "vous": "avez dormi", "ils_elles": "ont dormi"},
        ]
    },
    {
        "infinitive": "voir",
        "english": "to see",
        "spanish": "ver",
        "group": 3,
        "is_irregular": True,
        "auxiliary": "avoir",
        "past_participle": "vu",
        "present_participle": "voyant",
        "spanish_comparison": "Related to Spanish 'ver' - both irregular",
        "conjugations": [
            {"tense": "présent", "mood": "indicatif", "je": "vois", "tu": "vois", "il_elle": "voit", "nous": "voyons", "vous": "voyez", "ils_elles": "voient"},
            {"tense": "passé_composé", "mood": "indicatif", "je": "ai vu", "tu": "as vu", "il_elle": "a vu", "nous": "avons vu", "vous": "avez vu", "ils_elles": "ont vu"},
        ]
    },
    {
        "infinitive": "savoir",
        "english": "to know (facts)",
        "spanish": "saber",
        "group": 3,
        "is_irregular": True,
        "auxiliary": "avoir",
        "past_participle": "su",
        "present_participle": "sachant",
        "spanish_comparison": "Like Spanish 'saber' vs 'conocer', French has 'savoir' vs 'connaître'",
        "conjugations": [
            {"tense": "présent", "mood": "indicatif", "je": "sais", "tu": "sais", "il_elle": "sait", "nous": "savons", "vous": "savez", "ils_elles": "savent"},
            {"tense": "passé_composé", "mood": "indicatif", "je": "ai su", "tu": "as su", "il_elle": "a su", "nous": "avons su", "vous": "avez su", "ils_elles": "ont su"},
        ]
    },
    {
        "infinitive": "connaître",
        "english": "to know (people/places)",
        "spanish": "conocer",
        "group": 3,
        "is_irregular": True,
        "auxiliary": "avoir",
        "past_participle": "connu",
        "present_participle": "connaissant",
        "spanish_comparison": "Like Spanish 'conocer' - used for knowing people and places",
        "conjugations": [
            {"tense": "présent", "mood": "indicatif", "je": "connais", "tu": "connais", "il_elle": "connaît", "nous": "connaissons", "vous": "connaissez", "ils_elles": "connaissent"},
            {"tense": "passé_composé", "mood": "indicatif", "je": "ai connu", "tu": "as connu", "il_elle": "a connu", "nous": "avons connu", "vous": "avez connu", "ils_elles": "ont connu"},
        ]
    },
    {
        "infinitive": "devoir",
        "english": "to have to/must",
        "spanish": "deber",
        "group": 3,
        "is_irregular": True,
        "auxiliary": "avoir",
        "past_participle": "dû",
        "present_participle": "devant",
        "spanish_comparison": "Like Spanish 'deber' - expresses obligation",
        "conjugations": [
            {"tense": "présent", "mood": "indicatif", "je": "dois", "tu": "dois", "il_elle": "doit", "nous": "devons", "vous": "devez", "ils_elles": "doivent"},
            {"tense": "passé_composé", "mood": "indicatif", "je": "ai dû", "tu": "as dû", "il_elle": "a dû", "nous": "avons dû", "vous": "avez dû", "ils_elles": "ont dû"},
        ]
    },
]
