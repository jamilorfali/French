"""
A1 Level Grammar - Basic French grammar rules.
"""

GRAMMAR_A1 = [
    # ============ ARTICLES ============
    {
        "topic": "definite_articles",
        "title": "Definite Articles (le, la, les)",
        "order": 1,
        "explanation_en": """
French has three definite articles that correspond to "the" in English:
- **le** - masculine singular (le livre = the book)
- **la** - feminine singular (la table = the table)
- **les** - plural (les livres = the books)

Before a vowel or silent 'h', both le and la become **l'**:
- l'ami (the friend, m.)
- l'école (the school, f.)

Unlike English, French uses definite articles with:
- Abstract nouns: J'aime **la** musique (I like music)
- General categories: **Les** chats sont mignons (Cats are cute)
- Countries: **La** France, **le** Japon
        """.strip(),
        "explanation_es": """
Los artículos definidos en francés son similares al español:
- **le** = el (masculino singular)
- **la** = la (femenino singular)
- **les** = los/las (plural)

Antes de vocal o 'h' muda: **l'** (como en español con "el agua")
        """.strip(),
        "spanish_comparison": """
Very similar to Spanish! The main difference:
- French: le/la → l' before vowels
- Spanish: el/la (no contraction before vowels, except "el agua")
- French has ONE plural article (les) vs Spanish two (los/las)
        """.strip(),
        "examples": [
            {"french": "Le garçon mange.", "english": "The boy eats.", "spanish": "El chico come."},
            {"french": "La fille parle.", "english": "The girl speaks.", "spanish": "La chica habla."},
            {"french": "Les enfants jouent.", "english": "The children play.", "spanish": "Los niños juegan."},
            {"french": "J'aime l'école.", "english": "I like school.", "spanish": "Me gusta la escuela."},
        ],
        "common_mistakes": [
            "Forgetting to use articles with abstract nouns (J'aime musique → J'aime LA musique)",
            "Using le/la before vowels instead of l' (le ami → l'ami)",
        ],
        "tips": [
            "Learn each noun with its article: 'la table', not just 'table'",
            "Most nouns ending in -e are feminine (with exceptions)",
            "Most nouns ending in consonant are masculine (with exceptions)",
        ],
    },

    {
        "topic": "indefinite_articles",
        "title": "Indefinite Articles (un, une, des)",
        "order": 2,
        "explanation_en": """
French indefinite articles correspond to "a/an" and "some":
- **un** - masculine singular (un livre = a book)
- **une** - feminine singular (une table = a table)
- **des** - plural (des livres = some books)

Note: In negative sentences, un/une/des become **de/d'**:
- J'ai un chat → Je n'ai pas **de** chat (I don't have a cat)
- Elle a des amis → Elle n'a pas **d'**amis (She doesn't have friends)
        """.strip(),
        "explanation_es": """
Los artículos indefinidos:
- **un** = un (masculino)
- **une** = una (femenino)
- **des** = unos/unas (plural)

En negativo: un/une/des → **de/d'** (no existe en español)
        """.strip(),
        "spanish_comparison": """
Almost identical structure to Spanish (un/una/unos/unas), BUT:
- French 'des' is required where Spanish might omit the article
- In negative sentences, French changes to 'de' (Spanish doesn't change)
        """.strip(),
        "examples": [
            {"french": "J'ai un chien.", "english": "I have a dog.", "spanish": "Tengo un perro."},
            {"french": "C'est une idée.", "english": "It's an idea.", "spanish": "Es una idea."},
            {"french": "Il y a des problèmes.", "english": "There are (some) problems.", "spanish": "Hay problemas."},
            {"french": "Je n'ai pas de voiture.", "english": "I don't have a car.", "spanish": "No tengo coche."},
        ],
        "common_mistakes": [
            "Forgetting to use 'de' in negatives (Je n'ai pas un chat → Je n'ai pas DE chat)",
            "Omitting 'des' before plural nouns (J'ai livres → J'ai DES livres)",
        ],
        "tips": [
            "Always use an article before nouns (unlike English sometimes)",
            "Remember: negative = de/d' (not un/une/des)",
        ],
    },

    # ============ GENDER ============
    {
        "topic": "noun_gender",
        "title": "Noun Gender (Masculine & Feminine)",
        "order": 3,
        "explanation_en": """
All French nouns have a gender: masculine (m.) or feminine (f.).
There's no neutral gender like in English.

**Common masculine endings:**
- -age (le village, le fromage)
- -ment (le moment, le gouvernement)
- -eau (le bateau, le château)
- -isme (le tourisme, le capitalisme)

**Common feminine endings:**
- -tion/-sion (la nation, la télévision)
- -té (la liberté, la société)
- -ure (la nature, la culture)
- -ence/-ance (la patience, la distance)
- -ie (la philosophie, la géographie)

**Exceptions exist!** Always learn the article with the noun.
        """.strip(),
        "explanation_es": """
Como en español, todos los sustantivos tienen género.
Las terminaciones son similares:
- Masculino: -aje, -mento (similar al español)
- Femenino: -ción, -dad/-tad, -ura (similar al español)
        """.strip(),
        "spanish_comparison": """
Great news! French and Spanish gender often match:
- la nation (f.) = la nación (f.)
- le restaurant (m.) = el restaurante (m.)

Watch out for these FALSE FRIENDS:
- le lait (m.) but la leche (f.) - milk
- la mer (f.) but el mar (m.) - sea
        """.strip(),
        "examples": [
            {"french": "le fromage (m.)", "english": "the cheese", "spanish": "el queso (m.)"},
            {"french": "la liberté (f.)", "english": "the freedom", "spanish": "la libertad (f.)"},
            {"french": "le lait (m.)", "english": "the milk", "spanish": "la leche (f.) - different!"},
        ],
        "common_mistakes": [
            "Assuming gender always matches Spanish (it usually does, but not always)",
            "Guessing gender without learning it with the noun",
        ],
        "tips": [
            "Learn: 'la table' not just 'table'",
            "Most words ending in -e are feminine (but not all!)",
            "Words from English are usually masculine (le weekend, le parking)",
        ],
    },

    # ============ SUBJECT PRONOUNS ============
    {
        "topic": "subject_pronouns",
        "title": "Subject Pronouns",
        "order": 4,
        "explanation_en": """
French subject pronouns:

| French | English | Spanish |
|--------|---------|---------|
| je | I | yo |
| tu | you (informal) | tú |
| il | he/it (m.) | él |
| elle | she/it (f.) | ella |
| on | one/we (informal) | se/uno |
| nous | we | nosotros |
| vous | you (formal/plural) | usted/vosotros |
| ils | they (m./mixed) | ellos |
| elles | they (f.) | ellas |

**Important:**
- 'on' is very common in spoken French for "we" (instead of 'nous')
- 'vous' is both formal singular AND all plurals
- 'je' becomes 'j'' before a vowel: j'aime, j'habite
        """.strip(),
        "explanation_es": """
Muy similar al español, con algunas diferencias:
- **tu/vous** = tú/usted (mismo concepto de formalidad)
- **on** = se impersonal, pero también significa "nosotros" informalmente
- **il/elle** se usan para objetos según su género
        """.strip(),
        "spanish_comparison": """
The tu/vous distinction works like tú/usted in Spain!
The main differences:
- 'on' doesn't exist in Spanish - use it for informal "we"
- In French, subjects are ALWAYS stated (no dropping like Spanish 'como' for 'yo como')
        """.strip(),
        "examples": [
            {"french": "Je parle français.", "english": "I speak French.", "spanish": "Hablo francés."},
            {"french": "Tu habites où?", "english": "Where do you live?", "spanish": "¿Dónde vives?"},
            {"french": "On va au cinéma?", "english": "Shall we go to the cinema?", "spanish": "¿Vamos al cine?"},
        ],
        "common_mistakes": [
            "Dropping the subject pronoun like in Spanish (Parle français → JE parle français)",
            "Using 'tu' when 'vous' is more appropriate (in formal situations)",
        ],
        "tips": [
            "ALWAYS use the subject pronoun (unlike Spanish)",
            "Use 'on' for informal 'we' - it's very natural!",
            "When in doubt, use 'vous' - it's never offensive",
        ],
    },

    # ============ PRESENT TENSE ============
    {
        "topic": "present_tense_er_verbs",
        "title": "Present Tense: -ER Verbs",
        "order": 5,
        "explanation_en": """
-ER verbs are the largest group (about 90% of French verbs!).
All regular -ER verbs follow this pattern:

**parler (to speak)**
| Subject | Ending | Conjugation |
|---------|--------|-------------|
| je | -e | parle |
| tu | -es | parles |
| il/elle/on | -e | parle |
| nous | -ons | parlons |
| vous | -ez | parlez |
| ils/elles | -ent | parlent |

**Note:** je/tu/il/ils forms all SOUND THE SAME! (parl)
Only nous (-ons) and vous (-ez) sound different.

Common -ER verbs: aimer, habiter, travailler, manger, jouer, écouter, regarder
        """.strip(),
        "explanation_es": """
Similar a los verbos -AR en español:
- je parle = (yo) hablo
- tu parles = (tú) hablas
- il parle = (él) habla
- nous parlons = (nosotros) hablamos
- vous parlez = (vosotros) habláis
- ils parlent = (ellos) hablan

Las terminaciones suenan parecidas: -e, -es, -e, -ent son mudas
        """.strip(),
        "spanish_comparison": """
Very similar to Spanish -AR verbs!
- French -ons = Spanish -amos
- French -ez = Spanish -áis

Key difference: In French, many endings are SILENT
- je parle, tu parles, il parle, ils parlent all sound like "parl"!
        """.strip(),
        "examples": [
            {"french": "Je travaille à Paris.", "english": "I work in Paris.", "spanish": "Trabajo en París."},
            {"french": "Nous habitons en France.", "english": "We live in France.", "spanish": "Vivimos en Francia."},
            {"french": "Elles mangent au restaurant.", "english": "They eat at the restaurant.", "spanish": "Ellas comen en el restaurante."},
        ],
        "common_mistakes": [
            "Pronouncing the silent endings (-e, -es, -ent)",
            "Forgetting spelling changes: manger → nous mangeons (keep soft 'g')",
        ],
        "tips": [
            "je/tu/il/ils forms sound identical - focus on the stem",
            "Listen for nous (-ons) and vous (-ez) - they're distinct",
        ],
    },

    # ============ NEGATION ============
    {
        "topic": "negation",
        "title": "Negation (ne...pas)",
        "order": 6,
        "explanation_en": """
French negation uses TWO words that wrap around the verb:
**ne + verb + pas**

Examples:
- Je parle → Je **ne** parle **pas** (I don't speak)
- Il mange → Il **ne** mange **pas** (He doesn't eat)

Before a vowel, 'ne' becomes **n'**:
- J'aime → Je **n'**aime **pas** (I don't like)
- Elle écoute → Elle **n'**écoute **pas** (She doesn't listen)

In spoken French, 'ne' is often dropped:
- Je parle pas (informal)
- J'sais pas (I don't know - very common!)
        """.strip(),
        "explanation_es": """
La negación francesa usa DOS palabras: ne...pas
Similar al español antiguo "no...punto/nada"

- Je NE parle PAS = No hablo
- Il N'aime PAS = Él no ama

En francés hablado, se omite "ne" frecuentemente.
        """.strip(),
        "spanish_comparison": """
Main difference: French uses TWO words (ne...pas), Spanish uses ONE (no).
In casual speech, French often drops 'ne', becoming more like Spanish:
- Formal: Je ne sais pas
- Informal: Je sais pas (like Spanish: No sé)
        """.strip(),
        "examples": [
            {"french": "Je ne comprends pas.", "english": "I don't understand.", "spanish": "No comprendo."},
            {"french": "Elle n'habite pas ici.", "english": "She doesn't live here.", "spanish": "Ella no vive aquí."},
            {"french": "Ce n'est pas vrai.", "english": "It's not true.", "spanish": "No es verdad."},
        ],
        "common_mistakes": [
            "Forgetting 'pas' (Je ne parle → Je ne parle PAS)",
            "Wrong placement (Je parle ne pas → Je NE parle PAS)",
        ],
        "tips": [
            "Think of ne...pas as bookends around the verb",
            "Before vowels: ne → n'",
            "In casual speech, it's OK to drop 'ne' (but not in writing!)",
        ],
    },

    # ============ QUESTIONS ============
    {
        "topic": "asking_questions",
        "title": "Asking Questions",
        "order": 7,
        "explanation_en": """
Three ways to ask yes/no questions in French:

**1. Intonation (informal) - just raise your voice:**
- Tu parles français? ↗

**2. Est-ce que (standard):**
- Est-ce que tu parles français?

**3. Inversion (formal):**
- Parles-tu français?

**Question words:**
- Qui? (Who?)
- Que/Quoi? (What?)
- Où? (Where?)
- Quand? (When?)
- Pourquoi? (Why?)
- Comment? (How?)
- Combien? (How much/many?)
        """.strip(),
        "explanation_es": """
Tres formas de preguntar:
1. **Entonación** (informal): Tu parles? ↗ (como español)
2. **Est-ce que**: Est-ce que tu parles? (no existe en español)
3. **Inversión**: Parles-tu? (como ¿hablas tú?)

Las palabras interrogativas son similares al español.
        """.strip(),
        "spanish_comparison": """
Good news: Intonation questions work the same as Spanish!
- Tu viens? = ¿Vienes?

The 'est-ce que' structure doesn't exist in Spanish.
Inversion is similar to formal Spanish questions.
        """.strip(),
        "examples": [
            {"french": "Tu habites où?", "english": "Where do you live?", "spanish": "¿Dónde vives?"},
            {"french": "Est-ce que tu aimes le café?", "english": "Do you like coffee?", "spanish": "¿Te gusta el café?"},
            {"french": "Comment t'appelles-tu?", "english": "What's your name?", "spanish": "¿Cómo te llamas?"},
        ],
        "common_mistakes": [
            "Forgetting 'est-ce que' question structure exists",
            "Using wrong question word (qui vs que)",
        ],
        "tips": [
            "Start with intonation questions - easiest and very natural",
            "Est-ce que is very useful when you're unsure about inversion",
            "Question words often go at the end in casual speech: Tu vas où?",
        ],
    },

    # ============ ÊTRE & AVOIR ============
    {
        "topic": "etre_avoir",
        "title": "Essential Verbs: être and avoir",
        "order": 8,
        "explanation_en": """
The two most important French verbs - both irregular!

**être (to be)**
| Subject | Form |
|---------|------|
| je | suis |
| tu | es |
| il/elle/on | est |
| nous | sommes |
| vous | êtes |
| ils/elles | sont |

**avoir (to have)**
| Subject | Form |
|---------|------|
| je | ai |
| tu | as |
| il/elle/on | a |
| nous | avons |
| vous | avez |
| ils/elles | ont |

'Avoir' is used in expressions where English uses 'to be':
- J'ai faim (I'm hungry - lit. I have hunger)
- J'ai 25 ans (I'm 25 years old - lit. I have 25 years)
        """.strip(),
        "explanation_es": """
Como en español, estos verbos son irregulares:
- **être** combina 'ser' y 'estar'
- **avoir** combina 'tener' y 'haber'

¡Igual que en español!
- J'ai faim = Tengo hambre
- J'ai 25 ans = Tengo 25 años
        """.strip(),
        "spanish_comparison": """
Excellent news for Spanish speakers:
- 'Avoir' expressions work like 'tener' in Spanish!
- J'ai faim = Tengo hambre (not "Estoy hambriento")
- J'ai 20 ans = Tengo 20 años

The main challenge: 'être' combines ser AND estar.
        """.strip(),
        "examples": [
            {"french": "Je suis français.", "english": "I am French.", "spanish": "Soy francés."},
            {"french": "Elle est fatiguée.", "english": "She is tired.", "spanish": "Ella está cansada."},
            {"french": "J'ai une question.", "english": "I have a question.", "spanish": "Tengo una pregunta."},
            {"french": "Tu as faim?", "english": "Are you hungry?", "spanish": "¿Tienes hambre?"},
        ],
        "common_mistakes": [
            "Mixing up 'est' (is) and 'et' (and) - they sound similar!",
            "Using être for age: Je suis 25 ans → J'ai 25 ans",
        ],
        "tips": [
            "Memorize these completely - they're used constantly",
            "Remember: avoir for age, hunger, thirst, hot, cold (like Spanish tener)",
        ],
    },

    # ============ POSSESSIVE ADJECTIVES ============
    {
        "topic": "possessive_adjectives",
        "title": "Possessive Adjectives (my, your, his...)",
        "order": 9,
        "explanation_en": """
French possessive adjectives agree with the THING POSSESSED, not the owner:

| Owner | Masc. sing. | Fem. sing. | Plural |
|-------|-------------|------------|--------|
| my | mon | ma | mes |
| your (tu) | ton | ta | tes |
| his/her/its | son | sa | ses |
| our | notre | notre | nos |
| your (vous) | votre | votre | vos |
| their | leur | leur | leurs |

Before feminine nouns starting with a vowel, use the masculine form:
- mon amie (my friend, f.) - NOT "ma amie"
        """.strip(),
        "explanation_es": """
Similar al español, pero con una diferencia importante:
El adjetivo concuerda con lo POSEÍDO, no el poseedor.

- son livre = su libro (de él O de ella)
- sa maison = su casa (de él O de ella)

Como en español: "su libro" puede ser de él o de ella.
        """.strip(),
        "spanish_comparison": """
Key difference from Spanish:
- Spanish: su/sus (same for he/she)
- French: son/sa/ses (matches gender of object, not owner)

Just like Spanish, you can't tell gender of owner from the possessive:
- son livre = his book OR her book
        """.strip(),
        "examples": [
            {"french": "C'est mon livre.", "english": "It's my book.", "spanish": "Es mi libro."},
            {"french": "Où est ta sœur?", "english": "Where is your sister?", "spanish": "¿Dónde está tu hermana?"},
            {"french": "Il aime son travail.", "english": "He likes his work.", "spanish": "Le gusta su trabajo."},
            {"french": "Voici notre maison.", "english": "Here's our house.", "spanish": "Aquí está nuestra casa."},
        ],
        "common_mistakes": [
            "Using ma before vowels: ma amie → mon amie",
            "Matching to owner gender: son livre (his book) → correct for HER book too!",
        ],
        "tips": [
            "Focus on the gender of the OBJECT, not the owner",
            "Before vowels: always use mon/ton/son (even for feminine)",
        ],
    },

    # ============ PREPOSITIONS OF PLACE ============
    {
        "topic": "prepositions_place",
        "title": "Prepositions of Place",
        "order": 10,
        "explanation_en": """
Common prepositions for location:

**Basic positions:**
- dans (in/inside)
- sur (on)
- sous (under)
- devant (in front of)
- derrière (behind)
- entre (between)
- à côté de (next to)

**With places:**
- à + city: à Paris, à Madrid
- en + feminine country: en France, en Espagne
- au + masculine country: au Japon, au Portugal
- aux + plural: aux États-Unis

**Contractions:**
- à + le = au
- à + les = aux
- de + le = du
- de + les = des
        """.strip(),
        "explanation_es": """
Muy similar al español:
- dans = en/dentro de
- sur = sobre/en
- sous = debajo de

Con países:
- en + país femenino (en Francia)
- au + país masculino (en Japón = au Japon)

Contracciones como en español (a + el = al):
- à + le = au
- de + le = du
        """.strip(),
        "spanish_comparison": """
Prepositions work similarly! Key differences:
- French contracts: à + le = au (like Spanish a + el = al)
- French uses 'en' for feminine countries, 'au' for masculine

Good news: Most European countries are feminine in both languages!
- en France = en Francia
- en Espagne = en España
        """.strip(),
        "examples": [
            {"french": "Le chat est sur la table.", "english": "The cat is on the table.", "spanish": "El gato está sobre la mesa."},
            {"french": "J'habite à Paris.", "english": "I live in Paris.", "spanish": "Vivo en París."},
            {"french": "Elle va au cinéma.", "english": "She's going to the cinema.", "spanish": "Ella va al cine."},
            {"french": "Nous venons des États-Unis.", "english": "We come from the United States.", "spanish": "Venimos de Estados Unidos."},
        ],
        "common_mistakes": [
            "Forgetting contractions: à le restaurant → au restaurant",
            "Wrong country preposition: en Japon → au Japon (masculine)",
        ],
        "tips": [
            "Memorize: à + le = au, à + les = aux",
            "Most -e ending countries are feminine → use 'en'",
            "Cities always use 'à': à Paris, à New York, à Tokyo",
        ],
    },
]
