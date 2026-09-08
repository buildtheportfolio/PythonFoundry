import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(
    page_title="RetireCraft — FIRE Calculator",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=Inter:wght@300;400;500&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
h1, h2, h3, h4 { font-family: 'Syne', sans-serif !important; }

.stApp { background: #ffffff !important; color: #334155; }
[data-testid="stSidebar"] {
    background: #f8fafc !important;
    border-right: 1px solid #e2e8f0;
}
[data-testid="stSidebar"] .block-container { padding-top: 1rem; }

.stTabs [data-baseweb="tab-list"] {
    background: #f8fafc;
    border-bottom: 1px solid #e2e8f0;
    gap: 0;
}
.stTabs [data-baseweb="tab"] {
    color: #64748b !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    padding: 10px 16px !important;
}
.stTabs [aria-selected="true"] {
    color: #f59e0b !important;
    border-bottom: 2px solid #f59e0b !important;
    background: transparent !important;
}
.stTabs [data-baseweb="tab-panel"] { background: #ffffff; padding-top: 1.5rem; }

.stMetric {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 16px !important;
}
.stMetric label { color: #64748b !important; font-size: 0.72rem !important; text-transform: uppercase; letter-spacing: 0.08em; }
.stMetric [data-testid="stMetricValue"] { color: #0f172a !important; font-family: 'Syne', sans-serif !important; font-size: 1.5rem !important; }
.stMetric [data-testid="stMetricDelta"] { color: #10b981 !important; }

.stNumberInput input, .stSlider { color: #0f172a !important; }
[data-testid="stNumberInput"] input {
    background: #ffffff !important;
    border: 1px solid #cbd5e1 !important;
    color: #0f172a !important;
    border-radius: 6px !important;
}
.stSlider [data-baseweb="slider"] { margin-top: 6px; }
.stSlider [data-testid="stTickBar"] { color: #94a3b8 !important; font-size: 0.7rem !important; }

.card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 20px 22px;
    margin-bottom: 12px;
}

.fire-card {
    border-radius: 14px;
    padding: 20px;
    text-align: center;
    transition: transform 0.15s;
    background: #ffffff;
}
.fire-card:hover { transform: translateY(-2px); box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); }

.kpi-divider { height: 1px; background: #e2e8f0; margin: 1.2rem 0; }

.section-label {
    color: #475569;
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-weight: 600;
    margin: 1.2rem 0 0.4rem;
}

.insight-row {
    display: flex;
    align-items: center;
    gap: 10px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 10px 14px;
    margin-bottom: 8px;
    font-size: 0.85rem;
    color: #334155;
}

.stDataFrame { background: #ffffff !important; }
.stDataFrame thead { background: #f8fafc !important; }

footer { display: none !important; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<p style="font-family:Syne,sans-serif;font-size:1.4rem;font-weight:800;color:#f59e0b;margin:0 0 4px">🔥 RetireCraft</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#475569;font-size:0.72rem;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:1rem">FIRE Planning Dashboard</p>', unsafe_allow_html=True)
    st.markdown('<div style="height:1px;background:#e2e8f0;margin-bottom:1rem"></div>', unsafe_allow_html=True)

    st.markdown('<p class="section-label">👤 Personal</p>', unsafe_allow_html=True)
    current_age = st.number_input("Current Age", min_value=18, max_value=75, value=30)
    annual_income = st.number_input("Annual Gross Income ($)", min_value=0, value=80000, step=1000)
    current_savings = st.number_input("Current Portfolio ($)", min_value=0, value=50000, step=1000)

    st.markdown('<p class="section-label">💰 Savings</p>', unsafe_allow_html=True)
    monthly_contribution = st.number_input("Monthly Contribution ($)", min_value=0, value=1500, step=100)
    savings_rate = round((monthly_contribution * 12) / annual_income * 100, 1) if annual_income > 0 else 0
    st.metric("Annual Savings Rate", f"{savings_rate}%")

    st.markdown('<p class="section-label">📊 Market Assumptions</p>', unsafe_allow_html=True)
    annual_return = st.slider("Expected Annual Return (%)", 1.0, 15.0, 7.0, 0.1) / 100
    inflation = st.slider("Expected Inflation (%)", 0.0, 10.0, 2.5, 0.1) / 100
    safe_withdrawal_rate = st.slider("Safe Withdrawal Rate (%)", 2.0, 6.0, 4.0, 0.1) / 100

    st.markdown('<p class="section-label">🏖️ Retirement Expenses / Year</p>', unsafe_allow_html=True)
    target_annual_expenses = st.number_input("Regular FIRE ($)", min_value=10000, value=60000, step=1000)
    lean_fire_expenses = st.number_input("LeanFIRE ($)", min_value=5000, value=36000, step=1000)
    fat_fire_expenses = st.number_input("FatFIRE ($)", min_value=10000, value=100000, step=1000)

    st.markdown('<p class="section-label">☕ BaristaFIRE</p>', unsafe_allow_html=True)
    barista_income = st.number_input("Part-time Annual Income ($)", min_value=0, value=20000, step=1000)
    barista_expenses = st.number_input("BaristaFIRE Annual Expenses ($)", min_value=10000, value=60000, step=1000)

real_return = annual_return - inflation
fire_number = target_annual_expenses / safe_withdrawal_rate
lean_fire_number = lean_fire_expenses / safe_withdrawal_rate
fat_fire_number = fat_fire_expenses / safe_withdrawal_rate
net_barista_expenses = max(0, barista_expenses - barista_income)
barista_fire_number = net_barista_expenses / safe_withdrawal_rate
coast_fire_years = max(1, 65 - current_age)
coast_fire_number = fire_number / ((1 + real_return) ** coast_fire_years) if real_return > 0 else fire_number

records = []
w = current_savings
for year in range(51):
    records.append({
        'Year': year,
        'Age': current_age + year,
        'Net Worth': w,
        'Annual Investment Gain': w * real_return,
        'Annual Contribution': monthly_contribution * 12,
    })
    w = w * (1 + real_return) + monthly_contribution * 12

df = pd.DataFrame(records)

def find_fire_age(target):
    hit = df[df['Net Worth'] >= target]
    return int(hit.iloc[0]['Age']) if not hit.empty else None

lean_age = find_fire_age(lean_fire_number)
fire_age = find_fire_age(fire_number)
fat_age = find_fire_age(fat_fire_number)
barista_age = find_fire_age(barista_fire_number)
coast_age = find_fire_age(coast_fire_number)

st.markdown('<h1 style="font-family:Syne,sans-serif;font-size:2rem;font-weight:800;color:#0f172a;margin-bottom:4px">🔥 RetireCraft</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#64748b;font-size:0.9rem;margin-bottom:1.5rem">Financial Independence & Early Retirement Planner</p>', unsafe_allow_html=True)

k1, k2, k3, k4, k5, k6 = st.columns(6)
k1.metric("FIRE Number", f"${fire_number:,.0f}")
k2.metric("FIRE Age", str(fire_age) if fire_age else "50+", delta=f"{fire_age - current_age}y away" if fire_age else None)
k3.metric("LeanFIRE Age", str(lean_age) if lean_age else "50+")
k4.metric("BaristaFIRE Age", str(barista_age) if barista_age else "50+")
k5.metric("Coast FIRE #", f"${coast_fire_number:,.0f}")
k6.metric("Savings Rate", f"{savings_rate}%")

st.markdown('<div class="kpi-divider"></div>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["📈 Projection", "🎯 FIRE Variants", "🔀 Scenarios", "📊 Sensitivity", "📋 Year-by-Year"])

with tab1:
    area_chart = alt.Chart(df).mark_area(
        opacity=0.25,
        line={'color': '#10b981', 'strokeWidth': 2},
        color=alt.Gradient(
            gradient='linear',
            stops=[
                alt.GradientStop(color='#10b981', offset=1),
                alt.GradientStop(color='#ffffff', offset=0)
            ],
            x1=1, x2=1, y1=1, y2=0
        )
    ).encode(
        x=alt.X('Age:Q', title='Age', scale=alt.Scale(domain=[current_age, current_age + 50])),
        y=alt.Y('Net Worth:Q', title='Portfolio Value', axis=alt.Axis(format='$~s', labelColor='#64748b', titleColor='#64748b', gridColor='#e2e8f0', domainColor='#e2e8f0')),
        tooltip=[alt.Tooltip('Age:Q'), alt.Tooltip('Net Worth:Q', format='$,.0f', title='Net Worth')]
    )

    targets_df = pd.DataFrame([
        {'y': lean_fire_number, 'label': f'LeanFIRE  ${lean_fire_number:,.0f}', 'clr': '#0284c7'},
        {'y': fire_number, 'label': f'FIRE  ${fire_number:,.0f}', 'clr': '#d97706'},
        {'y': fat_fire_number, 'label': f'FatFIRE  ${fat_fire_number:,.0f}', 'clr': '#dc2626'},
    ])

    rules = alt.Chart(targets_df).mark_rule(strokeDash=[5, 4], strokeWidth=1.5).encode(
        y='y:Q',
        color=alt.Color('clr:N', scale=None),
        tooltip=[alt.Tooltip('label:N', title='Target'), alt.Tooltip('y:Q', format='$,.0f')]
    )

    t_labels = alt.Chart(targets_df).mark_text(align='left', dx=8, dy=-7, fontSize=11, fontWeight=600).encode(
        y='y:Q', x=alt.value(10), text='label:N',
        color=alt.Color('clr:N', scale=None)
    )

    main_chart = (area_chart + rules + t_labels).properties(height=400).configure_view(
        strokeOpacity=0
    ).configure_axis(
        labelFont='Inter', titleFont='Inter'
    ).interactive()

    st.altair_chart(main_chart, use_container_width=True)

    ci1, ci2 = st.columns(2)
    with ci1:
        st.markdown("##### Key Insights")
        insights = []
        if lean_age:
            insights.append(f"🥗 **LeanFIRE** at age **{lean_age}** ({lean_age - current_age} years)")
        if fire_age:
            insights.append(f"🔥 **Regular FIRE** at age **{fire_age}** ({fire_age - current_age} years)")
        if barista_age:
            insights.append(f"☕ **BaristaFIRE** at age **{barista_age}** ({barista_age - current_age} years)")
        if fat_age:
            insights.append(f"💎 **FatFIRE** at age **{fat_age}** ({fat_age - current_age} years)")
        if coast_age:
            insights.append(f"🏄 **Coast FIRE** milestone at age **{coast_age}** — contributions optional after")
        for ins in insights:
            st.markdown(f'<div class="insight-row">{ins}</div>', unsafe_allow_html=True)

    with ci2:
        st.markdown("##### Projection Parameters")
        st.markdown(f"""
| Parameter | Value |
|---|---|
| Nominal Return | {annual_return*100:.1f}% |
| Inflation Rate | {inflation*100:.1f}% |
| Real Return | {real_return*100:.2f}% |
| Safe Withdrawal Rate | {safe_withdrawal_rate*100:.1f}% |
| Annual Contribution | ${monthly_contribution*12:,.0f} |
| Starting Portfolio | ${current_savings:,.0f} |
| Target Expenses/yr | ${target_annual_expenses:,.0f} |
        """)

with tab2:
    st.markdown("##### Compare Four Paths to Financial Independence")
    st.markdown('<div style="margin-bottom:1rem"></div>', unsafe_allow_html=True)

    strategies = [
        ("🥗", "LeanFIRE", lean_fire_number, lean_fire_expenses, lean_age, "#0284c7", "#f0f9ff",
         "Frugal minimalist lifestyle with lean spending. Maximum freedom, minimum burn rate."),
        ("🔥", "Regular FIRE", fire_number, target_annual_expenses, fire_age, "#059669", "#ecfdf5",
         "Comfortable standard of living. The classic FIRE target for most households."),
        ("☕", "BaristaFIRE", barista_fire_number, barista_expenses - barista_income, barista_age, "#9333ea", "#faf5ff",
         f"Semi-retire with ${barista_income:,}/yr part-time income bridging the gap."),
        ("💎", "FatFIRE", fat_fire_number, fat_fire_expenses, fat_age, "#ea580c", "#fffbeb",
         "Luxury retirement with zero lifestyle compromises. Premium experiences, no budget."),
    ]

    cols = st.columns(4)
    for i, (icon, name, target, exp, age, color, bg, desc) in enumerate(strategies):
        age_str = str(age) if age else "50+"
        yrs = str(age - current_age) if age else "—"
        pct = min(100, current_savings / target * 100) if target > 0 else 0
        cols[i].markdown(f"""
<div class="fire-card" style="background:{bg};border:1px solid {color}33;border-top:3px solid {color}">
  <div style="font-size:2rem;margin-bottom:4px">{icon}</div>
  <div style="font-size:0.7rem;letter-spacing:0.1em;text-transform:uppercase;color:{color};font-weight:700;margin-bottom:8px">{name}</div>
  <div style="color:#64748b;font-size:0.75rem;min-height:46px;margin-bottom:12px">{desc}</div>
  <div style="font-size:1.5rem;font-weight:700;color:#0f172a;font-family:Syne,sans-serif">${target:,.0f}</div>
  <div style="color:#475569;font-size:0.65rem;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:10px">Target</div>
  <div style="background:#e2e8f0;border-radius:4px;height:4px;margin-bottom:10px">
    <div style="background:{color};height:4px;border-radius:4px;width:{pct:.0f}%"></div>
  </div>
  <div style="color:#64748b;font-size:0.7rem;margin-bottom:4px">{pct:.0f}% funded today</div>
  <div style="font-size:1.2rem;font-weight:700;color:{color};font-family:Syne,sans-serif">Age {age_str}</div>
  <div style="color:#475569;font-size:0.72rem">{yrs} years · ${exp:,}/yr</div>
</div>
""", unsafe_allow_html=True)

    st.markdown('<div style="margin-top:2rem"></div>', unsafe_allow_html=True)
    st.markdown("##### Coast FIRE Deep Dive")
    cc1, cc2 = st.columns([1, 2])
    with cc1:
        gap = max(0, coast_fire_number - current_savings)
        coast_funded = min(100, current_savings / coast_fire_number * 100) if coast_fire_number > 0 else 0
        st.markdown(f"""
<div class="card">
<p style="color:#9333ea;font-size:0.7rem;text-transform:uppercase;letter-spacing:0.1em;font-weight:700;margin-bottom:12px">Coast FIRE Analysis</p>
<p style="color:#64748b;font-size:0.82rem;margin-bottom:14px">Once you reach the Coast number, your portfolio grows to your FIRE number by age 65 <em>without further contributions</em>.</p>
<table style="width:100%;font-size:0.82rem;border-collapse:collapse">
<tr><td style="color:#64748b;padding:4px 0">Coast FIRE Target</td><td style="color:#0f172a;text-align:right;font-weight:600">${coast_fire_number:,.0f}</td></tr>
<tr><td style="color:#64748b;padding:4px 0">Current Portfolio</td><td style="color:#0f172a;text-align:right;font-weight:600">${current_savings:,.0f}</td></tr>
<tr><td style="color:#64748b;padding:4px 0">Gap to Coast</td><td style="color:#ef4444;text-align:right;font-weight:600">${gap:,.0f}</td></tr>
<tr><td style="color:#64748b;padding:4px 0">Currently Funded</td><td style="color:#9333ea;text-align:right;font-weight:600">{coast_funded:.1f}%</td></tr>
<tr><td style="color:#64748b;padding:4px 0">Coast Age</td><td style="color:#9333ea;text-align:right;font-weight:600">{str(coast_age) if coast_age else "50+"}</td></tr>
</table>
</div>
""", unsafe_allow_html=True)

    with cc2:
        coast_proj = []
        w_no_contrib = current_savings
        w_with_contrib = current_savings
        for year in range(51):
            coast_proj.append({
                'Age': current_age + year,
                'With Contributions': w_with_contrib,
                'Coast (No Contributions)': w_no_contrib,
            })
            w_with_contrib = w_with_contrib * (1 + real_return) + monthly_contribution * 12
            w_no_contrib = w_no_contrib * (1 + real_return)

        coast_df = pd.DataFrame(coast_proj)
        c_melted = coast_df.melt(id_vars=['Age'], var_name='Track', value_name='Value')

        coast_chart = alt.Chart(c_melted).mark_line(strokeWidth=2).encode(
            x='Age:Q',
            y=alt.Y('Value:Q', axis=alt.Axis(format='$~s', labelColor='#64748b', gridColor='#e2e8f0', domainColor='#e2e8f0')),
            color=alt.Color('Track:N', scale=alt.Scale(domain=['With Contributions', 'Coast (No Contributions)'], range=['#10b981', '#a855f7']),
                            legend=alt.Legend(labelColor='#64748b', titleColor='#475569')),
            tooltip=['Age:Q', 'Track:N', alt.Tooltip('Value:Q', format='$,.0f')]
        ).properties(height=240).configure_view(strokeOpacity=0).interactive()
        st.altair_chart(coast_chart, use_container_width=True)

with tab3:
    st.markdown("##### Compare Contribution Strategies")

    sc1, sc2, sc3 = st.columns(3)
    contrib_a = sc1.number_input("Scenario A (Conservative)", value=max(500, monthly_contribution - 500), step=100, key="sa")
    contrib_b = sc2.number_input("Scenario B (Current)", value=monthly_contribution, step=100, key="sb")
    contrib_c = sc3.number_input("Scenario C (Aggressive)", value=monthly_contribution + 500, step=100, key="sc")

    scenario_rows = []
    for label, contrib, clr in [("Conservative", contrib_a, "#0284c7"), ("Current", contrib_b, "#10b981"), ("Aggressive", contrib_c, "#d97706")]:
        w_s = current_savings
        for year in range(51):
            scenario_rows.append({'Age': current_age + year, 'Net Worth': w_s, 'Scenario': f"{label} (${contrib:,}/mo)", 'Color': clr})
            w_s = w_s * (1 + real_return) + contrib * 12

    s_df = pd.DataFrame(scenario_rows)

    s_chart = alt.Chart(s_df).mark_line(strokeWidth=2).encode(
        x=alt.X('Age:Q', title='Age'),
        y=alt.Y('Net Worth:Q', title='Portfolio Value', axis=alt.Axis(format='$~s', labelColor='#64748b', gridColor='#e2e8f0', domainColor='#e2e8f0')),
        color=alt.Color('Scenario:N', scale=alt.Scale(range=['#0284c7', '#10b981', '#d97706']),
                        legend=alt.Legend(labelColor='#64748b', titleColor='#475569')),
        tooltip=['Age:Q', 'Scenario:N', alt.Tooltip('Net Worth:Q', format='$,.0f')]
    )

    fire_rule = alt.Chart(pd.DataFrame({'y': [fire_number], 'label': [f'FIRE Target ${fire_number:,.0f}']})).mark_rule(
        strokeDash=[5, 4], color='#ef4444', strokeWidth=1.5
    ).encode(y='y:Q', tooltip=[alt.Tooltip('label:N')])

    fire_txt = alt.Chart(pd.DataFrame({'y': [fire_number], 't': [f'FIRE Target']})).mark_text(
        align='left', dx=6, dy=-8, color='#ef4444', fontSize=11, fontWeight=600
    ).encode(y='y:Q', x=alt.value(8), text='t:N')

    st.altair_chart(
        (s_chart + fire_rule + fire_txt).properties(height=380).configure_view(strokeOpacity=0).interactive(),
        use_container_width=True
    )

    st.markdown("##### Scenario Summary")
    summary = []
    for label, contrib in [("Conservative", contrib_a), ("Current", contrib_b), ("Aggressive", contrib_c)]:
        w_s = current_savings
        fa = None
        for year in range(51):
            if w_s >= fire_number and fa is None:
                fa = current_age + year
            w_s = w_s * (1 + real_return) + contrib * 12
        sr_s = round(contrib * 12 / annual_income * 100, 1) if annual_income > 0 else 0
        extra_savings = (contrib - monthly_contribution) * 12
        summary.append({
            "Scenario": label,
            "Monthly ($)": f"${contrib:,}",
            "Annual ($)": f"${contrib*12:,}",
            "Savings Rate": f"{sr_s}%",
            "vs. Current": f"+${extra_savings:,}/yr" if extra_savings >= 0 else f"-${abs(extra_savings):,}/yr",
            "FIRE Age": str(fa) if fa else "50+",
            "Years to FIRE": str(fa - current_age) if fa else "50+",
            "Portfolio @ FIRE": f"${w_s:,.0f}" if fa else "N/A",
        })

    st.dataframe(pd.DataFrame(summary), use_container_width=True, hide_index=True)

with tab4:
    st.markdown("##### FIRE Age — Real Return vs Safe Withdrawal Rate")
    st.markdown('<p style="color:#64748b;font-size:0.82rem;margin-bottom:1rem">Each cell shows the age at which you reach your FIRE number under that combination of real return and SWR.</p>', unsafe_allow_html=True)

    returns_grid = [0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10]
    swrs_grid = [0.025, 0.030, 0.035, 0.040, 0.045, 0.050, 0.055, 0.060]

    sens_rows = []
    for r in returns_grid:
        row = {"Real Return": f"{r*100:.0f}%"}
        for s in swrs_grid:
            fn = target_annual_expenses / s
            w_g = current_savings
            fa_g = None
            for year in range(51):
                if w_g >= fn and fa_g is None:
                    fa_g = current_age + year
                w_g = w_g * (1 + r) + monthly_contribution * 12
            row[f"{s*100:.1f}% SWR"] = str(fa_g) if fa_g else "50+"
        sens_rows.append(row)

    st.dataframe(pd.DataFrame(sens_rows).set_index("Real Return"), use_container_width=True)

    st.markdown("---")
    st.markdown("##### FIRE Age vs. Monthly Contribution")

    contrib_range = list(range(250, 5001, 250))
    contrib_sens = []
    for c in contrib_range:
        w_c = current_savings
        fa_c = None
        for year in range(51):
            if w_c >= fire_number and fa_c is None:
                fa_c = current_age + year
            w_c = w_c * (1 + real_return) + c * 12
        contrib_sens.append({
            'Monthly Contribution': c,
            'FIRE Age': fa_c if fa_c else current_age + 51,
            'Years to FIRE': (fa_c - current_age) if fa_c else 51
        })

    cs_df = pd.DataFrame(contrib_sens)

    contrib_line = alt.Chart(cs_df).mark_line(color='#10b981', strokeWidth=2).encode(
        x=alt.X('Monthly Contribution:Q', title='Monthly Contribution ($)', axis=alt.Axis(format='$,f', labelColor='#64748b', gridColor='#e2e8f0', domainColor='#e2e8f0')),
        y=alt.Y('FIRE Age:Q', title='Projected FIRE Age', axis=alt.Axis(labelColor='#64748b', gridColor='#e2e8f0', domainColor='#e2e8f0'),
                scale=alt.Scale(domain=[max(current_age, cs_df['FIRE Age'].min() - 2), current_age + 52])),
        tooltip=[alt.Tooltip('Monthly Contribution:Q', format='$,f'), alt.Tooltip('FIRE Age:Q'), alt.Tooltip('Years to FIRE:Q')]
    )

    you_pt = alt.Chart(pd.DataFrame({
        'x': [monthly_contribution],
        'y': [fire_age if fire_age else current_age + 51],
        'label': [f'You: ${monthly_contribution:,}/mo → Age {fire_age if fire_age else "50+"}']
    })).mark_point(color='#d97706', size=120, filled=True).encode(
        x='x:Q', y='y:Q', tooltip=[alt.Tooltip('label:N', title='Your Position')]
    )

    you_label = alt.Chart(pd.DataFrame({
        'x': [monthly_contribution],
        'y': [fire_age if fire_age else current_age + 51],
        'label': [f' Age {fire_age if fire_age else "50+"}']
    })).mark_text(align='left', dx=8, dy=-8, color='#d97706', fontSize=11, fontWeight=600).encode(
        x='x:Q', y='y:Q', text='label:N'
    )

    st.altair_chart(
        (contrib_line + you_pt + you_label).properties(height=320).configure_view(strokeOpacity=0).interactive(),
        use_container_width=True
    )

with tab5:
    st.markdown("##### Year-by-Year Wealth Projection")

    y1, y2 = st.columns(2)
    show_from = y1.number_input("From Year", min_value=0, max_value=49, value=0)
    show_to = y2.number_input("To Year", min_value=1, max_value=50, value=25)

    detailed = []
    w_d = current_savings
    for year in range(51):
        gain = w_d * real_return
        contrib_yr = monthly_contribution * 12
        detailed.append({
            'Year': year,
            'Age': current_age + year,
            'Net Worth': round(w_d),
            'Investment Gain': round(gain),
            'Contribution': round(contrib_yr),
            'Total Growth': round(gain + contrib_yr),
            'LeanFIRE %': f"{min(100, w_d / lean_fire_number * 100):.1f}%" if lean_fire_number > 0 else "N/A",
            'FIRE %': f"{min(100, w_d / fire_number * 100):.1f}%" if fire_number > 0 else "N/A",
            'FatFIRE %': f"{min(100, w_d / fat_fire_number * 100):.1f}%" if fat_fire_number > 0 else "N/A",
        })
        w_d = w_d * (1 + real_return) + monthly_contribution * 12

    detail_df = pd.DataFrame(detailed)
    filtered = detail_df[(detail_df['Year'] >= show_from) & (detail_df['Year'] <= show_to)].copy()
    for col in ['Net Worth', 'Investment Gain', 'Contribution', 'Total Growth']:
        filtered[col] = filtered[col].apply(lambda x: f"${x:,.0f}")

    st.dataframe(filtered, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.markdown("##### Contribution vs. Compounding Gains Over Time")

    gains_df = pd.DataFrame(detailed)
    g_melted = gains_df[['Age', 'Investment Gain', 'Contribution']].melt(id_vars=['Age'], var_name='Source', value_name='Amount')

    stack_chart = alt.Chart(g_melted).mark_bar(width=alt.RelativeBandSize(0.9)).encode(
        x=alt.X('Age:Q', title='Age', axis=alt.Axis(labelColor='#64748b', gridColor='#e2e8f0', domainColor='#e2e8f0')),
        y=alt.Y('Amount:Q', title='Annual Amount ($)', axis=alt.Axis(format='$~s', labelColor='#64748b', gridColor='#e2e8f0', domainColor='#e2e8f0')),
        color=alt.Color('Source:N', scale=alt.Scale(domain=['Contribution', 'Investment Gain'], range=['#3b82f6', '#10b981']),
                        legend=alt.Legend(labelColor='#64748b', titleColor='#475569')),
        tooltip=['Age:Q', 'Source:N', alt.Tooltip('Amount:Q', format='$,.0f')]
    ).properties(height=300).configure_view(strokeOpacity=0).interactive()

    st.altair_chart(stack_chart, use_container_width=True)
    st.caption("Watch compounding gains eventually eclipse your monthly contributions — that's financial independence building itself.")

st.markdown('<div style="height:1px;background:#e2e8f0;margin:2rem 0 1rem"></div>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center;color:#64748b;font-size:0.75rem">RetireCraft — For educational purposes only. Not financial advice. Consult a licensed financial planner for personalized guidance.</p>', unsafe_allow_html=True)