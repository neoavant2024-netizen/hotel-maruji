const fs = require('fs');
let html = fs.readFileSync('news_osechi/index.html', 'utf8');

const targetRegex = /<style>[\s\S]*?<\/div>\s*<\/div>/;

const replacement = `
        <style>
          .flip-book-container {
            position: relative;
            width: 100%;
            max-width: 600px;
            margin: 0 auto 40px;
            display: flex;
            flex-direction: column;
            align-items: center;
          }
          .flip-book {
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            margin: 0 auto;
          }
          .page {
            background-color: #fff;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            border-right: 1px solid #eee;
            border-bottom: 1px solid #ccc;
          }
          .page img {
            width: 100%;
            height: 100%;
            object-fit: contain;
          }
          .flip-controls {
            margin-top: 20px;
            display: flex;
            gap: 15px;
            align-items: center;
          }
          .flip-btn {
            background: #8c7348;
            color: #fff;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-family: inherit;
          }
          .flip-btn:disabled {
            background: #ccc;
            cursor: not-allowed;
          }
          .page-counter {
            font-weight: bold;
          }
        </style>
        
        <div class="flip-book-container">
          <div id="osechi-book">
            <div class="page"><img src="/images/news_osechi_2027.jpg" alt="1ページ"></div>
            <div class="page"><img src="/images/news_osechi_2027_summary.jpg" alt="2ページ"></div>
            <div class="page"><img src="/images/news_osechi_2027_fuku.jpg" alt="3ページ"></div>
            <div class="page"><img src="/images/news_osechi_2027_midori.jpg" alt="4ページ"></div>
            <div class="page"><img src="/images/news_osechi_2027_kotobuki.jpg" alt="5ページ"></div>
          </div>
          
          <div class="flip-controls">
            <button id="btn-prev" class="flip-btn"><i class="fas fa-chevron-left"></i> 前へ</button>
            <span class="page-counter"><span id="page-current">1</span> / <span id="page-total">5</span></span>
            <button id="btn-next" class="flip-btn">次へ <i class="fas fa-chevron-right"></i></button>
          </div>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/page-flip/dist/js/page-flip.browser.min.js"></script>
        <script>
          document.addEventListener('DOMContentLoaded', function() {
            const pageFlip = new St.PageFlip(document.getElementById('osechi-book'), {
                width: 400,
                height: 565,
                size: 'stretch',
                minWidth: 300,
                maxWidth: 600,
                minHeight: 424,
                maxHeight: 847,
                maxShadowOpacity: 0.5,
                showCover: true,
                mobileScrollSupport: false
            });
            
            pageFlip.loadFromHTML(document.querySelectorAll('.page'));

            const btnPrev = document.getElementById('btn-prev');
            const btnNext = document.getElementById('btn-next');
            const pageCurrent = document.getElementById('page-current');
            
            btnPrev.addEventListener('click', () => {
                pageFlip.flipPrev();
            });
            
            btnNext.addEventListener('click', () => {
                pageFlip.flipNext();
            });
            
            pageFlip.on('flip', (e) => {
                pageCurrent.textContent = e.data + 1;
            });
          });
        </script>
`;

html = html.replace(targetRegex, replacement.trim());
fs.writeFileSync('news_osechi/index.html', html, 'utf8');
console.log('done');
