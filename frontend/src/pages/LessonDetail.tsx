import { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { ArrowLeft, Clock, Target, BookOpen, Play, CheckCircle, Volume2 } from 'lucide-react';
import { getLesson, getGrammarTopics, getVocabulary } from '../services/api';
import { useLevel } from '../contexts/LevelContext';
import { useSpeechSynthesis } from '../hooks/useSpeechSynthesis';
import { GrammarContent } from '../components/GrammarContent';
import type { Lesson, Grammar, Vocabulary } from '../types';

export default function LessonDetail() {
  const { lessonId } = useParams<{ lessonId: string }>();
  const { currentLevel, loading: levelLoading } = useLevel();
  const { speakFrench, speaking } = useSpeechSynthesis();
  const [lesson, setLesson] = useState<Lesson | null>(null);
  const [relatedGrammar, setRelatedGrammar] = useState<Grammar[]>([]);
  const [relatedVocabulary, setRelatedVocabulary] = useState<Vocabulary[]>([]);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState<'overview' | 'grammar' | 'vocabulary'>('overview');

  useEffect(() => {
    const fetchData = async () => {
      if (!lessonId || levelLoading) return;

      try {
        // Fetch lesson details
        const lessonData = await getLesson(parseInt(lessonId));
        setLesson(lessonData);

        // Fetch related grammar topics
        const grammarData = await getGrammarTopics(currentLevel);
        const filteredGrammar = grammarData.filter((g: Grammar) =>
          (lessonData.grammar_topics || []).includes(g.topic)
        );
        setRelatedGrammar(filteredGrammar);

        // Fetch vocabulary related to lesson themes
        // Map themes to related vocabulary categories for better matching
        const themeToCategories: Record<string, string[]> = {
          'greetings': ['greetings', 'courtesy', 'introductions'],
          'introductions': ['greetings', 'courtesy', 'introductions', 'identity'],
          'identity': ['identity', 'introductions', 'personal'],
          'family': ['family', 'people', 'relationships'],
          'descriptions': ['adjectives', 'colors', 'descriptions', 'appearance'],
          'numbers': ['numbers', 'counting', 'time'],
          'days': ['days', 'time', 'calendar'],
          'months': ['months', 'time', 'calendar', 'seasons'],
          'time': ['time', 'numbers', 'days', 'calendar'],
          'preferences': ['preferences', 'food', 'activities', 'opinions'],
          'food': ['food', 'drinks', 'meals', 'restaurant'],
          'activities': ['activities', 'hobbies', 'sports', 'verbs'],
          'home': ['home', 'house', 'rooms', 'furniture'],
          'places': ['places', 'city', 'locations', 'buildings'],
          'location': ['location', 'places', 'prepositions', 'directions'],
          'daily_routines': ['daily', 'routines', 'activities', 'time'],
          'shopping': ['shopping', 'food', 'stores', 'money'],
          'transportation': ['transportation', 'travel', 'vehicles'],
          'directions': ['directions', 'location', 'prepositions'],
          'travel': ['travel', 'transportation', 'places'],
          'past': ['time', 'past', 'verbs'],
          'events': ['events', 'activities', 'time'],
          'movement': ['movement', 'verbs', 'travel'],
          'work': ['work', 'jobs', 'career', 'office'],
          'career': ['career', 'work', 'jobs', 'professional'],
          'professional': ['professional', 'work', 'office', 'business'],
          'memories': ['memories', 'past', 'time', 'family'],
          'hypotheses': ['hypotheses', 'conditions', 'grammar'],
          'conditions': ['conditions', 'hypotheses', 'grammar'],
          'wishes': ['wishes', 'desires', 'emotions'],
          'complex_sentences': ['grammar', 'sentences', 'writing'],
          'obligation': ['obligation', 'necessity', 'grammar'],
          'necessity': ['necessity', 'obligation', 'grammar'],
          'desire': ['desire', 'wishes', 'emotions'],
          'debate': ['debate', 'opinion', 'arguments'],
          'opinion': ['opinion', 'debate', 'arguments'],
          'argumentation': ['argumentation', 'debate', 'opinion'],
          'regret': ['regret', 'emotions', 'past'],
          'media': ['media', 'news', 'communication'],
          'processes': ['processes', 'work', 'actions'],
          'formal': ['formal', 'writing', 'professional'],
          'nuance': ['nuance', 'writing', 'formal'],
          'writing': ['writing', 'formal', 'academic'],
          'actions': ['actions', 'verbs', 'activities'],
          'manner': ['manner', 'adverbs', 'grammar'],
          'literature': ['literature', 'reading', 'writing'],
          'style': ['style', 'writing', 'literature'],
          'reading': ['reading', 'literature', 'books'],
          'emotions': ['emotions', 'feelings', 'adjectives'],
          'doubt': ['doubt', 'emotions', 'uncertainty'],
          'reporting': ['reporting', 'speech', 'communication'],
          'academic': ['academic', 'writing', 'formal'],
        };

        const vocabData = await getVocabulary({ level: currentLevel });
        const lessonThemes = lessonData.themes || [];

        // Get all relevant categories for the lesson themes
        const relevantCategories = new Set<string>();
        lessonThemes.forEach((theme: string) => {
          const themeLower = theme.toLowerCase();
          relevantCategories.add(themeLower);
          (themeToCategories[themeLower] || []).forEach(cat => relevantCategories.add(cat));
        });

        const filteredVocab = vocabData.filter((v: Vocabulary) => {
          const vocabCategory = v.category?.toLowerCase() || '';
          // Check if vocabulary category matches any relevant category
          return Array.from(relevantCategories).some(cat =>
            vocabCategory.includes(cat) || cat.includes(vocabCategory)
          );
        }).slice(0, 20);
        setRelatedVocabulary(filteredVocab);
      } catch (error) {
        console.error('Failed to fetch lesson:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [lessonId, currentLevel, levelLoading]);

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
      </div>
    );
  }

  if (!lesson) {
    return (
      <div className="text-center py-8">
        <BookOpen className="mx-auto mb-4 text-gray-400" size={48} />
        <p className="text-gray-500">Lesson not found.</p>
        <Link to="/lessons" className="text-primary-600 hover:underline mt-2 inline-block">
          Back to Lessons
        </Link>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center gap-4">
        <Link
          to="/lessons"
          className="p-2 hover:bg-gray-100 rounded-full transition-colors"
        >
          <ArrowLeft size={20} />
        </Link>
        <div className="flex-1">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-full bg-primary-100 flex items-center justify-center">
              <span className="text-lg font-bold text-primary-600">
                {lesson.unit_number}
              </span>
            </div>
            <div>
              <h1 className="text-2xl font-bold text-gray-900">{lesson.title}</h1>
              <p className="text-gray-600">{lesson.description}</p>
            </div>
          </div>
        </div>
      </div>

      {/* Meta info */}
      <div className="flex flex-wrap gap-3">
        <span className="badge bg-gray-100 text-gray-700">
          <Clock size={14} className="mr-1" />
          {lesson.estimated_duration} min
        </span>
        {(lesson.themes || []).map((theme) => (
          <span key={theme} className="badge badge-primary">
            {theme}
          </span>
        ))}
      </div>

      {/* Tab Navigation */}
      <div className="border-b border-gray-200">
        <nav className="flex gap-4">
          {[
            { id: 'overview', label: 'Overview' },
            { id: 'grammar', label: 'Grammar' },
            { id: 'vocabulary', label: 'Vocabulary' },
          ].map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id as typeof activeTab)}
              className={`py-3 px-1 border-b-2 font-medium text-sm transition-colors ${
                activeTab === tab.id
                  ? 'border-primary-500 text-primary-600'
                  : 'border-transparent text-gray-500 hover:text-gray-700'
              }`}
            >
              {tab.label}
            </button>
          ))}
        </nav>
      </div>

      {/* Tab Content */}
      <div className="min-h-[300px]">
        {activeTab === 'overview' && (
          <div className="space-y-6">
            {/* Objectives */}
            <div className="card">
              <h2 className="text-lg font-semibold text-gray-900 mb-4 flex items-center gap-2">
                <Target size={20} className="text-primary-500" />
                Learning Objectives
              </h2>
              <ul className="space-y-3">
                {(lesson.objectives || []).map((objective, idx) => (
                  <li key={idx} className="flex items-start gap-3">
                    <CheckCircle size={18} className="text-green-500 mt-0.5 flex-shrink-0" />
                    <span className="text-gray-700">{objective}</span>
                  </li>
                ))}
              </ul>
            </div>

            {/* Grammar Topics Preview */}
            {relatedGrammar.length > 0 && (
              <div className="card">
                <h2 className="text-lg font-semibold text-gray-900 mb-4 flex items-center gap-2">
                  <BookOpen size={20} className="text-primary-500" />
                  Grammar Topics
                </h2>
                <div className="space-y-2">
                  {relatedGrammar.map((grammar) => (
                    <div key={grammar.id} className="p-3 bg-gray-50 rounded-lg">
                      <h3 className="font-medium text-gray-900">{grammar.title}</h3>
                      <p className="text-sm text-gray-600 mt-1 line-clamp-2">
                        {grammar.explanation_en?.substring(0, 150)}...
                      </p>
                    </div>
                  ))}
                </div>
                <button
                  onClick={() => setActiveTab('grammar')}
                  className="text-primary-600 text-sm font-medium mt-3 hover:underline"
                >
                  View full grammar explanations →
                </button>
              </div>
            )}

            {/* Start Practice Button */}
            <div className="card bg-primary-50 border-primary-200">
              <div className="flex items-center justify-between">
                <div>
                  <h3 className="font-semibold text-gray-900">Ready to practice?</h3>
                  <p className="text-sm text-gray-600">
                    Test your knowledge with exercises based on this lesson.
                  </p>
                </div>
                <Link
                  to={`/practice?lesson=${lesson.id}`}
                  className="btn-primary inline-flex items-center gap-2"
                >
                  <Play size={18} />
                  Start Practice
                </Link>
              </div>
            </div>
          </div>
        )}

        {activeTab === 'grammar' && (
          <div className="space-y-4">
            {relatedGrammar.length === 0 ? (
              <div className="text-center py-8 text-gray-500">
                <BookOpen className="mx-auto mb-2" size={48} />
                <p>No grammar content available for this lesson yet.</p>
              </div>
            ) : (
              relatedGrammar.map((grammar) => (
                <div key={grammar.id} className="card">
                  <h2 className="text-lg font-semibold text-gray-900 mb-3">
                    {grammar.title}
                  </h2>
                  <div className="prose prose-sm max-w-none">
                    <GrammarContent content={grammar.explanation_en} />
                  </div>

                  {grammar.examples && grammar.examples.length > 0 && (
                    <div className="mt-4">
                      <h3 className="font-medium text-gray-900 mb-2">Examples:</h3>
                      <div className="space-y-2">
                        {grammar.examples.map((example, idx) => (
                          <div key={idx} className="p-3 bg-gray-50 rounded-lg">
                            <p className="font-medium text-primary-700">{example.french}</p>
                            <p className="text-sm text-gray-600">{example.english}</p>
                            {example.spanish && (
                              <p className="text-sm text-gray-500 italic">ES: {example.spanish}</p>
                            )}
                          </div>
                        ))}
                      </div>
                    </div>
                  )}

                  {grammar.tips && grammar.tips.length > 0 && (
                    <div className="mt-4 p-3 bg-yellow-50 border border-yellow-200 rounded-lg">
                      <h3 className="font-medium text-yellow-800 mb-2">Tips:</h3>
                      <ul className="text-sm text-yellow-700 space-y-1">
                        {grammar.tips.map((tip, idx) => (
                          <li key={idx}>• {tip}</li>
                        ))}
                      </ul>
                    </div>
                  )}

                  {grammar.spanish_comparison && (
                    <div className="mt-4 p-3 bg-blue-50 border border-blue-200 rounded-lg">
                      <h3 className="font-medium text-blue-800 mb-1">Spanish Comparison:</h3>
                      <p className="text-sm text-blue-700">{grammar.spanish_comparison}</p>
                    </div>
                  )}
                </div>
              ))
            )}
          </div>
        )}

        {activeTab === 'vocabulary' && (
          <div className="space-y-4">
            {relatedVocabulary.length === 0 ? (
              <div className="text-center py-8 text-gray-500">
                <BookOpen className="mx-auto mb-2" size={48} />
                <p>No vocabulary content available for this lesson yet.</p>
              </div>
            ) : (
              <div className="grid gap-3 md:grid-cols-2">
                {relatedVocabulary.map((vocab) => (
                  <div key={vocab.id} className="card p-4">
                    <div className="flex justify-between items-start">
                      <div className="flex items-center gap-2">
                        <button
                          onClick={() => speakFrench(vocab.french)}
                          disabled={speaking}
                          className="text-primary-600 hover:text-primary-700 p-1"
                          type="button"
                          aria-label={`Pronounce ${vocab.french}`}
                        >
                          <Volume2 size={18} />
                        </button>
                        <div>
                          <span className="text-lg font-semibold text-primary-700">
                            {vocab.french}
                          </span>
                          {vocab.gender && vocab.gender !== 'none' && (
                            <span className="ml-2 text-xs text-gray-500">
                              ({vocab.gender === 'masculine' ? 'm' : vocab.gender === 'feminine' ? 'f' : vocab.gender})
                            </span>
                          )}
                          {vocab.phonetic && (
                            <span className="ml-2 text-sm text-gray-400">[{vocab.phonetic}]</span>
                          )}
                        </div>
                      </div>
                      {vocab.is_cognate && (
                        <span className="badge bg-green-100 text-green-700 text-xs">Cognate</span>
                      )}
                    </div>
                    <p className="text-gray-700 mt-1">{vocab.english}</p>
                    {vocab.spanish && (
                      <p className="text-sm text-gray-500 italic">ES: {vocab.spanish}</p>
                    )}
                    {vocab.example_french && (
                      <div className="mt-2 pt-2 border-t border-gray-100">
                        <p className="text-sm text-primary-600 italic">"{vocab.example_french}"</p>
                        <p className="text-xs text-gray-500">{vocab.example_english}</p>
                      </div>
                    )}
                  </div>
                ))}
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
