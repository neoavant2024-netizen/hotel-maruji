/* ホテル丸治 共通スクリプト（全ページで読み込む） */
(() => {
  'use strict';

  /* モバイルメニューの開閉 */
  const menuToggle = document.getElementById('menu-toggle');
  const navMenu = document.getElementById('nav-menu');

  if (menuToggle && navMenu) {
    const setMenu = (open) => {
      navMenu.classList.toggle('active', open);
      document.body.classList.toggle('menu-open', open);
      menuToggle.setAttribute('aria-expanded', String(open));
      menuToggle.setAttribute('aria-label', open ? 'メニューを閉じる' : 'メニューを開く');
      menuToggle.innerHTML = open
        ? '<i class="fas fa-times" aria-hidden="true"></i>'
        : '<i class="fas fa-bars" aria-hidden="true"></i>';
    };

    menuToggle.addEventListener('click', () => {
      setMenu(!navMenu.classList.contains('active'));
    });

    // メニュー内のリンクを踏んだら閉じる
    navMenu.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => setMenu(false));
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && navMenu.classList.contains('active')) {
        setMenu(false);
        menuToggle.focus();
      }
    });
  }

  /* スクロールでヘッダーを白背景に切り替える（トップページのみ。下層は常時白） */
  const header = document.getElementById('header');
  if (header && !document.body.classList.contains('subpage')) {
    const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 50);
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* スクロールに応じたフェードイン */
  const fadeElements = document.querySelectorAll('.fade-in');
  if (fadeElements.length) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });

    fadeElements.forEach((el) => observer.observe(el));
  }

  /* 会席料理の自動スライダー（お料理ページ） */
  document.querySelectorAll('.auto-slider-track').forEach((track) => {
    const items = Array.from(track.children);
    if (items.length <= 1) return;

    items.forEach((item, i) => item.classList.toggle('is-active', i === 0));

    let index = 0;
    setInterval(() => {
      items[index].classList.remove('is-active');
      index = (index + 1) % items.length;
      items[index].classList.add('is-active');
    }, 3000);
  });
})();
