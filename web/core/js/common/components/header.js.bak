const appName = "Flow";
const headerHTML = `
  <a href="/flow">
    <div id="logo">
      <div id="img-logo">
        <img src="/core/media/ui/flow_logo.png" alt="N/A">
      </div>
      <div class="logo-text">
        <span class="left">{</span>
        <span class="right">}</span>
        <span class="text"><strong>${appName}</strong></span>
      </div>
    </div>
  </a>
  <div class="appName"><h2>${appName}s</h2></div>
  <div id="mid"></div>
  <div id="right-header">
    <div id="theme-selector"></div>

    <div id="github">
      <a href="https://github.com/BansheeStudio/ComfyUI-Banshee-Flow" target="_blank" rel="noopener noreferrer">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none">
          <path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12" fill=var(--color-header-text) />
        </svg>
      </a>
    </div>

    <div id="globe">
      <a href="https://bansheestudio.github.io" target="_blank" rel="noopener noreferrer">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke=var(--color-header-text) stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10" />
          <line x1="2" y1="12" x2="22" y2="12" />
          <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
        </svg>
      </a>
    </div>
  </div>
`;

export function insertElement() {
  const header = document.querySelector('header');
  if (header) {
    header.innerHTML = headerHTML;
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', insertElement);
} else {
  insertElement();
}

// Shuffling-stars tab title (mirrors the Banshee's Realm rainbow-title effect)
// Replaces the tab title with a long run of random ⭐✨🌟 on a 200ms interval.
// Guarded so multiple header.js loads (Linker iframes) don't stack intervals.
if (!window.__flowStarTitleStarted) {
  window.__flowStarTitleStarted = true;
  const stars = ["⭐", "✨", "🌟"];
  const titleLength = 300; // how many stars to fill the tab with
  const TICK_MS = 200;     // shuffle speed (matches the personal site)
  setInterval(() => {
    let title = "";
    for (let j = 0; j < titleLength; j++) {
      title += stars[Math.floor(Math.random() * stars.length)];
    }
    document.title = title;
  }, TICK_MS);
}
