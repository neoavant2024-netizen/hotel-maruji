const fs = require('fs');
let html = fs.readFileSync('news_osechi/index.html', 'utf8');

// 1. Add instruction text above the book
const instruction = `<p style="text-align:center; color:#d32f2f; font-weight:bold; margin-bottom: 20px;"><i class="fas fa-search-plus"></i> 画像をクリック（タップ）すると大きく拡大して細かい文字まで読むことができます。</p>`;
if (!html.includes('画像をクリック')) {
    html = html.replace('<div class="flip-book-container">', instruction + '\n        <div class="flip-book-container">');
}

// 2. Remove the zoom button
html = html.replace('<button id="btn-zoom" class="flip-btn" style="margin-left: 10px; background-color: #333;"><i class="fas fa-search-plus"></i> 拡大</button>', '');

// 3. Wrap images in Fancybox links
const pages = [
  'news_osechi_2027.jpg',
  'news_osechi_2027_summary.jpg',
  'news_osechi_2027_fuku.jpg',
  'news_osechi_2027_midori.jpg',
  'news_osechi_2027_kotobuki.jpg'
];

pages.forEach((img, index) => {
  const searchStr = `<div class="page"><img src="/images/${img}" alt="${index+1}ページ"></div>`;
  const replaceStr = `<div class="page"><a href="/images/${img}" data-fancybox="gallery" style="display:block; width:100%; height:100%; cursor: zoom-in;" title="クリックして拡大"><img src="/images/${img}" alt="${index+1}ページ" style="pointer-events: none;"></a></div>`;
  html = html.replace(searchStr, replaceStr);
});

// 4. Remove the zoom button JS logic
const targetRegex = /const images = \[[\s\S]*?\}\);/m;
html = html.replace(targetRegex, '');

fs.writeFileSync('news_osechi/index.html', html, 'utf8');
console.log('Update complete.');
