const fs = require('fs');
const path = require('path');

// 1. Update Navigation in all HTML files
function updateNavInDirectory(dir) {
    const files = fs.readdirSync(dir);
    files.forEach(file => {
        const fullPath = path.join(dir, file);
        if (fs.statSync(fullPath).isDirectory()) {
            updateNavInDirectory(fullPath);
        } else if (fullPath.endsWith('.html')) {
            let content = fs.readFileSync(fullPath, 'utf8');
            
            // Check if already updated
            if (!content.includes('plan.html">プラン</a>')) {
                // Regex to find the "お料理" link and insert "プラン" link after it
                const regex = /(<li><a href="[^"]*food\.html"(?:[^>]*)>お料理<\/a><\/li>)/g;
                content = content.replace(regex, '$1\n          <li><a href="/plan.html">プラン</a></li>');
                fs.writeFileSync(fullPath, content, 'utf8');
                console.log('Updated: ' + fullPath);
            }
        }
    });
}

updateNavInDirectory(__dirname);

// 2. Generate plan.html using access.html as base
let template = fs.readFileSync('access.html', 'utf8');

// Replace the main block
const mainRegex = /<main id="main">[\s\S]*?<\/main>/;

const newMain = `
<main id="main">
  <div class="page-header fade-in">
    <h1 class="page-title">各種プラン</h1>
    <p class="page-subtitle">様々なシーンに合わせた特別なプランをご用意しております。</p>
  </div>
  
  <style>
    .plan-buttons-grid {
       display: grid;
       grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
       gap: 25px;
       margin-bottom: 50px;
    }
    .plan-buttons-grid a.btn-plan {
       display: flex;
       align-items: center;
       justify-content: center;
       background-color: #8c7348;
       color: #fff;
       border-radius: 8px;
       text-decoration: none;
       padding: 30px 20px;
       font-size: 1.3rem;
       font-weight: bold;
       box-shadow: 0 4px 6px rgba(0,0,0,0.1);
       transition: transform 0.2s, box-shadow 0.2s, background-color 0.2s;
    }
    .plan-buttons-grid a.btn-plan:hover {
       transform: translateY(-3px);
       box-shadow: 0 8px 15px rgba(0,0,0,0.15);
       background-color: #7a643d;
    }
  </style>
  
  <section class="section fade-in">
    <div class="container" style="max-width: 900px;">
      <div class="plan-buttons-grid">
        <a href="#" class="btn-plan">忘年会　会席</a>
        <a href="#" class="btn-plan">忘年会　大皿</a>
        <a href="#" class="btn-plan">新年会　会席</a>
        <a href="#" class="btn-plan">新年会　大皿</a>
        <a href="#" class="btn-plan">卒園パーティ</a>
        <a href="#" class="btn-plan">卒団式プラン</a>
      </div>
    </div>
  </section>
</main>
`;

template = template.replace(mainRegex, newMain.trim());

// Update title and active state in nav
template = template.replace(/<title>.*?<\/title>/, '<title>各種プラン | 宇都宮の宴会・会議・ご法要なら「ホテル丸治」</title>');
template = template.replace('href="access.html" class="active" aria-current="page"', 'href="access.html"');
template = template.replace('href="/plan.html"', 'href="/plan.html" class="active" aria-current="page"');

fs.writeFileSync('plan.html', template, 'utf8');
console.log('Created: plan.html');

