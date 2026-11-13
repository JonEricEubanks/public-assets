(() => {
  const button = document.querySelector("#casebook-motion");
  if (!button) return;
  const preference = window.matchMedia("(prefers-reduced-motion: reduce)");
  let paused = false;

  function update() {
    const reduced = preference.matches;
    document.documentElement.dataset.motion = reduced || paused ? "off" : "on";
    button.hidden = false;
    button.disabled = reduced;
    button.textContent = reduced
      ? "Motion off (system preference)"
      : paused ? "Play animation" : "Show stills";
  }

  button.addEventListener("click", () => {
    paused = !paused;
    update();
  });
  preference.addEventListener("change", update);
  update();

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      entry.target.dataset.paused = String(!entry.isIntersecting);
    });
  }, { rootMargin: "100px" });
  document.querySelectorAll(".casebook-scene").forEach(scene => observer.observe(scene));
})();
