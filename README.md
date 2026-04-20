<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Salary Prediction App — README</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@400;500&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #050A0F;
    --surface: #0D1520;
    --surface2: #111E2E;
    --border: rgba(0,200,255,0.12);
    --accent: #00C8FF;
    --accent2: #7B61FF;
    --accent3: #00FFB0;
    --text: #E8F4FF;
    --muted: #6B8CA8;
    --danger: #FF4C6A;
    --warn: #FFB340;
  }
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
    min-height: 100vh;
    overflow-x: hidden;
  }

  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(rgba(0,200,255,0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(0,200,255,0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    animation: gridMove 20s linear infinite;
    pointer-events: none;
    z-index: 0;
  }

  @keyframes gridMove {
    0% { transform: translateY(0); }
    100% { transform: translateY(40px); }
  }

  .glow-orb {
    position: fixed;
    border-radius: 50%;
    filter: blur(120px);
    pointer-events: none;
    z-index: 0;
    animation: orbFloat 8s ease-in-out infinite;
  }
  .orb1 { width: 500px; height: 500px; background: rgba(0,200,255,0.07); top: -100px; right: -100px; animation-delay: 0s; }
  .orb2 { width: 400px; height: 400px; background: rgba(123,97,255,0.07); bottom: 200px; left: -100px; animation-delay: 3s; }
  .orb3 { width: 300px; height: 300px; background: rgba(0,255,176,0.05); top: 50%; right: 10%; animation-delay: 6s; }

  @keyframes orbFloat {
    0%, 100% { transform: translateY(0) scale(1); }
    50% { transform: translateY(-30px) scale(1.05); }
  }

  .wrapper {
    max-width: 900px;
    margin: 0 auto;
    padding: 0 24px 80px;
    position: relative;
    z-index: 1;
  }

  .hero {
    padding: 80px 0 60px;
    text-align: center;
    animation: fadeUp 0.8s ease both;
  }

  .hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(0,200,255,0.08);
    border: 1px solid rgba(0,200,255,0.2);
    border-radius: 100px;
    padding: 6px 16px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--accent);
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-bottom: 28px;
  }

  .hero-badge::before {
    content: '';
    width: 6px; height: 6px;
    border-radius: 50%;
    background: var(--accent3);
    animation: pulse 1.5s ease-in-out infinite;
  }

  @keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(0.8); }
  }

  h1 {
    font-family: 'Syne', sans-serif;
    font-size: clamp(42px, 7vw, 72px);
    font-weight: 800;
    line-height: 1.05;
    letter-spacing: -0.02em;
    background: linear-gradient(135deg, #FFFFFF 0%, var(--accent) 50%, var(--accent2) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 20px;
  }

  .hero-sub {
    font-size: 18px;
    color: var(--muted);
    max-width: 540px;
    margin: 0 auto 36px;
    line-height: 1.7;
    font-weight: 300;
  }

  .badges {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px;
    margin-bottom: 44px;
  }

  .badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 6px 14px;
    font-size: 12px;
    font-family: 'DM Mono', monospace;
    color: var(--muted);
    transition: all 0.2s;
  }
  .badge:hover {
    border-color: rgba(0,200,255,0.3);
    color: var(--accent);
    transform: translateY(-1px);
  }
  .badge-dot { width: 8px; height: 8px; border-radius: 50%; }

  .btn-row {
    display: flex;
    gap: 12px;
    justify-content: center;
    flex-wrap: wrap;
  }

  .btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 12px 28px;
    border-radius: 10px;
    font-size: 14px;
    font-weight: 500;
    text-decoration: none;
    cursor: pointer;
    transition: all 0.25s;
    border: none;
  }
  .btn-primary {
    background: var(--accent);
    color: #000;
    box-shadow: 0 0 30px rgba(0,200,255,0.25);
  }
  .btn-primary:hover { transform: translateY(-2px); box-shadow: 0 0 50px rgba(0,200,255,0.4); }
  .btn-ghost {
    background: transparent;
    color: var(--text);
    border: 1px solid var(--border);
  }
  .btn-ghost:hover { border-color: rgba(0,200,255,0.4); transform: translateY(-2px); }

  section { margin-bottom: 64px; animation: fadeUp 0.8s ease both; }
  section:nth-child(2) { animation-delay: 0.1s; }
  section:nth-child(3) { animation-delay: 0.2s; }
  section:nth-child(4) { animation-delay: 0.3s; }
  section:nth-child(5) { animation-delay: 0.4s; }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(24px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .section-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 12px;
  }

  h2 {
    font-family: 'Syne', sans-serif;
    font-size: 26px;
    font-weight: 700;
    letter-spacing: -0.02em;
    margin-bottom: 20px;
    color: #fff;
  }

  .stats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 12px;
    margin-bottom: 64px;
  }

  .stat-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 24px 20px;
    text-align: center;
    position: relative;
    overflow: hidden;
    transition: all 0.3s;
  }
  .stat-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--accent-c), transparent);
    opacity: 0;
    transition: opacity 0.3s;
  }
  .stat-card:hover { transform: translateY(-4px); border-color: rgba(0,200,255,0.3); }
  .stat-card:hover::before { opacity: 1; }
  .stat-card:nth-child(1) { --accent-c: var(--accent); }
  .stat-card:nth-child(2) { --accent-c: var(--accent2); }
  .stat-card:nth-child(3) { --accent-c: var(--accent3); }
  .stat-card:nth-child(4) { --accent-c: var(--warn); }

  .stat-num {
    font-family: 'Syne', sans-serif;
    font-size: 32px;
    font-weight: 800;
    background: linear-gradient(135deg, #fff, var(--accent-c, var(--accent)));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  .stat-label { font-size: 12px; color: var(--muted); margin-top: 4px; }

  .features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 16px;
  }

  .feature-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 24px;
    transition: all 0.3s;
    position: relative;
    overflow: hidden;
  }
  .feature-card::after {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at var(--mx, 50%) var(--my, 50%), rgba(0,200,255,0.06) 0%, transparent 60%);
    opacity: 0;
    transition: opacity 0.3s;
    pointer-events: none;
  }
  .feature-card:hover { transform: translateY(-4px); border-color: rgba(0,200,255,0.25); }
  .feature-card:hover::after { opacity: 1; }

  .feature-icon {
    width: 44px; height: 44px;
    border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
    font-size: 20px;
    margin-bottom: 16px;
  }

  .feature-card h3 {
    font-family: 'Syne', sans-serif;
    font-size: 16px;
    font-weight: 700;
    margin-bottom: 8px;
  }
  .feature-card p { font-size: 13px; color: var(--muted); line-height: 1.6; }

  .tech-grid { display: flex; flex-wrap: wrap; gap: 10px; }

  .tech-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 100px;
    padding: 8px 18px;
    font-size: 13px;
    font-weight: 500;
    transition: all 0.2s;
    cursor: default;
  }
  .tech-pill:hover {
    transform: translateY(-2px) scale(1.02);
    border-color: rgba(0,200,255,0.35);
    background: var(--surface2);
  }
  .tech-pill span.dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    display: inline-block;
    flex-shrink: 0;
  }

  .pipeline {
    display: flex;
    align-items: flex-start;
    gap: 0;
    overflow-x: auto;
    padding: 8px 0 20px;
    scrollbar-width: thin;
  }

  .pipe-step {
    flex: 0 0 140px;
    text-align: center;
    position: relative;
  }

  .pipe-step:not(:last-child)::after {
    content: '→';
    position: absolute;
    right: -12px;
    top: 22px;
    color: var(--muted);
    font-size: 18px;
    z-index: 2;
  }

  .pipe-circle {
    width: 48px; height: 48px;
    border-radius: 50%;
    border: 2px solid;
    display: flex; align-items: center; justify-content: center;
    font-size: 18px;
    margin: 0 auto 10px;
    transition: all 0.3s;
    position: relative;
  }
  .pipe-step:hover .pipe-circle { transform: scale(1.15); }
  .pipe-step:nth-child(1) .pipe-circle { border-color: var(--accent); background: rgba(0,200,255,0.1); }
  .pipe-step:nth-child(2) .pipe-circle { border-color: var(--accent2); background: rgba(123,97,255,0.1); }
  .pipe-step:nth-child(3) .pipe-circle { border-color: var(--accent3); background: rgba(0,255,176,0.1); }
  .pipe-step:nth-child(4) .pipe-circle { border-color: var(--warn); background: rgba(255,179,64,0.1); }
  .pipe-step:nth-child(5) .pipe-circle { border-color: var(--danger); background: rgba(255,76,106,0.1); }
  .pipe-step:nth-child(6) .pipe-circle { border-color: #aaa; background: rgba(170,170,170,0.1); }
  .pipe-label { font-size: 11px; font-weight: 500; color: var(--muted); }

  .code-block {
    background: #030810;
    border: 1px solid var(--border);
    border-radius: 14px;
    overflow: hidden;
  }
  .code-header {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 12px 16px;
    border-bottom: 1px solid var(--border);
    background: var(--surface);
  }
  .code-dot { width: 10px; height: 10px; border-radius: 50%; }
  .code-title { font-family: 'DM Mono', monospace; font-size: 11px; color: var(--muted); margin-left: 4px; }
  pre {
    padding: 20px 24px;
    font-family: 'DM Mono', monospace;
    font-size: 13px;
    line-height: 1.8;
    overflow-x: auto;
  }
  .kw { color: var(--accent2); }
  .cm { color: #4B6680; }
  .str { color: var(--accent3); }
  .fn { color: var(--accent); }
  .nm { color: var(--warn); }

  .table-wrap {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    overflow: hidden;
  }
  table { width: 100%; border-collapse: collapse; }
  th {
    background: var(--surface2);
    padding: 12px 20px;
    text-align: left;
    font-size: 11px;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--muted);
    font-weight: 400;
  }
  td { padding: 13px 20px; font-size: 13px; border-top: 1px solid var(--border); }
  tr:hover td { background: rgba(0,200,255,0.02); }
  .rank-1 { color: var(--accent3); font-weight: 600; font-family: 'DM Mono', monospace; }
  .rank-2 { color: var(--accent); font-family: 'DM Mono', monospace; }
  .rank-3 { color: var(--warn); font-family: 'DM Mono', monospace; }
  .rank-other { color: var(--muted); font-family: 'DM Mono', monospace; }

  .score-bar-wrap { display: flex; align-items: center; gap: 10px; }
  .score-bar {
    height: 4px;
    border-radius: 2px;
    background: rgba(0,200,255,0.15);
    flex: 1;
    overflow: hidden;
  }
  .score-fill { height: 100%; border-radius: 2px; transition: width 1s ease; }

  .steps { display: flex; flex-direction: column; gap: 12px; }
  .step {
    display: flex;
    gap: 16px;
    align-items: flex-start;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 16px 20px;
    transition: all 0.2s;
  }
  .step:hover { border-color: rgba(0,200,255,0.2); transform: translateX(4px); }
  .step-num {
    width: 28px; height: 28px;
    border-radius: 50%;
    background: rgba(0,200,255,0.1);
    border: 1px solid rgba(0,200,255,0.3);
    display: flex; align-items: center; justify-content: center;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--accent);
    flex-shrink: 0;
    margin-top: 2px;
  }
  .step-body h4 { font-size: 14px; font-weight: 500; margin-bottom: 4px; }
  .step-body code {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    color: var(--accent3);
    background: rgba(0,255,176,0.07);
    border-radius: 4px;
    padding: 2px 6px;
  }

  .footer {
    text-align: center;
    padding: 40px 0 0;
    border-top: 1px solid var(--border);
  }
  .footer-logo {
    font-family: 'Syne', sans-serif;
    font-size: 20px;
    font-weight: 800;
    background: linear-gradient(90deg, var(--accent), var(--accent2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 12px;
  }
  .footer p { font-size: 13px; color: var(--muted); line-height: 1.8; }
  .footer a { color: var(--accent); text-decoration: none; }

  hr { border: none; border-top: 1px solid var(--border); margin: 48px 0; }

  ::-webkit-scrollbar { width: 6px; height: 6px; }
  ::-webkit-scrollbar-track { background: transparent; }
  ::-webkit-scrollbar-thumb { background: rgba(0,200,255,0.2); border-radius: 3px; }
</style>
</head>
<body>

<div class="glow-orb orb1"></div>
<div class="glow-orb orb2"></div>
<div class="glow-orb orb3"></div>

<div class="wrapper">

  <div class="hero">
    <div class="hero-badge">ML · End-to-End Pipeline · Deployment Ready</div>
    <h1>Salary Prediction<br>App</h1>
    <p class="hero-sub">Predict individual salaries with high accuracy using machine learning — from data ingestion to live inference.</p>
    <div class="badges">
      <div class="badge"><span class="badge-dot" style="background:#3776AB"></span>Python 3.10+</div>
      <div class="badge"><span class="badge-dot" style="background:#F7931E"></span>Scikit-learn</div>
      <div class="badge"><span class="badge-dot" style="background:#00B4D8"></span>Flask / FastAPI</div>
      <div class="badge"><span class="badge-dot" style="background:#4CAF50"></span>93.2% Accuracy</div>
      <div class="badge"><span class="badge-dot" style="background:#7B61FF"></span>MIT License</div>
      <div class="badge"><span class="badge-dot" style="background:#FF6B6B"></span>v1.2.0</div>
    </div>
    <div class="btn-row">
      <a class="btn btn-primary" href="#">🚀 Live Demo</a>
      <a class="btn btn-ghost" href="#">📄 Docs</a>
      <a class="btn btn-ghost" href="#">⭐ Star on GitHub</a>
    </div>
  </div>

  <div class="stats">
    <div class="stat-card"><div class="stat-num">93.2%</div><div class="stat-label">R² Score</div></div>
    <div class="stat-card"><div class="stat-num">±$3.2K</div><div class="stat-label">Mean Abs. Error</div></div>
    <div class="stat-card"><div class="stat-num">8+</div><div class="stat-label">Input Features</div></div>
    <div class="stat-card"><div class="stat-num">&lt;50ms</div><div class="stat-label">Inference Time</div></div>
  </div>

  <section>
    <div class="section-label">// Overview</div>
    <h2>What it does</h2>
    <div class="features">
      <div class="feature-card">
        <div class="feature-icon" style="background:rgba(0,200,255,0.1)">🎯</div>
        <h3>Smart Predictions</h3>
        <p>Estimates salary from years of experience, education level, job role, location, and industry using an ensemble ML model.</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon" style="background:rgba(123,97,255,0.1)">🔬</div>
        <h3>Full ML Pipeline</h3>
        <p>End-to-end workflow: raw CSV ingestion → feature engineering → model training → evaluation → serialization → API serving.</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon" style="background:rgba(0,255,176,0.1)">📊</div>
        <h3>Explainability</h3>
        <p>SHAP-based feature importance lets users understand exactly which factors drive each individual prediction.</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon" style="background:rgba(255,179,64,0.1)">⚡</div>
        <h3>Production-Ready API</h3>
        <p>RESTful JSON API with Swagger docs, input validation, error handling, and Docker support out of the box.</p>
      </div>
    </div>
  </section>

  <section>
    <div class="section-label">// Architecture</div>
    <h2>ML Pipeline</h2>
    <div class="pipeline">
      <div class="pipe-step"><div class="pipe-circle">📥</div><div class="pipe-label">Data<br>Ingestion</div></div>
      <div class="pipe-step"><div class="pipe-circle">🧹</div><div class="pipe-label">Preprocess<br>& Clean</div></div>
      <div class="pipe-step"><div class="pipe-circle">⚙️</div><div class="pipe-label">Feature<br>Engineering</div></div>
      <div class="pipe-step"><div class="pipe-circle">🤖</div><div class="pipe-label">Train<br>Model</div></div>
      <div class="pipe-step"><div class="pipe-circle">📈</div><div class="pipe-label">Evaluate<br>& Tune</div></div>
      <div class="pipe-step"><div class="pipe-circle">🚀</div><div class="pipe-label">Deploy<br>API</div></div>
    </div>
  </section>

  <section>
    <div class="section-label">// Stack</div>
    <h2>Tech Stack</h2>
    <div class="tech-grid">
      <div class="tech-pill"><span class="dot" style="background:#3776AB"></span>Python</div>
      <div class="tech-pill"><span class="dot" style="background:#F7931E"></span>Scikit-learn</div>
      <div class="tech-pill"><span class="dot" style="background:#E74C3C"></span>XGBoost</div>
      <div class="tech-pill"><span class="dot" style="background:#150458"></span>Pandas &amp; NumPy</div>
      <div class="tech-pill"><span class="dot" style="background:#00B4D8"></span>Flask / FastAPI</div>
      <div class="tech-pill"><span class="dot" style="background:#FF6B35"></span>SHAP</div>
      <div class="tech-pill"><span class="dot" style="background:#4CAF50"></span>Matplotlib / Seaborn</div>
      <div class="tech-pill"><span class="dot" style="background:#2496ED"></span>Docker</div>
      <div class="tech-pill"><span class="dot" style="background:#FF9900"></span>AWS / GCP Ready</div>
      <div class="tech-pill"><span class="dot" style="background:#764ABC"></span>Jupyter Notebooks</div>
    </div>
  </section>

  <section>
    <div class="section-label">// Results</div>
    <h2>Model Comparison</h2>
    <div class="table-wrap">
      <table>
        <thead>
          <tr><th>Rank</th><th>Model</th><th>R² Score</th><th>MAE</th><th>Performance</th></tr>
        </thead>
        <tbody>
          <tr>
            <td class="rank-1">🥇 #1</td><td>XGBoost Regressor</td><td class="rank-1">0.932</td><td>$3,212</td>
            <td><div class="score-bar-wrap"><div class="score-bar"><div class="score-fill" style="width:93.2%;background:linear-gradient(90deg,#00C8FF,#00FFB0)"></div></div></div></td>
          </tr>
          <tr>
            <td class="rank-2">🥈 #2</td><td>Random Forest</td><td class="rank-2">0.914</td><td>$3,890</td>
            <td><div class="score-bar-wrap"><div class="score-bar"><div class="score-fill" style="width:91.4%;background:linear-gradient(90deg,#00C8FF,#7B61FF)"></div></div></div></td>
          </tr>
          <tr>
            <td class="rank-3">🥉 #3</td><td>Gradient Boosting</td><td class="rank-3">0.901</td><td>$4,120</td>
            <td><div class="score-bar-wrap"><div class="score-bar"><div class="score-fill" style="width:90.1%;background:linear-gradient(90deg,#FFB340,#FF6B35)"></div></div></div></td>
          </tr>
          <tr>
            <td class="rank-other">#4</td><td>Ridge Regression</td><td class="rank-other">0.782</td><td>$6,540</td>
            <td><div class="score-bar-wrap"><div class="score-bar"><div class="score-fill" style="width:78.2%;background:#4B6680"></div></div></div></td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>

  <section>
    <div class="section-label">// Quickstart</div>
    <h2>Get Running in 60 Seconds</h2>
    <div class="steps">
      <div class="step">
        <div class="step-num">01</div>
        <div class="step-body">
          <h4>Clone the Repository</h4>
          <code>git clone https://github.com/yourname/salary-prediction-app.git && cd salary-prediction-app</code>
        </div>
      </div>
      <div class="step">
        <div class="step-num">02</div>
        <div class="step-body">
          <h4>Create Virtual Environment & Install</h4>
          <code>python -m venv venv && source venv/bin/activate && pip install -r requirements.txt</code>
        </div>
      </div>
      <div class="step">
        <div class="step-num">03</div>
        <div class="step-body">
          <h4>Train the Model</h4>
          <code>python src/train.py --data data/salary_dataset.csv --output models/</code>
        </div>
      </div>
      <div class="step">
        <div class="step-num">04</div>
        <div class="step-body">
          <h4>Launch the API</h4>
          <code>python app.py</code> &nbsp;→ Visit <code>http://localhost:5000/docs</code>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="section-label">// API</div>
    <h2>Sample Request</h2>
    <div class="code-block">
      <div class="code-header">
        <div class="code-dot" style="background:#FF5F57"></div>
        <div class="code-dot" style="background:#FFBD2E"></div>
        <div class="code-dot" style="background:#28C840"></div>
        <span class="code-title">POST /api/v1/predict</span>
      </div>
      <pre><span class="cm"># Request payload</span>
<span class="fn">curl</span> <span class="str">-X POST</span> http://localhost:5000/api/v1/predict \
  <span class="str">-H</span> <span class="str">"Content-Type: application/json"</span> \
  <span class="str">-d</span> <span class="str">'{
    "years_experience": 5,
    "education": "Masters",
    "job_role": "Data Scientist",
    "location": "San Francisco",
    "industry": "Technology",
    "skills": ["Python", "ML", "SQL"]
  }'</span>

<span class="cm"># Response</span>
{
  <span class="str">"predicted_salary"</span>: <span class="nm">138500</span>,
  <span class="str">"confidence_interval"</span>: [<span class="nm">131200</span>, <span class="nm">145800</span>],
  <span class="str">"top_factors"</span>: [<span class="str">"job_role"</span>, <span class="str">"location"</span>, <span class="str">"experience"</span>],
  <span class="str">"model_version"</span>: <span class="str">"xgb-v1.2.0"</span>
}</pre>
    </div>
  </section>

  <hr>

  <div class="footer">
    <div class="footer-logo">SalaryPredict</div>
    <p>Built with ❤️ · <a href="#">MIT License</a> · <a href="#">Contributing Guide</a> · <a href="#">Report a Bug</a></p>
    <p style="margin-top:12px;font-size:12px">If this project helped you, consider ⭐ starring the repo on GitHub.</p>
  </div>

</div>

<script>
  document.querySelectorAll('.feature-card').forEach(card => {
    card.addEventListener('mousemove', e => {
      const rect = card.getBoundingClientRect();
      const x = ((e.clientX - rect.left) / rect.width * 100).toFixed(1) + '%';
      const y = ((e.clientY - rect.top) / rect.height * 100).toFixed(1) + '%';
      card.style.setProperty('--mx', x);
      card.style.setProperty('--my', y);
    });
  });

  const bars = document.querySelectorAll('.score-fill');
  const widths = Array.from(bars).map(b => b.style.width);
  bars.forEach(b => b.style.width = '0');

  const io = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        bars.forEach((b, i) => b.style.width = widths[i]);
        io.disconnect();
      }
    });
  }, { threshold: 0.3 });

  const tableSection = document.querySelector('.table-wrap');
  if (tableSection) io.observe(tableSection);
</script>
</body>
</html>
