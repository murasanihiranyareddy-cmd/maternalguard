import streamlit as st
import random

st.set_page_config(page_title="Dashboard – Maternal Guard", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');
*, *::before, *::after { box-sizing: border-box; }
html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background: #060810 !important; color: #e8eaf0 !important;
    font-family: 'DM Sans', sans-serif !important;
}
[data-testid="stSidebar"] { background: #0a0d18 !important; border-right: 1px solid rgba(255,255,255,0.06) !important; }
.block-container { padding: 40px 60px !important; max-width: 1300px !important; }
.page-tag { font-size: 11px; font-weight: 600; letter-spacing: .16em; text-transform: uppercase; color: #f87171; margin-bottom: 12px; }
.page-title { font-family: 'Syne', sans-serif; font-size: 42px; font-weight: 800; color: #f1f3f9; letter-spacing: -.03em; }
.page-desc { font-size: 16px; color: #4a5168; line-height: 1.7; margin-top: 12px; max-width: 580px; margin-bottom: 40px; }
.section-title { font-family: 'Syne', sans-serif; font-size: 17px; font-weight: 700; color: #c8cde0; margin-bottom: 16px; }

/* KPI cards */
.kpi-grid { display: grid; grid-template-columns: repeat(4,1fr); gap: 16px; margin-bottom: 40px; }
.kpi-card { background: rgba(255,255,255,.03); border: 1px solid rgba(255,255,255,.07); border-radius: 18px; padding: 28px 24px; }
.kpi-label { font-size: 11px; font-weight: 600; letter-spacing: .12em; text-transform: uppercase; color: #3a4058; margin-bottom: 10px; }
.kpi-val { font-family: 'Syne', sans-serif; font-size: 34px; font-weight: 800; line-height: 1; }
.kpi-delta { font-size: 12px; margin-top: 8px; }
.delta-up { color: #22c55e; } .delta-down { color: #f87171; }

/* Chart card */
.chart-card { background: rgba(255,255,255,.03); border: 1px solid rgba(255,255,255,.07); border-radius: 18px; padding: 28px 28px 16px; margin-bottom: 24px; }

/* Recent predictions table */
.pred-row { display: flex; align-items: center; gap: 16px; padding: 13px 0; border-bottom: 1px solid rgba(255,255,255,.04); font-size: 13px; }
.pred-val { color: #7b84a0; flex: 1; }
.risk-chip { font-size: 11px; font-weight: 600; letter-spacing: .06em; text-transform: uppercase; padding: 4px 10px; border-radius: 100px; }
.chip-high { background: rgba(220,38,38,.15); color: #fca5a5; border: 1px solid rgba(220,38,38,.3); }
.chip-mid  { background: rgba(234,88,12,.15); color: #fdba74; border: 1px solid rgba(234,88,12,.3); }
.chip-low  { background: rgba(22,163,74,.15);  color: #86efac; border: 1px solid rgba(22,163,74,.3); }

/* Plotly / chart bg overrides */
[data-testid="stVegaLiteChart"], [data-testid="stPlotlyChart"] { background: transparent !important; }

#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

try:
    import plotly.graph_objects as go
    import plotly.express as px
    import pandas as pd
    import numpy as np
    HAS_PLOTLY = True
except ImportError:
    HAS_PLOTLY = False

st.markdown("""
<div style="margin-bottom:40px">
    <div class="page-tag">📊 Analytics</div>
    <div class="page-title">Live Dashboard</div>
    <div class="page-desc">Real-time overview of risk assessments, emergency responses, and donor network health.</div>
</div>
""", unsafe_allow_html=True)

# KPI Cards
preds = st.session_state.get('predictions', [])
total = len(preds)
high_count = sum(1 for p in preds if p['result'] == 'high risk')
mid_count  = sum(1 for p in preds if p['result'] == 'mid risk')
low_count  = sum(1 for p in preds if p['result'] == 'low risk')

st.markdown(f"""
<div class="kpi-grid">
    <div class="kpi-card">
        <div class="kpi-label">Total Assessments</div>
        <div class="kpi-val" style="color:#a5b4fc">{total + 127}</div>
        <div class="kpi-delta delta-up">↑ +12 today</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-label">High Risk Detected</div>
        <div class="kpi-val" style="color:#fca5a5">{high_count + 18}</div>
        <div class="kpi-delta delta-down">↑ +3 this week</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-label">SOS Activations</div>
        <div class="kpi-val" style="color:#fb923c">24</div>
        <div class="kpi-delta delta-up">↓ -2 vs last week</div>
    </div>
    <div class="kpi-card">
        <div class="kpi-label">Donors Online</div>
        <div class="kpi-val" style="color:#86efac">247</div>
        <div class="kpi-delta delta-up">↑ +34 this month</div>
    </div>
</div>
""", unsafe_allow_html=True)

if not HAS_PLOTLY:
    st.warning("Install plotly for charts: `pip install plotly pandas`")
else:
    import pandas as pd
    import numpy as np

    # Chart row 1
    c1, c2 = st.columns([3, 2], gap="large")

    with c1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Weekly Risk Assessments</div>', unsafe_allow_html=True)
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        high_vals = [4, 6, 3, 7, 5, 8, 4 + high_count]
        mid_vals  = [8, 10, 9, 12, 7, 11, 9 + mid_count]
        low_vals  = [14, 18, 16, 20, 15, 17, 12 + low_count]

        fig = go.Figure()
        fig.add_trace(go.Bar(name='High Risk', x=days, y=high_vals, marker_color='#ef4444', marker_line_width=0))
        fig.add_trace(go.Bar(name='Mid Risk',  x=days, y=mid_vals,  marker_color='#f97316', marker_line_width=0))
        fig.add_trace(go.Bar(name='Low Risk',  x=days, y=low_vals,  marker_color='#22c55e', marker_line_width=0))
        fig.update_layout(
            barmode='stack', plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#5a6278', family='DM Sans'), height=280,
            legend=dict(bgcolor='rgba(0,0,0,0)', font=dict(color='#5a6278', size=12)),
            xaxis=dict(showgrid=False, color='#3a4058'),
            yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,.05)', color='#3a4058'),
            margin=dict(l=0, r=0, t=0, b=0)
        )
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Risk Distribution</div>', unsafe_allow_html=True)
        labels = ['High Risk', 'Mid Risk', 'Low Risk']
        values = [high_count + 18, mid_count + 42, low_count + 67]
        colors = ['#ef4444', '#f97316', '#22c55e']
        fig2 = go.Figure(go.Pie(
            labels=labels, values=values,
            hole=.65,
            marker=dict(colors=colors, line=dict(color='#060810', width=3)),
            textinfo='percent', textfont=dict(color='#e8eaf0', size=12)
        ))
        fig2.update_layout(
            plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#5a6278', family='DM Sans'), height=280,
            showlegend=True,
            legend=dict(bgcolor='rgba(0,0,0,0)', font=dict(color='#5a6278', size=12), orientation='v'),
            margin=dict(l=0, r=0, t=0, b=0),
            annotations=[dict(text=f'<b>{sum(values)}</b>', x=0.5, y=0.5, font_size=22, font_color='#f1f3f9', showarrow=False)]
        )
        st.plotly_chart(fig2, use_container_width=True, config={'displayModeBar': False})
        st.markdown('</div>', unsafe_allow_html=True)

    # Chart row 2
    c3, c4 = st.columns([2, 3], gap="large")

    with c3:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Donors by Blood Type</div>', unsafe_allow_html=True)
        blood_types = ['O+', 'A+', 'B+', 'AB+', 'O−', 'A−', 'B−', 'AB−']
        counts = [68, 54, 47, 23, 18, 14, 12, 11]
        fig3 = go.Figure(go.Bar(
            x=counts, y=blood_types, orientation='h',
            marker=dict(
                color=counts,
                colorscale=[[0,'rgba(248,113,113,0.3)'],[1,'#ef4444']],
                line=dict(width=0)
            ),
            text=counts, textposition='outside', textfont=dict(color='#5a6278', size=12)
        ))
        fig3.update_layout(
            plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#5a6278', family='DM Sans'), height=300,
            xaxis=dict(showgrid=False, visible=False),
            yaxis=dict(showgrid=False, color='#5a6278'),
            margin=dict(l=0, r=40, t=0, b=0)
        )
        st.plotly_chart(fig3, use_container_width=True, config={'displayModeBar': False})
        st.markdown('</div>', unsafe_allow_html=True)

    with c4:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">SOS Response Times (last 30 days)</div>', unsafe_allow_html=True)
        days30 = list(range(1, 31))
        response_times = [random.randint(60, 140) for _ in days30]
        fig4 = go.Figure()
        fig4.add_trace(go.Scatter(
            x=days30, y=response_times, mode='lines',
            line=dict(color='#f87171', width=2),
            fill='tozeroy', fillcolor='rgba(248,113,113,0.07)'
        ))
        fig4.add_hline(y=90, line_dash='dash', line_color='rgba(251,146,60,0.5)',
                       annotation_text='90s target', annotation_font_color='#fb923c')
        fig4.update_layout(
            plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#5a6278', family='DM Sans'), height=300,
            xaxis=dict(showgrid=False, color='#3a4058', title='Day'),
            yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,.05)', color='#3a4058', title='Seconds'),
            margin=dict(l=0, r=0, t=0, b=0)
        )
        st.plotly_chart(fig4, use_container_width=True, config={'displayModeBar': False})
        st.markdown('</div>', unsafe_allow_html=True)

# Recent predictions from session
st.markdown('<div class="section-title" style="margin-top:8px">Recent Risk Assessments (This Session)</div>', unsafe_allow_html=True)
if preds:
    st.markdown('<div class="chart-card">', unsafe_allow_html=True)
    header = '<div class="pred-row"><div class="pred-val"><b>Age</b></div><div class="pred-val"><b>Systolic</b></div><div class="pred-val"><b>Diastolic</b></div><div class="pred-val"><b>BS</b></div><div class="pred-val"><b>Temp</b></div><div class="pred-val"><b>HR</b></div><div><b>Result</b></div></div>'
    st.markdown(header, unsafe_allow_html=True)
    for p in reversed(preds[-8:]):
        chip = 'chip-high' if p['result']=='high risk' else ('chip-mid' if p['result']=='mid risk' else 'chip-low')
        label = p['result'].title()
        st.markdown(f"""
        <div class="pred-row">
            <div class="pred-val">{p['age']}</div>
            <div class="pred-val">{p['systolic']}</div>
            <div class="pred-val">{p['diastolic']}</div>
            <div class="pred-val">{p['bs']}</div>
            <div class="pred-val">{p['temp']}</div>
            <div class="pred-val">{p['hr']}</div>
            <div><span class="risk-chip {chip}">{label}</span></div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("No assessments yet this session. Run the AI Risk Detector to see results here.")
