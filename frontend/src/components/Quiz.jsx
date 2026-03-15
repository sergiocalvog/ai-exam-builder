import { useState } from 'react';
import { Check, X, ArrowRight, RotateCcw } from 'lucide-react';

export default function Quiz({ quiz, onRestart }) {
  const [currentIdx, setCurrentIdx] = useState(0);
  const [selectedIdx, setSelectedIdx] = useState(null);
  const [isAnswered, setIsAnswered] = useState(false);
  const [score, setScore] = useState(0);
  const [showResults, setShowResults] = useState(false);
  const [userAnswers, setUserAnswers] = useState([]);

  if (showResults) {
    return (
      <div className="animate-fade container" style={{ textAlign: 'center' }}>
        <div className="glass-card" style={{ padding: '4rem 3rem' }}>
          <h2 style={{ fontSize: '4rem', marginBottom: '1.5rem' }}>🎯</h2>
          <h2 style={{ fontSize: '2.5rem', marginBottom: '1rem', color: 'var(--deep-text)' }}>Evaluación Completada</h2>
          <div style={{ fontSize: '5rem', margin: '2.5rem 0', color: 'var(--primary)', fontWeight: 800 }}>
            {score}/{quiz.questions.length}
          </div>
          <p style={{ color: 'var(--text-low)', marginBottom: '3rem', fontSize: '1.2rem' }}>
            Has logrado una puntuación del {Math.round((score / quiz.questions.length) * 100)}% en esta evaluación académica.
          </p>
          <button className="btn btn-primary" onClick={onRestart}>
            <RotateCcw size={22} /> Reintentar con otro PDF
          </button>
        </div>
      </div>
    );
  }

  const question = quiz.questions[currentIdx];

  const handleAnswerSelect = (idx) => {
    if (isAnswered) return;
    
    setSelectedIdx(idx);
    const correct = idx === question.correctAnswer;
    if (correct) setScore(score + 1);
    
    setIsAnswered(true);
    setUserAnswers([...userAnswers, { questionId: question.id, selected: idx, correct }]);
  };

  const handleNext = () => {
    if (currentIdx < quiz.questions.length - 1) {
      setCurrentIdx(currentIdx + 1);
      setSelectedIdx(null);
      setIsAnswered(false);
    } else {
      setShowResults(true);
    }
  };

  return (
    <div className="animate-fade container" style={{ maxWidth: '900px' }}>
      <div style={{ marginBottom: '3rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '0.5rem' }}>
          <span style={{ color: 'var(--text-low)', fontWeight: 700, textTransform: 'uppercase', fontSize: '0.8rem', letterSpacing: '0.05em' }}>
            Pregunta Actual
          </span>
          <span style={{ color: 'var(--deep-text)', fontSize: '1.2rem', fontWeight: 800 }}>
            {currentIdx + 1} de {quiz.questions.length}
          </span>
        </div>
        <div style={{ width: '240px', height: '10px', background: 'rgba(0,0,0,0.05)', borderRadius: '10px', overflow: 'hidden', boxShadow: 'inset 0 2px 4px rgba(0,0,0,0.05)' }}>
          <div style={{ 
            width: `${((currentIdx + 1) / quiz.questions.length) * 100}%`, 
            height: '100%', 
            background: 'linear-gradient(90deg, var(--primary), var(--primary-hover))',
            transition: 'width 0.5s cubic-bezier(0.4, 0, 0.2, 1)',
            boxShadow: '0 0 10px rgba(37, 99, 235, 0.4)'
          }} />
        </div>
      </div>

      <div className="glass-card" style={{ padding: '3.5rem' }}>
        <h3 style={{ marginBottom: '3rem', fontSize: '1.8rem', lineHeight: '1.3', color: 'var(--deep-text)' }}>{question.question}</h3>
        
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.2rem' }}>
          {question.options.map((option, idx) => {
            let bgColor = 'var(--glass-bg)';
            let borderColor = 'var(--glass-border)';
            let textColor = 'var(--deep-text)';
            
            if (selectedIdx === idx) {
              borderColor = 'var(--primary)';
              bgColor = 'rgba(37, 99, 235, 0.08)';
              textColor = 'var(--primary)';
            }
            
            if (isAnswered) {
              if (idx === question.correctAnswer) {
                borderColor = 'var(--success)';
                bgColor = 'rgba(16, 185, 129, 0.12)';
                textColor = 'var(--success)';
              } else if (selectedIdx === idx) {
                borderColor = 'var(--error)';
                bgColor = 'rgba(239, 68, 68, 0.12)';
                textColor = 'var(--error)';
              }
            }

            return (
              <button
                key={idx}
                className="btn glass-card"
                onClick={() => handleAnswerSelect(idx)}
                style={{
                  textAlign: 'left',
                  display: 'flex',
                  justifyContent: 'space-between',
                  background: bgColor,
                  border: `2px solid ${borderColor}`,
                  padding: '1.5rem',
                  width: '100%',
                  color: textColor,
                  opacity: isAnswered && idx !== selectedIdx && idx !== question.correctAnswer ? 0.4 : 1,
                  borderRadius: 'var(--radius-md)',
                  boxShadow: selectedIdx === idx ? '0 8px 24px rgba(37, 99, 235, 0.2)' : 'none',
                  fontSize: '1.15rem',
                  fontWeight: 500
                }}
              >
                <span style={{ flex: 1 }}>{option}</span>
                {isAnswered && idx === question.correctAnswer && <Check size={24} color="var(--success)" strokeWidth={3} />}
                {isAnswered && idx === selectedIdx && idx !== question.correctAnswer && <X size={24} color="var(--error)" strokeWidth={3} />}
              </button>
            );
          })}
        </div>

        {isAnswered && (
          <div style={{ 
            marginTop: '3rem', 
            padding: '2rem', 
            background: 'rgba(0,0,0,0.03)', 
            borderRadius: 'var(--radius-md)', 
            borderLeft: '4px solid var(--primary)',
            animation: 'fadeIn 0.4s ease'
          }}>
            <p style={{ fontWeight: 800, color: 'var(--deep-text)', marginBottom: '0.8rem', textTransform: 'uppercase', fontSize: '0.85rem', letterSpacing: '0.05em' }}>Explicación:</p>
            <p style={{ color: 'var(--text-low)', fontSize: '1.05rem', lineHeight: '1.5' }}>{question.explanation}</p>
          </div>
        )}

        <div style={{ marginTop: '3.5rem', display: 'flex', justifyContent: 'flex-end', height: '56px' }}>
          {isAnswered && (
            <button className="btn btn-primary animate-fade" onClick={handleNext}>
              {currentIdx < quiz.questions.length - 1 ? 'Siguiente Pregunta' : 'Finalizar Evaluación'} <ArrowRight size={22} />
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
