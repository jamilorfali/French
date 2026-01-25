import { useState, useEffect } from 'react';
import { ChevronDown, ChevronUp, BookOpen } from 'lucide-react';
import { getGrammarTopics } from '../services/api';
import { useLevel } from '../contexts/LevelContext';
import type { Grammar as GrammarType } from '../types';

export default function Grammar() {
  const { currentLevel, currentLevelInfo, loading: levelLoading } = useLevel();
  const [topics, setTopics] = useState<GrammarType[]>([]);
  const [loading, setLoading] = useState(true);
  const [expandedId, setExpandedId] = useState<number | null>(null);

  useEffect(() => {
    if (levelLoading) return;

    const fetchData = async () => {
      setLoading(true);
      try {
        const data = await getGrammarTopics(currentLevel);
        setTopics(data);
      } catch (error) {
        console.error('Failed to fetch grammar:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [currentLevel, levelLoading]);

  if (loading || levelLoading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-gray-900">Grammar Guide</h1>
        <p className="text-gray-600">
          Level {currentLevel} - {currentLevelInfo?.name || 'Beginner'} | Master French grammar with explanations tailored for Spanish speakers.
        </p>
      </div>

      <div className="space-y-3">
        {topics.map((topic) => (
          <div key={topic.id} className="card">
            <button
              onClick={() =>
                setExpandedId(expandedId === topic.id ? null : topic.id)
              }
              className="w-full flex items-center justify-between text-left"
            >
              <div className="flex items-center gap-3">
                <BookOpen className="text-primary-600" size={20} />
                <span className="font-semibold text-gray-900">{topic.title}</span>
              </div>
              {expandedId === topic.id ? (
                <ChevronUp className="text-gray-400" size={20} />
              ) : (
                <ChevronDown className="text-gray-400" size={20} />
              )}
            </button>

            {expandedId === topic.id && (
              <div className="mt-4 space-y-4">
                {/* English Explanation */}
                <div className="prose prose-sm max-w-none">
                  <div className="whitespace-pre-wrap text-gray-700">
                    {topic.explanation_en}
                  </div>
                </div>

                {/* Spanish Comparison */}
                {topic.spanish_comparison && (
                  <div className="p-3 bg-yellow-50 rounded-lg">
                    <h4 className="font-medium text-yellow-800 mb-1">
                      🇪🇸 Spanish Comparison
                    </h4>
                    <p className="text-sm text-yellow-700">
                      {topic.spanish_comparison}
                    </p>
                  </div>
                )}

                {/* Examples */}
                {topic.examples && topic.examples.length > 0 && (
                  <div>
                    <h4 className="font-medium text-gray-900 mb-2">Examples</h4>
                    <div className="space-y-2">
                      {topic.examples.map((ex, idx) => (
                        <div key={idx} className="p-3 bg-gray-50 rounded-lg">
                          <p className="font-medium text-gray-900">{ex.french}</p>
                          <p className="text-sm text-gray-600">{ex.english}</p>
                          {ex.spanish && (
                            <p className="text-sm text-yellow-600">ES: {ex.spanish}</p>
                          )}
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* Tips */}
                {topic.tips && topic.tips.length > 0 && (
                  <div>
                    <h4 className="font-medium text-gray-900 mb-2">💡 Tips</h4>
                    <ul className="list-disc list-inside space-y-1 text-sm text-gray-600">
                      {topic.tips.map((tip, idx) => (
                        <li key={idx}>{tip}</li>
                      ))}
                    </ul>
                  </div>
                )}

                {/* Common Mistakes */}
                {topic.common_mistakes && topic.common_mistakes.length > 0 && (
                  <div>
                    <h4 className="font-medium text-error-600 mb-2">
                      ⚠️ Common Mistakes
                    </h4>
                    <ul className="list-disc list-inside space-y-1 text-sm text-error-600">
                      {topic.common_mistakes.map((mistake, idx) => (
                        <li key={idx}>{mistake}</li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
