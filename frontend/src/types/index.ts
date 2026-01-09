// ============ CEFR Levels ============
export interface CEFRLevel {
  id: number;
  code: string;
  name: string;
  description?: string;
  order: number;
  af_levels?: string;
  vocabulary_target: number;
}

// ============ Vocabulary ============
export interface Vocabulary {
  id: number;
  french: string;
  english: string;
  spanish?: string;
  gender?: 'm' | 'f' | 'mf' | '-';
  part_of_speech: string;
  category?: string;
  is_cognate: boolean;
  phonetic?: string;
  cognate_spanish?: string;
  cognate_note?: string;
  example_french?: string;
  example_english?: string;
  example_spanish?: string;
}

// ============ Grammar ============
export interface Grammar {
  id: number;
  topic: string;
  title: string;
  cefr_level_id: number;
  order: number;
  explanation_en: string;
  explanation_es?: string;
  spanish_comparison?: string;
  examples: Array<{
    french: string;
    english: string;
    spanish?: string;
  }>;
  common_mistakes: string[];
  tips: string[];
}

// ============ Verbs ============
export interface Conjugation {
  tense: string;
  mood: string;
  je?: string;
  tu?: string;
  il_elle?: string;
  nous?: string;
  vous?: string;
  ils_elles?: string;
  spanish_equivalent?: string;
}

export interface Verb {
  id: number;
  infinitive: string;
  english: string;
  spanish?: string;
  group: 1 | 2 | 3;
  is_irregular: boolean;
  cefr_level_id: number;
  auxiliary: 'avoir' | 'être';
  past_participle?: string;
  present_participle?: string;
  notes?: string;
  spanish_comparison?: string;
  conjugations: Conjugation[];
}

// ============ Lessons ============
export interface Lesson {
  id: number;
  cefr_level_id: number;
  unit_number: number;
  title: string;
  description?: string;
  objectives: string[];
  themes: string[];
  grammar_topics: string[];
  estimated_duration: number;
}

// ============ Exercises ============
export type ExerciseType =
  | 'vocabulary_flashcard'
  | 'multiple_choice'
  | 'listening'
  | 'speaking'
  | 'conjugation'
  | 'gender'
  | 'sentence_builder'
  | 'fill_blank'
  | 'translation';

export interface Exercise {
  type: ExerciseType;
  content: Record<string, unknown>;
  hints?: string[];
  spanish_hint?: string;
}

export interface ExerciseResult {
  correct: boolean;
  correct_answer: unknown;
  explanation?: string;
  spanish_note?: string;
  points_earned: number;
  streak: number;
}

// ============ Practice Sessions ============
export interface PracticeSession {
  id: number;
  session_type: string;
  target_duration_mins: number;
  actual_duration_mins?: number;
  items_practiced: number;
  correct_count: number;
  incorrect_count: number;
  accuracy: number;
  started_at: string;
  completed_at?: string;
  focus_areas: string[];
}

export interface PracticeSessionConfig {
  session_type: string;
  duration_mins: number;
  focus_areas: string[];
  cefr_level?: string;
}

// ============ Progress ============
export interface OverallProgress {
  current_level: string;
  vocabulary_learned: number;
  vocabulary_total: number;
  grammar_learned: number;
  grammar_total: number;
  verbs_learned: number;
  verbs_total: number;
  total_practice_time_mins: number;
  current_streak_days: number;
  accuracy_7_days: number;
  items_due_for_review: number;
}

export interface WeakArea {
  area_type: string;
  area_name: string;
  accuracy: number;
  last_practiced?: string;
  recommended_exercises: number;
}

// ============ User ============
export interface UserSettings {
  session_duration: number;
  speech_rate: number;
  show_spanish_hints: boolean;
  show_phonetic: boolean;
  daily_goal: number;
  focus_areas: string[];
}

export interface User {
  id: number;
  name: string;
  native_language: string;
  secondary_language: string;
  target_language: string;
  current_cefr_level: string;
  settings: UserSettings;
  created_at: string;
  updated_at?: string;
  last_active?: string;
}

// ============ API Responses ============
export interface ApiError {
  detail: string;
}

export interface PracticeStartResponse {
  session_id: number;
  total_exercises: number;
  duration_mins: number;
  focus_areas: string[];
}

export interface NextExerciseResponse {
  complete: boolean;
  exercise_index?: number;
  total_exercises?: number;
  exercise?: Exercise;
  message?: string;
  total?: number;
  correct?: number;
}
