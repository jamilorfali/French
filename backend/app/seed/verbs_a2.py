"""
A2 Level Verbs - Elementary
Alliance Française A200-A205 equivalent
Focus on passé composé, imparfait introduction, and more irregular verbs
"""

VERBS_A2 = [
    # Note: venir, prendre, savoir, devoir are already defined in A1
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
]
