import re

with open('food_september.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix 6500
html = re.sub(r'            </div>\s*<div class="slider-item">\s*<img src="images/august_6500_01_hashizuke\.jpg".*?フルーツ盛り合わせ</div>\s*</div>', '            </div>', html, flags=re.DOTALL)

# Fix 5500
html = re.sub(r'            </div>\s*<div class="slider-item">\s*<img src="images/august_5500_01_hashizuke\.jpg".*?メロンパンナコッタ</div>\s*</div>', '            </div>', html, flags=re.DOTALL)

with open('food_september.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("HTML cleaned.")
