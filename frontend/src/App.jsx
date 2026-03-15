import { useState, useEffect } from 'react';
import { Sparkles, Loader2, GraduationCap, Sun, Moon } from 'lucide-react';
import UploadZone from './components/UploadZone';
import Quiz from './components/Quiz';
import './index.css';

function App() {
  const [loading, setLoading] = useState(false);
  const [quiz, setQuiz] = useState(null);
  const [error, setError] = useState(null);
  const [theme, setTheme] = useState(() => {
    if (typeof window !== 'undefined') {
      return localStorage.getItem('theme') || 'light';
    }
    return 'light';
  });

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
  }, [theme]);

  const toggleTheme = () => {
    setTheme(prev => prev === 'light' ? 'dark' : 'light');
  };

  const handleFileUpload = async (file, numQuestions = 10) => {
    setLoading(true);
    setError(null);
    
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch(`http://localhost:8000/api/generate?num_questions=${numQuestions}`, {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Error al generar el examen. Por favor, intenta de nuevo.');
      }

      const data = await response.json();
      setQuiz(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const restart = () => {
    setQuiz(null);
    setError(null);
  };

  return (
    <div className="min-h-screen">
      <button className="theme-toggle" onClick={toggleTheme} title="Cambiar tema">
        {theme === 'light' ? <Moon size={20} /> : <Sun size={20} />}
      </button>

      {/* Navbar / Header */}
      <nav style={{ 
        padding: '1.5rem 2rem', 
        display: 'flex', 
        alignItems: 'center', 
        justifyContent: 'space-between',
        position: 'absolute',
        width: '100%',
        zIndex: 10,
        color: quiz ? 'var(--deep-text)' : 'white'
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
          <div style={{ 
            background: 'var(--primary)', padding: '8px', borderRadius: '12px',
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            boxShadow: '0 5px 15px rgba(37, 99, 235, 0.4)'
          }}>
            <GraduationCap color="white" size={24} />
          </div>
          <h1 style={{ fontSize: '1.5rem', letterSpacing: '-0.5px', fontFamily: 'Outfit' }}>Examiname</h1>
        </div>
        
        <button className="btn" style={{ 
          background: quiz ? 'rgba(0,0,0,0.05)' : 'rgba(255, 255, 255, 0.2)', 
          backdropFilter: 'blur(10px)',
          color: quiz ? 'var(--deep-text)' : 'white',
          border: '1px solid rgba(255,255,255,0.3)',
          padding: '0.5rem 1.2rem', 
          fontSize: '0.9rem' 
        }}>
          Documentación
        </button>
      </nav>

      <main>
        {!loading && !quiz && (
          <div className="animate-fade">
            <div className="hero-bg">
              <h1 style={{ fontSize: '4.5rem', marginBottom: '1.5rem', maxWidth: '1000px', margin: '0 auto 1.5rem' }}>
                Transforma tus PDFs en <span style={{ color: 'white', textDecoration: 'underline', textDecorationColor: 'var(--primary)' }}>Exámenes Inteligentes</span>
              </h1>
              <p style={{ color: 'rgba(255,255,255,0.9)', fontSize: '1.4rem', maxWidth: '750px', margin: '0 auto 4rem', fontWeight: 500 }}>
                Experimenta el futuro de las evaluaciones académicas con generación por IA de última generación.
              </p>
              <UploadZone onUpload={handleFileUpload} />
            </div>
            {error && <p style={{ color: 'var(--error)', textAlign: 'center', marginTop: '2rem' }}>{error}</p>}
          </div>
        )}

        {loading && (
          <div className="animate-fade container" style={{ textAlign: 'center', marginTop: '12rem' }}>
            <div className="glass-card" style={{ padding: '5rem', display: 'inline-block', maxWidth: '500px' }}>
              <div style={{ position: 'relative', display: 'inline-block', marginBottom: '2.5rem' }}>
                <Loader2 size={80} className="animate-spin" color="var(--primary)" />
                <Sparkles size={32} style={{ position: 'absolute', top: -15, right: -15 }} color="var(--primary)" />
              </div>
              <h2 style={{ fontSize: '2rem' }}>Creando tu Examen...</h2>
              <p style={{ color: 'var(--text-low)', marginTop: '1.5rem', fontSize: '1.1rem' }}>
                Nuestra IA está analizando tu documento para diseñar la evaluación perfecta.
              </p>
            </div>
          </div>
        )}

        {quiz && (
          <div style={{ marginTop: '8rem' }} className="animate-fade">
            <div style={{ textAlign: 'center', marginBottom: '4rem' }}>
              <h1 style={{ fontSize: '3rem', color: 'var(--deep-text)' }}>{quiz.title}</h1>
              <p style={{ color: 'var(--text-low)', fontSize: '1.1rem', marginTop: '0.5rem' }}>Evaluación Académica • {quiz.questions.length} Preguntas</p>
            </div>
            <Quiz quiz={quiz} onRestart={restart} />
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
