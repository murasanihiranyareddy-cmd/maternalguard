import streamlit as st
import random
import time

st.set_page_config(page_title="Emergency SOS – Maternal Guard", layout="wide")

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

.page-tag { font-size: 11px; font-weight: 600; letter-spacing: .16em; text-transform: uppercase; color: #f87171; margin-bottom: 12px; }
.page-title { font-family: 'Syne', sans-serif; font-size: 42px; font-weight: 800; color: #f1f3f9; letter-spacing: -.03em; line-height: 1.1; }
.page-desc { font-size: 16px; color: #4a5168; line-height: 1.7; margin-top: 12px; max-width: 580px; margin-bottom: 40px; }

/* SOS button zone */
.sos-zone {
    background: linear-gradient(135deg, rgba(220,38,38,.15), rgba(244,63,94,.07));
    border: 1px solid rgba(220,38,38,.3); border-radius: 24px;
    padding: 56px 48px; text-align: center; margin-bottom: 32px;
    position: relative; overflow: hidden;
}
.sos-zone::before {
    content: ''; position: absolute; inset: 0;
    background: radial-gradient(ellipse 60% 60% at 50% 50%, rgba(220,38,38,.08), transparent);
    animation: sosPulse 2s ease infinite;
}
@keyframes sosPulse { 0%,100%{opacity:1} 50%{opacity:.3} }
.sos-title { font-family: 'Syne', sans-serif; font-size: 28px; font-weight: 800; color: #fca5a5; margin-bottom: 10px; }
.sos-sub { font-size: 15px; color: #5a6278; margin-bottom: 32px; }

/* Info cards */
.info-grid { display: grid; grid-template-columns: repeat(3,1fr); gap: 16px; margin-bottom: 32px; }
.info-card {
    background: rgba(255,255,255,.03); border: 1px solid rgba(255,255,255,.07);
    border-radius: 16px; padding: 24px 22px;
}
.info-card .ic-label { font-size: 11px; font-weight: 600; letter-spacing: .1em; text-transform: uppercase; color: #3a4058; margin-bottom: 8px; }
.info-card .ic-val { font-family: 'Syne', sans-serif; font-size: 22px; font-weight: 800; color: #f1f3f9; }

/* Donor list */
.donor-card {
    background: rgba(255,255,255,.03); border: 1px solid rgba(255,255,255,.07);
    border-radius: 16px; padding: 20px 24px;
    display: flex; align-items: center; justify-content: space-between;
    margin-bottom: 12px; animation: slideIn .4s ease both;
}
.donor-card:nth-child(2) { animation-delay: .1s; }
.donor-card:nth-child(3) { animation-delay: .2s; }
.donor-card:nth-child(4) { animation-delay: .3s; }
.donor-card:nth-child(5) { animation-delay: .4s; }
@keyframes slideIn { from{opacity:0;transform:translateX(-20px)} to{opacity:1;transform:translateX(0)} }
.donor-info .d-name { font-family: 'Syne', sans-serif; font-size: 16px; font-weight: 700; color: #e0e4f0; }
.donor-info .d-meta { font-size: 13px; color: #3a4058; margin-top: 3px; }
.donor-badge {
    font-size: 11px; font-weight: 600; letter-spacing: .07em; text-transform: uppercase;
    padding: 5px 12px; border-radius: 100px;
}
.badge-enroute { background: rgba(234,88,12,.15); color: #fb923c; border: 1px solid rgba(234,88,12,.3); }
.badge-alerted { background: rgba(99,102,241,.15); color: #a5b4fc; border: 1px solid rgba(99,102,241,.3); }
.badge-standby { background: rgba(255,255,255,.06); color: #5a6278; border: 1px solid rgba(255,255,255,.1); }

/* Alert log */
.log-item { display: flex; align-items: center; gap: 14px; padding: 14px 0; border-bottom: 1px solid rgba(255,255,255,.04); font-size: 13px; color: #4a5168; }
.log-dot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }
.log-dot-red { background: #ef4444; box-shadow: 0 0 6px #ef4444; }
.log-dot-orange { background: #f97316; }
.log-dot-blue { background: #6366f1; }
.log-dot-green { background: #22c55e; }
.log-time { color: #2a2f42; font-size: 12px; min-width: 60px; }

/* Form input overrides */
[data-testid="stSelectbox"] > div, [data-testid="stTextInput"] input {
    background: rgba(255,255,255,.05) !important; border: 1px solid rgba(255,255,255,.1) !important;
    border-radius: 10px !important; color: #e8eaf0 !important;
}
label { color: #7b84a0 !important; font-size: 13px !important; font-weight: 500 !important; }
[data-testid="stButton"] button {
    background: linear-gradient(135deg, #dc2626, #f43f5e) !important;
    color: white !important; border: none !important; border-radius: 12px !important;
    font-family: 'DM Sans', sans-serif !important; font-weight: 600 !important;
    font-size: 16px !important; padding: 16px 36px !important; width: 100% !important;
    box-shadow: 0 8px 28px rgba(220,38,38,.4) !important;
    letter-spacing: .02em !important;
}
.section-title { font-family: 'Syne', sans-serif; font-size: 18px; font-weight: 700; color: #c8cde0; margin: 32px 0 18px; }
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div style="margin-bottom:40px">
    <div class="page-tag">🚨 Emergency Response</div>
    <div class="page-title">Emergency SOS</div>
    <div class="page-desc">Instantly alert nearby verified blood donors during a hemorrhage or obstetric emergency. Donors are matched by blood type, proximity, and availability.</div>
</div>
""", unsafe_allow_html=True)

# SOS form
col_form, col_info = st.columns([1, 1], gap="large")

with col_form:
    st.markdown('<div class="section-title">Patient Emergency Details</div>', unsafe_allow_html=True)
    patient_name = st.text_input("Patient Name", placeholder="e.g. Priya Sharma")
    hospital     = st.text_input("Hospital / Facility", placeholder="e.g. Apollo Hospital, Kurnool")
    blood_type   = st.selectbox("Required Blood Type", ["A+", "A−", "B+", "B−", "AB+", "AB−", "O+", "O−"])
    emergency_type = st.selectbox("Emergency Type", [
        "Postpartum Hemorrhage (PPH)",
        "Placenta Previa",
        "Ectopic Pregnancy Rupture",
        "Eclampsia / Severe Preeclampsia",
        "Other Obstetric Emergency"
    ])
    units_needed = st.number_input("Units of Blood Needed", min_value=1, max_value=10, value=2)

    triggered = st.button("🚨 TRIGGER EMERGENCY SOS")

with col_info:
    st.markdown('<div class="section-title">Live Network Status</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-grid">
        <div class="info-card">
            <div class="ic-label">Online Donors</div>
            <div class="ic-val" style="color:#86efac">247</div>
        </div>
        <div class="info-card">
            <div class="ic-label">Avg Match Time</div>
            <div class="ic-val" style="color:#fb923c">&lt;90s</div>
        </div>
        <div class="info-card">
            <div class="ic-label">Active SOSes</div>
            <div class="ic-val" style="color:#f87171">3</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-title" style="margin-top:16px">Recent Activity Log</div>
    <div class="log-item"><div class="log-dot log-dot-red"></div><div class="log-time">2m ago</div><div>SOS triggered — O+ blood needed, City Hospital</div></div>
    <div class="log-item"><div class="log-dot log-dot-orange"></div><div class="log-time">11m ago</div><div>Donor Arun K. en route — ETA 7 min</div></div>
    <div class="log-item"><div class="log-dot log-dot-blue"></div><div class="log-time">28m ago</div><div>New donor registered — B+ blood type, 2.1km away</div></div>
    <div class="log-item"><div class="log-dot log-dot-green"></div><div class="log-time">44m ago</div><div>Emergency resolved — 2 units delivered successfully</div></div>
    <div class="log-item"><div class="log-dot log-dot-orange"></div><div class="log-time">1h ago</div><div>SOS triggered — AB− blood needed, Govt Hospital</div></div>
    """, unsafe_allow_html=True)

# After trigger
if triggered:
    if not patient_name or not hospital:
        st.error("Please fill in Patient Name and Hospital before triggering SOS.")
    else:
        with st.spinner("🔴 Alerting nearby donors..."):
            time.sleep(2)

        st.success(f"✅ SOS Activated for **{patient_name}** at **{hospital}** — **{blood_type}** blood required!")

        # Simulated matched donors
        donor_names = ["Ravi Kumar", "Sneha Patel", "Mohammed Ali", "Lakshmi Devi", "Arjun Reddy"]
        distances   = [1.2, 2.4, 3.1, 4.0, 5.5]
        statuses    = ["En Route", "Alerted", "Alerted", "Standby", "Standby"]
        badge_css   = ["badge-enroute", "badge-alerted", "badge-alerted", "badge-standby", "badge-standby"]
        etas        = ["~8 min", "~14 min", "~19 min", "~25 min", "~35 min"]

        st.markdown('<div class="section-title" style="margin-top:32px">🩸 Matched Donors</div>', unsafe_allow_html=True)
        for i in range(5):
            st.markdown(f"""
            <div class="donor-card">
                <div class="donor-info">
                    <div class="d-name">{donor_names[i]}</div>
                    <div class="d-meta">{blood_type} · {distances[i]} km away · ETA {etas[i]}</div>
                </div>
                <div class="donor-badge {badge_css[i]}">{statuses[i]}</div>
            </div>
            """, unsafe_allow_html=True)

        st.info(f"📲 SMS + push notifications sent to **{units_needed * 3} donors**. Medical team has been notified.")
