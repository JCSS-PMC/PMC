/* Keep the PMC theme styling while offering only explicit light/dark choices. */
(() => {
  const root = document.documentElement;
  let storedMode;
  try {
    storedMode = localStorage.getItem('mode');
  } catch {
    // The switch remains usable when the browser does not permit storage.
  }
  const initialMode = storedMode === 'light' || storedMode === 'dark' ? storedMode
    : (root.dataset.theme === 'dark' ? 'dark' : 'light');

  function setMode(mode) {
    root.dataset.mode = mode;
    root.dataset.theme = mode;
    try {
      localStorage.setItem('mode', mode);
      localStorage.setItem('theme', mode);
    } catch {
      // Apply the choice for this page even if it cannot be remembered.
    }
    // The installed PMC theme uses Bootstrap's separate dropdown colour class.
    document.querySelectorAll('.dropdown-menu').forEach(menu => {
      menu.classList.toggle('dropdown-menu-dark', mode === 'dark');
    });
    const nextMode = mode === 'dark' ? 'light' : 'dark';
    document.querySelectorAll('.pmc-theme-switch').forEach(button => {
      const label = `Switch to ${nextMode} mode`;
      button.setAttribute('aria-label', label);
      button.title = label;
      button.querySelectorAll('[data-pmc-theme-icon]').forEach(icon => {
        // Font Awesome replaces <i> with SVG, whose hidden property differs.
        icon.toggleAttribute('hidden', icon.dataset.pmcThemeIcon !== nextMode);
      });
    });
  }

  setMode(initialMode);
  document.addEventListener('DOMContentLoaded', () => {
    setMode(root.dataset.mode === 'dark' ? 'dark' : 'light');
    document.querySelectorAll('.pmc-theme-switch').forEach(button => {
      button.addEventListener('click', () => {
        setMode(root.dataset.mode === 'dark' ? 'light' : 'dark');
      });
    });
  });
})();
