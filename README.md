# Python Foundry

A hub for small, self-contained Python projects built to explore programming fundamentals, algorithms, systems, networking, tooling and practical automation.

> Every project is independently runnable and intentionally focused.

## Project structure

```text
PythonFoundry/
├── index.html
├── style.css
├── script.js
├── Ideas.md
├── projects/
│   ├── _template/
│   │   ├── app.py
│   │   ├── index.html
│   │   └── style.css
│   └── ...
└── README.md
```

The hub automatically discovers project folders under `projects/`. `Ideas.md` is the backlog and source of truth for the Python project collection. fileciteturn6file0

## Add a project

1. Copy `projects/_template/` to a new folder.
2. Implement the project described in `Ideas.md`.
3. Keep the entry point as `app.py`.
4. Run `python app.py` from the project directory.
5. Push the folder to GitHub.

## Project rules

- One project = one folder.
- Prefer Python standard library modules.
- Add external dependencies only when the idea genuinely requires them.
- Keep each project independently runnable.
- Keep source code free of comments.
- Deployment is manual.
- No GitHub Actions are required.
