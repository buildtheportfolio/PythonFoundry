# CipherSense

CipherSense is a browser-first password security analyzer built with Python and Streamlit. The GitHub Pages build uses Stlite so the Streamlit application and analysis logic execute client-side; no application server is required.

## Features

- Transparent character-pool and entropy calculation
- Effective-entropy adjustment for common passwords, repetition, sequences, and keyboard patterns
- Strength score and security classification
- Theoretical search-space estimate with a configurable guesses-per-second model
- Composition checks and actionable recommendations
- Strong-password generation using Python's `secrets` module
- No password persistence or server-side submission in the GitHub Pages build
- Pure Python analysis module with unit tests

## Run locally

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```

## Run tests

```bash
python -m unittest -v
```

## GitHub Pages deployment

The repository contains a static `index.html` that mounts the Python application with Stlite. GitHub Pages can therefore serve the project as a static site while Python executes in the browser through WebAssembly.

The browser runtime is pinned instead of using `@latest`, and `index.html` explicitly mounts both `app.py` and `ciphersense.py`.

Enable **Settings → Pages → Source → GitHub Actions**, then push to `main`. The included workflow under `.github/workflows/pages.yml` builds and deploys the site.

## Important security note

CipherSense provides a transparent educational estimator. Entropy-based estimates assume the password was generated uniformly from the modeled character pool and do not reproduce real attacker behavior. Real compromise can be much faster when passwords are leaked, reused, predictable, targeted, or attacked through credential stuffing and password dictionaries.
