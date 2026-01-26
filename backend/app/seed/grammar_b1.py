"""
B1 Level Grammar - Intermediate
Alliance Française B100-B105 equivalent
"""

GRAMMAR_B1 = [
    {
        "topic": "imparfait",
        "title": "L'Imparfait (Imperfect Tense)",
        "explanation_en": "The imparfait describes ongoing past actions, habitual actions in the past, or background descriptions. It's formed by taking the nous form of the present tense, removing -ons, and adding: -ais, -ais, -ait, -ions, -iez, -aient.",
        "explanation_fr": "L'imparfait décrit des actions passées continues, des habitudes passées, ou des descriptions. On forme l'imparfait avec le radical de 'nous' au présent + les terminaisons.",
        "examples": [
            {"french": "Quand j'étais jeune, j'habitais à Paris.", "english": "When I was young, I lived in Paris.", "spanish": "Cuando era joven, vivía en París."},
            {"french": "Il faisait beau et les oiseaux chantaient.", "english": "The weather was nice and the birds were singing.", "spanish": "Hacía buen tiempo y los pájaros cantaban."},
            {"french": "Nous allions à la plage chaque été.", "english": "We used to go to the beach every summer.", "spanish": "Íbamos a la playa cada verano."}
        ],
        "tips": [
            "The only irregular verb in imparfait is 'être': j'étais, tu étais, il était...",
            "Use imparfait for descriptions, habits, and ongoing actions in the past",
            "The endings are the same for all verbs: -ais, -ais, -ait, -ions, -iez, -aient"
        ],
        "spanish_comparison": "Very similar to Spanish imperfect tense. French 'j'habitais' = Spanish 'yo vivía'. The uses are almost identical."
    },
    {
        "topic": "passe_compose_vs_imparfait",
        "title": "Passé Composé vs Imparfait",
        "explanation_en": "Use passé composé for completed actions with a clear beginning/end, and imparfait for ongoing states, habits, or background. Often used together: imparfait sets the scene while passé composé describes what happened.",
        "explanation_fr": "Le passé composé exprime des actions terminées. L'imparfait décrit le contexte ou les habitudes. Souvent utilisés ensemble dans un récit.",
        "examples": [
            {"french": "Je lisais quand le téléphone a sonné.", "english": "I was reading when the phone rang.", "spanish": "Estaba leyendo cuando sonó el teléfono."},
            {"french": "Il pleuvait, alors j'ai pris un parapluie.", "english": "It was raining, so I took an umbrella.", "spanish": "Estaba lloviendo, así que tomé un paraguas."},
            {"french": "Hier, j'ai mangé au restaurant. C'était délicieux.", "english": "Yesterday, I ate at a restaurant. It was delicious.", "spanish": "Ayer, comí en un restaurante. Estaba delicioso."}
        ],
        "tips": [
            "Time markers: 'soudain', 'tout à coup' usually signal passé composé",
            "Duration/habit markers: 'toujours', 'souvent', 'd'habitude' signal imparfait",
            "Think: completed action (PC) vs. background/description (imparfait)"
        ],
        "spanish_comparison": "Same distinction as Spanish pretérito vs imperfecto. 'Mientras caminaba, vi a mi amigo' = 'Pendant que je marchais, j'ai vu mon ami'."
    },
    {
        "topic": "futur_simple",
        "title": "Le Futur Simple (Simple Future)",
        "explanation_en": "The futur simple expresses future actions. For regular verbs, add endings to the infinitive: -ai, -as, -a, -ons, -ez, -ont. For -re verbs, drop the final 'e' first. Many common verbs have irregular stems.",
        "explanation_fr": "Le futur simple exprime des actions futures. Formation: infinitif + terminaisons du futur. Les verbes en -re perdent le 'e' final.",
        "examples": [
            {"french": "Demain, je parlerai avec mon professeur.", "english": "Tomorrow, I will speak with my teacher.", "spanish": "Mañana, hablaré con mi profesor."},
            {"french": "Nous irons en France l'année prochaine.", "english": "We will go to France next year.", "spanish": "Iremos a Francia el año próximo."},
            {"french": "Quand tu arriveras, appelle-moi.", "english": "When you arrive, call me.", "spanish": "Cuando llegues, llámame."}
        ],
        "tips": [
            "Irregular stems to memorize: être→ser-, avoir→aur-, aller→ir-, faire→fer-, venir→viendr-",
            "The endings are always the same: -ai, -as, -a, -ons, -ez, -ont",
            "After 'quand' (when), use futur simple in French (unlike English)"
        ],
        "spanish_comparison": "Very similar to Spanish future tense. The endings are nearly identical: hablaré/parlerai, hablarás/parleras, etc."
    },
    {
        "topic": "conditionnel_present",
        "title": "Le Conditionnel Présent (Present Conditional)",
        "explanation_en": "The conditional expresses hypothetical situations, polite requests, or reported speech. Use the futur simple stem + imparfait endings: -ais, -ais, -ait, -ions, -iez, -aient.",
        "explanation_fr": "Le conditionnel exprime des situations hypothétiques, des demandes polies, ou le discours indirect. Formation: radical du futur + terminaisons de l'imparfait.",
        "examples": [
            {"french": "Je voudrais un café, s'il vous plaît.", "english": "I would like a coffee, please.", "spanish": "Querría un café, por favor."},
            {"french": "Si j'avais de l'argent, j'achèterais une maison.", "english": "If I had money, I would buy a house.", "spanish": "Si tuviera dinero, compraría una casa."},
            {"french": "Pourriez-vous m'aider?", "english": "Could you help me?", "spanish": "¿Podría ayudarme?"}
        ],
        "tips": [
            "For polite requests, use conditional of 'vouloir', 'pouvoir', or 'aimer'",
            "In 'si' clauses: si + imparfait → conditionnel (just like Spanish)",
            "Same irregular stems as futur simple"
        ],
        "spanish_comparison": "Identical function to Spanish conditional. 'Je voudrais' = 'Querría', 'Je pourrais' = 'Podría'. Si clause structure is the same."
    },
    {
        "topic": "pronoms_relatifs",
        "title": "Relative Pronouns: qui, que, où, dont",
        "explanation_en": "'Qui' replaces a subject, 'que' replaces a direct object, 'où' indicates place/time, and 'dont' replaces 'de + noun'. These connect clauses and avoid repetition.",
        "explanation_fr": "'Qui' remplace un sujet, 'que' un objet direct, 'où' indique le lieu/temps, 'dont' remplace 'de + nom'. Ils relient les propositions.",
        "examples": [
            {"french": "L'homme qui parle est mon père.", "english": "The man who is speaking is my father.", "spanish": "El hombre que habla es mi padre."},
            {"french": "Le livre que j'ai lu était intéressant.", "english": "The book that I read was interesting.", "spanish": "El libro que leí era interesante."},
            {"french": "La ville où j'habite est belle.", "english": "The city where I live is beautiful.", "spanish": "La ciudad donde vivo es bonita."},
            {"french": "C'est le film dont je t'ai parlé.", "english": "That's the movie I told you about.", "spanish": "Es la película de la que te hablé."}
        ],
        "tips": [
            "'Qui' is always followed by a verb (it's the subject)",
            "'Que' is followed by a subject + verb (it's the object)",
            "'Dont' replaces expressions with 'de': parler de, avoir besoin de, etc."
        ],
        "spanish_comparison": "'Qui' and 'que' both translate to Spanish 'que', but French distinguishes subject vs object. 'Où' = 'donde'. 'Dont' = 'del que/de la que/cuyo'."
    },
    {
        "topic": "pronoms_y_en",
        "title": "Pronouns Y and EN",
        "explanation_en": "'Y' replaces à + noun (place or thing) and 'en' replaces de + noun (partitive quantities). They go before the verb in most tenses.",
        "explanation_fr": "'Y' remplace à + nom (lieu ou chose). 'En' remplace de + nom (quantités). Ils se placent avant le verbe.",
        "examples": [
            {"french": "Tu vas à Paris? - Oui, j'y vais.", "english": "Are you going to Paris? - Yes, I'm going there.", "spanish": "¿Vas a París? - Sí, voy (allí)."},
            {"french": "Tu penses à ton travail? - Oui, j'y pense.", "english": "Are you thinking about your work? - Yes, I'm thinking about it.", "spanish": "¿Piensas en tu trabajo? - Sí, pienso en ello."},
            {"french": "Tu veux du café? - Oui, j'en veux.", "english": "Do you want coffee? - Yes, I want some.", "spanish": "¿Quieres café? - Sí, quiero."},
            {"french": "Combien de livres as-tu? - J'en ai trois.", "english": "How many books do you have? - I have three.", "spanish": "¿Cuántos libros tienes? - Tengo tres."}
        ],
        "tips": [
            "'Y' = there (places) or it (à + thing)",
            "'En' = some/any (partitive) or of it/them (quantities)",
            "Position: before verb, but after subject in affirmative"
        ],
        "spanish_comparison": "Spanish doesn't have direct equivalents. 'Y' is somewhat like Spanish 'allí/ahí' but used more broadly. 'En' has no Spanish equivalent - Spanish often omits this pronoun."
    },
    {
        "topic": "subjonctif_introduction",
        "title": "Introduction to Subjunctive",
        "explanation_en": "The subjunctive mood expresses doubt, desire, emotion, necessity, or uncertainty. It's used after certain expressions like 'il faut que', 'je veux que', 'je suis content que'. Formation: take ils/elles present stem + -e, -es, -e, -ions, -iez, -ent.",
        "explanation_fr": "Le subjonctif exprime le doute, le désir, l'émotion, la nécessité. On l'utilise après certaines expressions. Formation: radical de ils/elles au présent + terminaisons.",
        "examples": [
            {"french": "Il faut que tu fasses tes devoirs.", "english": "You must do your homework.", "spanish": "Es necesario que hagas tus deberes."},
            {"french": "Je veux que tu viennes avec moi.", "english": "I want you to come with me.", "spanish": "Quiero que vengas conmigo."},
            {"french": "Je suis content qu'il soit là.", "english": "I'm happy he's here.", "spanish": "Me alegro de que esté aquí."}
        ],
        "tips": [
            "Triggers: il faut que, vouloir que, souhaiter que, avoir peur que, être content/triste que",
            "Common irregular subjunctives: être→sois, avoir→aie, aller→aille, faire→fasse",
            "After 'que' with expressions of will/emotion/doubt"
        ],
        "spanish_comparison": "Very similar to Spanish subjunctive! Same triggers: 'quiero que' = 'je veux que', 'es necesario que' = 'il faut que'. Your Spanish knowledge is a huge advantage here."
    },
    {
        "topic": "discours_indirect",
        "title": "Indirect Speech (Reported Speech)",
        "explanation_en": "When reporting what someone said, use 'que' after verbs like 'dire', 'penser', 'croire'. Tenses shift when the main verb is past: present→imparfait, passé composé→plus-que-parfait, futur→conditionnel.",
        "explanation_fr": "Pour rapporter les paroles de quelqu'un, on utilise 'que' après les verbes comme 'dire', 'penser'. Les temps changent quand le verbe principal est au passé.",
        "examples": [
            {"french": "Il dit qu'il est fatigué.", "english": "He says (that) he is tired.", "spanish": "Dice que está cansado."},
            {"french": "Elle a dit qu'elle viendrait demain.", "english": "She said she would come tomorrow.", "spanish": "Dijo que vendría mañana."},
            {"french": "Je pensais que tu avais fini.", "english": "I thought you had finished.", "spanish": "Pensaba que habías terminado."}
        ],
        "tips": [
            "Main verb present → no tense change in subordinate clause",
            "Main verb past → tenses shift back (concordance des temps)",
            "Question words change: 'Est-ce que tu viens?' → 'Je demande si tu viens.'"
        ],
        "spanish_comparison": "Same tense-shifting rules as Spanish. 'Dijo que vendría' = 'Il a dit qu'il viendrait'. The sequence of tenses is identical."
    }
]
