import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { BookOpen, Clock, Target, Play } from 'lucide-react';
import { getLessons } from '../services/api';
import type { Lesson } from '../types';

export default function Lessons() {
  const [lessons, setLessons] = useState<Lesson[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await getLessons('A1');
        setLessons(data);
      } catch (error) {
        console.error('Failed to fetch lessons:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-gray-900">Lessons</h1>
        <p className="text-gray-600">Level A1 - Beginner</p>
      </div>

      <div className="space-y-4">
        {lessons.map((lesson, index) => (
          <div key={lesson.id} className="card card-hover">
            <div className="flex items-start gap-4">
              <div className="w-12 h-12 rounded-full bg-primary-100 flex items-center justify-center flex-shrink-0">
                <span className="text-xl font-bold text-primary-600">
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
                  to={`/practice?lesson=${lesson.id}`}
                  className="btn-primary btn-sm mt-4 inline-flex"
                >
                  <Play size={16} />
                  Start Lesson
                </Link>
              </div>
            </div>
          </div>
        ))}

        {lessons.length === 0 && (
          <div className="text-center py-8 text-gray-500">
            <BookOpen className="mx-auto mb-2" size={48} />
            <p>No lessons available yet.</p>
          </div>
        )}
      </div>
    </div>
  );
}
