import { Routes, Route } from 'react-router-dom';
import Layout from './components/layout/Layout';
import Home from './pages/Home';
import Practice from './pages/Practice';
import Vocabulary from './pages/Vocabulary';
import Grammar from './pages/Grammar';
import Verbs from './pages/Verbs';
import Progress from './pages/Progress';
import Lessons from './pages/Lessons';
import LessonDetail from './pages/LessonDetail';

function App() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/practice" element={<Practice />} />
        <Route path="/vocabulary" element={<Vocabulary />} />
        <Route path="/grammar" element={<Grammar />} />
        <Route path="/verbs" element={<Verbs />} />
        <Route path="/lessons" element={<Lessons />} />
        <Route path="/lessons/:lessonId" element={<LessonDetail />} />
        <Route path="/progress" element={<Progress />} />
      </Routes>
    </Layout>
  );
}

export default App;
