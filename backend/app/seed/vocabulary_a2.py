"""
A2 Level Vocabulary - Elementary
Alliance Française A200-A205 equivalent
"""

VOCABULARY_A2 = [
    # Daily Routines & Activities
    {"french": "se réveiller", "english": "to wake up", "spanish": "despertarse", "gender": "-", "part_of_speech": "verb", "category": "daily_routines", "is_cognate": False, "example_french": "Je me réveille à sept heures.", "example_english": "I wake up at seven o'clock."},
    {"french": "se coucher", "english": "to go to bed", "spanish": "acostarse", "gender": "-", "part_of_speech": "verb", "category": "daily_routines", "is_cognate": False, "example_french": "Elle se couche tard.", "example_english": "She goes to bed late."},
    {"french": "se doucher", "english": "to shower", "spanish": "ducharse", "gender": "-", "part_of_speech": "verb", "category": "daily_routines", "is_cognate": False},
    {"french": "se brosser les dents", "english": "to brush one's teeth", "spanish": "cepillarse los dientes", "gender": "-", "part_of_speech": "phrase", "category": "daily_routines", "is_cognate": False},
    {"french": "s'habiller", "english": "to get dressed", "spanish": "vestirse", "gender": "-", "part_of_speech": "verb", "category": "daily_routines", "is_cognate": False},

    # Shopping & Commerce
    {"french": "le magasin", "english": "store/shop", "spanish": "la tienda", "gender": "m", "part_of_speech": "noun", "category": "shopping", "is_cognate": False, "example_french": "Le magasin ouvre à neuf heures.", "example_english": "The store opens at nine o'clock."},
    {"french": "la boulangerie", "english": "bakery", "spanish": "la panadería", "gender": "f", "part_of_speech": "noun", "category": "shopping", "is_cognate": False},
    {"french": "la pharmacie", "english": "pharmacy", "spanish": "la farmacia", "gender": "f", "part_of_speech": "noun", "category": "shopping", "is_cognate": True, "cognate_spanish": "farmacia"},
    {"french": "le supermarché", "english": "supermarket", "spanish": "el supermercado", "gender": "m", "part_of_speech": "noun", "category": "shopping", "is_cognate": True, "cognate_spanish": "supermercado"},
    {"french": "acheter", "english": "to buy", "spanish": "comprar", "gender": "-", "part_of_speech": "verb", "category": "shopping", "is_cognate": False},
    {"french": "vendre", "english": "to sell", "spanish": "vender", "gender": "-", "part_of_speech": "verb", "category": "shopping", "is_cognate": True, "cognate_spanish": "vender"},
    {"french": "le prix", "english": "price", "spanish": "el precio", "gender": "m", "part_of_speech": "noun", "category": "shopping", "is_cognate": True, "cognate_spanish": "precio"},
    {"french": "cher", "english": "expensive", "spanish": "caro", "gender": "m", "part_of_speech": "adjective", "category": "shopping", "is_cognate": False},
    {"french": "bon marché", "english": "cheap/inexpensive", "spanish": "barato", "gender": "-", "part_of_speech": "adjective", "category": "shopping", "is_cognate": False},

    # Transportation
    {"french": "le train", "english": "train", "spanish": "el tren", "gender": "m", "part_of_speech": "noun", "category": "transportation", "is_cognate": True, "cognate_spanish": "tren"},
    {"french": "le bus", "english": "bus", "spanish": "el autobús", "gender": "m", "part_of_speech": "noun", "category": "transportation", "is_cognate": True, "cognate_spanish": "bus"},
    {"french": "le métro", "english": "subway/metro", "spanish": "el metro", "gender": "m", "part_of_speech": "noun", "category": "transportation", "is_cognate": True, "cognate_spanish": "metro"},
    {"french": "l'avion", "english": "airplane", "spanish": "el avión", "gender": "m", "part_of_speech": "noun", "category": "transportation", "is_cognate": True, "cognate_spanish": "avión"},
    {"french": "le billet", "english": "ticket", "spanish": "el billete", "gender": "m", "part_of_speech": "noun", "category": "transportation", "is_cognate": True, "cognate_spanish": "billete"},
    {"french": "la gare", "english": "train station", "spanish": "la estación", "gender": "f", "part_of_speech": "noun", "category": "transportation", "is_cognate": False},
    {"french": "l'aéroport", "english": "airport", "spanish": "el aeropuerto", "gender": "m", "part_of_speech": "noun", "category": "transportation", "is_cognate": True, "cognate_spanish": "aeropuerto"},
    {"french": "partir", "english": "to leave/depart", "spanish": "partir", "gender": "-", "part_of_speech": "verb", "category": "transportation", "is_cognate": True, "cognate_spanish": "partir"},
    {"french": "arriver", "english": "to arrive", "spanish": "llegar", "gender": "-", "part_of_speech": "verb", "category": "transportation", "is_cognate": False},

    # Weather
    {"french": "le temps", "english": "weather/time", "spanish": "el tiempo", "gender": "m", "part_of_speech": "noun", "category": "weather", "is_cognate": True, "cognate_spanish": "tiempo"},
    {"french": "il fait beau", "english": "it's nice weather", "spanish": "hace buen tiempo", "gender": "-", "part_of_speech": "phrase", "category": "weather", "is_cognate": False},
    {"french": "il fait chaud", "english": "it's hot", "spanish": "hace calor", "gender": "-", "part_of_speech": "phrase", "category": "weather", "is_cognate": False},
    {"french": "il fait froid", "english": "it's cold", "spanish": "hace frío", "gender": "-", "part_of_speech": "phrase", "category": "weather", "is_cognate": False},
    {"french": "il pleut", "english": "it's raining", "spanish": "llueve", "gender": "-", "part_of_speech": "phrase", "category": "weather", "is_cognate": False},
    {"french": "il neige", "english": "it's snowing", "spanish": "nieva", "gender": "-", "part_of_speech": "phrase", "category": "weather", "is_cognate": False},
    {"french": "le soleil", "english": "sun", "spanish": "el sol", "gender": "m", "part_of_speech": "noun", "category": "weather", "is_cognate": True, "cognate_spanish": "sol"},
    {"french": "la pluie", "english": "rain", "spanish": "la lluvia", "gender": "f", "part_of_speech": "noun", "category": "weather", "is_cognate": False},
    {"french": "le nuage", "english": "cloud", "spanish": "la nube", "gender": "m", "part_of_speech": "noun", "category": "weather", "is_cognate": False},

    # Health & Body
    {"french": "la tête", "english": "head", "spanish": "la cabeza", "gender": "f", "part_of_speech": "noun", "category": "health", "is_cognate": False},
    {"french": "le bras", "english": "arm", "spanish": "el brazo", "gender": "m", "part_of_speech": "noun", "category": "health", "is_cognate": True, "cognate_spanish": "brazo"},
    {"french": "la jambe", "english": "leg", "spanish": "la pierna", "gender": "f", "part_of_speech": "noun", "category": "health", "is_cognate": False},
    {"french": "le dos", "english": "back", "spanish": "la espalda", "gender": "m", "part_of_speech": "noun", "category": "health", "is_cognate": False},
    {"french": "avoir mal", "english": "to hurt/have pain", "spanish": "tener dolor", "gender": "-", "part_of_speech": "phrase", "category": "health", "is_cognate": False, "example_french": "J'ai mal à la tête.", "example_english": "I have a headache."},
    {"french": "le médecin", "english": "doctor", "spanish": "el médico", "gender": "m", "part_of_speech": "noun", "category": "health", "is_cognate": True, "cognate_spanish": "médico"},
    {"french": "malade", "english": "sick/ill", "spanish": "enfermo", "gender": "-", "part_of_speech": "adjective", "category": "health", "is_cognate": False},
    {"french": "la santé", "english": "health", "spanish": "la salud", "gender": "f", "part_of_speech": "noun", "category": "health", "is_cognate": False},

    # Describing People & Things
    {"french": "grand", "english": "tall/big", "spanish": "grande", "gender": "m", "part_of_speech": "adjective", "category": "descriptions", "is_cognate": True, "cognate_spanish": "grande"},
    {"french": "petit", "english": "small/short", "spanish": "pequeño", "gender": "m", "part_of_speech": "adjective", "category": "descriptions", "is_cognate": False},
    {"french": "jeune", "english": "young", "spanish": "joven", "gender": "-", "part_of_speech": "adjective", "category": "descriptions", "is_cognate": True, "cognate_spanish": "joven"},
    {"french": "vieux", "english": "old", "spanish": "viejo", "gender": "m", "part_of_speech": "adjective", "category": "descriptions", "is_cognate": True, "cognate_spanish": "viejo"},
    {"french": "beau", "english": "beautiful/handsome", "spanish": "bello", "gender": "m", "part_of_speech": "adjective", "category": "descriptions", "is_cognate": True, "cognate_spanish": "bello"},
    {"french": "nouveau", "english": "new", "spanish": "nuevo", "gender": "m", "part_of_speech": "adjective", "category": "descriptions", "is_cognate": True, "cognate_spanish": "nuevo"},
    {"french": "facile", "english": "easy", "spanish": "fácil", "gender": "-", "part_of_speech": "adjective", "category": "descriptions", "is_cognate": True, "cognate_spanish": "fácil"},
    {"french": "difficile", "english": "difficult", "spanish": "difícil", "gender": "-", "part_of_speech": "adjective", "category": "descriptions", "is_cognate": True, "cognate_spanish": "difícil"},
]
