/**
 * Portal Kabupaten Bandung Barat — script.js
 * Vanilla ES6, no external dependencies.
 */

document.addEventListener('DOMContentLoaded', () => {

  // ─────────────────────────────────────────────────────────────
  // 1. MOBILE SIDEBAR TOGGLE
  // ─────────────────────────────────────────────────────────────

  const menuToggle = document.getElementById('menuToggle');
  const sidebar    = document.getElementById('sidebar');
  const shell      = document.querySelector('.shell');

  if (menuToggle && sidebar) {
    // Open / close sidebar when the hamburger button is clicked
    menuToggle.addEventListener('click', (e) => {
      e.stopPropagation();
      const isOpen = sidebar.classList.toggle('open');
      menuToggle.setAttribute('aria-label', isOpen ? 'Tutup menu' : 'Buka menu');
      menuToggle.innerHTML = isOpen ? '&times;' : '&#9776;';
    });

    // Close sidebar when clicking anywhere outside of it (on the shell overlay)
    document.addEventListener('click', (e) => {
      if (
        sidebar.classList.contains('open') &&
        !sidebar.contains(e.target) &&
        e.target !== menuToggle
      ) {
        sidebar.classList.remove('open');
        menuToggle.setAttribute('aria-label', 'Buka menu');
        menuToggle.innerHTML = '&#9776;';
      }
    });
  }


  // ─────────────────────────────────────────────────────────────
  // 2. SIDEBAR SUBMENU ACCORDION
  // ─────────────────────────────────────────────────────────────

  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const submenuTriggers = document.querySelectorAll('.has-submenu > .nav-parent');

  submenuTriggers.forEach((trigger) => {
    const item = trigger.closest('.has-submenu');
    if (!item) return;

    const targetHref = trigger.getAttribute('href');
    const linkPage = targetHref ? targetHref.split('/').pop() : '';
    const isCurrentPage = !!(linkPage && linkPage !== '#' && linkPage === currentPath);

    trigger.addEventListener('click', (e) => {
      const shouldToggle = !targetHref || targetHref === '#' || isCurrentPage;

      if (shouldToggle) {
        e.preventDefault();

        const isAlreadyOpen = item.classList.contains('submenu-open');
        const siblingSubmenus = item.parentElement.querySelectorAll(':scope > .has-submenu');

        // Close only sibling submenus at the same nesting level.
        siblingSubmenus.forEach((other) => {
          if (other !== item) {
            other.classList.remove('submenu-open');
          }
        });

        // Toggle the clicked item.
        item.classList.toggle('submenu-open', !isAlreadyOpen);
      }
    });
  });


  // ─────────────────────────────────────────────────────────────
  // 3. TOPNAV DROPDOWN
  // ─────────────────────────────────────────────────────────────

  const topnavItems = document.querySelectorAll('.topnav-item');

  topnavItems.forEach((item) => {
    const dropdown = item.querySelector('.tn-dropdown');
    const trigger  = item.querySelector('a.has-tn-dropdown');

    if (!dropdown || !trigger) return; // No dropdown — skip

    // Toggle this item's dropdown on click
    trigger.addEventListener('click', (e) => {
      e.preventDefault(); // Don't follow href="#" for parent links

      const isAlreadyOpen = item.classList.contains('tn-open');

      // Close all other open topnav dropdowns (exclusive)
      topnavItems.forEach((other) => {
        if (other !== item) {
          other.classList.remove('tn-open');
        }
      });

      // Toggle the clicked item
      item.classList.toggle('tn-open', !isAlreadyOpen);
    });
  });

  // Close all topnav dropdowns when clicking anywhere outside the topnav
  document.addEventListener('click', (e) => {
    const topnav = document.querySelector('.topnav');
    if (topnav && !topnav.contains(e.target)) {
      topnavItems.forEach((item) => item.classList.remove('tn-open'));
    }
  });

  // Close topnav dropdowns when pressing Escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      topnavItems.forEach((item) => item.classList.remove('tn-open'));
    }
  });


  // ─────────────────────────────────────────────────────────────
  // 4. ACTIVE NAV HIGHLIGHT
  // ─────────────────────────────────────────────────────────────

  /**
   * Match the current page URL against sidebar and topnav link hrefs.
   * Add 'active' class to the matching link and its parent container.
   * Falls back gracefully to the first item if no match is found.
   */

  // — Sidebar links —
  const sidenavLinks = document.querySelectorAll('nav.sidenav a');
  sidenavLinks.forEach((link) => {
    link.classList.remove('active');
    const linkPage = link.getAttribute('href').split('/').pop();
    if (linkPage && linkPage !== '#' && linkPage === currentPath) {
      link.classList.add('active');

      // Open the full ancestor chain for the active page so nested routes
      // like Rumah Sakit / Puskesmas keep their parent branches expanded.
      let currentMenuItem = link.closest('.has-submenu');
      while (currentMenuItem) {
        const siblingMenus = currentMenuItem.parentElement.querySelectorAll(':scope > .has-submenu');
        siblingMenus.forEach((other) => {
          if (other !== currentMenuItem) {
            other.classList.remove('submenu-open');
          }
        });
        currentMenuItem.classList.add('submenu-open');
        currentMenuItem = currentMenuItem.parentElement.closest('.has-submenu');
      }
    }
  });

  // — Topnav items —
  // Remove any hard-coded 'active' from the HTML first
  topnavItems.forEach((item) => {
    item.classList.remove('active');
    const links = item.querySelectorAll('a');
    links.forEach((link) => {
      const linkPage = link.getAttribute('href').split('/').pop();
      if (linkPage && linkPage !== '#' && linkPage === currentPath) {
        item.classList.add('active');
      }
    });
  });

  // If we're on the root/index, mark the first topnav item (Beranda) active
  if (
    currentPath === '' ||
    currentPath === 'index.html' ||
    currentPath === '/'
  ) {
    // Only set active on Beranda if nothing else matched
    const anyActive = document.querySelector('.topnav-item.active');
    if (!anyActive && topnavItems.length > 0) {
      topnavItems[0].classList.add('active');
    }
  }


  // ─────────────────────────────────────────────────────────────
  // 5. DIR-ROW INTERACTION
  // ─────────────────────────────────────────────────────────────

  /**
   * The hover arrow animation on .dir-row is handled entirely by CSS
   * (transform: translateX(4px) on :hover). No JS needed for that.
   *
   * A click ripple or navigation behaviour can be wired here if needed
   * in a future iteration, e.g.:
   *
   *   document.querySelectorAll('.dir-row').forEach((row) => {
   *     row.addEventListener('click', () => { window.location.href = row.dataset.href; });
   *   });
   */

  // ─────────────────────────────────────────────────────────────
  // 6. BERITA TERKINI SLIDER (scrollable feature-card carousel)
  // ─────────────────────────────────────────────────────────────

  document.querySelectorAll('.news-featured').forEach((section) => {
    const slider = section.querySelector('.feature-slider');
    const prevBtn = section.querySelector('.slider-prev');
    const nextBtn = section.querySelector('.slider-next');
    if (!slider) return;

    const scrollByCard = (direction) => {
      slider.scrollBy({ left: slider.clientWidth * direction, behavior: 'smooth' });
    };

    if (prevBtn) prevBtn.addEventListener('click', () => scrollByCard(-1));
    if (nextBtn) nextBtn.addEventListener('click', () => scrollByCard(1));
  });

}); // end DOMContentLoaded