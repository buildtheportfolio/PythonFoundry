import re
from datetime import datetime

import streamlit as st

st.set_page_config(page_title="ReadmeForge", page_icon="📝", layout="wide")

LICENSES = {
    "MIT": "MIT",
    "Apache 2.0": "Apache License 2.0",
    "GPLv3": "GNU General Public License v3.0",
    "BSD 3-Clause": "BSD 3-Clause License",
    "None": "None",
}

TEMPLATES = {
    "Python Package": {
        "description": "A Python package that solves a useful problem for developers.",
        "installation": "python -m pip install your-package",
        "usage": "from your_package import main\nmain()",
        "features": "Easy to install\nPython-first API\nTested and documented",
    },
    "CLI Tool": {
        "description": "A command-line tool for automating a developer workflow.",
        "installation": "git clone https://github.com/you/project.git\ncd project\npython -m pip install -r requirements.txt",
        "usage": "python -m your_tool --help\npython -m your_tool run",
        "features": "Simple CLI\nConfigurable workflows\nUseful terminal output",
    },
    "Web App": {
        "description": "A web application built to provide a focused, maintainable user experience.",
        "installation": "git clone https://github.com/you/project.git\ncd project\npython -m pip install -r requirements.txt",
        "usage": "streamlit run app.py",
        "features": "Interactive interface\nResponsive workflow\nEasy local development",
    },
    "Minimal": {
        "description": "A concise open source project description.",
        "installation": "python -m pip install -r requirements.txt",
        "usage": "python main.py",
        "features": "Lightweight\nOpen source\nEasy to use",
    },
}


def clean_heading(value):
    value = re.sub(r"[^A-Za-z0-9 _-]", "", value).strip()
    return value or "Project"


def clean_text(value):
    return value.strip()


def lines_to_bullets(value):
    items = [line.strip() for line in value.splitlines() if line.strip()]
    return "\n".join(f"- {item}" for item in items)


def badge(label, value, color="blue"):
    return f"![{label}](https://img.shields.io/badge/{label}-{value}-{color})"


def build_readme(data):
    project_name = clean_heading(data["project_name"])
    description = clean_text(data["description"])
    parts = [f"# {project_name}", "", description]

    if data["badges"]:
        parts.extend(["", " ".join(data["badges"])])

    if data["toc"]:
        parts.extend(["", "## Table of Contents", "", "- [Features](#features)", "- [Installation](#installation)", "- [Usage](#usage)"])
        if data["contributing"]:
            parts.append("- [Contributing](#contributing)")
        parts.extend(["- [License](#license)"])

    if data["features"]:
        parts.extend(["", "## Features", "", lines_to_bullets(data["features"])])

    parts.extend(["", "## Installation", "", "```bash", clean_text(data["installation"]), "```"])
    parts.extend(["", "## Usage", "", "```python", clean_text(data["usage"]), "```"])

    if data["configuration"]:
        parts.extend(["", "## Configuration", "", clean_text(data["configuration"])])

    if data["contributing"]:
        parts.extend(["", "## Contributing", "", clean_text(data["contributing"])])

    if data["roadmap"]:
        parts.extend(["", "## Roadmap", "", lines_to_bullets(data["roadmap"])])

    if data["author"]:
        parts.extend(["", "## Author", "", f"**{clean_text(data['author'])}**"])

    license_name = LICENSES[data["license"]]
    parts.extend(["", "## License"])
    if license_name == "None":
        parts.append("This project does not currently specify a license.")
    else:
        parts.append(f"Distributed under the {license_name}.")

    return "\n".join(parts).rstrip() + "\n"


st.title("📝 ReadmeForge")
st.caption("Build polished, repository-ready README files without leaving Python.")

if "template" not in st.session_state:
    st.session_state.template = "Python Package"

with st.sidebar:
    st.header("Project setup")
    template = st.selectbox("Template", list(TEMPLATES), index=list(TEMPLATES).index(st.session_state.template))
    st.session_state.template = template
    preset = TEMPLATES[template]
    apply_template = st.button("Apply template", use_container_width=True)
    st.divider()
    show_preview = st.toggle("Live preview", True)
    st.toggle("Table of contents", True, key="toc")

if apply_template:
    st.session_state.description = preset["description"]
    st.session_state.installation = preset["installation"]
    st.session_state.usage = preset["usage"]
    st.session_state.features = preset["features"]
    st.rerun()

left, right = st.columns([1, 1], gap="large")

with left:
    st.subheader("Project details")
    project_name = st.text_input("Project name", "My Awesome Project", key="project_name")
    description = st.text_area("Description", preset["description"], height=110, key="description")

    st.subheader("Badges")
    badge_options = st.multiselect("Add badges", ["Build", "Python", "License", "Version", "Stars"], default=["Python", "License"])
    badges = []
    for item in badge_options:
        if item == "Build":
            badges.append(badge("build", "passing", "brightgreen"))
        elif item == "Python":
            badges.append(badge("python", "3.10%2B", "blue"))
        elif item == "License":
            badges.append(badge("license", LICENSES[st.selectbox("License badge", list(LICENSES), key="license_badge")].replace(" ", "%20"), "green"))
        elif item == "Version":
            badges.append(badge("version", "v1.0.0", "blue"))
        elif item == "Stars":
            badges.append(badge("stars", "github", "yellow"))

    st.subheader("Project content")
    features = st.text_area("Features", preset["features"], height=120, key="features")
    installation = st.text_area("Installation commands", preset["installation"], height=120, key="installation")
    usage = st.text_area("Usage code", preset["usage"], height=140, key="usage")
    configuration = st.text_area("Configuration", "Add environment variables, configuration files, or runtime options here.", height=100)

with right:
    st.subheader("Optional sections")
    contributing_enabled = st.checkbox("Include contributing guide", True)
    contributing = st.text_area("Contributing", "Fork the repository, create a feature branch, make your changes, and open a pull request.", height=100, disabled=not contributing_enabled)
    roadmap = st.text_area("Roadmap", "Add automated tests\nPublish releases\nImprove documentation", height=100)
    author = st.text_input("Author", "")
    license_type = st.selectbox("License", list(LICENSES), index=0)

    data = {
        "project_name": project_name,
        "description": description,
        "badges": badges,
        "toc": st.session_state.toc,
        "features": features,
        "installation": installation,
        "usage": usage,
        "configuration": configuration,
        "contributing": contributing if contributing_enabled else "",
        "roadmap": roadmap,
        "author": author,
        "license": license_type,
    }
    markdown_content = build_readme(data)

    if show_preview:
        st.subheader("Live preview")
        st.markdown(markdown_content)

st.divider()
st.subheader("Export")
export_name = f"{clean_heading(project_name).lower().replace(' ', '-')}-README.md"
st.download_button("Download README.md", markdown_content, file_name=export_name, mime="text/markdown", use_container_width=True)
st.text_area("Raw Markdown", markdown_content, height=420)
st.caption(f"Generated {datetime.now().strftime('%Y-%m-%d %H:%M')}")
