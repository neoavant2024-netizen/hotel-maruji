const fs = require('fs');
let html = fs.readFileSync('news_osechi/index.html', 'utf8');

// 1. Add Fancybox CSS before <style>
html = html.replace('<style>', '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fancyapps/ui@5.0/dist/fancybox/fancybox.css" />\n        <style>');

// 2. Add Fancybox JS before page-flip
html = html.replace('<script src="https://cdn.jsdelivr.net/npm/page-flip', '<script src="https://cdn.jsdelivr.net/npm/@fancyapps/ui@5.0/dist/fancybox/fancybox.umd.js"></script>\n        <script src="https://cdn.jsdelivr.net/npm/page-flip');

// 3. Update CSS rules for max-width
html = html.replace('max-width: 600px;', 'max-width: 1000px;');

// 4. Add the Zoom button to HTML controls
html = html.replace('<button id="btn-next" class="flip-btn">次へ <i class="fas fa-chevron-right"></i></button>', '<button id="btn-next" class="flip-btn">次へ <i class="fas fa-chevron-right"></i></button>\n            <button id="btn-zoom" class="flip-btn" style="margin-left: 10px; background-color: #333;"><i class="fas fa-search-plus"></i> 拡大</button>');

// 5. Update JS options for larger size
html = html.replace('width: 400,', 'width: 600,');
html = html.replace('height: 565,', 'height: 848,');
html = html.replace('maxWidth: 600,', 'maxWidth: 1000,');
html = html.replace('maxHeight: 847,', 'maxHeight: 1413,');

// 6. Add JS for the Zoom button
const zoomJs = `
            const images = [
              "/images/news_osechi_2027.jpg",
              "/images/news_osechi_2027_summary.jpg",
              "/images/news_osechi_2027_fuku.jpg",
              "/images/news_osechi_2027_midori.jpg",
              "/images/news_osechi_2027_kotobuki.jpg"
            ];
            document.getElementById('btn-zoom').addEventListener('click', () => {
                const idx = pageFlip.getCurrentPageIndex();
                Fancybox.show([{ src: images[idx], type: "image" }]);
            });
`;
html = html.replace('pageFlip.on(\'flip\'', zoomJs + '\n            pageFlip.on(\'flip\'');

fs.writeFileSync('news_osechi/index.html', html, 'utf8');
console.log('Update complete.');
