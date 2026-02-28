import streamlit as st

st.set_page_config(page_title="Maternal Guard", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background: #060810 !important;
    color: #e8eaf0 !important;
    font-family: 'DM Sans', sans-serif !important;
}

[data-testid="stSidebar"] {
    background: #0c0f1a !important;
    border-right: 1px solid rgba(255,255,255,0.06) !important;
}

[data-testid="stSidebar"] * { color: #a0a8c0 !important; }

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* ─── HERO ─── */
.hero-wrap {
    position: relative;
    min-height: 92vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 80px 40px 60px;
    overflow: hidden;
}

.hero-bg {
    position: absolute;
    inset: 0;
    background:
        radial-gradient(ellipse 70% 55% at 50% 0%, rgba(220,38,38,0.18) 0%, transparent 65%),
        radial-gradient(ellipse 50% 40% at 80% 80%, rgba(99,102,241,0.14) 0%, transparent 60%),
        radial-gradient(ellipse 40% 35% at 10% 70%, rgba(236,72,153,0.10) 0%, transparent 60%);
    z-index: 0;
}

.hero-grid {
    position: absolute;
    inset: 0;
    background-image:
        linear-gradient(rgba(255,255,255,0.025) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.025) 1px, transparent 1px);
    background-size: 60px 60px;
    z-index: 0;
    mask-image: radial-gradient(ellipse 80% 80% at 50% 50%, black 30%, transparent 80%);
}

.hero-content { position: relative; z-index: 1; max-width: 900px; }

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(220,38,38,0.12);
    border: 1px solid rgba(220,38,38,0.3);
    color: #fca5a5;
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 7px 18px;
    border-radius: 100px;
    margin-bottom: 36px;
    animation: fadeSlideDown 0.6s ease both;
}

.hero-badge::before {
    content: '';
    width: 7px; height: 7px;
    border-radius: 50%;
    background: #ef4444;
    box-shadow: 0 0 8px #ef4444;
    animation: pulse 1.5s ease infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(1.3); }
}

.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(48px, 7vw, 88px);
    font-weight: 800;
    line-height: 1.0;
    letter-spacing: -0.03em;
    color: #f1f3f9;
    animation: fadeSlideDown 0.7s ease 0.1s both;
}

.hero-title .accent {
    background: linear-gradient(135deg, #f87171 0%, #fb923c 40%, #f43f5e 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-sub {
    margin-top: 24px;
    font-size: 18px;
    font-weight: 300;
    color: #7b84a0;
    line-height: 1.7;
    max-width: 620px;
    margin-left: auto;
    margin-right: auto;
    animation: fadeSlideDown 0.7s ease 0.2s both;
}

.hero-ctas {
    margin-top: 44px;
    display: flex;
    gap: 16px;
    justify-content: center;
    flex-wrap: wrap;
    animation: fadeSlideDown 0.7s ease 0.3s both;
}

.btn-primary {
    display: inline-flex; align-items: center; gap: 10px;
    background: linear-gradient(135deg, #dc2626, #f43f5e);
    color: white;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    font-size: 15px;
    padding: 14px 32px;
    border-radius: 12px;
    text-decoration: none;
    border: none;
    box-shadow: 0 8px 30px rgba(220,38,38,0.35), 0 0 0 1px rgba(255,255,255,0.05);
    transition: all 0.2s;
    cursor: pointer;
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 14px 40px rgba(220,38,38,0.45);
}

.btn-secondary {
    display: inline-flex; align-items: center; gap: 10px;
    background: rgba(255,255,255,0.05);
    color: #c8cde0;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    font-size: 15px;
    padding: 14px 32px;
    border-radius: 12px;
    text-decoration: none;
    border: 1px solid rgba(255,255,255,0.1);
    transition: all 0.2s;
    cursor: pointer;
}

.btn-secondary:hover {
    background: rgba(255,255,255,0.09);
    transform: translateY(-2px);
}

/* ─── STATS BAR ─── */
.stats-bar {
    display: flex;
    justify-content: center;
    gap: 0;
    flex-wrap: wrap;
    border-top: 1px solid rgba(255,255,255,0.06);
    border-bottom: 1px solid rgba(255,255,255,0.06);
    background: rgba(255,255,255,0.02);
    animation: fadeSlideDown 0.7s ease 0.4s both;
}

.stat-item {
    flex: 1;
    min-width: 180px;
    padding: 36px 24px;
    text-align: center;
    border-right: 1px solid rgba(255,255,255,0.06);
}
.stat-item:last-child { border-right: none; }

.stat-num {
    font-family: 'Syne', sans-serif;
    font-size: 40px;
    font-weight: 800;
    letter-spacing: -0.02em;
    background: linear-gradient(135deg, #f87171, #fb923c);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.stat-label {
    margin-top: 6px;
    font-size: 13px;
    color: #5a6278;
    font-weight: 400;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

/* ─── SECTION ─── */
.section {
    padding: 100px 60px;
    max-width: 1300px;
    margin: 0 auto;
}

.section-tag {
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #f87171;
    margin-bottom: 16px;
}

.section-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(32px, 4vw, 52px);
    font-weight: 800;
    color: #f1f3f9;
    letter-spacing: -0.03em;
    line-height: 1.1;
    margin-bottom: 20px;
}

.section-desc {
    font-size: 17px;
    color: #5a6278;
    line-height: 1.75;
    max-width: 560px;
}

/* ─── FEATURE CARDS ─── */
.features-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    margin-top: 60px;
}

.feat-card {
    position: relative;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 24px;
    padding: 40px 36px;
    overflow: hidden;
    transition: all 0.3s cubic-bezier(0.16,1,0.3,1);
}

.feat-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(248,113,113,0.5), transparent);
    opacity: 0;
    transition: opacity 0.3s;
}

