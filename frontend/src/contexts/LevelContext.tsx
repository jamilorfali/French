import { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { getLevels, getUserProfile, updateUserProfile } from '../services/api';
import type { CEFRLevel } from '../types';

interface LevelContextType {
  currentLevel: string;
  levels: CEFRLevel[];
  currentLevelInfo: CEFRLevel | undefined;
  setLevel: (level: string) => Promise<void>;
  loading: boolean;
  levelChanging: boolean;
}

const LevelContext = createContext<LevelContextType | undefined>(undefined);

export function LevelProvider({ children }: { children: ReactNode }) {
  const [currentLevel, setCurrentLevel] = useState<string>('A1');
  const [levels, setLevels] = useState<CEFRLevel[]>([]);
  const [loading, setLoading] = useState(true);
  const [levelChanging, setLevelChanging] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [levelsData, userProfile] = await Promise.all([
          getLevels(),
          getUserProfile(),
        ]);
        setLevels(levelsData);
        setCurrentLevel(userProfile.current_cefr_level || 'A1');
      } catch (error) {
        console.error('Failed to fetch level data:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const setLevel = async (newLevel: string) => {
    if (newLevel === currentLevel || levelChanging) return;

    setLevelChanging(true);
    try {
      await updateUserProfile({ current_cefr_level: newLevel });
      setCurrentLevel(newLevel);
    } catch (error) {
      console.error('Failed to update level:', error);
      throw error;
    } finally {
      setLevelChanging(false);
    }
  };

  const currentLevelInfo = levels.find(l => l.code === currentLevel);

  return (
    <LevelContext.Provider
      value={{
        currentLevel,
        levels,
        currentLevelInfo,
        setLevel,
        loading,
        levelChanging,
      }}
    >
      {children}
    </LevelContext.Provider>
  );
}

export function useLevel() {
  const context = useContext(LevelContext);
  if (context === undefined) {
    throw new Error('useLevel must be used within a LevelProvider');
  }
  return context;
}
