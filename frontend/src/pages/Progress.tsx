import { useState, useEffect } from 'react';
import {
  BarChart3,
  TrendingUp,
  Zap,
  Clock,
  Target,
  AlertCircle,
} from 'lucide-react';
import { getOverallProgress, getWeakAreas, getPracticeSessions } from '../services/api';
import type { OverallProgress, WeakArea, PracticeSession } from '../types';

export default function Progress() {
  const [progress, setProgress] = useState<OverallProgress | null>(null);
  const [weakAreas, setWeakAreas] = useState<WeakArea[]>([]);
  const [sessions, setSessions] = useState<PracticeSession[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [progressData, weakAreasData, sessionsData] = await Promise.all([
          getOverallProgress(),
          getWeakAreas(10),
          getPracticeSessions(10),
        ]);
        setProgress(progressData);
        setWeakAreas(weakAreasData);
        setSessions(sessionsData);
      } catch (error) {
        console.error('Failed to fetch progress:', error);
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
      <h1 className="text-2xl font-bold text-gray-900">Your Progress</h1>

      {/* Stats Grid */}
      {progress && (
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div className="card text-center">
            <div className="text-3xl font-bold text-primary-600">
              {progress.current_level}
            </div>
            <div className="text-sm text-gray-500">Current Level</div>
          </div>
          <div className="card text-center">
            <div className="text-3xl font-bold text-success-600">
              {progress.current_streak_days}
            </div>
            <div className="text-sm text-gray-500 flex items-center justify-center gap-1">
              <Zap size={14} /> Day Streak
            </div>
          </div>
          <div className="card text-center">
            <div className="text-3xl font-bold text-gray-900">
              {progress.accuracy_7_days.toFixed(0)}%
            </div>
            <div className="text-sm text-gray-500">7-Day Accuracy</div>
          </div>
          <div className="card text-center">
            <div className="text-3xl font-bold text-gray-900">
              {progress.total_practice_time_mins}
            </div>
            <div className="text-sm text-gray-500 flex items-center justify-center gap-1">
              <Clock size={14} /> Minutes
            </div>
          </div>
        </div>
      )}

      {/* Learning Progress */}
      {progress && (
        <div className="card">
          <h2 className="text-lg font-semibold text-gray-900 mb-4 flex items-center gap-2">
            <TrendingUp size={20} className="text-primary-600" />
            Learning Progress
          </h2>
          <div className="space-y-4">
            <div>
              <div className="flex justify-between text-sm mb-1">
                <span className="text-gray-600">Vocabulary</span>
                <span className="text-gray-900 font-medium">
                  {progress.vocabulary_learned} / {progress.vocabulary_total}
                </span>
              </div>
              <div className="progress-bar">
                <div
                  className="progress-bar-fill"
                  style={{
                    width: `${
                      progress.vocabulary_total > 0
                        ? (progress.vocabulary_learned / progress.vocabulary_total) * 100
                        : 0
                    }%`,
                  }}
                />
              </div>
            </div>
            <div>
              <div className="flex justify-between text-sm mb-1">
                <span className="text-gray-600">Grammar</span>
                <span className="text-gray-900 font-medium">
                  {progress.grammar_learned} / {progress.grammar_total}
                </span>
              </div>
              <div className="progress-bar">
                <div
                  className="progress-bar-fill bg-green-500"
                  style={{
                    width: `${
                      progress.grammar_total > 0
                        ? (progress.grammar_learned / progress.grammar_total) * 100
                        : 0
                    }%`,
                  }}
                />
              </div>
            </div>
            <div>
              <div className="flex justify-between text-sm mb-1">
                <span className="text-gray-600">Verbs</span>
                <span className="text-gray-900 font-medium">
                  {progress.verbs_learned} / {progress.verbs_total}
                </span>
              </div>
              <div className="progress-bar">
                <div
                  className="progress-bar-fill bg-purple-500"
                  style={{
                    width: `${
                      progress.verbs_total > 0
                        ? (progress.verbs_learned / progress.verbs_total) * 100
                        : 0
                    }%`,
                  }}
                />
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Weak Areas */}
      {weakAreas.length > 0 && (
        <div className="card">
          <h2 className="text-lg font-semibold text-gray-900 mb-4 flex items-center gap-2">
            <Target size={20} className="text-error-500" />
            Areas Needing Practice
          </h2>
          <div className="space-y-2">
            {weakAreas.map((area, index) => (
              <div
                key={index}
                className="flex items-center justify-between p-3 bg-gray-50 rounded-lg"
              >
                <div>
                  <span className="font-medium text-gray-900">{area.area_name}</span>
                  <span className="text-sm text-gray-500 ml-2">({area.area_type})</span>
                </div>
                <span
                  className={`badge ${
                    area.accuracy < 40
                      ? 'badge-error'
                      : area.accuracy < 60
                      ? 'badge-warning'
                      : 'badge-primary'
                  }`}
                >
                  {area.accuracy.toFixed(0)}%
                </span>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Recent Sessions */}
      {sessions.length > 0 && (
        <div className="card">
          <h2 className="text-lg font-semibold text-gray-900 mb-4 flex items-center gap-2">
            <BarChart3 size={20} className="text-primary-600" />
            Recent Practice Sessions
          </h2>
          <div className="space-y-2">
            {sessions.map((session) => (
              <div
                key={session.id}
                className="flex items-center justify-between p-3 bg-gray-50 rounded-lg"
              >
                <div>
                  <span className="font-medium text-gray-900 capitalize">
                    {session.session_type}
                  </span>
                  <span className="text-sm text-gray-500 ml-2">
                    {new Date(session.started_at).toLocaleDateString()}
                  </span>
                </div>
                <div className="flex items-center gap-3 text-sm">
                  <span className="text-success-600">
                    ✓ {session.correct_count}
                  </span>
                  <span className="text-error-600">
                    ✗ {session.incorrect_count}
                  </span>
                  <span className="badge badge-primary">
                    {session.accuracy.toFixed(0)}%
                  </span>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Items Due for Review */}
      {progress && progress.items_due_for_review > 0 && (
        <div className="card bg-warning-50 border-warning-200">
          <div className="flex items-center gap-3">
            <AlertCircle className="text-warning-600" size={24} />
            <div>
              <h3 className="font-semibold text-gray-900">
                {progress.items_due_for_review} items due for review
              </h3>
              <p className="text-sm text-gray-600">
                Practice these items to maintain your memory
              </p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