.feat-card:hover {
    transform: translateY(-6px);
    background: rgba(255,255,255,0.055);
    border-color: rgba(248,113,113,0.2);
    box-shadow: 0 30px 60px rgba(0,0,0,0.4), 0 0 0 1px rgba(248,113,113,0.1);
}

.feat-card:hover::before { opacity: 1; }

.feat-icon-wrap {
    width: 52px; height: 52px;
    border-radius: 14px;
    display: flex; align-items: center; justify-content: center;
    font-size: 24px;
    margin-bottom: 28px;
}

.icon-red    { background: rgba(220,38,38,0.15);   border: 1px solid rgba(220,38,38,0.25); }
.icon-orange { background: rgba(234,88,12,0.15);   border: 1px solid rgba(234,88,12,0.25); }
.icon-pink   { background: rgba(236,72,153,0.15);  border: 1px solid rgba(236,72,153,0.25); }

.feat-title {
    font-family: 'Syne', sans-serif;
    font-size: 20px;
    font-weight: 700;
    color: #e8eaf0;
    margin-bottom: 14px;
    letter-spacing: -0.01em;
}

.feat-desc {
    font-size: 15px;
    color: #5a6278;
    line-height: 1.7;
}

.feat-tag {
    display: inline-block;
    margin-top: 24px;
    font-size: 12px;
    font-weight: 500;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    padding: 5px 12px;
    border-radius: 100px;
    background: rgba(248,113,113,0.08);
    color: #f87171;
    border: 1px solid rgba(248,113,113,0.2);
}

/* ─── HOW IT WORKS ─── */
.how-section {
    background: rgba(255,255,255,0.015);
    border-top: 1px solid rgba(255,255,255,0.05);
    border-bottom: 1px solid rgba(255,255,255,0.05);
    padding: 100px 60px;
}

.how-inner {
    max-width: 1300px;
    margin: 0 auto;
}

.steps-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 2px;
    margin-top: 60px;
    background: rgba(255,255,255,0.05);
    border-radius: 20px;
    overflow: hidden;
}

.step-item {
    background: #060810;
    padding: 44px 32px;
    position: relative;
}

.step-num {
    font-family: 'Syne', sans-serif;
    font-size: 64px;
    font-weight: 800;
    color: rgba(248,113,113,0.12);
    line-height: 1;
    margin-bottom: 16px;
    letter-spacing: -0.04em;
}

.step-title {
    font-family: 'Syne', sans-serif;
    font-size: 17px;
    font-weight: 700;
    color: #c8cde0;
    margin-bottom: 12px;
}

.step-desc {
    font-size: 14px;
    color: #4a5168;
    line-height: 1.65;
}

/* ─── ALERT BANNER ─── */
.alert-banner {
    margin: 0 60px;
    background: linear-gradient(135deg, rgba(220,38,38,0.12), rgba(244,63,94,0.08));
    border: 1px solid rgba(220,38,38,0.25);
    border-radius: 20px;
    padding: 36px 48px;
    display: flex;
    align-items: center;
    gap: 28px;
}

