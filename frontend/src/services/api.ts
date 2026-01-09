import axios from 'axios';
import type {
  CEFRLevel,
  Vocabulary,
  Grammar,
  Verb,
  Lesson,
  User,
  OverallProgress,
  WeakArea,
  PracticeSession,
  PracticeSessionConfig,
  PracticeStartResponse,
  NextExerciseResponse,
  ExerciseResult,
} from '../types';

// Create axios instance with base configuration
const api = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

// ============ CEFR Levels ============
export const getLevels = async (): Promise<CEFRLevel[]> => {
  const response = await api.get('/levels/');
  return response.data;
};

export const getLevel = async (code: string): Promise<CEFRLevel> => {
  const response = await api.get(`/levels/${code}`);
  return response.data;
};

// ============ Vocabulary ============
export const getVocabulary = async (params?: {
  level?: string;
  category?: string;
  cognates_only?: boolean;
  search?: string;
  limit?: number;
}): Promise<Vocabulary[]> => {
  const response = await api.get('/vocabulary/', { params });
  return response.data;
};

export const getVocabularyItem = async (id: number): Promise<Vocabulary> => {
  const response = await api.get(`/vocabulary/${id}`);
  return response.data;
};

export const getRandomVocabulary = async (count: number, level?: string): Promise<Vocabulary[]> => {
  const response = await api.get(`/vocabulary/random/${count}`, {
    params: level ? { level } : undefined,
  });
  return response.data;
};

export const getVocabularyCategories = async (level?: string): Promise<{ categories: string[] }> => {
  const response = await api.get('/vocabulary/categories', {
    params: level ? { level } : undefined,
  });
  return response.data;
};

// ============ Grammar ============
export const getGrammarTopics = async (level?: string): Promise<Grammar[]> => {
  const response = await api.get('/grammar/', {
    params: level ? { level } : undefined,
  });
  return response.data;
};

export const getGrammarTopic = async (id: number): Promise<Grammar> => {
  const response = await api.get(`/grammar/${id}`);
  return response.data;
};

// ============ Verbs ============
export const getVerbs = async (params?: {
  level?: string;
  group?: number;
  irregular_only?: boolean;
  search?: string;
}): Promise<Verb[]> => {
  const response = await api.get('/verbs/', { params });
  return response.data;
};

export const getVerb = async (id: number): Promise<Verb> => {
  const response = await api.get(`/verbs/${id}`);
  return response.data;
};

export const getVerbByInfinitive = async (infinitive: string): Promise<Verb> => {
  const response = await api.get(`/verbs/infinitive/${infinitive}`);
  return response.data;
};

// ============ Lessons ============
export const getLessons = async (level?: string): Promise<Lesson[]> => {
  const response = await api.get('/lessons/', {
    params: level ? { level } : undefined,
  });
  return response.data;
};

export const getLesson = async (id: number): Promise<Lesson> => {
  const response = await api.get(`/lessons/${id}`);
  return response.data;
};

// ============ Practice Sessions ============
export const startPracticeSession = async (
  config: PracticeSessionConfig
): Promise<PracticeStartResponse> => {
  const response = await api.post('/practice/start', config);
  return response.data;
};

export const getNextExercise = async (sessionId: number): Promise<NextExerciseResponse> => {
  const response = await api.get(`/practice/${sessionId}/next`);
  return response.data;
};

export const submitAnswer = async (
  sessionId: number,
  exerciseId: number,
  answer: unknown,
  timeTakenSeconds: number
): Promise<ExerciseResult> => {
  const response = await api.post(`/practice/${sessionId}/answer`, {
    exercise_id: exerciseId,
    answer,
    time_taken_seconds: timeTakenSeconds,
  });
  return response.data;
};

export const completePracticeSession = async (sessionId: number): Promise<PracticeSession> => {
  const response = await api.post(`/practice/${sessionId}/complete`);
  return response.data;
};

// ============ Progress ============
export const getOverallProgress = async (): Promise<OverallProgress> => {
  const response = await api.get('/progress/');
  return response.data;
};

export const getWeakAreas = async (limit?: number): Promise<WeakArea[]> => {
  const response = await api.get('/progress/weak-areas', {
    params: limit ? { limit } : undefined,
  });
  return response.data;
};

export const getPracticeSessions = async (limit?: number): Promise<PracticeSession[]> => {
  const response = await api.get('/progress/sessions', {
    params: limit ? { limit } : undefined,
  });
  return response.data;
};

// ============ User ============
export const getUserProfile = async (): Promise<User> => {
  const response = await api.get('/user/profile');
  return response.data;
};

export const updateUserProfile = async (updates: Partial<User>): Promise<User> => {
  const response = await api.put('/user/profile', updates);
  return response.data;
};

export const touchUserActivity = async (): Promise<void> => {
  await api.post('/user/touch');
};

export default api;
