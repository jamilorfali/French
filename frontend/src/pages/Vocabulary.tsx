import { useState, useEffect } from 'react';
import { Search, Volume2, Filter } from 'lucide-react';
import { getVocabulary, getVocabularyCategories } from '../services/api';
import { useSpeechSynthesis } from '../hooks/useSpeechSynthesis';
import type { Vocabulary as VocabType } from '../types';

export default function Vocabulary() {
  const [vocabulary, setVocabulary] = useState<VocabType[]>([]);
  const [categories, setCategories] = useState<string[]>([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState('');
  const [selectedCategory, setSelectedCategory] = useState<string>('');
  const [showCognatesOnly, setShowCognatesOnly] = useState(false);

  const { speakFrench, speaking } = useSpeechSynthesis();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [vocabData, categoryData] = await Promise.all([
          getVocabulary({
            level: 'A1',
            category: selectedCategory || undefined,
            cognates_only: showCognatesOnly,
            search: search || undefined,
            limit: 100,
          }),
          getVocabularyCategories('A1'),
        ]);
        setVocabulary(vocabData);
        setCategories(categoryData.categories);
      } catch (error) {
        console.error('Failed to fetch vocabulary:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [selectedCategory, showCognatesOnly, search]);

  const getGenderBadge = (gender?: string) => {
    if (!gender || gender === '-') return null;
    return (
      <span
        className={`badge ${
          gender === 'm' ? 'bg-blue-100 text-blue-700' : 'bg-pink-100 text-pink-700'
        }`}
      >
        {gender === 'm' ? 'le' : 'la'}
      </span>
    );
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-900">Vocabulary</h1>

      {/* Search and Filters */}
      <div className="space-y-3">
        <div className="relative">
          <Search
            className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400"
            size={20}
          />
          <input
            type="text"
            placeholder="Search words..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="input pl-10"
          />
        </div>

        <div className="flex flex-wrap gap-2">
          <select
            value={selectedCategory}
            onChange={(e) => setSelectedCategory(e.target.value)}
            className="input w-auto"
          >
            <option value="">All Categories</option>
            {categories.map((cat) => (
              <option key={cat} value={cat}>
                {cat}
              </option>
            ))}
          </select>

          <button
            onClick={() => setShowCognatesOnly(!showCognatesOnly)}
            className={`badge cursor-pointer ${
              showCognatesOnly ? 'badge-success' : 'bg-gray-100'
            }`}
          >
            🇪🇸 Cognates Only
          </button>
        </div>
      </div>

      {/* Vocabulary List */}
      <div className="space-y-3">
        {vocabulary.map((item) => (
          <div
            key={item.id}
            className="card card-hover flex items-start justify-between"
          >
            <div className="flex-1">
              <div className="flex items-center gap-2 mb-1">
                <span className="text-lg font-semibold text-gray-900">
                  {item.french}
                </span>
                {getGenderBadge(item.gender)}
                {item.is_cognate && (
                  <span className="badge bg-yellow-100 text-yellow-700">🇪🇸</span>
                )}
              </div>
              <p className="text-gray-600">{item.english}</p>
              {item.spanish && (
                <p className="text-sm text-gray-500">ES: {item.spanish}</p>
              )}
              {item.phonetic && (
                <p className="text-sm text-gray-400">[{item.phonetic}]</p>
              )}
              {item.cognate_note && (
                <p className="text-sm text-yellow-600 mt-1">{item.cognate_note}</p>
              )}
            </div>

            <button
              onClick={() => speakFrench(item.french)}
              disabled={speaking}
              className="btn-secondary btn-sm"
            >
              <Volume2 size={18} />
            </button>
          </div>
        ))}

        {vocabulary.length === 0 && (
          <div className="text-center py-8 text-gray-500">
            No vocabulary found matching your criteria.
          </div>
        )}
      </div>
    </div>
  );
}
