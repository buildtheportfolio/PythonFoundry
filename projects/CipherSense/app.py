import secrets
import string
from pathlib import Path

import streamlit as st

from ciphersense import analyze_password, format_duration


st.set_page_config(
    page_title="CipherSense — Password Security Analyzer",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="collapsed",
)

try:
    st.markdown(f"<style>{Path('theme.css').read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)
except OSError:
    pass

if "password_value" not in st.session_state:
    st.session_state["password_value"] = ""

st.markdown(
    """
    <section class="cs-hero">
      <div class="cs-eyebrow">Password security analyzer</div>
      <h1>CipherSense</h1>
      <p>Analyze password length, character space, entropy, predictable patterns, and practical security signals with a transparent Python model.</p>
    </section>
    <div class="cs-notice">Local analysis only. Password values are processed by the application and are not intentionally stored or transmitted.</div>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("### Analysis settings")
    guesses_rate = st.number_input(
        "Theoretical guesses / second",
        min_value=1_000.0,
        max_value=1_000_000_000_000_000.0,
        value=10_000_000_000.0,
        step=1_000_000_000.0,
        format="%.0f",
        help="Used only for the theoretical search-space estimate.",
    )

st.markdown('<div class="cs-section-label">01 / Analyze</div><h2 class="cs-section-title">Password assessment</h2>', unsafe_allow_html=True)
show_password = st.checkbox("Show password")
password = st.text_input(
    "Password",
    value=st.session_state["password_value"],
    type="default" if show_password else "password",
    placeholder="Enter a password or passphrase",
    label_visibility="collapsed",
)
st.session_state["password_value"] = password

left_action, right_action = st.columns(2)
with left_action:
    generate_clicked = st.button("Generate strong password", use_container_width=True)
with right_action:
    clear_clicked = st.button("Clear", use_container_width=True)

if generate_clicked:
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}?"
    st.session_state["password_value"] = "".join(secrets.choice(alphabet) for _ in range(20))
    st.rerun()

if clear_clicked:
    st.session_state["password_value"] = ""
    st.rerun()

if not password:
    st.info("Enter a password above to start the analysis.")
else:
    result = analyze_password(password, guesses_per_second=guesses_rate)

    st.markdown('<div class="cs-section-label">02 / Results</div><h2 class="cs-section-title">Security assessment</h2>', unsafe_allow_html=True)
    metrics = st.columns(4)
    metrics[0].metric("Length", result.length)
    metrics[1].metric("Character pool", result.pool_size)
    metrics[2].metric("Raw entropy", f"{result.entropy_bits:.1f} bits")
    metrics[3].metric("Effective entropy", f"{result.effective_entropy_bits:.1f} bits")

    if result.strength == "Very strong":
        st.success(f"**{result.strength}** · score {result.score}/100")
    elif result.strength == "Strong":
        st.info(f"**{result.strength}** · score {result.score}/100")
    elif result.strength == "Fair":
        st.warning(f"**{result.strength}** · score {result.score}/100")
    else:
        st.error(f"**{result.strength}** · score {result.score}/100")
    st.progress(result.score / 100)

    flags = []
    if result.common_password:
        flags.append("Common password")
    if result.repeated_pattern:
        flags.append("Repeated pattern")
    if result.sequence_pattern:
        flags.append("Sequence")
    if result.keyboard_pattern:
        flags.append("Keyboard pattern")
    if flags:
        st.markdown("".join(f'<span class="cs-flag">{flag}</span>' for flag in flags), unsafe_allow_html=True)
    else:
        st.markdown('<span class="cs-flag cs-flag-good">No obvious simple pattern detected</span>', unsafe_allow_html=True)

    result_left, result_right = st.columns(2)
    with result_left:
        st.markdown('<div class="cs-card"><h3>Theoretical search-space estimate</h3>', unsafe_allow_html=True)
        st.markdown(f'<p>{format_duration(result.theoretical_seconds)}</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with result_right:
        checks = {
            "Lowercase": any(char.islower() for char in password),
            "Uppercase": any(char.isupper() for char in password),
            "Digits": any(char.isdigit() for char in password),
            "Symbols": any(not char.isalnum() for char in password),
            "12+ characters": len(password) >= 12,
            "16+ characters": len(password) >= 16,
        }
        st.markdown('<div class="cs-card"><h3>Composition</h3>', unsafe_allow_html=True)
        for label, passed in checks.items():
            st.markdown(f'<div class="cs-check">{"✓" if passed else "·"} {label}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="cs-section-label">03 / Guidance</div><h2 class="cs-section-title">Recommendations</h2>', unsafe_allow_html=True)
    for recommendation in result.recommendations:
        st.write(f"• {recommendation}")

st.markdown('<div class="cs-section-label">04 / Generate</div><h2 class="cs-section-title">Secure password generator</h2>', unsafe_allow_html=True)
gen_length = st.number_input("Generated length", min_value=12, max_value=64, value=20, step=1)
if st.button("Generate password", use_container_width=True):
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}?"
    generated = "".join(secrets.choice(alphabet) for _ in range(int(gen_length)))
    st.code(generated, language="text")
    st.caption("Generated locally with Python's secrets module.")

st.divider()
st.markdown(
    '<p class="cs-footnote">CipherSense uses a transparent entropy model. It does not account for leaked-password databases, target-specific information, credential stuffing, or every modern password-cracking strategy.</p>',
    unsafe_allow_html=True,
)
