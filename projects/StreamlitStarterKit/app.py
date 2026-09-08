import streamlit as st
import pandas as pd
import altair as alt
import datetime
import json
import re
from collections import Counter

st.set_page_config(
    page_title="Python Dev Kit",
    page_icon="⚗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    .stButton > button { transition: all 0.2s ease-in-out; }
    .stButton > button:hover { transform: scale(1.02); }
    [data-testid="stMetricValue"] { font-size: 1.4rem; }
</style>
""", unsafe_allow_html=True)

_defaults = {
    "user_name": "Developer",
    "activity_log": [],
    "uploaded_df": None,
    "scratch_note": "",
    "transform_result": "",
    "json_result": "",
    "json_error": "",
    "session_start": datetime.datetime.now().strftime("%H:%M"),
    "visited_pages": set(),
}
for _k, _v in _defaults.items():
    if _k not in st.session_state:
        st.session_state[_k] = _v


def log(msg):
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    st.session_state.activity_log.insert(0, f"[{ts}] {msg}")
    st.session_state.activity_log = st.session_state.activity_log[:25]


with st.sidebar:
    st.title("⚗️ Dev Kit")
    page = st.radio(
        "Nav",
        ["Dashboard", "Data Lab", "Text Tools", "Utilities", "Settings"],
        label_visibility="collapsed"
    )
    st.session_state.visited_pages.add(page)

    st.divider()
    st.markdown("**Session**")
    st.caption(f"👤 {st.session_state.user_name}")
    st.caption(f"🕐 Started at {st.session_state.session_start}")
    st.caption(f"📅 {datetime.date.today().strftime('%b %d, %Y')}")
    st.caption("⚡ In-browser · WebAssembly")

    if st.session_state.activity_log:
        st.divider()
        st.markdown("**Recent Activity**")
        for entry in st.session_state.activity_log[:6]:
            st.caption(entry)


if page == "Dashboard":
    st.header(f"Welcome back, {st.session_state.user_name} 👋")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Pages Visited", len(st.session_state.visited_pages))
    c2.metric("Actions Logged", len(st.session_state.activity_log))
    c3.metric("Dataset Loaded", "Yes" if st.session_state.uploaded_df is not None else "No")
    c4.metric("Session Since", st.session_state.session_start)

    st.divider()

    left, right = st.columns([3, 2])

    with left:
        st.subheader("Scratch Pad")
        note = st.text_area(
            "note",
            value=st.session_state.scratch_note,
            height=180,
            label_visibility="collapsed",
            placeholder="Jot something down — persists across pages…",
        )
        if st.button("Save Note"):
            st.session_state.scratch_note = note
            log("Scratch pad saved")
            st.success("Saved!")

    with right:
        st.subheader("Activity Feed")
        if st.session_state.activity_log:
            for entry in st.session_state.activity_log[:10]:
                st.caption(entry)
        else:
            st.caption("No activity yet. Start exploring the pages!")


elif page == "Data Lab":
    st.header("Data Lab")
    st.markdown("Upload a CSV to profile, visualize, and filter your data.")

    uploaded = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
        st.session_state.uploaded_df = df
        log(f'Loaded "{uploaded.name}" — {df.shape[0]:,} rows × {df.shape[1]} cols')

    df = st.session_state.uploaded_df

    using_sample = df is None
    if using_sample:
        st.info("No file uploaded yet — showing a sample dataset as a placeholder.")
        df = pd.DataFrame({
            "Month": ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
            "Revenue": [15000,18000,22000,21000,25000,30000,28000,32000,35000,31000,38000,42000],
            "Expenses": [12000,13000,14000,13500,15000,18000,16000,19000,20000,18000,22000,25000],
            "Profit": [3000,5000,8000,7500,10000,12000,12000,13000,15000,13000,16000,17000],
        })

    tab_ov, tab_chart, tab_filter, tab_profile = st.tabs(
        ["📊 Overview", "📈 Chart Builder", "🔍 Filter & Search", "📋 Profile"]
    )

    with tab_ov:
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Rows", f"{df.shape[0]:,}")
        m2.metric("Columns", df.shape[1])
        m3.metric("Numeric Cols", len(df.select_dtypes(include="number").columns))
        m4.metric("Missing Values", int(df.isnull().sum().sum()))
        st.dataframe(df, use_container_width=True, hide_index=True)

    with tab_chart:
        numeric_cols = df.select_dtypes(include="number").columns.tolist()
        all_cols = df.columns.tolist()

        cc1, cc2, cc3, cc4 = st.columns(4)
        chart_type = cc1.selectbox("Chart Type", ["Bar", "Line", "Area", "Point", "Boxplot"])
        x_col = cc2.selectbox("X Axis", all_cols)
        y_col = cc3.selectbox("Y Axis", numeric_cols if numeric_cols else all_cols)
        color_col = cc4.selectbox("Color By", ["— none —"] + all_cols)

        x_dtype = "N" if df[x_col].dtype == object else "Q"
        encode = dict(
            x=alt.X(f"{x_col}:{x_dtype}"),
            y=alt.Y(f"{y_col}:Q"),
            tooltip=all_cols[:6],
        )
        if color_col != "— none —":
            encode["color"] = alt.Color(f"{color_col}:N")

        base = alt.Chart(df)
        if chart_type == "Bar":
            chart = base.mark_bar(cornerRadiusTopLeft=3, cornerRadiusTopRight=3).encode(**encode)
        elif chart_type == "Line":
            chart = base.mark_line(point=True).encode(**encode)
        elif chart_type == "Area":
            chart = base.mark_area(opacity=0.6).encode(**encode)
        elif chart_type == "Point":
            chart = base.mark_circle(size=80).encode(**encode)
        elif chart_type == "Boxplot":
            chart = base.mark_boxplot(extent="min-max").encode(**encode)

        st.altair_chart(chart.properties(height=420).interactive(), use_container_width=True)
        log(f"Chart — {chart_type}: {x_col} vs {y_col}")

    with tab_filter:
        filtered = df.copy()

        numeric_cols = df.select_dtypes(include="number").columns.tolist()
        text_cols = df.select_dtypes(include="object").columns.tolist()

        fa, fb = st.columns(2)
        with fa:
            if numeric_cols:
                filter_col = st.selectbox("Numeric Filter Column", numeric_cols)
                col_min = float(df[filter_col].min())
                col_max = float(df[filter_col].max())
                rng = st.slider(f"{filter_col} range", col_min, col_max, (col_min, col_max))
                filtered = filtered[
                    (filtered[filter_col] >= rng[0]) & (filtered[filter_col] <= rng[1])
                ]

        with fb:
            if text_cols:
                search_col = st.selectbox("Search Column", text_cols)
                term = st.text_input("Search Term")
                if term:
                    filtered = filtered[
                        filtered[search_col].astype(str).str.contains(term, case=False, na=False)
                    ]

        sort_col = st.selectbox("Sort By", ["— none —"] + df.columns.tolist())
        if sort_col != "— none —":
            asc = st.toggle("Ascending", value=True)
            filtered = filtered.sort_values(sort_col, ascending=asc)

        st.caption(f"Showing {len(filtered):,} of {len(df):,} rows")
        st.dataframe(filtered, use_container_width=True, hide_index=True)

    with tab_profile:
        numeric_df = df.select_dtypes(include="number")
        if not numeric_df.empty:
            desc = numeric_df.describe().T.round(2)
            desc["missing"] = df.isnull().sum()[numeric_df.columns].values
            desc["missing %"] = (desc["missing"] / len(df) * 100).round(1)
            st.dataframe(
                desc.style.background_gradient(subset=["mean", "std"], cmap="Blues"),
                use_container_width=True,
            )
        else:
            st.warning("No numeric columns to profile.")

        st.divider()
        st.markdown("**Column Types**")
        dtype_df = pd.DataFrame(
            {"Column": df.columns, "Type": df.dtypes.astype(str).values, "Non-Null": df.notnull().sum().values}
        )
        st.dataframe(dtype_df, use_container_width=True, hide_index=True)


elif page == "Text Tools":
    st.header("Text Tools")

    tab_analyze, tab_transform, tab_diff = st.tabs(["📝 Analyzer", "🔄 Transform", "🔀 Diff"])

    with tab_analyze:
        text = st.text_area("Text", height=200, label_visibility="collapsed", placeholder="Paste or type any text…")

        if text.strip():
            log("Text analyzed")
            words = re.findall(r"\b\w+\b", text.lower())
            sentences = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]
            paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

            m1, m2, m3, m4, m5 = st.columns(5)
            m1.metric("Characters", f"{len(text):,}")
            m2.metric("Words", f"{len(words):,}")
            m3.metric("Sentences", len(sentences))
            m4.metric("Paragraphs", len(paragraphs))
            m5.metric("Avg Word Len", f"{sum(len(w) for w in words)/max(len(words),1):.1f}")

            st.divider()

            stopwords = {
                "the","a","an","and","or","but","in","on","at","to","for","of","with",
                "is","it","this","that","are","was","be","as","by","from","not","have",
                "has","had","he","she","they","we","you","i","do","did","will","would",
                "could","should","may","might","can","their","there","then","than","so",
                "if","about","which","who","when","what","how","its","our","your","my",
                "his","her","all","been","were","more","just","some","any","no","up",
            }
            word_counts = Counter(w for w in words if w not in stopwords and len(w) > 2)
            top_words = word_counts.most_common(20)

            if top_words:
                freq_df = pd.DataFrame(top_words, columns=["Word", "Count"])
                chart = (
                    alt.Chart(freq_df)
                    .mark_bar(cornerRadiusTopLeft=3, cornerRadiusTopRight=3, color="#6366f1")
                    .encode(
                        x=alt.X("Count:Q", title="Frequency"),
                        y=alt.Y("Word:N", sort="-x", title=None),
                        tooltip=["Word", "Count"],
                    )
                    .properties(height=min(400, len(top_words) * 22))
                )
                st.altair_chart(chart, use_container_width=True)

    with tab_transform:
        input_text = st.text_area("Input", height=160, label_visibility="collapsed", placeholder="Enter text to transform…")
        transforms = [
            "UPPERCASE", "lowercase", "Title Case", "Sentence case",
            "Reverse Words", "Reverse Characters", "Remove Extra Spaces",
            "Strip Punctuation", "Extract Numbers", "Extract Emails",
        ]
        tc1, tc2 = st.columns([3, 1])
        transform = tc1.selectbox("Transform", transforms)

        if tc2.button("Apply", use_container_width=True) and input_text:
            if transform == "UPPERCASE":
                res = input_text.upper()
            elif transform == "lowercase":
                res = input_text.lower()
            elif transform == "Title Case":
                res = input_text.title()
            elif transform == "Sentence case":
                res = input_text.capitalize()
            elif transform == "Reverse Words":
                res = " ".join(input_text.split()[::-1])
            elif transform == "Reverse Characters":
                res = input_text[::-1]
            elif transform == "Remove Extra Spaces":
                res = re.sub(r"\s+", " ", input_text).strip()
            elif transform == "Strip Punctuation":
                res = re.sub(r"[^\w\s]", "", input_text)
            elif transform == "Extract Numbers":
                nums = re.findall(r"-?\d+\.?\d*", input_text)
                res = "\n".join(nums) if nums else "(no numbers found)"
            elif transform == "Extract Emails":
                emails = re.findall(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}", input_text)
                res = "\n".join(emails) if emails else "(no emails found)"

            st.session_state.transform_result = res
            log(f"Transform: {transform}")

        if st.session_state.transform_result:
            st.text_area("Result", value=st.session_state.transform_result, height=160, label_visibility="collapsed")
            rc1, rc2 = st.columns(2)
            rc1.metric("Input length", len(input_text))
            rc2.metric("Output length", len(st.session_state.transform_result))

    with tab_diff:
        st.markdown("Compare two blocks of text line-by-line.")
        da, db = st.columns(2)
        text_a = da.text_area("Text A", height=200, label_visibility="collapsed", placeholder="Original text…")
        text_b = db.text_area("Text B", height=200, label_visibility="collapsed", placeholder="Modified text…")

        if st.button("Compare") and text_a and text_b:
            log("Diff run")
            lines_a = set(text_a.splitlines())
            lines_b = set(text_b.splitlines())
            only_a = sorted(lines_a - lines_b)
            only_b = sorted(lines_b - lines_a)
            shared = sorted(lines_a & lines_b)

            dm1, dm2, dm3 = st.columns(3)
            dm1.metric("Only in A", len(only_a))
            dm2.metric("Only in B", len(only_b))
            dm3.metric("Shared", len(shared))

            if only_a:
                st.markdown("**Lines only in A**")
                for l in only_a:
                    st.markdown(f"<span style='color:#ef4444'>— {l}</span>", unsafe_allow_html=True)
            if only_b:
                st.markdown("**Lines only in B**")
                for l in only_b:
                    st.markdown(f"<span style='color:#22c55e'>+ {l}</span>", unsafe_allow_html=True)


elif page == "Utilities":
    st.header("Utilities")

    tab_unit, tab_date, tab_json = st.tabs(["📐 Unit Converter", "📅 Date Tools", "🔧 JSON"])

    with tab_unit:
        category = st.selectbox("Category", ["Length", "Weight", "Temperature", "Data Size", "Speed"])

        if category == "Length":
            units = {"Meters": 1, "Kilometers": 1000, "Miles": 1609.344, "Feet": 0.3048, "Inches": 0.0254, "Centimeters": 0.01, "Millimeters": 0.001, "Nautical Miles": 1852}
        elif category == "Weight":
            units = {"Kilograms": 1, "Grams": 0.001, "Pounds": 0.453592, "Ounces": 0.0283495, "Tonnes": 1000, "Stone": 6.35029}
        elif category == "Temperature":
            units = {"Celsius": "C", "Fahrenheit": "F", "Kelvin": "K"}
        elif category == "Data Size":
            units = {"Bytes": 1, "Kilobytes": 1024, "Megabytes": 1048576, "Gigabytes": 1073741824, "Terabytes": 1099511627776, "Petabytes": 1125899906842624}
        elif category == "Speed":
            units = {"m/s": 1, "km/h": 0.277778, "mph": 0.44704, "knots": 0.514444, "ft/s": 0.3048}

        uc1, uc2, uc3 = st.columns([2, 1, 2])
        with uc1:
            from_unit = st.selectbox("From", list(units.keys()), key="from_u")
            value = st.number_input("Value", value=1.0, format="%.6g", key="conv_val")
        with uc2:
            st.markdown("<br><br><div style='text-align:center;font-size:1.8rem;opacity:.5'>⇒</div>", unsafe_allow_html=True)
        with uc3:
            to_unit = st.selectbox("To", list(units.keys()), key="to_u")

            if category == "Temperature":
                def to_celsius(v, u):
                    if u == "Celsius": return v
                    if u == "Fahrenheit": return (v - 32) * 5 / 9
                    return v - 273.15

                def from_celsius(c, u):
                    if u == "Celsius": return c
                    if u == "Fahrenheit": return c * 9 / 5 + 32
                    return c + 273.15

                result = from_celsius(to_celsius(value, from_unit), to_unit)
            else:
                result = value * units[from_unit] / units[to_unit]

            st.metric(f"Result ({to_unit})", f"{result:,.8g}")

        if from_unit != to_unit:
            log(f"Converted {value} {from_unit} → {to_unit}")

    with tab_date:
        da, db = st.columns(2)

        with da:
            st.subheader("Date Difference")
            d1 = st.date_input("Start", value=datetime.date.today() - datetime.timedelta(days=30), key="d1")
            d2 = st.date_input("End", value=datetime.date.today(), key="d2")
            if d2 >= d1:
                diff = d2 - d1
                dm1, dm2, dm3 = st.columns(3)
                dm1.metric("Days", f"{diff.days:,}")
                dm2.metric("Weeks", f"{diff.days / 7:.2f}")
                dm3.metric("Months", f"{diff.days / 30.4375:.2f}")
                st.caption(f"Business days (approx): {max(0, diff.days - (diff.days // 7) * 2):,}")
            else:
                st.error("End must be after start date.")

        with db:
            st.subheader("Add / Subtract")
            base = st.date_input("Base Date", value=datetime.date.today(), key="base_d")
            delta = st.number_input("Days (negative to go back)", value=30, step=1, key="delta_d")
            result_date = base + datetime.timedelta(days=int(delta))
            st.metric("Result", result_date.strftime("%B %d, %Y"))
            st.caption(f"Day of week: **{result_date.strftime('%A')}**")
            st.caption(f"ISO week: {result_date.isocalendar()[1]}  ·  Day of year: {result_date.timetuple().tm_yday}")
            st.caption(f"Unix timestamp: {int(datetime.datetime.combine(result_date, datetime.time()).timestamp()):,}")

    with tab_json:
        json_input = st.text_area("JSON Input", height=220, label_visibility="collapsed", placeholder='{ "key": "value" }')

        jc1, jc2, jc3 = st.columns(3)
        run_format = jc1.button("Format / Validate", use_container_width=True)
        run_minify = jc2.button("Minify", use_container_width=True)
        run_keys = jc3.button("List Top-Level Keys", use_container_width=True)

        if (run_format or run_minify or run_keys) and json_input:
            try:
                parsed = json.loads(json_input)
                st.session_state.json_error = ""
                if run_format:
                    st.session_state.json_result = json.dumps(parsed, indent=2, ensure_ascii=False)
                    log("JSON formatted")
                elif run_minify:
                    st.session_state.json_result = json.dumps(parsed, separators=(",", ":"), ensure_ascii=False)
                    log("JSON minified")
                elif run_keys:
                    if isinstance(parsed, dict):
                        st.session_state.json_result = "\n".join(parsed.keys())
                    elif isinstance(parsed, list):
                        st.session_state.json_result = f"Array with {len(parsed)} item(s)"
                    log("JSON keys listed")
            except json.JSONDecodeError as e:
                st.session_state.json_error = str(e)

        if st.session_state.json_error:
            st.error(f"Invalid JSON: {st.session_state.json_error}")
        elif st.session_state.json_result:
            st.code(st.session_state.json_result, language="json")
            jm1, jm2 = st.columns(2)
            jm1.metric("Input chars", f"{len(json_input):,}")
            jm2.metric("Output chars", f"{len(st.session_state.json_result):,}")


elif page == "Settings":
    st.header("Settings")

    st.subheader("Profile")
    new_name = st.text_input("Display Name", value=st.session_state.user_name)
    if st.button("Save Profile"):
        st.session_state.user_name = new_name
        log("Profile updated")
        st.success("Profile saved!")

    st.divider()

    st.subheader("Preferences")
    pc1, pc2 = st.columns(2)
    with pc1:
        st.toggle("Compact Mode", key="compact_mode")
        st.toggle("Enable Experimental Features", key="exp_features")
        st.toggle("Show Activity in Sidebar", key="show_activity", value=True)
    with pc2:
        st.selectbox("Default Chart Type", ["Bar", "Line", "Area", "Point"], key="default_chart")
        st.selectbox("Date Format", ["MMM DD, YYYY", "DD/MM/YYYY", "YYYY-MM-DD"], key="date_format")
        st.selectbox("Number Format", ["Comma (1,000)", "Dot (1.000)", "Plain (1000)"], key="num_format")

    st.divider()

    st.subheader("Session Management")
    sm1, sm2 = st.columns(2)
    with sm1:
        if st.button("Clear Activity Log", use_container_width=True):
            st.session_state.activity_log = []
            st.success("Activity log cleared.")
    with sm2:
        if st.button("Clear Uploaded Dataset", use_container_width=True):
            st.session_state.uploaded_df = None
            log("Dataset cleared")
            st.success("Dataset cleared.")