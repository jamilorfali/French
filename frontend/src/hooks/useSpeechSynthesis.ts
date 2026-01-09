import { useState, useEffect, useCallback } from 'react';

interface SpeechOptions {
  rate?: number;
  pitch?: number;
  volume?: number;
}

export function useSpeechSynthesis() {
  const [speaking, setSpeaking] = useState(false);
  const [supported, setSupported] = useState(false);
  const [voices, setVoices] = useState<SpeechSynthesisVoice[]>([]);
  const [frenchVoice, setFrenchVoice] = useState<SpeechSynthesisVoice | null>(null);

  useEffect(() => {
    if (typeof window !== 'undefined' && 'speechSynthesis' in window) {
      setSupported(true);

      const loadVoices = () => {
        const availableVoices = window.speechSynthesis.getVoices();
        setVoices(availableVoices);

        // Find best French voice
        const frVoice = availableVoices.find(
          (v) => v.lang.startsWith('fr') && v.name.toLowerCase().includes('french')
        ) || availableVoices.find((v) => v.lang.startsWith('fr'));

        if (frVoice) {
          setFrenchVoice(frVoice);
        }
      };

      loadVoices();

      // Voices might load asynchronously
      window.speechSynthesis.onvoiceschanged = loadVoices;
    }
  }, []);

  const speak = useCallback(
    (text: string, lang: 'fr-FR' | 'es-ES' | 'en-US' = 'fr-FR', options: SpeechOptions = {}) => {
      if (!supported) return;

      // Cancel any ongoing speech
      window.speechSynthesis.cancel();

      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = lang;
      utterance.rate = options.rate ?? 0.9; // Slightly slower for learning
      utterance.pitch = options.pitch ?? 1;
      utterance.volume = options.volume ?? 1;

      // Use French voice if available and speaking French
      if (lang === 'fr-FR' && frenchVoice) {
        utterance.voice = frenchVoice;
      }

      utterance.onstart = () => setSpeaking(true);
      utterance.onend = () => setSpeaking(false);
      utterance.onerror = () => setSpeaking(false);

      window.speechSynthesis.speak(utterance);
    },
    [supported, frenchVoice]
  );

  const stop = useCallback(() => {
    if (supported) {
      window.speechSynthesis.cancel();
      setSpeaking(false);
    }
  }, [supported]);

  const speakFrench = useCallback(
    (text: string, options?: SpeechOptions) => speak(text, 'fr-FR', options),
    [speak]
  );

  const speakSpanish = useCallback(
    (text: string, options?: SpeechOptions) => speak(text, 'es-ES', options),
    [speak]
  );

  const speakEnglish = useCallback(
    (text: string, options?: SpeechOptions) => speak(text, 'en-US', options),
    [speak]
  );

  return {
    speak,
    speakFrench,
    speakSpanish,
    speakEnglish,
    stop,
    speaking,
    supported,
    voices,
    frenchVoice,
  };
}
