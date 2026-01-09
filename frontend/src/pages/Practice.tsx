import { useState, useEffect, useCallback } from 'react';
import { useSearchParams, useNavigate } from 'react-router-dom';
import {
  Play,
  Pause,
  Volume2,
  Mic,
  Check,
  X,
  ArrowRight,
  RotateCcw,
  Clock,
} from 'lucide-react';
import {
  startPracticeSession,
  getNextExercise,
  submitAnswer,
  completePracticeSession,
} from '../services/api';
import { useSpeechSynthesis } from '../hooks/useSpeechSynthesis';
import { useSpeechRecognition } from '../hooks/useSpeechRecognition';
import type { Exercise, ExerciseResult, PracticeStartResponse } from '../types';

type SessionState = 'config' | 'active' | 'feedback' | 'complete';

export default function Practice() {
  const [searchParams] = useSearchParams();
  const navigate = useNavigate();

  // Session state
  const [sessionState, setSessionState] = useState<SessionState>('config');
  const [sessionId, setSessionId] = useState<number | null>(null);
  const [totalExercises, setTotalExercises] = useState(0);
  const [currentIndex, setCurrentIndex] = useState(0);

  // Exercise state
  const [exercise, setExercise] = useState<Exercise | null>(null);
  const [userAnswer, setUserAnswer] = useState<string | number>('');
  const [result, setResult] = useState<ExerciseResult | null>(null);
  const [startTime, setStartTime] = useState<number>(0);

  // Summary state
  const [correctCount, setCorrectCount] = useState(0);
  const [incorrectCount, setIncorrectCount] = useState(0);

  // Config state
  const [duration, setDuration] = useState(
    parseInt(searchParams.get('duration') || '15')
  );
  const [focusAreas, setFocusAreas] = useState<string[]>([]);

  // Hooks
  const { speakFrench, speaking, supported: ttsSupported } = useSpeechSynthesis();
  const {
    listenForFrench,
    listening,
    transcript,
    supported: sttSupported,
  } = useSpeechRecognition();

  // Start session
  const handleStartSession = async () => {
    try {
      const response: PracticeStartResponse = await startPracticeSession({
        session_type: 'mixed',
        duration_mins: duration,
        focus_areas: focusAreas,
      });

      setSessionId(response.session_id);
      setTotalExercises(response.total_exercises);
      setCurrentIndex(0);
      setCorrectCount(0);
      setIncorrectCount(0);
      setSessionState('active');

      // Fetch first exercise
      await fetchNextExercise(response.session_id);
    } catch (error) {
      console.error('Failed to start session:', error);
    }
  };

  // Fetch next exercise
  const fetchNextExercise = async (sid: number) => {
    try {
      const response = await getNextExercise(sid);

      if (response.complete) {
        setSessionState('complete');
        await completePracticeSession(sid);
      } else if (response.exercise) {
        setExercise(response.exercise);
        setCurrentIndex(response.exercise_index || 0);
        setUserAnswer('');
        setResult(null);
        setStartTime(Date.now());
        setSessionState('active');
      }
    } catch (error) {
      console.error('Failed to fetch exercise:', error);
    }
  };

  // Submit answer
  const handleSubmit = async () => {
    if (!sessionId || !exercise || userAnswer === '') return;

    const timeTaken = Math.round((Date.now() - startTime) / 1000);

    try {
      const response = await submitAnswer(sessionId, 0, userAnswer, timeTaken);
      setResult(response);

      if (response.correct) {
        setCorrectCount((c) => c + 1);
      } else {
        setIncorrectCount((c) => c + 1);
      }

      setSessionState('feedback');
    } catch (error) {
      console.error('Failed to submit answer:', error);
    }
  };

  // Next exercise
  const handleNext = async () => {
    if (!sessionId) return;
    await fetchNextExercise(sessionId);
  };

  // Handle speaking exercise
  const handleSpeak = async () => {
    try {
      const result = await listenForFrench();
      setUserAnswer(result.transcript);
    } catch (error) {
      console.error('Speech recognition error:', error);
    }
  };

  // Play audio for listening exercises
  const handlePlayAudio = useCallback(() => {
    if (exercise?.content?.french_text) {
      speakFrench(exercise.content.french_text as string);
    } else if (exercise?.content?.prompt) {
      speakFrench(exercise.content.prompt as string);
    }
  }, [exercise, speakFrench]);

  // Render config screen
  if (sessionState === 'config') {
    return (
      <div className="max-w-md mx-auto space-y-6">
        <h1 className="text-2xl font-bold text-gray-900">Start Practice</h1>

        <div className="card">
          <h2 className="text-lg font-semibold text-gray-900 mb-4">
            Session Length
          </h2>
          <div className="grid grid-cols-3 gap-3">
            {[5, 15, 30].map((mins) => (
              <button
                key={mins}
                onClick={() => setDuration(mins)}
                className={`py-3 rounded-lg font-medium transition-colors ${
                  duration === mins
                    ? 'bg-primary-600 text-white'
                    : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                }`}
              >
                {mins} min
              </button>
            ))}
          </div>
        </div>

        <div className="card">
          <h2 className="text-lg font-semibold text-gray-900 mb-4">
            Focus Areas (optional)
          </h2>
          <div className="flex flex-wrap gap-2">
            {['listening', 'conjugation', 'gender', 'pronunciation'].map(
              (area) => (
                <button
                  key={area}
                  onClick={() =>
                    setFocusAreas((prev) =>
                      prev.includes(area)
                        ? prev.filter((a) => a !== area)
                        : [...prev, area]
                    )
                  }
                  className={`badge cursor-pointer transition-colors ${
                    focusAreas.includes(area) ? 'badge-primary' : 'bg-gray-100'
                  }`}
                >
                  {area}
                </button>
              )
            )}
          </div>
        </div>

        <button onClick={handleStartSession} className="btn-primary btn-lg w-full">
          <Play size={20} />
          Start Practice
        </button>
      </div>
    );
  }

  // Render complete screen
  if (sessionState === 'complete') {
    const accuracy =
      correctCount + incorrectCount > 0
        ? (correctCount / (correctCount + incorrectCount)) * 100
        : 0;

    return (
      <div className="max-w-md mx-auto space-y-6 text-center">
        <div className="text-6xl mb-4">🎉</div>
        <h1 className="text-2xl font-bold text-gray-900">Session Complete!</h1>

        <div className="card">
          <div className="grid grid-cols-3 gap-4">
            <div>
              <div className="text-3xl font-bold text-success-600">
                {correctCount}
              </div>
              <div className="text-sm text-gray-500">Correct</div>
            </div>
            <div>
              <div className="text-3xl font-bold text-error-600">
                {incorrectCount}
              </div>
              <div className="text-sm text-gray-500">Incorrect</div>
            </div>
            <div>
              <div className="text-3xl font-bold text-primary-600">
                {accuracy.toFixed(0)}%
              </div>
              <div className="text-sm text-gray-500">Accuracy</div>
            </div>
          </div>
        </div>

        <div className="flex gap-3">
          <button
            onClick={() => navigate('/')}
            className="btn-secondary flex-1"
          >
            Home
          </button>
          <button
            onClick={() => {
              setSessionState('config');
              setSessionId(null);
            }}
            className="btn-primary flex-1"
          >
            <RotateCcw size={18} />
            Practice Again
          </button>
        </div>
      </div>
    );
  }

  // Render exercise
  return (
    <div className="max-w-md mx-auto space-y-6">
      {/* Progress bar */}
      <div className="flex items-center gap-3">
        <div className="flex-1 progress-bar">
          <div
            className="progress-bar-fill"
            style={{
              width: `${((currentIndex + 1) / totalExercises) * 100}%`,
            }}
          />
        </div>
        <span className="text-sm text-gray-500">
          {currentIndex + 1}/{totalExercises}
        </span>
      </div>

      {/* Exercise Card */}
      {exercise && (
        <div
          className={`card ${
            sessionState === 'feedback'
              ? result?.correct
                ? 'flash-correct'
                : 'flash-incorrect'
              : ''
          }`}
        >
          {/* Exercise Type Badge */}
          <div className="mb-4">
            <span className="badge badge-primary">
              {exercise.type.replace('_', ' ')}
            </span>
          </div>

          {/* Exercise Content */}
          <div className="space-y-4">
            {/* Prompt/Question */}
            <div className="text-center">
              {exercise.type === 'listening' && (
                <button
                  onClick={handlePlayAudio}
                  disabled={speaking}
                  className="btn-primary btn-lg mb-4"
                >
                  {speaking ? <Pause size={24} /> : <Volume2 size={24} />}
                  {speaking ? 'Playing...' : 'Play Audio'}
                </button>
              )}

              <p className="text-xl font-semibold text-gray-900">
                {(exercise.content?.prompt as string) ||
                  (exercise.content?.question as string) ||
                  'Complete the exercise'}
              </p>

              {exercise.content?.phonetic && sessionState === 'active' && (
                <p className="text-sm text-gray-500 mt-2">
                  [{exercise.content.phonetic as string}]
                </p>
              )}
            </div>

            {/* Answer Input based on exercise type */}
            {sessionState === 'active' && (
              <>
                {exercise.type === 'multiple_choice' && (
                  <div className="space-y-2">
                    {(exercise.content?.options as string[])?.map(
                      (option, idx) => (
                        <button
                          key={idx}
                          onClick={() => setUserAnswer(idx)}
                          className={`w-full p-3 rounded-lg text-left transition-colors ${
                            userAnswer === idx
                              ? 'bg-primary-100 border-2 border-primary-500'
                              : 'bg-gray-50 border-2 border-transparent hover:bg-gray-100'
                          }`}
                        >
                          {option}
                        </button>
                      )
                    )}
                  </div>
                )}

                {exercise.type === 'gender' && (
                  <div className="flex gap-3">
                    {['le', 'la'].map((article) => (
                      <button
                        key={article}
                        onClick={() => setUserAnswer(article)}
                        className={`flex-1 py-4 text-2xl font-bold rounded-lg transition-colors ${
                          userAnswer === article
                            ? 'bg-primary-100 border-2 border-primary-500'
                            : 'bg-gray-50 border-2 border-transparent hover:bg-gray-100'
                        }`}
                      >
                        {article}
                      </button>
                    ))}
                  </div>
                )}

                {(exercise.type === 'vocabulary_flashcard' ||
                  exercise.type === 'conjugation' ||
                  exercise.type === 'translation') && (
                  <input
                    type="text"
                    value={userAnswer as string}
                    onChange={(e) => setUserAnswer(e.target.value)}
                    placeholder="Type your answer..."
                    className="input text-center text-lg"
                    autoFocus
                  />
                )}

                {exercise.type === 'speaking' && sttSupported && (
                  <div className="text-center">
                    <button
                      onClick={handleSpeak}
                      disabled={listening}
                      className={`btn-lg rounded-full p-6 ${
                        listening ? 'bg-error-500' : 'bg-primary-600'
                      } text-white`}
                    >
                      <Mic size={32} />
                    </button>
                    {transcript && (
                      <p className="mt-3 text-lg text-gray-700">
                        You said: "{transcript}"
                      </p>
                    )}
                  </div>
                )}
              </>
            )}

            {/* Spanish Hint */}
            {exercise.spanish_hint && sessionState === 'active' && (
              <div className="p-3 bg-yellow-50 rounded-lg text-sm text-yellow-800">
                🇪🇸 {exercise.spanish_hint}
              </div>
            )}
          </div>

          {/* Feedback */}
          {sessionState === 'feedback' && result && (
            <div
              className={`mt-4 p-4 rounded-lg ${
                result.correct ? 'bg-success-50' : 'bg-error-50'
              }`}
            >
              <div className="flex items-center gap-2 mb-2">
                {result.correct ? (
                  <>
                    <Check className="text-success-600" size={20} />
                    <span className="font-semibold text-success-700">
                      Correct!
                    </span>
                  </>
                ) : (
                  <>
                    <X className="text-error-600" size={20} />
                    <span className="font-semibold text-error-700">
                      Incorrect
                    </span>
                  </>
                )}
              </div>

              {!result.correct && (
                <p className="text-gray-700">
                  Correct answer:{' '}
                  <span className="font-medium">
                    {typeof result.correct_answer === 'object'
                      ? JSON.stringify(result.correct_answer)
                      : String(result.correct_answer)}
                  </span>
                </p>
              )}

              {result.explanation && (
                <p className="mt-2 text-sm text-gray-600">{result.explanation}</p>
              )}

              {result.spanish_note && (
                <p className="mt-2 text-sm text-yellow-700">
                  🇪🇸 {result.spanish_note}
                </p>
              )}
            </div>
          )}
        </div>
      )}

      {/* Action Buttons */}
      <div className="flex gap-3">
        {sessionState === 'active' && (
          <button
            onClick={handleSubmit}
            disabled={userAnswer === ''}
            className="btn-primary btn-lg flex-1"
          >
            <Check size={20} />
            Submit
          </button>
        )}

        {sessionState === 'feedback' && (
          <button onClick={handleNext} className="btn-primary btn-lg flex-1">
            <ArrowRight size={20} />
            Next
          </button>
        )}
      </div>

      {/* TTS/STT not supported warning */}
      {(!ttsSupported || !sttSupported) && (
        <p className="text-sm text-center text-gray-500">
          Some audio features may not work in your browser.
        </p>
      )}
    </div>
  );
}
