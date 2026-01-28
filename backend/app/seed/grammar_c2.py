"""
C2 Level Grammar - Mastery
Alliance Française C200+ equivalent
Focus on literary tenses, rare constructions, and stylistic mastery
"""

GRAMMAR_C2 = [
    {
        "topic": "passe_anterieur",
        "title": "Le Passé Antérieur (Past Anterior)",
        "explanation_en": """The passé antérieur is a literary tense expressing an action completed immediately before another past action. It's used exclusively in written French, typically with conjunctions like 'quand', 'lorsque', 'dès que', 'aussitôt que', 'après que'.

Formation: passé simple of avoir/être + past participle

| Subject | avoir | être |
|---------|-------|------|
| je | eus parlé | fus arrivé(e) |
| tu | eus parlé | fus arrivé(e) |
| il/elle | eut parlé | fut arrivé(e) |
| nous | eûmes parlé | fûmes arrivé(e)s |
| vous | eûtes parlé | fûtes arrivé(e)(s) |
| ils/elles | eurent parlé | furent arrivé(e)s |

Key usage: The main clause uses passé simple, the subordinate clause uses passé antérieur.""",
        "explanation_fr": "Le passé antérieur exprime une action achevée immédiatement avant une autre action passée. Temps exclusivement littéraire.",
        "examples": [
            {"french": "Quand il eut fini de parler, il sortit.", "english": "When he had finished speaking, he left.", "spanish": "Cuando hubo terminado de hablar, salió."},
            {"french": "Dès qu'elle fut arrivée, la fête commença.", "english": "As soon as she had arrived, the party began.", "spanish": "En cuanto hubo llegado, la fiesta comenzó."},
            {"french": "Aussitôt qu'il eut compris, il réagit.", "english": "As soon as he had understood, he reacted.", "spanish": "En cuanto hubo comprendido, reaccionó."}
        ],
        "tips": [
            "Recognition only - you'll find this in classic literature",
            "In modern French, the plus-que-parfait replaces it",
            "Always paired with passé simple in the main clause"
        ],
        "spanish_comparison": "Identical to Spanish 'pretérito anterior' (hubo llegado, hubo dicho), which is also literary and rarely used in modern Spanish."
    },
    {
        "topic": "subjonctif_plus_que_parfait",
        "title": "Le Subjonctif Plus-que-parfait (Pluperfect Subjunctive)",
        "explanation_en": """The subjonctif plus-que-parfait is a literary tense expressing hypothetical past actions or unrealized conditions. It appears in very formal writing and classic literature.

Formation: imparfait du subjonctif of avoir/être + past participle

| Subject | avoir | être |
|---------|-------|------|
| je | eusse parlé | fusse arrivé(e) |
| tu | eusses parlé | fusses arrivé(e) |
| il/elle | eût parlé | fût arrivé(e) |
| nous | eussions parlé | fussions arrivé(e)s |
| vous | eussiez parlé | fussiez arrivé(e)(s) |
| ils/elles | eussent parlé | fussent arrivé(e)s |

Used in literary conditional sentences and after main clauses in past tenses requiring subjunctive.""",
        "explanation_fr": "Le subjonctif plus-que-parfait exprime des actions hypothétiques passées. Temps exclusivement littéraire.",
        "examples": [
            {"french": "S'il eût su, il fût venu. (= S'il avait su, il serait venu)", "english": "Had he known, he would have come.", "spanish": "Si hubiera sabido, habría venido."},
            {"french": "Je regrettais qu'il ne fût pas venu.", "english": "I regretted that he hadn't come.", "spanish": "Lamentaba que no hubiera venido."},
            {"french": "Il eût fallu qu'elle eût compris.", "english": "She would have had to understand.", "spanish": "Habría sido necesario que hubiera comprendido."}
        ],
        "tips": [
            "Can replace both 'si + plus-que-parfait' AND 'conditionnel passé' in literary texts",
            "The circumflex accent is crucial: 'fût' (subjunctive) vs 'fut' (passé simple)",
            "In modern French, use conditionnel passé + plus-que-parfait"
        ],
        "spanish_comparison": "Functions like Spanish 'hubiera/hubiese + participio'. The literary French 'fût venu' = Spanish 'hubiera venido'."
    },
    {
        "topic": "inversion_stylistique",
        "title": "L'Inversion Stylistique (Stylistic Inversion)",
        "explanation_en": """In formal and literary French, subject-verb inversion creates elegant, emphatic, or dramatic effects. Unlike question inversion, stylistic inversion maintains declarative meaning.

Common contexts:
1. After certain adverbs: à peine, peut-être, aussi, encore, sans doute, ainsi, du moins, encore moins
2. In incises (reporting clauses): dit-il, répondit-elle, pensais-je
3. After direct speech
4. In relative clauses for elegance
5. After restrictive expressions: 'Seul compte...'

With compound subjects, only the pronoun inverts: 'Peut-être Pierre viendra-t-il.'""",
        "explanation_fr": "L'inversion du sujet crée des effets stylistiques de mise en relief, d'élégance ou d'emphase dans le français soutenu.",
        "examples": [
            {"french": "À peine fut-il sorti qu'il commença à pleuvoir.", "english": "Hardly had he gone out when it started to rain.", "spanish": "Apenas hubo salido cuando empezó a llover."},
            {"french": "Peut-être viendra-t-il demain.", "english": "Perhaps he will come tomorrow.", "spanish": "Quizá venga mañana."},
            {"french": "Ainsi parlait Zarathoustra.", "english": "Thus spoke Zarathustra.", "spanish": "Así habló Zaratustra."},
            {"french": "« Je pars », dit-elle.", "english": "'I'm leaving,' she said.", "spanish": "«Me voy», dijo ella."},
            {"french": "Rarement avait-on vu pareille chose.", "english": "Rarely had one seen such a thing.", "spanish": "Raramente se había visto algo así."}
        ],
        "tips": [
            "'À peine' with inversion requires 'que' for the result clause",
            "With 'peut-être' and 'aussi', inversion is optional but more elegant",
            "Noun subjects require pronoun reduplication: 'Marie viendra-t-elle?'"
        ],
        "spanish_comparison": "Spanish uses different structures: 'apenas' doesn't require inversion, and reporting verbs follow different patterns. French stylistic inversion has no direct Spanish parallel."
    },
    {
        "topic": "ne_explétif_complet",
        "title": "Le Ne Explétif (Expletive Ne - Complete Guide)",
        "explanation_en": """The expletive 'ne' appears in subordinate clauses without negative meaning. It's optional but adds stylistic elegance in formal register.

Required/expected contexts:
1. After verbs of fearing: craindre que, avoir peur que, redouter que
2. After 'empêcher que', 'éviter que'
3. After 'avant que', 'à moins que'
4. In comparisons of inequality: plus...que, moins...que, autre...que
5. After 'de peur que', 'de crainte que'
6. After 'douter' in negative/interrogative form
7. After 'nier' in negative form

Note: 'Sans que' does NOT take expletive ne.""",
        "explanation_fr": "Le 'ne' explétif n'a pas de valeur négative. Il apparaît dans certaines subordonnées pour des raisons stylistiques ou historiques.",
        "examples": [
            {"french": "Je crains qu'il ne parte. (= qu'il parte)", "english": "I fear he may leave.", "spanish": "Temo que se vaya."},
            {"french": "Elle est plus intelligente que tu ne le penses.", "english": "She is smarter than you think.", "spanish": "Es más inteligente de lo que piensas."},
            {"french": "Avant qu'il ne soit trop tard.", "english": "Before it's too late.", "spanish": "Antes de que sea demasiado tarde."},
            {"french": "À moins qu'il ne pleuve.", "english": "Unless it rains.", "spanish": "A menos que llueva."},
            {"french": "Évitez qu'il ne vous voie.", "english": "Avoid him seeing you.", "spanish": "Evite que le vea."}
        ],
        "tips": [
            "The expletive 'ne' adds NO negative meaning",
            "Omitting it is acceptable in informal contexts",
            "Never use with 'sans que' - this is a common error",
            "In comparisons, the 'ne' appears before the verb in the second clause"
        ],
        "spanish_comparison": "Spanish has no equivalent. Where French uses 'Je crains qu'il ne vienne', Spanish simply uses 'Temo que venga' without any negative particle."
    },
    {
        "topic": "constructions_impersonnelles",
        "title": "Constructions Impersonnelles Avancées (Advanced Impersonal Constructions)",
        "explanation_en": """French uses 'il' as an impersonal subject more extensively than Spanish. Mastery includes recognizing and using these sophisticated structures:

1. Il + être + adjective + de/que: Il est crucial de comprendre...
2. Il + verbs of appearance: Il semble que, Il paraît que, Il s'avère que
3. Il + verbs of occurrence: Il arrive que, Il se trouve que, Il advient que
4. Il + passive constructions: Il a été décidé que...
5. Weather/time (basic): Il pleut, Il est tard
6. Formal announcements: Il sera procédé à... (We will proceed to...)
7. Literary: Il est des jours où... (There are days when...)

Note the subjunctive triggers: 'Il semble que' + subjunctive, but 'Il me semble que' + indicative.""",
        "explanation_fr": "Les constructions impersonnelles avec 'il' sont particulièrement riches en français soutenu et littéraire.",
        "examples": [
            {"french": "Il s'avère que nous avions raison.", "english": "It turns out we were right.", "spanish": "Resulta que teníamos razón."},
            {"french": "Il sera procédé à l'examen des candidatures.", "english": "The applications will be reviewed.", "spanish": "Se procederá al examen de las candidaturas."},
            {"french": "Il est des moments où tout semble possible.", "english": "There are moments when everything seems possible.", "spanish": "Hay momentos en que todo parece posible."},
            {"french": "Il advint qu'un roi perdit son fils.", "english": "It happened that a king lost his son.", "spanish": "Aconteció que un rey perdió a su hijo."},
            {"french": "Il appert que le document est faux.", "english": "It appears that the document is false.", "spanish": "Consta que el documento es falso."}
        ],
        "tips": [
            "'Il semble que' + subjunctive, 'Il me semble que' + indicative",
            "'Il est' + noun (literary) = 'There is/are': 'Il est des gens qui...'",
            "Legal/formal French uses many impersonal passives: 'Il a été convenu que...'"
        ],
        "spanish_comparison": "Spanish often uses 'se' constructions where French uses 'il': 'Il a été décidé' = 'Se ha decidido'. French impersonal constructions are more varied and common in formal registers."
    },
    {
        "topic": "concordance_des_temps",
        "title": "La Concordance des Temps (Sequence of Tenses)",
        "explanation_en": """In formal French, strict rules govern the relationship between main and subordinate clause tenses. This is particularly important with subjunctive:

Main Clause Present/Future → Subordinate Subjunctive:
- Present subjunctive for simultaneous/future action
- Past subjunctive (passé du subjonctif) for prior action

Main Clause Past → Subordinate Subjunctive:
- Imperfect subjunctive for simultaneous/future action (literary)
- Pluperfect subjunctive for prior action (literary)
- In modern French: present/past subjunctive often replace literary forms

With indicative subordinates, the shift is more predictable:
| Main | Subordinate (simultaneous) | Subordinate (prior) |
|------|---------------------------|---------------------|
| Present | Present | Passé composé |
| Past | Imparfait | Plus-que-parfait |
| Future | Future | Future anterior |""",
        "explanation_fr": "La concordance des temps régit les rapports temporels entre proposition principale et subordonnée.",
        "examples": [
            {"french": "Je veux qu'il vienne. → Je voulais qu'il vînt. (literary)", "english": "I want him to come. → I wanted him to come.", "spanish": "Quiero que venga. → Quería que viniera."},
            {"french": "Je regrette qu'il soit parti. → Je regrettais qu'il fût parti. (literary)", "english": "I regret he left. → I regretted he had left.", "spanish": "Lamento que se haya ido. → Lamentaba que se hubiera ido."},
            {"french": "Il dit qu'il viendra. → Il a dit qu'il viendrait.", "english": "He says he will come. → He said he would come.", "spanish": "Dice que vendrá. → Dijo que vendría."}
        ],
        "tips": [
            "Literary tenses (imparfait/plus-que-parfait du subjonctif) are for recognition",
            "Modern French often uses present subjunctive even after past main verbs",
            "Reported speech follows the same shift pattern as in Spanish"
        ],
        "spanish_comparison": "The rules are nearly identical to Spanish 'concordancia temporal'. The main difference: French has distinct literary subjunctive tenses that Spanish uses actively (imperfecto de subjuntivo)."
    },
    {
        "topic": "registres_de_langue",
        "title": "Les Registres de Langue (Language Registers)",
        "explanation_en": """Mastering register variation is essential for C2 proficiency. French distinguishes clearly between:

**Soutenu (Formal/Literary)**
- Literary tenses: passé simple, passé antérieur, subjonctif imparfait
- Inversion: 'Peut-être viendra-t-il'
- Full negation: 'Je ne sais pas'
- Vocabulary: 'demeure' (not maison), 'véhicule' (not voiture)
- 'Nous' form, 'l'on' for 'on'

**Standard (Neutral)**
- Passé composé, standard subjunctive
- 'Peut-être qu'il viendra'
- Full negation
- Standard vocabulary

**Familier (Colloquial)**
- Dropped 'ne': 'Je sais pas'
- 'On' for 'nous'
- Truncated words: 'resto', 'sympa'
- Informal vocabulary: 'bagnole', 'fric'

**Populaire/Argot (Slang)**
- Heavy elision, verlan (backwards slang)
- Non-standard grammar""",
        "explanation_fr": "La maîtrise des registres est essentielle au niveau C2. Chaque contexte social demande le registre approprié.",
        "examples": [
            {"french": "Soutenu: Il n'en demeure pas moins que...", "english": "The fact remains that...", "spanish": "No obstante..."},
            {"french": "Standard: Quand même, c'est vrai que...", "english": "Still, it's true that...", "spanish": "De todas formas, es verdad que..."},
            {"french": "Familier: N'empêche, c'est vrai...", "english": "Still, it's true...", "spanish": "Igual, es verdad..."},
            {"french": "Soutenu: Je n'y comprends goutte.", "english": "I don't understand a thing.", "spanish": "No entiendo nada en absoluto."},
            {"french": "Familier: J'y pige rien.", "english": "I don't get it at all.", "spanish": "No pillo nada."}
        ],
        "tips": [
            "Academic writing requires soutenu or standard register",
            "Mixing registers inappropriately sounds very odd to native speakers",
            "Understanding familiar/populaire is crucial for comprehension",
            "Business French is generally standard with some soutenu elements"
        ],
        "spanish_comparison": "Spanish also has register variation, but French literary language (passé simple, inversion) is further removed from spoken language than Spanish equivalents."
    },
    {
        "topic": "gallicismes",
        "title": "Les Gallicismes (Idiomatic French Structures)",
        "explanation_en": """Gallicisms are constructions particular to French that cannot be translated literally. Mastery of these marks true fluency:

**Temporal structures:**
- venir de + infinitif (immediate past)
- aller + infinitif (immediate future)
- être en train de + infinitif (ongoing action)

**Emphatic structures:**
- C'est...qui/que (cleft sentences)
- Ce qui/que...c'est (pseudo-cleft)
- Il y a...qui (presentative)
- Voilà...qui (presentative + action)

**Idiomatic with 'faire':**
- faire + infinitif (causative)
- se faire + infinitif (have something done to oneself)
- ne faire que + infinitif (only do)

**Other essential structures:**
- avoir beau + infinitif (futility)
- être censé + infinitif (supposed to)
- quitte à + infinitif (even if it means)""",
        "explanation_fr": "Les gallicismes sont des tournures idiomatiques propres au français, essentielles à maîtriser.",
        "examples": [
            {"french": "Je viens de lui parler.", "english": "I've just spoken to him.", "spanish": "Acabo de hablarle."},
            {"french": "C'est lui qui l'a fait.", "english": "He's the one who did it.", "spanish": "Es él quien lo hizo."},
            {"french": "Il ne fait que se plaindre.", "english": "All he does is complain.", "spanish": "No hace más que quejarse."},
            {"french": "Voilà qu'il se met à pleuvoir.", "english": "And now it starts raining.", "spanish": "Y ahora se pone a llover."},
            {"french": "J'ai beau essayer, je n'y arrive pas.", "english": "No matter how hard I try, I can't do it.", "spanish": "Por más que lo intente, no lo consigo."}
        ],
        "tips": [
            "'Venir de' only works in present and imperfect tenses",
            "Cleft sentences (C'est...qui/que) are far more common in French than in Spanish",
            "'Avoir beau' always expresses futility or contrast"
        ],
        "spanish_comparison": "Spanish 'acabar de' = 'venir de', but many gallicisms have no equivalent: 'avoir beau' ≈ 'por más que', and French uses cleft sentences much more frequently."
    }
]
