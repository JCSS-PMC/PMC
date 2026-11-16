/* Close mobile navigation after following a link and focus the destination. */
document.addEventListener('DOMContentLoaded', () => {
  // The base theme binds the first button for each sidebar; the book header
  // adds another. Reuse the theme's drawer and desktop-collapse behaviour.
  for (const selector of ['.primary-toggle', '.secondary-toggle']) {
    const buttons = [...document.querySelectorAll(selector)];
    const drawerButton = buttons[0];
    for (const headerButton of buttons.slice(1)) {
      headerButton.addEventListener('click', () => drawerButton.click());
    }
  }

  for (const id of ['pst-primary-sidebar-modal', 'pst-secondary-sidebar-modal']) {
    const dialog = document.getElementById(id);
    if (!dialog) continue;
    dialog.addEventListener('click', event => {
      const link = event.target.closest('a[href]');
      if (!dialog.open || !link || event.button !== 0 || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      const destination = new URL(link.href, location.href);
      if (destination.origin !== location.origin) return;
      const samePage = destination.pathname === location.pathname && destination.search === location.search;
      const section = samePage && destination.hash
        ? document.getElementById(decodeURIComponent(destination.hash.slice(1))) : null;
      if (section) {
        // The theme restores focus to its opener when the dialog closes. Move
        // it to the chosen heading afterwards, keeping keyboard reading order.
        dialog.addEventListener('close', () => requestAnimationFrame(() => {
          const target = section.querySelector('h1,h2,h3,h4,h5,h6') || section;
          target.setAttribute('tabindex', '-1');
          target.focus({ preventScroll: true });
        }), { once: true });
      }
      dialog.close();
    });
  }
});
