import { useState, useEffect } from 'react';
import { Search, Volume2, ChevronDown, ChevronUp } from 'lucide-react';
import { getVerbs, getVerb } from '../services/api';
import { useSpeechSynthesis } from '../hooks/useSpeechSynthesis';
import { useLevel } from '../contexts/LevelContext';
import type { Verb } from '../types';

export default function Verbs() {
  const { currentLevel, currentLevelInfo, loading: levelLoading } = useLevel();
  const [verbs, setVerbs] = useState<Verb[]>([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState('');
  const [expandedId, setExpandedId] = useState<number | null>(null);
  const [expandedVerb, setExpandedVerb] = useState<Verb | null>(null);

  const { speakFrench, speaking } = useSpeechSynthesis();

  useEffect(() => {
    if (levelLoading) return;

    const fetchData = async () => {
      setLoading(true);
      try {
        const data = await getVerbs({
          level: currentLevel,
          search: search || undefined,
        });
        setVerbs(data);
      } catch (error) {
        console.error('Failed to fetch verbs:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [currentLevel, levelLoading, search]);

  const handleExpand = async (id: number) => {
    if (expandedId === id) {
      setExpandedId(null);
      setExpandedVerb(null);
    } else {
      setExpandedId(id);
      try {
        const verb = await getVerb(id);
        setExpandedVerb(verb);
      } catch (error) {
        console.error('Failed to fetch verb details:', error);
      }
    }
  };

  const getGroupBadge = (group: number) => {
    const colors = {
      1: 'bg-green-100 text-green-700',
      2: 'bg-blue-100 text-blue-700',
      3: 'bg-purple-100 text-purple-700',
    };
    const labels = {
      1: '-ER',
      2: '-IR',
      3: 'Irreg',
    };
    return (
      <span className={`badge ${colors[group as keyof typeof colors]}`}>
        {labels[group as keyof typeof labels]}
      </span>
    );
  };

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
        <h1 className="text-2xl font-bold text-gray-900">Verbs</h1>
        <p className="text-gray-600">
          Level {currentLevel} - {currentLevelInfo?.name || 'Beginner'}
        </p>
      </div>

      {/* Search */}
      <div className="relative">
        <Search
          className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"
          size={20}
        />
        <input
          type="text"
          placeholder="Search verbs..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="input pl-10"
        />
      </div>

      {/* Verb List */}
      <div className="space-y-3">
        {verbs.map((verb) => (
          <div key={verb.id} className="card">
            <button
              onClick={() => handleExpand(verb.id)}
              className="w-full flex items-center justify-between text-left"
            >
              <div className="flex items-center gap-3">
                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    speakFrench(verb.infinitive);
                  }}
                  disabled={speaking}
                  className="text-primary-600 hover:text-primary-700"
                >
                  <Volume2 size={18} />
                </button>
                <div>
                  <span className="font-semibold text-gray-900">
                    {verb.infinitive}
                  </span>
                  <span className="text-gray-600 ml-2">- {verb.english}</span>
                </div>
                {getGroupBadge(verb.group)}
                {verb.is_irregular && (
                  <span className="badge bg-orange-100 text-orange-700">
                    Irregular
                  </span>
                )}
              </div>
              {expandedId === verb.id ? (
                <ChevronUp className="text-gray-400" size={20} />
              ) : (
                <ChevronDown className="text-gray-400" size={20} />
              )}
            </button>

            {expandedId === verb.id && expandedVerb && (
              <div className="mt-4 space-y-4">
                {/* Spanish comparison */}
                {expandedVerb.spanish && (
                  <p className="text-sm text-yellow-600">
                    🇪🇸 Spanish: {expandedVerb.spanish}
                  </p>
                )}

                {expandedVerb.spanish_comparison && (
                  <div className="p-3 bg-yellow-50 rounded-lg text-sm text-yellow-700">
                    {expandedVerb.spanish_comparison}
                  </div>
                )}

                {/* Conjugations */}
                {expandedVerb.conjugations.map((conj) => (
                  <div key={`${conj.tense}-${conj.mood}`}>
                    <h4 className="font-medium text-gray-900 mb-2 capitalize">
                      {conj.tense.replace('_', ' ')} ({conj.mood})
                    </h4>
                    <div className="grid grid-cols-2 gap-2 text-sm">
                      <div className="bg-gray-50 p-2 rounded">
                        <span className="text-gray-500">je</span>
                        <span className="ml-2 font-medium">{conj.je}</span>
                      </div>
                      <div className="bg-gray-50 p-2 rounded">
                        <span className="text-gray-500">tu</span>
                        <span className="ml-2 font-medium">{conj.tu}</span>
                      </div>
                      <div className="bg-gray-50 p-2 rounded">
                        <span className="text-gray-500">il/elle</span>
                        <span className="ml-2 font-medium">{conj.il_elle}</span>
                      </div>
                      <div className="bg-gray-50 p-2 rounded">
                        <span className="text-gray-500">nous</span>
                        <span className="ml-2 font-medium">{conj.nous}</span>
                      </div>
                      <div className="bg-gray-50 p-2 rounded">
                        <span className="text-gray-500">vous</span>
                        <span className="ml-2 font-medium">{conj.vous}</span>
                      </div>
                      <div className="bg-gray-50 p-2 rounded">
                        <span className="text-gray-500">ils/elles</span>
                        <span className="ml-2 font-medium">{conj.ils_elles}</span>
                      </div>
                    </div>
                    {conj.spanish_equivalent && (
                      <p className="text-xs text-yellow-600 mt-1">
                        🇪🇸 {conj.spanish_equivalent}
                      </p>
                    )}
                  </div>
                ))}
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
