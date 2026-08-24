const projects = [
  {
    name: "Number Guessing Game",
    path: "projects/number-guessing-game/app.py"
  }
];

const container = document.getElementById("projects");

projects.forEach((project) => {
  const card = document.createElement("a");
  card.className = "project";
  card.href = project.path;
  card.textContent = project.name;
  card.target = "_blank";
  container.appendChild(card);
});
