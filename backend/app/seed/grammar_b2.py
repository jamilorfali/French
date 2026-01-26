"""
B2 Level Grammar - Upper Intermediate
Alliance Française B200-B205 equivalent
"""

GRAMMAR_B2 = [
    {
        "topic": "subjonctif_advanced",
        "title": "Advanced Subjunctive Uses",
        "explanation_en": "Beyond basic triggers, subjunctive is used after: conjunctions (bien que, pour que, avant que, sans que), superlatives (le meilleur que), and expressions of uniqueness (le seul qui). Also after negative/indefinite antecedents.",
        "explanation_fr": "Le subjonctif s'utilise après certaines conjonctions, les superlatifs, et les expressions d'unicité. Aussi après des antécédents négatifs ou indéfinis.",
        "examples": [
            {"french": "Bien qu'il soit riche, il n'est pas heureux.", "english": "Although he is rich, he is not happy.", "spanish": "Aunque sea rico, no es feliz."},
            {"french": "Je travaille pour que mes enfants puissent étudier.", "english": "I work so that my children can study.", "spanish": "Trabajo para que mis hijos puedan estudiar."},
            {"french": "C'est le meilleur film que j'aie vu.", "english": "It's the best movie I've seen.", "spanish": "Es la mejor película que haya visto."},
            {"french": "Je cherche quelqu'un qui sache parler chinois.", "english": "I'm looking for someone who can speak Chinese.", "spanish": "Busco a alguien que sepa hablar chino."}
        ],
        "tips": [
            "Conjunctions requiring subjunctive: bien que, quoique, pour que, afin que, avant que, sans que, à moins que",
            "After superlatives: le plus/moins... que, le meilleur/pire que",
            "After le seul, l'unique, le premier, le dernier + qui/que"
        ],
        "spanish_comparison": "Same usage as Spanish subjunctive! 'Aunque sea' = 'bien qu'il soit', 'para que pueda' = 'pour qu'il puisse'. Your Spanish intuition applies directly."
    },
    {
        "topic": "plus_que_parfait",
        "title": "Le Plus-que-parfait (Pluperfect)",
        "explanation_en": "The plus-que-parfait describes actions completed before another past action. Formation: imparfait of avoir/être + past participle. It's the 'past of the past'.",
        "explanation_fr": "Le plus-que-parfait décrit des actions terminées avant une autre action passée. Formation: auxiliaire à l'imparfait + participe passé.",
        "examples": [
            {"french": "Quand je suis arrivé, il était déjà parti.", "english": "When I arrived, he had already left.", "spanish": "Cuando llegué, él ya había salido."},
            {"french": "Elle m'a dit qu'elle avait fini son travail.", "english": "She told me she had finished her work.", "spanish": "Me dijo que había terminado su trabajo."},
            {"french": "Je ne savais pas qu'ils s'étaient mariés.", "english": "I didn't know they had gotten married.", "spanish": "No sabía que se habían casado."}
        ],
        "tips": [
            "Same auxiliary (avoir/être) as passé composé",
            "Use for reported speech when main verb is past",
            "Marks the 'earlier' past in a sequence of past events"
        ],
        "spanish_comparison": "Identical to Spanish pluscuamperfecto: 'había llegado' = 'j'étais arrivé', 'había comido' = 'j'avais mangé'. Same function and usage."
    },
    {
        "topic": "conditionnel_passe",
        "title": "Le Conditionnel Passé (Past Conditional)",
        "explanation_en": "The past conditional expresses what would have happened. Formation: conditional of avoir/être + past participle. Used in hypothetical past situations and to express regret.",
        "explanation_fr": "Le conditionnel passé exprime ce qui aurait pu se passer. Formation: conditionnel de avoir/être + participe passé. Utilisé pour les situations hypothétiques passées.",
        "examples": [
            {"french": "Si j'avais su, je serais venu plus tôt.", "english": "If I had known, I would have come earlier.", "spanish": "Si hubiera sabido, habría venido antes."},
            {"french": "J'aurais aimé voyager plus.", "english": "I would have liked to travel more.", "spanish": "Me habría gustado viajar más."},
            {"french": "Elle aurait dû appeler avant de venir.", "english": "She should have called before coming.", "spanish": "Debería haber llamado antes de venir."}
        ],
        "tips": [
            "Si + plus-que-parfait → conditionnel passé (for unreal past)",
            "'J'aurais dû' = I should have, 'J'aurais pu' = I could have",
            "Often expresses regret or criticism of past actions"
        ],
        "spanish_comparison": "Works like Spanish 'habría + participle'. 'Habría comido' = 'j'aurais mangé'. The si-clause structure is identical to Spanish."
    },
    {
        "topic": "passive_voice",
        "title": "La Voix Passive (Passive Voice)",
        "explanation_en": "Passive voice emphasizes the action recipient. Formation: être (in any tense) + past participle + par (by). The participle agrees with the subject in gender and number.",
        "explanation_fr": "La voix passive met l'accent sur le sujet qui subit l'action. Formation: être + participe passé + par. Le participe s'accorde avec le sujet.",
        "examples": [
            {"french": "Le livre a été écrit par Victor Hugo.", "english": "The book was written by Victor Hugo.", "spanish": "El libro fue escrito por Victor Hugo."},
            {"french": "La maison sera construite l'année prochaine.", "english": "The house will be built next year.", "spanish": "La casa será construida el año próximo."},
            {"french": "Les étudiants sont informés des résultats.", "english": "The students are informed of the results.", "spanish": "Los estudiantes son informados de los resultados."}
        ],
        "tips": [
            "Passive is less common in French than in English",
            "Alternative: use 'on' (On parle français ici = French is spoken here)",
            "Participle must agree: 'Elle a été invitée' (feminine)"
        ],
        "spanish_comparison": "Very similar structure to Spanish passive with 'ser'. 'Fue escrito' = 'a été écrit'. French also uses reflexive passive like Spanish 'se habla'."
    },
    {
        "topic": "faire_causatif",
        "title": "Faire Causatif (Causative Construction)",
        "explanation_en": "Use 'faire + infinitive' to express having something done by someone else. The structure indicates that the subject causes an action to happen rather than doing it themselves.",
        "explanation_fr": "On utilise 'faire + infinitif' pour exprimer qu'on fait faire quelque chose par quelqu'un d'autre. Le sujet cause l'action sans l'exécuter lui-même.",
        "examples": [
            {"french": "Je fais réparer ma voiture.", "english": "I'm having my car repaired.", "spanish": "Hago reparar mi coche."},
            {"french": "Elle a fait construire une maison.", "english": "She had a house built.", "spanish": "Ella hizo construir una casa."},
            {"french": "Il nous fait attendre.", "english": "He's making us wait.", "spanish": "Nos hace esperar."}
        ],
        "tips": [
            "Object pronouns go before 'faire': 'Je la fais réparer'",
            "Past participle 'fait' is invariable in this construction",
            "'Se faire' = to have something done to oneself: 'Je me fais couper les cheveux'"
        ],
        "spanish_comparison": "Identical to Spanish 'hacer + infinitive'. 'Hacer construir' = 'faire construire'. The structure and meaning are the same."
    },
    {
        "topic": "gerondif",
        "title": "Le Gérondif (Present Participle)",
        "explanation_en": "The gérondif (en + present participle) expresses simultaneous actions, manner, or condition. Formation: en + verb stem (nous form without -ons) + -ant.",
        "explanation_fr": "Le gérondif (en + participe présent) exprime la simultanéité, la manière ou la condition. Formation: en + radical de 'nous' + -ant.",
        "examples": [
            {"french": "Il écoute de la musique en travaillant.", "english": "He listens to music while working.", "spanish": "Escucha música mientras trabaja."},
            {"french": "En apprenant le français, j'ai découvert la culture.", "english": "By learning French, I discovered the culture.", "spanish": "Al aprender francés, descubrí la cultura."},
            {"french": "C'est en forgeant qu'on devient forgeron.", "english": "Practice makes perfect. (By forging, one becomes a blacksmith)", "spanish": "La práctica hace al maestro."}
        ],
        "tips": [
            "Only three irregular forms: étant (être), ayant (avoir), sachant (savoir)",
            "The subject of gérondif must be the same as the main verb",
            "'Tout en' adds emphasis: 'Tout en sachant la vérité...'"
        ],
        "spanish_comparison": "Similar to Spanish gerund but used differently. French gérondif always needs 'en'. Spanish uses gerund alone more freely."
    },
    {
        "topic": "mise_en_relief",
        "title": "Mise en Relief (Emphasis Structures)",
        "explanation_en": "French uses special structures to emphasize parts of a sentence: 'C'est...qui/que' for emphasis, and dislocation (moving elements to beginning/end with pronouns).",
        "explanation_fr": "Le français utilise des structures spéciales pour mettre en valeur: 'C'est...qui/que' et la dislocation (déplacer des éléments avec des pronoms).",
        "examples": [
            {"french": "C'est Marie qui a téléphoné.", "english": "It's Marie who called.", "spanish": "Es María quien llamó."},
            {"french": "C'est ce livre que je veux.", "english": "It's this book that I want.", "spanish": "Es este libro el que quiero."},
            {"french": "Ce film, je l'ai vu trois fois.", "english": "This movie, I've seen it three times.", "spanish": "Esta película, la he visto tres veces."},
            {"french": "Il est génial, ce restaurant!", "english": "It's great, this restaurant!", "spanish": "¡Es genial este restaurante!"}
        ],
        "tips": [
            "'C'est...qui' for subject emphasis, 'C'est...que' for object",
            "Dislocation needs matching pronoun: 'Ce livre, je le lis'",
            "Very common in spoken French for natural emphasis"
        ],
        "spanish_comparison": "Spanish uses 'es...quien/que' similarly. Dislocation exists in Spanish too: 'Este libro, lo quiero'. Both languages use these for emphasis."
    },
    {
        "topic": "nominalisation",
        "title": "La Nominalisation (Creating Nouns from Verbs)",
        "explanation_en": "Nominalisation transforms verbs into nouns, common in formal/written French. Patterns include: -tion/-sion (action), -ment (process), -age (action/result), -ure (result).",
        "explanation_fr": "La nominalisation transforme les verbes en noms, fréquent dans le français formel. Suffixes: -tion/-sion (action), -ment (processus), -age (action/résultat).",
        "examples": [
            {"french": "La construction du pont a duré deux ans. (construire)", "english": "The construction of the bridge lasted two years.", "spanish": "La construcción del puente duró dos años."},
            {"french": "Le développement économique est important. (développer)", "english": "Economic development is important.", "spanish": "El desarrollo económico es importante."},
            {"french": "L'apprentissage d'une langue demande du temps. (apprendre)", "english": "Learning a language takes time.", "spanish": "El aprendizaje de un idioma requiere tiempo."}
        ],
        "tips": [
            "-tion often corresponds to Spanish -ción: construction/construcción",
            "-ment often corresponds to Spanish -miento: développement/desarrollo",
            "Essential for formal writing and academic French"
        ],
        "spanish_comparison": "Very similar patterns to Spanish! -tion = -ción, -ment = -miento/-mento. 'Construction' = 'construcción', 'développement' ≈ 'desarrollo'."
    }
]
