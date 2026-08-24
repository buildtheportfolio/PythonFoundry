# PythonFoundry

A collection of small, practical Python applications built with a simple `app.py` entry point and minimal styling.

## Structure

Each application should live in its own directory under `projects/`.

```text
PythonFoundry/
├── index.html
├── script.js
├── style.css
└── projects/
    └── _template/
        ├── app.py
        ├── index.html
        └── style.css
```

## Project Convention

Each project should be intentionally small and self-contained.

- `app.py` — Python application entry point
- `index.html` — minimal interface when a browser UI is appropriate
- `style.css` — minimal styling
- Avoid unnecessary frameworks and dependencies
- Keep each project easy to understand and run independently

## Adding a Project

Create a new directory under `projects/` and use `_template` as the starting structure.

## Philosophy

PythonFoundry is the Python counterpart to VanillaJsFoundry: a simple home for small, focused projects and experiments.
