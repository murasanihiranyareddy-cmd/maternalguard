import streamlit as st
import random

st.set_page_config(page_title="Donor Network – Maternal Guard", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');
*, *::before, *::after { box-sizing: border-box; }
html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background: #060810 !important; color: #e8eaf0 !important;
    font-family: 'DM Sans', sans-serif !important;
}
[data-testid="stSidebar"] { background: #0a0d18 !important; border-right: 1px solid rgba(255,255,255,0.06) !important; }
.block-container { padding: 40px 60px !important; max-width: 1200px !important; }
.page-tag { font-size: 11px; font-weight: 600; letter-spacing: .16em; text-transform: uppercase; color: #f87171; margin-bottom: 12px; }
.page-title { font-family: 'Syne', sans-serif; font-size: 42px; font-weight: 800; color: #f1f3f9; letter-spacing: -.03em; }
.page-desc { font-size: 16px; color: #4a5168; line-height: 1.7; margin-top: 12px; max-width: 580px; margin-bottom: 40px; }
.section-title { font-family: 'Syne', sans-serif; font-size: 18px; font-weight: 700; color: #c8cde0; margin: 0 0 20px; }

/* Form card */
.form-card { background: rgba(255,255,255,.03); border: 1px solid rgba(255,255,255,.07); border-radius: 24px; padding: 40px 44px; }

/* Stats */
.stats-row { display: flex; gap: 16px; margin-bottom: 32px; }
.stat-card { flex: 1; background: rgba(255,255,255,.03); border: 1px solid rgba(255,255,255,.07); border-radius: 16px; padding: 24px 20px; text-align: center; }
.s-num { font-family: 'Syne', sans-serif; font-size: 30px; font-weight: 800; }
.s-label { font-size: 11px; color: #3a4058; text-transform: uppercase; letter-spacing: .09em; margin-top: 4px; }

/* Donor table */
.donor-row {
    display: flex; align-items: center; justify-content: space-between;
    padding: 16px 20px; border-radius: 12px; margin-bottom: 8px;
    background: rgba(255,255,255,.025); border: 1px solid rgba(255,255,255,.06);
    transition: all .2s;
}
.donor-row:hover { background: rgba(255,255,255,.05); border-color: rgba(248,113,113,.15); }
.dr-name { font-family: 'Syne', sans-serif; font-size: 15px; font-weight: 700; color: #e0e4f0; }
.dr-meta { font-size: 12px; color: #3a4058; margin-top: 2px; }
.blood-badge { font-family: 'Syne', sans-serif; font-size: 14px; font-weight: 800;
    padding: 4px 12px; border-radius: 8px; background: rgba(248,113,113,.12);
    color: #f87171; border: 1px solid rgba(248,113,113,.25); min-width: 48px; text-align: center; }
.avail-dot { width: 9px; height: 9px; border-radius: 50%; display: inline-block; margin-right: 6px; }
.dot-green { background: #22c55e; box-shadow: 0 0 6px #22c55e; }
.dot-yellow { background: #eab308; }
.dot-gray { background: #374151; }
.avail-text { font-size: 12px; }

/* Input overrides */
[data-testid="stSelectbox"] > div > div, [data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input {
    background: rgba(255,255,255,.05) !important; border: 1px solid rgba(255,255,255,.1) !important;
    border-radius: 10px !important; color: #e8eaf0 !important;
}
label { color: #7b84a0 !important; font-size: 13px !important; font-weight: 500 !important; }
[data-testid="stButton"] button {
    background: linear-gradient(135deg, #dc2626, #f43f5e) !important;
    color: white !important; border: none !important; border-radius: 12px !important;
    font-family: 'DM Sans', sans-serif !important; font-weight: 500 !important;
    font-size: 15px !important; padding: 13px 32px !important;
    box-shadow: 0 8px 24px rgba(220,38,38,.35) !important; width: 100% !important;
}
[data-testid="stTabs"] [data-baseweb="tab"] { color: #4a5168 !important; font-family: 'DM Sans', sans-serif !important; font-weight: 500 !important; }
[data-testid="stTabs"] [aria-selected="true"] { color: #f87171 !important; border-bottom-color: #f87171 !important; }
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="margin-bottom:40px">
    <div class="page-tag">🩸 Donor Network</div>
    <div class="page-title">Smart Donor Network</div>
    <div class="page-desc">Register as a blood donor or search for available donors by blood type and location. Every registration can save a life.</div>
</div>
""", unsafe_allow_html=True)

# Stats
st.markdown("""
<div class="stats-row">
    <div class="stat-card"><div class="s-num" style="color:#86efac">247</div><div class="s-label">Online Now</div></div>
    <div class="stat-card"><div class="s-num" style="color:#f87171">12,483</div><div class="s-label">Total Registered</div></div>
    <div class="stat-card"><div class="s-num" style="color:#fb923c">340</div><div class="s-label">Donations Made</div></div>
    <div class="stat-card"><div class="s-num" style="color:#a5b4fc">8</div><div class="s-label">Blood Types Covered</div></div>
</div>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🩸 Register as Donor", "🔍 Find Donors"])

# ── TAB 1: REGISTER ──
with tab1:
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<div class="form-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Donor Registration Form</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        d_name    = st.text_input("Full Name", placeholder="Your full name")
        d_age     = st.number_input("Age", min_value=18, max_value=65, value=25)
        d_blood   = st.selectbox("Blood Type", ["A+", "A−", "B+", "B−", "AB+", "AB−", "O+", "O−"])
        d_city    = st.text_input("City / Area", placeholder="e.g. Kurnool, AP")
    with c2:
        d_phone   = st.text_input("Phone Number", placeholder="+91 XXXXX XXXXX")
        d_weight  = st.number_input("Weight (kg)", min_value=45, max_value=150, value=65)
        d_avail   = st.selectbox("Availability", ["Available Now", "Available on Call", "Not Available Currently"])
        d_last    = st.text_input("Last Donation Date (if any)", placeholder="e.g. Jan 2024 or Never")

    d_consent = st.checkbox("✅ I confirm that I am healthy, above 18, and consent to be contacted in emergencies.")

    if st.button("💉 Register as Donor"):
        if not d_name or not d_phone or not d_city:
            st.error("Please fill in Name, Phone, and City.")
        elif not d_consent:
            st.error("Please confirm your consent to register.")
        else:
            st.success(f"🎉 **{d_name}** registered successfully as a **{d_blood}** donor in **{d_city}**!")
            st.info("📲 You'll receive an SMS confirmation shortly. Thank you for saving lives! 🩸")
            if 'donors' not in st.session_state:
                st.session_state.donors = []
            st.session_state.donors.append({
                'name': d_name, 'blood': d_blood, 'city': d_city,
                'age': d_age, 'availability': d_avail, 'phone': d_phone
            })
    st.markdown('</div>', unsafe_allow_html=True)

# ── TAB 2: FIND DONORS ──
with tab2:
    st.markdown('<br>', unsafe_allow_html=True)
    fc1, fc2, fc3 = st.columns(3)
    with fc1:
        filter_blood = st.selectbox("Filter by Blood Type", ["All", "A+", "A−", "B+", "B−", "AB+", "AB−", "O+", "O−"])
    with fc2:
        filter_city = st.text_input("Filter by City", placeholder="e.g. Kurnool")
    with fc3:
        filter_avail = st.selectbox("Filter by Availability", ["All", "Available Now", "Available on Call"])

    st.markdown('<div class="section-title" style="margin-top:24px">Donor Directory</div>', unsafe_allow_html=True)

    # Simulated + session donors
    base_donors = [
        {"name": "Ravi Kumar",    "blood": "O+",  "city": "Kurnool",    "age": 28, "availability": "Available Now"},
        {"name": "Sneha Patel",   "blood": "A+",  "city": "Kurnool",    "age": 24, "availability": "Available on Call"},
        {"name": "Mohammed Ali",  "blood": "B+",  "city": "Nandyal",    "age": 32, "availability": "Available Now"},
        {"name": "Lakshmi Devi",  "blood": "AB+", "city": "Kurnool",    "age": 29, "availability": "Available Now"},
        {"name": "Arjun Reddy",   "blood": "O−",  "city": "Hyderabad",  "age": 35, "availability": "Not Available Currently"},
        {"name": "Priya Nair",    "blood": "A−",  "city": "Kurnool",    "age": 27, "availability": "Available on Call"},
        {"name": "Suresh Babu",   "blood": "B−",  "city": "Kadapa",     "age": 31, "availability": "Available Now"},
        {"name": "Anitha Rao",    "blood": "AB−", "city": "Kurnool",    "age": 26, "availability": "Available on Call"},
    ]

    all_donors = base_donors + (st.session_state.get('donors', []))

    # Filter
    filtered = all_donors
    if filter_blood != "All":
        filtered = [d for d in filtered if d['blood'] == filter_blood]
    if filter_city:
        filtered = [d for d in filtered if filter_city.lower() in d['city'].lower()]
    if filter_avail != "All":
        filtered = [d for d in filtered if d['availability'] == filter_avail]

    if not filtered:
        st.warning("No donors found matching those filters.")
    else:
        avail_map = {
            "Available Now":       ('<span class="avail-dot dot-green"></span>', "Available Now"),
            "Available on Call":   ('<span class="avail-dot dot-yellow"></span>', "On Call"),
            "Not Available Currently": ('<span class="avail-dot dot-gray"></span>', "Unavailable"),
        }
        for d in filtered:
            dot, label = avail_map.get(d['availability'], ('', d['availability']))
            st.markdown(f"""
            <div class="donor-row">
                <div>
                    <div class="dr-name">{d['name']}</div>
                    <div class="dr-meta">{d['city']} · Age {d['age']}</div>
                </div>
                <div class="blood-badge">{d['blood']}</div>
                <div class="avail-text">{dot}{label}</div>
            </div>
            """, unsafe_allow_html=True)
