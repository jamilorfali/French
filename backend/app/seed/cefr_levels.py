"""
CEFR Level seed data.
"""

CEFR_LEVELS = [
    {
        "code": "A1",
        "name": "Beginner",
        "order": 1,
        "af_levels": "A100-A105",
        "vocabulary_target": 500,
        "description": """
Basic user. Can understand and use familiar everyday expressions and very basic phrases
aimed at the satisfaction of needs of a concrete type. Can introduce themselves and others
and can ask and answer questions about personal details such as where they live, people
they know and things they have. Can interact in a simple way provided the other person
talks slowly and clearly and is prepared to help.
        """.strip()
    },
    {
        "code": "A2",
        "name": "Elementary",
        "order": 2,
        "af_levels": "A200-A205",
        "vocabulary_target": 1000,
        "description": """
Can understand sentences and frequently used expressions related to areas of most immediate
relevance (e.g. very basic personal and family information, shopping, local geography,
employment). Can communicate in simple and routine tasks requiring a simple and direct
exchange of information on familiar and routine matters. Can describe in simple terms
aspects of their background, immediate environment and matters in areas of immediate need.
        """.strip()
    },
    {
        "code": "B1",
        "name": "Intermediate",
        "order": 3,
        "af_levels": "B100-B105",
        "vocabulary_target": 2000,
        "description": """
Independent user. Can understand the main points of clear standard input on familiar matters
regularly encountered in work, school, leisure, etc. Can deal with most situations likely
to arise whilst travelling in an area where the language is spoken. Can produce simple
connected text on topics which are familiar or of personal interest. Can describe experiences
and events, dreams, hopes and ambitions and briefly give reasons and explanations.
        """.strip()
    },
    {
        "code": "B2",
        "name": "Upper Intermediate",
        "order": 4,
        "af_levels": "B200-B205",
        "vocabulary_target": 4000,
        "description": """
Can understand the main ideas of complex text on both concrete and abstract topics, including
technical discussions in their field of specialization. Can interact with a degree of fluency
and spontaneity that makes regular interaction with native speakers quite possible without
strain for either party. Can produce clear, detailed text on a wide range of subjects and
explain a viewpoint on a topical issue giving the advantages and disadvantages of various options.
        """.strip()
    },
    {
        "code": "C1",
        "name": "Advanced",
        "order": 5,
        "af_levels": "C100-C105",
        "vocabulary_target": 8000,
        "description": """
Proficient user. Can understand a wide range of demanding, longer texts, and recognize implicit
meaning. Can express themselves fluently and spontaneously without much obvious searching for
expressions. Can use language flexibly and effectively for social, academic and professional
purposes. Can produce clear, well-structured, detailed text on complex subjects, showing
controlled use of organizational patterns, connectors and cohesive devices.
        """.strip()
    },
    {
        "code": "C2",
        "name": "Mastery",
        "order": 6,
        "af_levels": "C200-C205",
        "vocabulary_target": 16000,
        "description": """
Can understand with ease virtually everything heard or read. Can summarize information from
different spoken and written sources, reconstructing arguments and accounts in a coherent
presentation. Can express themselves spontaneously, very fluently and precisely, differentiating
finer shades of meaning even in the most complex situations.
        """.strip()
    },
]
