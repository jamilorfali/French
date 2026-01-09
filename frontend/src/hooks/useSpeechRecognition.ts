import { useState, useCallback, useRef, useEffect } from 'react';

// Type declarations for Web Speech API
interface SpeechRecognitionEvent {
  results: SpeechRecognitionResultList;
  resultIndex: number;
}

interface SpeechRecognitionResultList {
  length: number;
  item(index: number): SpeechRecognitionResult;
  [index: number]: SpeechRecognitionResult;
}

interface SpeechRecognitionResult {
  isFinal: boolean;
  length: number;
  item(index: number): SpeechRecognitionAlternative;
  [index: number]: SpeechRecognitionAlternative;
}

interface SpeechRecognitionAlternative {
  transcript: string;
  confidence: number;
}

interface SpeechRecognition extends EventTarget {
  continuous: boolean;
  interimResults: boolean;
  lang: string;
  onresult: ((event: SpeechRecognitionEvent) => void) | null;
  onerror: ((event: { error: string }) => void) | null;
  onend: (() => void) | null;
  onstart: (() => void) | null;
  start(): void;
  stop(): void;
  abort(): void;
}

declare global {
  interface Window {
    SpeechRecognition?: new () => SpeechRecognition;
    webkitSpeechRecognition?: new () => SpeechRecognition;
  }
}

interface RecognitionResult {
  transcript: string;
  confidence: number;
}

export function useSpeechRecognition() {
  const [listening, setListening] = useState(false);
  const [supported, setSupported] = useState(false);
  const [transcript, setTranscript] = useState('');
  const [confidence, setConfidence] = useState(0);
  const [error, setError] = useState<string | null>(null);

  const recognitionRef = useRef<SpeechRecognition | null>(null);

  useEffect(() => {
    if (typeof window !== 'undefined') {
      const SpeechRecognitionClass =
        window.SpeechRecognition || window.webkitSpeechRecognition;

      if (SpeechRecognitionClass) {
        setSupported(true);
        recognitionRef.current = new SpeechRecognitionClass();
        recognitionRef.current.continuous = false;
        recognitionRef.current.interimResults = false;
      }
    }
  }, []);

  const startListening = useCallback(
    (lang: string = 'fr-FR'): Promise<RecognitionResult> => {
      return new Promise((resolve, reject) => {
        if (!recognitionRef.current) {
          reject(new Error('Speech recognition not supported'));
          return;
        }

        setError(null);
        setTranscript('');
        setConfidence(0);

        const recognition = recognitionRef.current;
        recognition.lang = lang;

        recognition.onstart = () => {
          setListening(true);
        };

        recognition.onresult = (event: SpeechRecognitionEvent) => {
          const result = event.results[0][0];
          setTranscript(result.transcript);
          setConfidence(result.confidence);
          resolve({
            transcript: result.transcript,
            confidence: result.confidence,
          });
        };

        recognition.onerror = (event) => {
          setError(event.error);
          setListening(false);
          reject(new Error(event.error));
        };

        recognition.onend = () => {
          setListening(false);
        };

        try {
          recognition.start();
        } catch (err) {
          reject(err);
        }
      });
    },
    []
  );

  const stopListening = useCallback(() => {
    if (recognitionRef.current) {
      recognitionRef.current.stop();
      setListening(false);
    }
  }, []);

  const listenForFrench = useCallback(
    () => startListening('fr-FR'),
    [startListening]
  );

  // Compare user's speech to expected text
  const compareSpeech = useCallback(
    (expected: string, actual: string): { match: boolean; similarity: number } => {
      const normalize = (s: string) =>
        s
          .toLowerCase()
          .normalize('NFD')
          .replace(/[\u0300-\u036f]/g, '') // Remove accents for comparison
          .replace(/[^\w\s]/g, '')
          .trim();

      const normalizedExpected = normalize(expected);
      const normalizedActual = normalize(actual);

      if (normalizedExpected === normalizedActual) {
        return { match: true, similarity: 1 };
      }

      // Calculate Levenshtein distance for partial matching
      const distance = levenshteinDistance(normalizedExpected, normalizedActual);
      const maxLen = Math.max(normalizedExpected.length, normalizedActual.length);
      const similarity = maxLen > 0 ? 1 - distance / maxLen : 0;

      return {
        match: similarity >= 0.8, // 80% similarity threshold
        similarity,
      };
    },
    []
  );

  return {
    startListening,
    stopListening,
    listenForFrench,
    listening,
    supported,
    transcript,
    confidence,
    error,
    compareSpeech,
  };
}

// Levenshtein distance helper
function levenshteinDistance(a: string, b: string): number {
  const matrix: number[][] = [];

  for (let i = 0; i <= b.length; i++) {
    matrix[i] = [i];
  }

  for (let j = 0; j <= a.length; j++) {
    matrix[0][j] = j;
  }

  for (let i = 1; i <= b.length; i++) {
    for (let j = 1; j <= a.length; j++) {
      if (b.charAt(i - 1) === a.charAt(j - 1)) {
        matrix[i][j] = matrix[i - 1][j - 1];
      } else {
        matrix[i][j] = Math.min(
          matrix[i - 1][j - 1] + 1,
          matrix[i][j - 1] + 1,
          matrix[i - 1][j] + 1
        );
      }
    }
  }

  return matrix[b.length][a.length];
}
