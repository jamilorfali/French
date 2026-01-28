import { useState, useCallback, useEffect } from 'react';
import { useNavigate, useSearchParams } from 'react-router-dom';
import {
  Play,
  Pause,
  Volume2,
  Check,
  X,
  ArrowRight,
  RotateCcw,
  SkipForward,
  Target,
} from 'lucide-react';
import {
  startPracticeSession,
  getNextExercise,
  submitAnswer,
  completePracticeSession,
} from '../services/api';
import { useSpeechSynthesis } from '../hooks/useSpeechSynthesis';
import type { Exercise, ExerciseResult, PracticeStartResponse } from '../types';

type SessionState = 'config' | 'active' | 'feedback' | 'complete';

export default function Practice() {
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();
  const [sessionState, setSessionState] = useState<SessionState>('config');
  const [sessionId, setSessionId] = useState<number | null>(null);
  const [totalExercises, setTotalExercises] = useState(0);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [exercise, setExercise] = useState<Exercise | null>(null);
  const [userAnswer, setUserAnswer] = useState<string | number | null>(null);
  const [result, setResult] = useState<ExerciseResult | null>(null);
  const [startTime, setStartTime] = useState<number>(0);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [correctCount, setCorrectCount] = useState(0);
  const [incorrectCount, setIncorrectCount] = useState(0);
  const [duration, setDuration] = useState(() => {
    // Read initial duration from URL query param, default to 15
    const urlDuration = searchParams.get('duration');
    return urlDuration ? parseInt(urlDuration, 10) : 15;
  });
  const [focusAreas, setFocusAreas] = useState<string[]>(() => {
    // Read initial focus area from URL query param (e.g., ?type=weak_areas)
    const urlType = searchParams.get('type');
    return urlType === 'weak_areas' ? ['weak_areas'] : [];
  });

  const { speakFrench, speaking, supported: ttsSupported } = useSpeechSynthesis();

  const handleStartSession = async () => {
    try {
      const sessionType = focusAreas.length === 1 ? focusAreas[0] : 'mixed';
      const response: PracticeStartResponse = await startPracticeSession({
        session_type: sessionType,
        duration_mins: duration,
        focus_areas: focusAreas,
      });
      setSessionId(response.session_id);
      setTotalExercises(response.total_exercises);
      setCurrentIndex(0);
      setCorrectCount(0);
      setIncorrectCount(0);
      setSessionState('active');
      await fetchNextExercise(response.session_id);
    } catch (error) {
      console.error('Failed to start session:', error);
      alert('Failed to start. Make sure server is running.');
    }
  };

  const fetchNextExercise = async (sid: number) => {
    try {
      const response = await getNextExercise(sid);
      if (response.complete) {
        setSessionState('complete');
        await completePracticeSession(sid);
      } else if (response.exercise) {
        setExercise(response.exercise);
        setCurrentIndex(response.exercise_index || 0);
        setUserAnswer(null);
        setResult(null);
        setStartTime(Date.now());
        setSessionState('active');
      }
    } catch (error) {
      console.error('Failed to fetch exercise:', error);
    }
  };

  const handleSubmit = async () => {
    if (!sessionId || !exercise || userAnswer === null || isSubmitting) return;
    setIsSubmitting(true);
    const timeTaken = Math.round((Date.now() - startTime) / 1000);
    try {
      const response = await submitAnswer(sessionId, 0, userAnswer, timeTaken);
      setResult(response);
      if (response.correct) setCorrectCount((c) => c + 1);
      else setIncorrectCount((c) => c + 1);
      setSessionState('feedback');
    } catch (error) {
      console.error('Failed to submit:', error);
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleNext = async () => {
    if (!sessionId) return;
    await fetchNextExercise(sessionId);
  };

  const handleSkip = async () => {
    // Skip the current exercise without submitting (counts as incorrect)
    if (!sessionId) return;
    setIncorrectCount((c) => c + 1);
    await fetchNextExercise(sessionId);
  };

  const handlePlayAudio = useCallback(() => {
    const text = exercise?.content?.french_text || exercise?.content?.expected_text || exercise?.content?.prompt;
    if (text) {
      const frenchMatch = String(text).match(/[''""]([ ^''""]+)[''""]/) ;
      speakFrench(frenchMatch ? frenchMatch[1] : String(text));
    }
  }, [exercise, speakFrench]);

  const getExerciseDisplayType = (): string => {
    if (!exercise) return '';
    const names: Record<string, string> = {
      vocabulary_flashcard: 'Vocabulary', multiple_choice: 'Multiple Choice',
      listening: 'Listening', speaking: 'Pronunciation',
      conjugation: 'Conjugation', gender: 'Gender Practice',
    };
    return names[exercise.type] || exercise.type.replace(/_/g, ' ');
  };

  const hasOptions = () => !!(exercise?.content?.options && Array.isArray(exercise.content.options));

  if (sessionState === 'config') {
    return (
      <div className="max-w-md mx-auto space-y-6">
        <h1 className="text-2xl font-bold text-gray-900">Start Practice</h1>
        <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <h2 className="text-lg font-semibold text-gray-900 mb-4">Session Length</h2>
          <div className="grid grid-cols-3 gap-3">
            {[5, 15, 30].map((mins) => (
              <button key={mins} onClick={() => setDuration(mins)}
                className={`px-4 py-2 rounded-lg font-medium transition-colors ${duration === mins ? 'bg-blue-600 text-white' : 'bg-gray-100 text-gray-700 hover:bg-gray-200'}`}>
                {mins} min
              </button>
            ))}
          </div>
        </div>
        <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <h2 className="text-lg font-semibold text-gray-900 mb-4">Focus Area (select one)</h2>
          <div className="flex flex-wrap gap-2">
            {[
              { id: 'weak_areas', label: 'Focus Areas', icon: Target, description: 'Practice your weak spots' },
              { id: 'listening', label: 'Listening', icon: null, description: null },
              { id: 'conjugation', label: 'Conjugation', icon: null, description: null },
              { id: 'gender', label: 'Gender', icon: null, description: null },
            ].map((area) => (
              <button key={area.id}
                onClick={() => setFocusAreas(focusAreas.includes(area.id) ? [] : [area.id])}
                className={`px-4 py-2 rounded-lg font-medium transition-colors flex items-center gap-2 ${
                  focusAreas.includes(area.id)
                    ? area.id === 'weak_areas' ? 'bg-red-600 text-white' : 'bg-blue-600 text-white'
                    : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                }`}>
                {area.icon && <area.icon size={16} />}
                {area.label}
              </button>
            ))}
          </div>
          {focusAreas.includes('weak_areas') && (
            <p className="text-sm text-red-600 mt-2 font-medium">
              You'll practice items you've gotten wrong in past sessions
            </p>
          )}
          {!focusAreas.includes('weak_areas') && (
            <p className="text-sm text-gray-500 mt-2">Leave empty for mixed practice</p>
          )}
        </div>
        <button onClick={handleStartSession}
          className="w-full py-4 bg-blue-600 text-white rounded-lg font-semibold flex items-center justify-center gap-2 hover:bg-blue-700">
          <Play size={20} /> Start Practice
        </button>
      </div>
    );
  }

  if (sessionState === 'complete') {
    const total = correctCount + incorrectCount;
    const accuracy = total > 0 ? (correctCount / total) * 100 : 0;
    return (
      <div className="max-w-md mx-auto space-y-6 text-center">
        <div className="text-6xl mb-4">🎉</div>
        <h1 className="text-2xl font-bold text-gray-900">Session Complete!</h1>
        <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <div className="grid grid-cols-3 gap-4">
            <div><div className="text-3xl font-bold text-green-600">{correctCount}</div><div className="text-sm text-gray-500">Correct</div></div>
            <div><div className="text-3xl font-bold text-red-600">{incorrectCount}</div><div className="text-sm text-gray-500">Incorrect</div></div>
            <div><div className="text-3xl font-bold text-blue-600">{accuracy.toFixed(0)}%</div><div className="text-sm text-gray-500">Accuracy</div></div>
          </div>
        </div>
        <div className="flex gap-3">
          <button onClick={() => navigate('/')} className="flex-1 py-3 bg-gray-200 text-gray-700 rounded-lg font-medium hover:bg-gray-300">Home</button>
          <button onClick={() => { setSessionState('config'); setSessionId(null); setExercise(null); }}
            className="flex-1 py-3 bg-blue-600 text-white rounded-lg font-medium flex items-center justify-center gap-2 hover:bg-blue-700">
            <RotateCcw size={18} /> Practice Again
          </button>
        </div>
      </div>
    );
  }

  const progressWidth = `${((currentIndex + 1) / Math.max(totalExercises, 1)) * 100}%`;

  return (
    <div className="max-w-md mx-auto space-y-6">
      <div className="flex items-center gap-3">
        <div className="flex-1 h-2 bg-gray-200 rounded-full overflow-hidden">
          <div className="h-full bg-blue-600 transition-all duration-300" style={{ width: progressWidth }} />
        </div>
        <span className="text-sm text-gray-500 font-medium">{currentIndex + 1}/{totalExercises}</span>
      </div>

      {exercise && (
        <div className={`bg-white rounded-xl shadow-sm border p-6 ${sessionState === 'feedback' ? (result?.correct ? 'border-green-300 bg-green-50' : 'border-red-300 bg-red-50') : 'border-gray-200'}`}>
          <div className="mb-4">
            <span className="inline-block px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-sm font-medium capitalize">{getExerciseDisplayType()}</span>
          </div>

          <div className="space-y-4">
            {(exercise.type === 'listening' || exercise.type === 'speaking') && (
              <div className="text-center mb-4">
                <button onClick={handlePlayAudio} disabled={speaking}
                  className={`px-6 py-3 rounded-lg font-medium flex items-center gap-2 mx-auto ${speaking ? 'bg-gray-300 text-gray-500' : 'bg-blue-600 text-white hover:bg-blue-700'}`}>
                  {speaking ? <Pause size={20} /> : <Volume2 size={20} />}
                  {speaking ? 'Playing...' : 'Play Audio'}
                </button>
              </div>
            )}

            <div className="text-center">
              <p className="text-xl font-semibold text-gray-900">{exercise.content?.prompt || exercise.content?.question || 'Complete the exercise'}</p>
              {exercise.content?.phonetic && sessionState === 'active' && <p className="text-sm text-gray-500 mt-2 font-mono">[{exercise.content.phonetic}]</p>}
              {exercise.content?.english && <p className="text-sm text-gray-500 mt-2">({exercise.content.english})</p>}
            </div>

            {sessionState === 'active' && (
              <div className="mt-6">
                {hasOptions() && (
                  <div className="space-y-2">
                    {(exercise.content?.options as string[]).map((option, idx) => (
                      <button key={idx} onClick={() => setUserAnswer(idx)}
                        className={`w-full p-4 text-left rounded-lg flex items-center gap-3 transition-colors ${userAnswer === idx ? 'bg-blue-100 border-2 border-blue-500 text-blue-900' : 'bg-gray-50 border-2 border-transparent hover:bg-gray-100'}`}>
                        <span className="font-medium">{String.fromCharCode(65 + idx)}.</span> {option}
                      </button>
                    ))}
                  </div>
                )}

                {exercise.type === 'gender' && !hasOptions() && (
                  <div className="flex gap-4 justify-center">
                    {['le', 'la'].map((article) => (
                      <button key={article} onClick={() => setUserAnswer(article)}
                        className={`px-8 py-4 text-2xl font-bold rounded-lg transition-colors ${userAnswer === article ? 'bg-blue-100 border-2 border-blue-500 text-blue-900' : 'bg-gray-50 border-2 border-transparent hover:bg-gray-100'}`}>
                        {article}
                      </button>
                    ))}
                  </div>
                )}

                {(exercise.type === 'vocabulary_flashcard' || exercise.type === 'conjugation') && !hasOptions() && (
                  <input type="text" value={(userAnswer as string) || ''} onChange={(e) => setUserAnswer(e.target.value)}
                    placeholder="Type your answer..." className="w-full p-4 text-lg text-center border-2 border-gray-200 rounded-lg focus:border-blue-500 focus:outline-none" autoFocus
                    onKeyDown={(e) => { if (e.key === 'Enter' && userAnswer) handleSubmit(); }} />
                )}

                {(exercise.type === 'speaking' || exercise.type === 'pronunciation') && !hasOptions() && (
                  <div className="text-center space-y-4">
                    <div className="p-4 bg-yellow-50 border border-yellow-200 rounded-lg">
                      <p className="text-yellow-800 font-medium">Pronunciation exercises are not available</p>
                      <p className="text-sm text-yellow-700 mt-1">Speech recognition requires browser permissions that may not be available.</p>
                    </div>
                    <button onClick={handleSkip}
                      className="px-6 py-3 bg-gray-500 text-white rounded-lg font-medium flex items-center gap-2 mx-auto hover:bg-gray-600">
                      <SkipForward size={20} /> Skip This Exercise
                    </button>
                  </div>
                )}
              </div>
            )}

            {exercise.content?.spanish_hint && sessionState === 'active' && (
              <div className="p-3 bg-yellow-50 rounded-lg text-sm text-yellow-800 mt-4">🇪🇸 Hint: {exercise.content.spanish_hint}</div>
            )}
          </div>

          {sessionState === 'feedback' && result && (
            <div className={`mt-4 p-4 rounded-lg ${result.correct ? 'bg-green-100' : 'bg-red-100'}`}>
              <div className="flex items-center gap-2 mb-2">
                {result.correct ? (<><Check className="text-green-600" size={24} /><span className="font-bold text-green-700 text-lg">Correct!</span></>) : (<><X className="text-red-600" size={24} /><span className="font-bold text-red-700 text-lg">Incorrect</span></>)}
              </div>
              {!result.correct && result.correct_answer && (
                <p className="text-gray-700 mt-2">Correct answer: <span className="font-semibold">{typeof result.correct_answer === 'object' ? ((result.correct_answer as any).correct_answer || (result.correct_answer as any).french || (result.correct_answer as any).correct_article || JSON.stringify(result.correct_answer)) : String(result.correct_answer)}</span></p>
              )}
              {result.spanish_note && <p className="mt-2 text-sm text-yellow-700">🇪🇸 {result.spanish_note}</p>}
            </div>
          )}
        </div>
      )}

      <div className="flex gap-3">
        {sessionState === 'active' && (
          <button onClick={handleSubmit} disabled={userAnswer === null || isSubmitting}
            className={`flex-1 py-4 rounded-lg font-semibold flex items-center justify-center gap-2 ${userAnswer === null || isSubmitting ? 'bg-gray-200 text-gray-400 cursor-not-allowed' : 'bg-blue-600 text-white hover:bg-blue-700'}`}>
            <Check size={20} /> {isSubmitting ? 'Submitting...' : 'Submit'}
          </button>
        )}
        {sessionState === 'feedback' && (
          <button onClick={handleNext} className="flex-1 py-4 bg-blue-600 text-white rounded-lg font-semibold flex items-center justify-center gap-2 hover:bg-blue-700">
            <ArrowRight size={20} /> Next
          </button>
        )}
      </div>

      {!ttsSupported && <p className="text-sm text-center text-orange-600">Text-to-speech not supported. Audio may not work.</p>}
    </div>
  );
}
