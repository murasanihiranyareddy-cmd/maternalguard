import streamlit as st
import joblib
import numpy as np
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="AI Risk Detector – Maternal Guard", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');
*, *::before, *::after { box-sizing: border-box; }
html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background: #060810 !important; color: #e8eaf0 !important;
    font-family: 'DM Sans', sans-serif !important;
}
[data-testid="stSidebar"] { background: #0a0d18 !important; border-right: 1px solid rgba(255,255,255,0.06) !important; }
.block-container { padding: 40px 60px !important; max-width: 1100px !important; }

/* Page header */
.page-header { margin-bottom: 48px; }
.page-tag { font-size: 11px; font-weight: 600; letter-spacing: .16em; text-transform: uppercase; color: #f87171; margin-bottom: 12px; }
.page-title { font-family: 'Syne', sans-serif; font-size: 42px; font-weight: 800; color: #f1f3f9; letter-spacing: -.03em; line-height: 1.1; }
.page-desc { font-size: 16px; color: #4a5168; line-height: 1.7; margin-top: 12px; max-width: 580px; }

/* Form card */
.form-card {
    background: rgba(255,255,255,.03); border: 1px solid rgba(255,255,255,.07);
    border-radius: 24px; padding: 44px 48px; margin-bottom: 32px;
}
.form-section-title {
    font-family: 'Syne', sans-serif; font-size: 16px; font-weight: 700;
    color: #c8cde0; margin-bottom: 24px; padding-bottom: 14px;
    border-bottom: 1px solid rgba(255,255,255,.06);
}

/* Streamlit input overrides */
[data-testid="stNumberInput"] input, [data-testid="stTextInput"] input {
    background: rgba(255,255,255,.05) !important;
    border: 1px solid rgba(255,255,255,.1) !important;
    border-radius: 10px !important; color: #e8eaf0 !important;
}
[data-testid="stNumberInput"] input:focus, [data-testid="stTextInput"] input:focus {
    border-color: rgba(248,113,113,.5) !important;
    box-shadow: 0 0 0 3px rgba(248,113,113,.12) !important;
}
label { color: #7b84a0 !important; font-size: 13px !important; font-weight: 500 !important; }

/* Result cards */
.result-high {
    background: linear-gradient(135deg, rgba(220,38,38,.18), rgba(244,63,94,.1));
    border: 1px solid rgba(220,38,38,.4); border-radius: 20px; padding: 40px 44px;
    text-align: center; animation: popIn .4s cubic-bezier(.16,1,.3,1) both;
}
.result-mid {
    background: linear-gradient(135deg, rgba(234,88,12,.18), rgba(251,146,60,.1));
    border: 1px solid rgba(234,88,12,.4); border-radius: 20px; padding: 40px 44px;
    text-align: center; animation: popIn .4s cubic-bezier(.16,1,.3,1) both;
}
.result-low {
    background: linear-gradient(135deg, rgba(22,163,74,.18), rgba(34,197,94,.1));
    border: 1px solid rgba(22,163,74,.4); border-radius: 20px; padding: 40px 44px;
    text-align: center; animation: popIn .4s cubic-bezier(.16,1,.3,1) both;
}
.result-emoji { font-size: 56px; margin-bottom: 16px; }
.result-label { font-family: 'Syne', sans-serif; font-size: 32px; font-weight: 800; margin-bottom: 10px; }
.result-label-high { color: #fca5a5; }
.result-label-mid  { color: #fdba74; }
.result-label-low  { color: #86efac; }
.result-sub { font-size: 15px; color: #5a6278; line-height: 1.65; max-width: 500px; margin: 0 auto; }

/* Probability bars */
.prob-bars { margin-top: 32px; text-align: left; }
.prob-row { margin-bottom: 14px; }
.prob-label { font-size: 12px; font-weight: 600; letter-spacing: .06em; text-transform: uppercase; color: #5a6278; margin-bottom: 6px; display: flex; justify-content: space-between; }
.prob-track { background: rgba(255,255,255,.06); border-radius: 100px; height: 8px; overflow: hidden; }
.prob-fill-high { background: linear-gradient(90deg,#dc2626,#f43f5e); border-radius: 100px; height: 8px; transition: width .8s cubic-bezier(.16,1,.3,1); }
.prob-fill-mid  { background: linear-gradient(90deg,#ea580c,#fb923c); border-radius: 100px; height: 8px; transition: width .8s cubic-bezier(.16,1,.3,1); }
.prob-fill-low  { background: linear-gradient(90deg,#16a34a,#22c55e); border-radius: 100px; height: 8px; transition: width .8s cubic-bezier(.16,1,.3,1); }

/* Advice box */
.advice-box {
    margin-top: 24px; background: rgba(255,255,255,.03);
    border: 1px solid rgba(255,255,255,.08); border-radius: 16px; padding: 28px 32px;
}
.advice-title { font-family: 'Syne', sans-serif; font-size: 15px; font-weight: 700; color: #c8cde0; margin-bottom: 14px; }
.advice-item { display: flex; align-items: flex-start; gap: 10px; margin-bottom: 10px; font-size: 14px; color: #5a6278; line-height: 1.55; }

/* Button override */
[data-testid="stButton"] button {
    background: linear-gradient(135deg, #dc2626, #f43f5e) !important;
    color: white !important; border: none !important; border-radius: 12px !important;
    font-family: 'DM Sans', sans-serif !important; font-weight: 500 !important;
    font-size: 15px !important; padding: 14px 36px !important; width: 100% !important;
    box-shadow: 0 8px 28px rgba(220,38,38,.35) !important; transition: all .2s !important;
}
[data-testid="stButton"] button:hover { transform: translateY(-2px) !important; box-shadow: 0 14px 36px rgba(220,38,38,.5) !important; }

@keyframes popIn { from { opacity: 0; transform: scale(.95) translateY(10px); } to { opacity: 1; transform: scale(1) translateY(0); } }
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# Load model
@st.cache_resource
def load_model():
    return joblib.load('maternal_model.pkl')

try:
    model = load_model()
    model_loaded = True
except:
    model_loaded = False

# Header
st.markdown("""
<div class="page-header">
    <div class="page-tag">🧠 AI-Powered</div>
    <div class="page-title">Maternal Risk Detector</div>
    <div class="page-desc">Enter patient vitals below. Our Random Forest model will instantly assess pregnancy risk level based on 6 key health indicators.</div>
</div>
""", unsafe_allow_html=True)

if not model_loaded:
    st.error("⚠️ Could not load model. Make sure `maternal_model.pkl` is in the root directory.")
    st.stop()

# Input form
st.markdown('<div class="form-card">', unsafe_allow_html=True)
st.markdown('<div class="form-section-title">Patient Health Indicators</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    age = st.number_input("Age (years)", min_value=10, max_value=70, value=25, step=1)
    bs  = st.number_input("Blood Sugar – BS (mmol/L)", min_value=1.0, max_value=20.0, value=6.5, step=0.1, format="%.1f")
with col2:
    systolic_bp  = st.number_input("Systolic BP (mmHg)", min_value=60, max_value=200, value=120, step=1)
    body_temp    = st.number_input("Body Temperature (°F)", min_value=95.0, max_value=105.0, value=98.0, step=0.1, format="%.1f")
with col3:
    diastolic_bp = st.number_input("Diastolic BP (mmHg)", min_value=40, max_value=140, value=80, step=1)
    heart_rate   = st.number_input("Heart Rate (bpm)", min_value=40, max_value=180, value=72, step=1)

st.markdown('</div>', unsafe_allow_html=True)

# Predict button
if st.button("⚡ Analyse Risk Now"):
    input_data = np.array([[age, systolic_bp, diastolic_bp, bs, body_temp, heart_rate]])
    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]
    classes = model.classes_

    prob_dict = dict(zip(classes, probabilities))
    high_p = prob_dict.get('high risk', 0)
    mid_p  = prob_dict.get('mid risk', 0)
    low_p  = prob_dict.get('low risk', 0)

    # Result card
    if prediction == 'high risk':
        css_class, emoji, label_class = 'result-high', '🚨', 'result-label-high'
        message = "Immediate medical attention is recommended. Activate emergency protocols and notify the care team."
        advice = [
            ("🏥", "Refer to specialist OB/GYN immediately"),
            ("💉", "Monitor blood pressure every 15 minutes"),
            ("🩸", "Prepare blood donor alert via Emergency SOS"),
            ("📋", "Document all vitals and escalate to ICU if needed"),
        ]
    elif prediction == 'mid risk':
        css_class, emoji, label_class = 'result-mid', '⚠️', 'result-label-mid'
        message = "Elevated risk detected. Close monitoring and follow-up appointments are strongly advised."
        advice = [
            ("📅", "Schedule follow-up within 48 hours"),
            ("💊", "Review current medications and supplements"),
            ("🏃", "Advise reduced physical activity"),
            ("📊", "Re-test blood sugar and BP daily"),
        ]
    else:
        css_class, emoji, label_class = 'result-low', '✅', 'result-label-low'
        message = "Patient vitals are within normal range. Continue routine prenatal care and monitoring."
        advice = [
            ("📅", "Maintain regular prenatal checkups"),
            ("🥗", "Continue balanced diet and hydration"),
            ("🧘", "Light exercise and stress management recommended"),
            ("📋", "Next review in 4 weeks as scheduled"),
        ]

    label_display = prediction.title()

    st.markdown(f"""
    <div class="{css_class}">
        <div class="result-emoji">{emoji}</div>
        <div class="result-label {label_class}">{label_display}</div>
        <div class="result-sub">{message}</div>
        <div class="prob-bars">
            <div class="prob-row">
                <div class="prob-label"><span>High Risk</span><span>{high_p*100:.1f}%</span></div>
                <div class="prob-track"><div class="prob-fill-high" style="width:{high_p*100:.1f}%"></div></div>
            </div>
            <div class="prob-row">
                <div class="prob-label"><span>Mid Risk</span><span>{mid_p*100:.1f}%</span></div>
                <div class="prob-track"><div class="prob-fill-mid" style="width:{mid_p*100:.1f}%"></div></div>
            </div>
            <div class="prob-row">
                <div class="prob-label"><span>Low Risk</span><span>{low_p*100:.1f}%</span></div>
                <div class="prob-track"><div class="prob-fill-low" style="width:{low_p*100:.1f}%"></div></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Advice
    advice_html = ''.join([f'<div class="advice-item"><span>{icon}</span><span>{text}</span></div>' for icon, text in advice])
    st.markdown(f"""
    <div class="advice-box">
        <div class="advice-title">📋 Recommended Actions</div>
        {advice_html}
    </div>
    """, unsafe_allow_html=True)

    # Save to session for dashboard
    if 'predictions' not in st.session_state:
        st.session_state.predictions = []
    st.session_state.predictions.append({
        'age': age, 'systolic': systolic_bp, 'diastolic': diastolic_bp,
        'bs': bs, 'temp': body_temp, 'hr': heart_rate,
        'result': prediction,
        'high_p': high_p, 'mid_p': mid_p, 'low_p': low_p
    })
