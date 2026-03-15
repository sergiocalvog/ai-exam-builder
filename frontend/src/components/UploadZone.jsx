import { useState, useRef } from 'react';
import { Upload, FileText, X, CheckCircle } from 'lucide-react';

export default function UploadZone({ onUpload }) {
  const [file, setFile] = useState(null);
  const [error, setError] = useState('');
  const [isDragging, setIsDragging] = useState(false);
  const [numQuestions, setNumQuestions] = useState(10);
  const fileInputRef = useRef(null);

  const handleFile = (selectedFile) => {
    if (selectedFile && selectedFile.type === 'application/pdf') {
      setFile(selectedFile);
      setError('');
    } else {
      setError('Por favor, selecciona un archivo PDF válido.');
      setFile(null);
    }
  };

  const onDrop = (e) => {
    e.preventDefault();
    setIsDragging(false);
    handleFile(e.dataTransfer.files[0]);
  };

  const onFileSelect = (e) => {
    handleFile(e.target.files[0]);
  };

  const handleGenerate = () => {
    if (file) onUpload(file, numQuestions);
  };

  return (
    <div className="animate-fade" style={{ maxWidth: '600px', margin: '0 auto' }}>
      <div 
        className={`glass-card ${isDragging ? 'dragging' : ''}`}
        style={{ 
          padding: '4rem 3rem', 
          textAlign: 'center',
          transition: 'all 0.3s ease',
          margin: '0 auto'
        }}
        onDragOver={(e) => { e.preventDefault(); setIsDragging(true); }}
        onDragLeave={() => setIsDragging(false)}
        onDrop={onDrop}
      >
        <div style={{ marginBottom: '2rem' }}>
          {file ? (
            <div style={{ position: 'relative', display: 'inline-block' }}>
              <FileText size={80} color="var(--primary)" />
              <button 
                onClick={() => setFile(null)}
                style={{ 
                  position: 'absolute', top: -10, right: -10, 
                  background: 'var(--error)', border: 'none', borderRadius: '50%',
                  color: 'white', cursor: 'pointer', padding: '6px',
                  boxShadow: '0 5px 10px rgba(239, 68, 68, 0.3)'
                }}
              >
                <X size={18} />
              </button>
            </div>
          ) : (
            <div style={{ 
              width: '100px', height: '100px', borderRadius: '50%', 
              background: 'rgba(37, 99, 235, 0.1)', display: 'flex', 
              alignItems: 'center', justifyContent: 'center', margin: '0 auto',
              border: '1px solid rgba(37, 99, 235, 0.2)'
            }}>
              <Upload size={48} color="var(--primary)" />
            </div>
          )}
        </div>

        <h2 style={{ marginBottom: '1rem', fontSize: '2rem' }}>
          {file ? 'Documento Cargado' : 'Sube tu Material'}
        </h2>
        <p style={{ color: 'var(--text-low)', marginBottom: '2.5rem', fontSize: '1.1rem' }}>
          {file ? 'Listo para generar tu evaluación inteligente.' : 'Arrastra tu archivo PDF aquí o haz clic para buscar.'}
        </p>

        {error && <p style={{ color: 'var(--error)', marginBottom: '1.5rem', fontWeight: 600 }}>{error}</p>}

        <div style={{ marginBottom: '2.5rem' }}>
          <label style={{ 
            display: 'block', 
            marginBottom: '0.75rem', 
            fontWeight: 700, 
            color: 'var(--deep-text)',
            fontSize: '0.9rem',
            textTransform: 'uppercase',
            letterSpacing: '0.05em'
          }}>
            ¿Cuántas preguntas quieres?
          </label>
          <select 
            value={numQuestions}
            onChange={(e) => setNumQuestions(Number(e.target.value))}
            className="glass-card"
            style={{ 
              padding: '0.75rem 1.5rem', 
              borderRadius: 'var(--radius-md)', 
              background: 'var(--glass-bg)',
              cursor: 'pointer',
              fontWeight: 700,
              color: 'var(--primary)',
              border: '2px solid var(--primary)',
              fontSize: '1rem',
              outline: 'none',
              boxShadow: '0 4px 12px rgba(37, 99, 235, 0.1)'
            }}
          >
            {[10, 20, 30, 40, 50].map(n => (
              <option key={n} value={n} style={{ background: 'var(--surface)', color: 'var(--deep-text)' }}>
                {n} preguntas
              </option>
            ))}
          </select>
        </div>

        {file ? (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1.2rem', alignItems: 'center' }}>
            <span style={{ fontWeight: 700, color: 'var(--deep-text)', fontSize: '1.1rem' }}>{file.name}</span>
            <button className="btn btn-primary" onClick={handleGenerate} style={{ padding: '1rem 2.5rem', fontSize: '1.1rem' }}>
              Generar Examen con IA
            </button>
          </div>
        ) : (
          <button 
            className="btn" 
            style={{ 
              background: 'transparent', 
              color: 'var(--primary)', 
              border: '2px solid var(--primary)',
              padding: '0.8rem 2rem'
            }}
            onClick={() => fileInputRef.current.click()}
          >
            Seleccionar PDF
          </button>
        )}

        <input 
          type="file" 
          ref={fileInputRef} 
          style={{ display: 'none' }} 
          accept="application/pdf"
          onChange={onFileSelect}
        />
      </div>
    </div>
  );
}
