# Python Foundry

A hub for small, self-contained Python projects covering scripting, automation, data, backend development, AI and practical engineering.

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
│   ├── number-guessing-game/
│   │   └── app.py
│   └── ...
└── README.md
```

The hub automatically discovers project folders under `projects/`. A directory is included in the project catalog only when it contains an `app.py`; `_template` is always excluded.

## Add a project

1. Copy `projects/_template/` to a new folder.
2. Implement the project from `Ideas.md`.
3. Run the project from its directory using the documented Python entry point.
4. Push the folder to GitHub.
5. The project is automatically discovered by the hub without editing a registry.

## Project rules

- One project = one folder.
- Each project has a clear Python entry point.
- Keep dependencies minimal and project-specific.
- Keep projects independently runnable.
- Keep source code free of comments.
- Deployment is manual.
- No GitHub Actions are required.