.alert-icon {
    font-size: 40px;
    flex-shrink: 0;
}

.alert-text h3 {
    font-family: 'Syne', sans-serif;
    font-size: 20px;
    font-weight: 700;
    color: #fca5a5;
    margin-bottom: 8px;
}

.alert-text p {
    font-size: 15px;
    color: #7b84a0;
    line-height: 1.6;
}

/* ─── FOOTER ─── */
.footer {
    padding: 60px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-top: 1px solid rgba(255,255,255,0.05);
    max-width: 100%;
}

.footer-brand {
    font-family: 'Syne', sans-serif;
    font-size: 18px;
    font-weight: 800;
    color: #e8eaf0;
}

.footer-brand span {
    background: linear-gradient(135deg, #f87171, #fb923c);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.footer-note {
    font-size: 13px;
    color: #3a4058;
}

/* ─── SIDEBAR NAV ─── */
.nav-item {
    display: block;
    padding: 12px 20px;
    border-radius: 10px;
    font-size: 14px;
    font-weight: 500;
    color: #6b7290 !important;
    text-decoration: none;
    transition: all 0.2s;
    margin: 3px 0;
}

/* ─── ANIMATIONS ─── */
@keyframes fadeSlideDown {
    from { opacity: 0; transform: translateY(-20px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* hide streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stDecoration"] { display: none; }
</style>
""", unsafe_allow_html=True)

# ─── SIDEBAR ──────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding: 20px 0 30px;">
        <div style="font-family:'Syne',sans-serif; font-size:20px; font-weight:800; color:#f1f3f9;">
            Maternal<span style="background:linear-gradient(135deg,#f87171,#fb923c);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;"> Guard</span>
        </div>
        <div style="font-size:12px; color:#3a4058; margin-top:4px; letter-spacing:0.06em; text-transform:uppercase;">AI Maternal Safety Platform</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="font-size:11px; font-weight:600; letter-spacing:0.12em; text-transform:uppercase; color:#2e3448; padding: 0 4px; margin-bottom:10px;">Navigation</div>
    """, unsafe_allow_html=True)

    pages = [
        ("🏠", "Home", True),
        ("🧠", "AI Risk Detection", False),
        ("🚨", "Emergency SOS", False),
        ("🩸", "Donor Network", False),
        ("📊", "Dashboard", False),
        ("⚙️", "Settings", False),
    ]
    for icon, label, active in pages:
        bg = "rgba(248,113,113,0.1); color:#f87171 !important; border:1px solid rgba(248,113,113,0.2)" if active else "transparent; border:1px solid transparent"
        st.markdown(f"""
        <div style="display:flex; align-items:center; gap:12px; padding:12px 16px; border-radius:12px; margin:3px 0;
             background:{bg}; cursor:pointer; font-size:14px; font-weight:500; color:{'#f87171' if active else '#4a5168'};">
            <span>{icon}</span><span>{label}</span>
        </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div style="position:absolute; bottom:30px; left:24px; right:24px;">
        <div style="background:rgba(220,38,38,0.1); border:1px solid rgba(220,38,38,0.2); border-radius:14px; padding:18px;">
            <div style="font-size:12px; font-weight:700; color:#fca5a5; margin-bottom:6px;">🔴 Emergency Mode</div>
            <div style="font-size:12px; color:#4a5168; line-height:1.5;">Activate to alert nearby donors instantly</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ─── HERO ─────────────────────────────────────────────────
st.markdown("""
<div class="hero-wrap">
  <div class="hero-bg"></div>
  <div class="hero-grid"></div>
  <div class="hero-content">
    <div class="hero-badge">🔴 Live Platform &nbsp;·&nbsp; AI-Powered Maternal Safety</div>
    <h1 class="hero-title">
      Saving Mothers.<br>
      <span class="accent">One Signal at a Time.</span>
    </h1>
    <p class="hero-sub">
      Maternal Guard combines real-time AI risk detection with an emergency blood donor network —
      built to prevent the preventable, and protect every pregnancy.
    </p>
    <div class="hero-ctas">
      <button class="btn-primary">⚡ Activate Emergency SOS</button>
      <button class="btn-secondary">🧠 View AI Dashboard →</button>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── STATS ────────────────────────────────────────────────
st.markdown("""
<div class="stats-bar">
  <div class="stat-item">
    <div class="stat-num">94.7%</div>
    <div class="stat-label">Risk Detection Accuracy</div>
  </div>
  <div class="stat-item">
    <div class="stat-num">&lt; 90s</div>
    <div class="stat-label">Avg. Donor Match Time</div>
  </div>
  <div class="stat-item">
    <div class="stat-num">12K+</div>
    <div class="stat-label">Registered Donors</div>
  </div>
  <div class="stat-item">
    <div class="stat-num">340+</div>
    <div class="stat-label">Lives Protected</div>
  </div>
  <div class="stat-item">
    <div class="stat-num">24/7</div>
    <div class="stat-label">Always-On Monitoring</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── CORE FEATURES ────────────────────────────────────────
st.markdown("""
<div class="section">
  <div class="section-tag">Core Features</div>
  <h2 class="section-title">Everything you need.<br>Nothing you don't.</h2>
  <p class="section-desc">Three tightly integrated systems, built to work together under pressure — when every second counts.</p>

  <div class="features-grid">

    <div class="feat-card">
      <div class="feat-icon-wrap icon-red">🧠</div>
      <div class="feat-title">AI Risk Detection</div>
      <div class="feat-desc">Our model processes vitals, history, and lab data in real time — flagging high-risk pregnancies hours before a crisis develops. Trained on 2M+ maternal health records.</div>
      <div class="feat-tag">Machine Learning · NLP</div>
    </div>

    <div class="feat-card">
      <div class="feat-icon-wrap icon-orange">🚨</div>
      <div class="feat-title">Emergency SOS</div>
      <div class="feat-desc">One tap sends a geolocated alert to nearby verified donors. A severity-ranked queue is built instantly using blood type, proximity, and availability data.</div>
      <div class="feat-tag">Real-Time · Geofencing</div>
    </div>

    <div class="feat-card">
      <div class="feat-icon-wrap icon-pink">🩸</div>
      <div class="feat-title">Smart Donor Network</div>
      <div class="feat-desc">Live donor registration with health verification, availability scheduling, and intelligent filtering. Donors receive push alerts and routing instructions within seconds.</div>
      <div class="feat-tag">Community · Data Pipeline</div>
    </div>

  </div>
</div>
""", unsafe_allow_html=True)

# ─── ALERT BANNER ─────────────────────────────────────────
st.markdown("""
<div class="alert-banner">
  <div class="alert-icon">🩺</div>
  <div class="alert-text">
    <h3>Why it matters: Postpartum hemorrhage kills a mother every 3 minutes globally.</h3>
    <p>Most of these deaths are preventable with early detection and rapid blood access. Maternal Guard exists to close that gap — combining AI prediction with community-powered emergency response.</p>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── HOW IT WORKS ─────────────────────────────────────────
st.markdown("""
<div class="how-section">
  <div class="how-inner">
    <div class="section-tag">Protocol</div>
    <h2 class="section-title">How it works</h2>
    <p class="section-desc">From passive monitoring to life-saving response — a seamless four-step protocol.</p>

    <div class="steps-grid">
      <div class="step-item">
        <div class="step-num">01</div>
        <div class="step-title">Continuous Monitoring</div>
        <div class="step-desc">Patient vitals and health data are streamed in real time to the AI engine for continuous risk assessment throughout pregnancy.</div>
      </div>
      <div class="step-item">
        <div class="step-num">02</div>
        <div class="step-title">Risk Score Generated</div>
        <div class="step-desc">The AI assigns a dynamic risk score, notifying healthcare providers of elevated danger — before symptoms become critical.</div>
      </div>
      <div class="step-item">
        <div class="step-num">03</div>
        <div class="step-title">SOS Triggered</div>
        <div class="step-desc">If hemorrhage risk spikes or an emergency is manually reported, the SOS system immediately activates and begins donor matching.</div>
      </div>
      <div class="step-item">
        <div class="step-num">04</div>
        <div class="step-title">Donor Dispatched</div>
        <div class="step-desc">The top-matched donor receives a real-time alert with navigation to the facility. ETA and status are tracked live by medical staff.</div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── FOOTER ───────────────────────────────────────────────
st.markdown("""
<div class="footer">
  <div>
    <div class="footer-brand">Maternal<span> Guard</span></div>
    <div style="font-size:13px; color:#2e3448; margin-top:4px;">AI + Emergency Blood Network for Safer Pregnancies</div>
  </div>
  <div class="footer-note">Built for impact. Designed to save lives.</div>
</div>
""", unsafe_allow_html=True)
