import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import {
  Play,
  Clock,
  Target,
  TrendingUp,
  AlertCircle,
  BookOpen,
  Zap,
} from 'lucide-react';
import { getOverallProgress, getWeakAreas } from '../services/api';
import type { OverallProgress, WeakArea } from '../types';

export default function Home() {
  const [progress, setProgress] = useState<OverallProgress | null>(null);
  const [weakAreas, setWeakAreas] = useState<WeakArea[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [progressData, weakAreasData] = await Promise.all([
          getOverallProgress(),
          getWeakAreas(5),
        ]);
        setProgress(progressData);
        setWeakAreas(weakAreasData);
      } catch (error) {
        console.error('Failed to fetch data:', error);
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
      {/* Welcome Section */}
      <div className="card bg-gradient-to-r from-primary-600 to-primary-700 text-white">
        <h1 className="text-2xl font-bold mb-2">Bonjour! 👋</h1>
        <p className="text-primary-100">
          Ready to continue your French journey? You're at level{' '}
          <span className="font-bold text-white">{progress?.current_level || 'A1'}</span>
        </p>
        {progress && progress.current_streak_days > 0 && (
          <div className="mt-3 flex items-center gap-2 text-primary-100">
            <Zap className="text-yellow-300" size={18} />
            <span>{progress.current_streak_days} day streak! Keep it up!</span>
          </div>
        )}
      </div>

      {/* Quick Practice Buttons */}
      <div className="space-y-3">
        <h2 className="text-lg font-semibold text-gray-900">Quick Practice</h2>
        <div className="grid grid-cols-3 gap-3">
          <Link
            to="/practice?duration=5"
            className="card card-hover text-center py-4"
          >
            <Clock className="mx-auto mb-2 text-primary-600" size={24} />
            <span className="font-medium text-gray-900">5 min</span>
          </Link>
          <Link
            to="/practice?duration=15"
            className="card card-hover text-center py-4 border-2 border-primary-200 bg-primary-50"
          >
            <Clock className="mx-auto mb-2 text-primary-600" size={24} />
            <span className="font-medium text-gray-900">15 min</span>
            <span className="block text-xs text-primary-600 mt-1">Recommended</span>
          </Link>
          <Link
            to="/practice?duration=30"
            className="card card-hover text-center py-4"
          >
            <Clock className="mx-auto mb-2 text-primary-600" size={24} />
            <span className="font-medium text-gray-900">30 min</span>
          </Link>
        </div>
      </div>

      {/* Progress Overview */}
      {progress && (
        <div className="card">
          <h2 className="text-lg font-semibold text-gray-900 mb-4 flex items-center gap-2">
            <TrendingUp size={20} className="text-primary-600" />
            Your Progress
          </h2>
          <div className="grid grid-cols-2 gap-4">
            <div>
              <div className="text-sm text-gray-500">Vocabulary</div>
              <div className="flex items-end gap-1">
                <span className="text-2xl font-bold text-gray-900">
                  {progress.vocabulary_learned}
                </span>
                <span className="text-gray-500 mb-1">/ {progress.vocabulary_total}</span>
              </div>
              <div className="progress-bar mt-2">
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
              <div className="text-sm text-gray-500">7-Day Accuracy</div>
              <div className="text-2xl font-bold text-gray-900">
                {progress.accuracy_7_days.toFixed(0)}%
              </div>
              <div className="text-sm text-gray-500 mt-2">
                {progress.total_practice_time_mins} min practiced
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Items Due for Review */}
      {progress && progress.items_due_for_review > 0 && (
        <Link to="/practice?type=review" className="card card-hover block">
          <div className="flex items-center gap-3">
            <div className="w-12 h-12 rounded-full bg-warning-100 flex items-center justify-center">
              <AlertCircle className="text-warning-600" size={24} />
            </div>
            <div>
              <h3 className="font-semibold text-gray-900">
                {progress.items_due_for_review} items due for review
              </h3>
              <p className="text-sm text-gray-500">
                Practice these to improve retention
              </p>
            </div>
          </div>
        </Link>
      )}

      {/* Weak Areas */}
      {weakAreas.length > 0 && (
        <div className="card">
          <h2 className="text-lg font-semibold text-gray-900 mb-4 flex items-center gap-2">
            <Target size={20} className="text-error-500" />
            Focus Areas
          </h2>
          <div className="space-y-3">
            {weakAreas.map((area, index) => (
              <div
                key={index}
                className="flex items-center justify-between p-3 bg-gray-50 rounded-lg"
              >
                <div>
                  <span className="font-medium text-gray-900">{area.area_name}</span>
                  <span className="text-sm text-gray-500 ml-2">({area.area_type})</span>
                </div>
                <div className="flex items-center gap-2">
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
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Quick Links */}
      <div className="grid grid-cols-2 gap-3">
        <Link to="/vocabulary" className="card card-hover">
          <BookOpen className="text-primary-600 mb-2" size={24} />
          <h3 className="font-semibold text-gray-900">Browse Vocabulary</h3>
          <p className="text-sm text-gray-500">Explore words by category</p>
        </Link>
        <Link to="/grammar" className="card card-hover">
          <Play className="text-primary-600 mb-2" size={24} />
          <h3 className="font-semibold text-gray-900">Grammar Guide</h3>
          <p className="text-sm text-gray-500">Review grammar rules</p>
        </Link>
      </div>

      {/* Spanish Advantage Note */}
      <div className="card bg-gradient-to-r from-yellow-50 to-orange-50 border-yellow-200">
        <div className="flex items-start gap-3">
          <span className="text-2xl">🇪🇸</span>
          <div>
            <h3 className="font-semibold text-gray-900">Your Spanish Advantage</h3>
            <p className="text-sm text-gray-600">
              As a fluent Spanish speaker, you'll see cognate hints and Spanish comparisons
              throughout your learning. French and Spanish share ~75% lexical similarity!
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
