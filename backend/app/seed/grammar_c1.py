"""
C1 Level Grammar - Advanced
Alliance Française C100-C105 equivalent
"""

GRAMMAR_C1 = [
    {
        "topic": "passe_simple",
        "title": "Le Passé Simple (Literary Past Tense)",
        "explanation_en": "The passé simple is a literary tense used in formal writing, literature, and historical narratives. It replaces the passé composé in written French. Regular endings: -er verbs (-ai, -as, -a, -âmes, -âtes, -èrent), -ir/-re verbs (-is, -is, -it, -îmes, -îtes, -irent).",
        "explanation_fr": "Le passé simple est un temps littéraire utilisé dans l'écriture formelle et les récits historiques. Il remplace le passé composé à l'écrit.",
        "examples": [
            {"french": "Il entra dans la pièce et s'assit.", "english": "He entered the room and sat down.", "spanish": "Entró en la habitación y se sentó."},
            {"french": "La révolution française commença en 1789.", "english": "The French Revolution began in 1789.", "spanish": "La revolución francesa comenzó en 1789."},
            {"french": "Soudain, il comprit la vérité.", "english": "Suddenly, he understood the truth.", "spanish": "De repente, comprendió la verdad."}
        ],
        "tips": [
            "You only need to recognize passé simple, not produce it in speaking",
            "Common in novels, history books, fairy tales, and news reports",
            "Many irregular forms: être→fut, avoir→eut, faire→fit, venir→vint"
        ],
        "spanish_comparison": "Very similar to Spanish pretérito indefinido. 'Entró' = 'il entra', 'habló' = 'il parla'. The function is identical - completed past actions in narrative."
    },
    {
        "topic": "subjonctif_passe",
        "title": "Le Subjonctif Passé (Past Subjunctive)",
        "explanation_en": "The past subjunctive expresses doubt, emotion, or necessity about a past action. Formation: subjunctive of avoir/être + past participle. Used when the subordinate action happened before the main clause.",
        "explanation_fr": "Le subjonctif passé exprime le doute, l'émotion ou la nécessité concernant une action passée. Formation: subjonctif de avoir/être + participe passé.",
        "examples": [
            {"french": "Je suis content qu'il soit venu.", "english": "I'm happy that he came.", "spanish": "Me alegro de que haya venido."},
            {"french": "Il est possible qu'elle ait oublié.", "english": "It's possible she forgot.", "spanish": "Es posible que haya olvidado."},
            {"french": "Bien qu'il ait travaillé dur, il a échoué.", "english": "Although he worked hard, he failed.", "spanish": "Aunque haya trabajado duro, fracasó."}
        ],
        "tips": [
            "Same triggers as present subjunctive, but for past actions",
            "Main verb can be present or past",
            "'Que' + avoir/être in subjunctive + past participle"
        ],
        "spanish_comparison": "Identical to Spanish subjuntivo perfecto: 'haya venido' = 'qu'il soit venu'. Same usage and triggers."
    },
    {
        "topic": "subjonctif_imparfait",
        "title": "Le Subjonctif Imparfait (Imperfect Subjunctive)",
        "explanation_en": "The imperfect subjunctive is a literary tense, used in very formal writing when the main verb is in a past tense. Formation: passé simple stem + -sse, -sses, -^t, -ssions, -ssiez, -ssent.",
        "explanation_fr": "Le subjonctif imparfait est un temps littéraire, utilisé à l'écrit formel quand le verbe principal est au passé.",
        "examples": [
            {"french": "Il voulait qu'elle vînt. (literary)", "english": "He wanted her to come.", "spanish": "Quería que viniera."},
            {"french": "Je craignais qu'il ne fût trop tard.", "english": "I feared it might be too late.", "spanish": "Temía que fuera demasiado tarde."},
            {"french": "Bien qu'il fît froid, nous sortîmes.", "english": "Although it was cold, we went out.", "spanish": "Aunque hiciera frío, salimos."}
        ],
        "tips": [
            "Recognition only - you'll encounter it in literature",
            "In modern spoken/written French, subjonctif présent is used instead",
            "The circumflex accent on 3rd person singular: qu'il fût, qu'il vînt"
        ],
        "spanish_comparison": "Functions like Spanish imperfect subjunctive (-ra/-se forms). 'Quisiera que viniera' = literary 'Je voudrais qu'il vînt'. Modern French uses present subjunctive where Spanish still uses imperfect."
    },
    {
        "topic": "discours_indirect_advanced",
        "title": "Advanced Reported Speech",
        "explanation_en": "Complex reported speech includes questions, commands, and multiple tense shifts. Questions become si-clauses or interrogative words + declarative order. Commands become de + infinitive.",
        "explanation_fr": "Le discours indirect complexe inclut les questions, les ordres, et les concordances de temps multiples.",
        "examples": [
            {"french": "Il m'a demandé si j'avais fini. (← As-tu fini?)", "english": "He asked me if I had finished.", "spanish": "Me preguntó si había terminado."},
            {"french": "Elle a demandé où j'allais. (← Où vas-tu?)", "english": "She asked where I was going.", "spanish": "Preguntó adónde iba."},
            {"french": "Il m'a dit de partir. (← Pars!)", "english": "He told me to leave.", "spanish": "Me dijo que me fuera."},
            {"french": "Il a annoncé qu'il partirait le lendemain.", "english": "He announced he would leave the next day.", "spanish": "Anunció que partiría al día siguiente."}
        ],
        "tips": [
            "Yes/no questions → si clause",
            "Information questions → interrogative word + declarative order",
            "Commands → de + infinitive",
            "Time expressions change: demain→le lendemain, hier→la veille"
        ],
        "spanish_comparison": "Same rules as Spanish. 'Me preguntó si...' = 'Il m'a demandé si...'. Time expression shifts are parallel: mañana→al día siguiente, ayer→el día anterior."
    },
    {
        "topic": "negation_avancee",
        "title": "Advanced Negation",
        "explanation_en": "Beyond ne...pas, French has nuanced negative expressions: ne...guère (hardly), ne...point (not at all - literary), ne...nullement (in no way), ne...aucunement (in no way). The expletive 'ne' appears after certain verbs without negative meaning.",
        "explanation_fr": "Au-delà de ne...pas, le français a des négations nuancées. Le 'ne' explétif apparaît après certains verbes sans sens négatif.",
        "examples": [
            {"french": "Il ne mange guère.", "english": "He hardly eats.", "spanish": "Apenas come."},
            {"french": "Je n'y comprends rien.", "english": "I don't understand any of it.", "spanish": "No entiendo nada de eso."},
            {"french": "Je crains qu'il ne vienne. (expletive ne)", "english": "I fear he might come.", "spanish": "Temo que venga."},
            {"french": "Il est plus intelligent qu'on ne le pense. (expletive ne)", "english": "He is smarter than people think.", "spanish": "Es más inteligente de lo que se piensa."}
        ],
        "tips": [
            "'Ne...guère' is more literary than 'ne...pas beaucoup'",
            "Expletive 'ne' after: craindre que, avant que, à moins que, comparatives",
            "The expletive 'ne' adds no negative meaning - it's stylistic"
        ],
        "spanish_comparison": "Spanish doesn't have expletive negation like French. 'Temo que venga' = 'Je crains qu'il ne vienne' - the French 'ne' has no Spanish equivalent."
    },
    {
        "topic": "participe_present_adjectif_verbal",
        "title": "Participe Présent vs Adjectif Verbal",
        "explanation_en": "The present participle (-ant) describes an action and is invariable. The verbal adjective (same form) describes a quality and agrees in gender/number. Some have different spellings: fatigant/fatiguant, négligeant/négligent.",
        "explanation_fr": "Le participe présent décrit une action (invariable). L'adjectif verbal décrit une qualité (accordé en genre/nombre). Certains ont des orthographes différentes.",
        "examples": [
            {"french": "Les enfants, courant dans le jardin, riaient. (participle)", "english": "The children, running in the garden, were laughing.", "spanish": "Los niños, corriendo en el jardín, reían."},
            {"french": "C'est une histoire passionnante. (adjective)", "english": "It's an exciting story.", "spanish": "Es una historia apasionante."},
            {"french": "Fatigant les élèves, le professeur parlait. (participle: -gant)", "english": "Tiring the students, the teacher spoke.", "spanish": "Cansando a los alumnos, el profesor hablaba."},
            {"french": "C'est un travail fatiguant. (adjective: -guant)", "english": "It's tiring work.", "spanish": "Es un trabajo agotador."}
        ],
        "tips": [
            "Participle: describes ongoing action, invariable",
            "Verbal adjective: describes quality, agrees with noun",
            "Spelling differences exist for some pairs (navigation required)"
        ],
        "spanish_comparison": "Spanish gerund is always invariable, but the distinction exists with past participles used as adjectives. French is more complex with present participles."
    },
    {
        "topic": "concession_opposition",
        "title": "Concession and Opposition",
        "explanation_en": "Advanced concessive structures express 'although/despite': bien que/quoique (+ subjunctive), même si (+ indicative), avoir beau (+ infinitive), en dépit de/malgré (+ noun). Each has different nuances.",
        "explanation_fr": "Les structures concessives avancées expriment 'bien que/malgré': bien que/quoique (+ subjonctif), même si (+ indicatif), avoir beau (+ infinitif).",
        "examples": [
            {"french": "Bien qu'il soit malade, il travaille.", "english": "Although he is sick, he works.", "spanish": "Aunque esté enfermo, trabaja."},
            {"french": "Même s'il pleut, je sors.", "english": "Even if it rains, I'm going out.", "spanish": "Aunque llueva, salgo."},
            {"french": "J'ai beau essayer, je n'y arrive pas.", "english": "No matter how hard I try, I can't do it.", "spanish": "Por más que intente, no lo logro."},
            {"french": "Malgré ses efforts, il a échoué.", "english": "Despite his efforts, he failed.", "spanish": "A pesar de sus esfuerzos, fracasó."}
        ],
        "tips": [
            "'Bien que/quoique' + subjunctive (formal)",
            "'Même si' + indicative (hypothetical/real)",
            "'Avoir beau' + infinitive = 'no matter how much' (emphasis on futility)"
        ],
        "spanish_comparison": "'Bien que' = 'aunque' with subjunctive. 'Même si' = 'aunque' with indicative. 'Avoir beau' has no direct Spanish equivalent - closest is 'por más que'."
    },
    {
        "topic": "infinitif_passe",
        "title": "L'Infinitif Passé (Past Infinitive)",
        "explanation_en": "The past infinitive (avoir/être + past participle) expresses a completed action before another. Common after 'après', 'pour', 'sans'. It shows anteriority without conjugating a verb.",
        "explanation_fr": "L'infinitif passé (avoir/être + participe passé) exprime une action achevée avant une autre. Fréquent après 'après', 'pour', 'sans'.",
        "examples": [
            {"french": "Après avoir mangé, il est parti.", "english": "After eating, he left.", "spanish": "Después de haber comido, se fue."},
            {"french": "Elle regrette d'être partie.", "english": "She regrets having left.", "spanish": "Lamenta haberse ido."},
            {"french": "Sans avoir compris, il a signé.", "english": "Without having understood, he signed.", "spanish": "Sin haber entendido, firmó."},
            {"french": "Il est accusé d'avoir menti.", "english": "He is accused of having lied.", "spanish": "Es acusado de haber mentido."}
        ],
        "tips": [
            "Use after 'après' to show sequence",
            "Same être/avoir rules as passé composé",
            "Participle agrees with subject when using être"
        ],
        "spanish_comparison": "Identical to Spanish 'haber + participio': 'después de haber llegado' = 'après être arrivé'. Same usage and meaning."
    }
]
