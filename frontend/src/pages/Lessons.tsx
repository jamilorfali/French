import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { BookOpen, Clock, Target, Play, MessageCircle } from 'lucide-react';
import { getLessons } from '../services/api';
import { useLevel } from '../contexts/LevelContext';
import type { Lesson } from '../types';

export default function Lessons() {
  const { currentLevel, currentLevelInfo, loading: levelLoading } = useLevel();
  const [lessons, setLessons] = useState<Lesson[]>([]);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState<'standard' | 'colloquial'>('standard');

  useEffect(() => {
    if (levelLoading) return;

    const fetchData = async () => {
      setLoading(true);
      try {
        const data = await getLessons(currentLevel);
        setLessons(data);
      } catch (error) {
        console.error('Failed to fetch lessons:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [currentLevel, levelLoading]);

  // Separate lessons into standard and colloquial
  const isColloquialLesson = (lesson: Lesson) =>
    (lesson.themes || []).some(theme => theme.toLowerCase() === 'colloquial');

  const standardLessons = lessons.filter(lesson => !isColloquialLesson(lesson));
  const colloquialLessons = lessons.filter(lesson => isColloquialLesson(lesson));

  if (loading || levelLoading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
      </div>
    );
  }

  const displayedLessons = activeTab === 'standard' ? standardLessons : colloquialLessons;

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-gray-900">Lessons</h1>
        <p className="text-gray-600">
          Level {currentLevel} - {currentLevelInfo?.name || 'Beginner'}
        </p>
      </div>

      {/* Tab Navigation */}
      <div className="border-b border-gray-200">
        <nav className="flex gap-4">
          <button
            onClick={() => setActiveTab('standard')}
            className={`py-3 px-1 border-b-2 font-medium text-sm transition-colors flex items-center gap-2 ${
              activeTab === 'standard'
                ? 'border-primary-500 text-primary-600'
                : 'border-transparent text-gray-500 hover:text-gray-700'
            }`}
          >
            <BookOpen size={16} />
            Standard Lessons ({standardLessons.length})
          </button>
          <button
            onClick={() => setActiveTab('colloquial')}
            className={`py-3 px-1 border-b-2 font-medium text-sm transition-colors flex items-center gap-2 ${
              activeTab === 'colloquial'
                ? 'border-purple-500 text-purple-600'
                : 'border-transparent text-gray-500 hover:text-gray-700'
            }`}
          >
            <MessageCircle size={16} />
            Colloquial French ({colloquialLessons.length})
          </button>
        </nav>
      </div>

      {/* Colloquial French description */}
      {activeTab === 'colloquial' && (
        <div className="bg-purple-50 border border-purple-200 rounded-lg p-4">
          <h3 className="font-semibold text-purple-800 flex items-center gap-2">
            <MessageCircle size={18} />
            Street French - Real-World Expressions
          </h3>
          <p className="text-sm text-purple-700 mt-1">
            Learn informal French expressions, slang, and colloquialisms that native speakers use daily.
            This content covers spoken French not typically taught in textbooks - essential for living in a French-speaking environment.
          </p>
        </div>
      )}

      <div className="space-y-4">
        {displayedLessons.map((lesson, index) => (
          <div key={lesson.id} className={`card card-hover ${activeTab === 'colloquial' ? 'border-purple-200' : ''}`}>
            <div className="flex items-start gap-4">
              <div className={`w-12 h-12 rounded-full flex items-center justify-center flex-shrink-0 ${
                activeTab === 'colloquial' ? 'bg-purple-100' : 'bg-primary-100'
              }`}>
                <span className={`text-xl font-bold ${
                  activeTab === 'colloquial' ? 'text-purple-600' : 'text-primary-600'
                }`}>
                  {lesson.unit_number}
                </span>
              </div>

              <div className="flex-1">
                <h3 className="font-semibold text-gray-900 text-lg">
                  {lesson.title}
                </h3>
                <p className="text-gray-600 text-sm mt-1">{lesson.description}</p>

                <div className="flex flex-wrap gap-2 mt-3">
                  <span className="badge bg-gray-100 text-gray-600">
                    <Clock size={12} className="mr-1" />
                    {lesson.estimated_duration} min
                  </span>
                  {(lesson.themes || []).slice(0, 3).map((theme) => (
                    <span key={theme} className="badge badge-primary">
                      {theme}
                    </span>
                  ))}
                </div>

                {(lesson.objectives || []).length > 0 && (
                  <div className="mt-3">
                    <h4 className="text-sm font-medium text-gray-700 mb-1">
                      Objectives:
                    </h4>
                    <ul className="text-sm text-gray-600 space-y-1">
                      {(lesson.objectives || []).slice(0, 3).map((obj, idx) => (
                        <li key={idx} className="flex items-start gap-2">
                          <Target size={14} className="mt-0.5 text-primary-500" />
                          {obj}
                        </li>
                      ))}
                    </ul>
                  </div>
                )}

                <Link
                  to={`/lessons/${lesson.id}`}
                  className="btn-primary btn-sm mt-4 inline-flex"
                >
                  <Play size={16} />
                  View Lesson
                </Link>
              </div>
            </div>
          </div>
        ))}

        {displayedLessons.length === 0 && (
          <div className="text-center py-8 text-gray-500">
            {activeTab === 'colloquial' ? (
              <>
                <MessageCircle className="mx-auto mb-2" size={48} />
                <p>No colloquial French lessons available for this level yet.</p>
                <p className="text-sm mt-2">Check back soon or try a different level!</p>
              </>
            ) : (
              <>
                <BookOpen className="mx-auto mb-2" size={48} />
                <p>No lessons available yet.</p>
              </>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
