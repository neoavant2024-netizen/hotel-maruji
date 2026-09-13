import re

with open('food_september.html', 'r', encoding='utf-8') as f:
    html = f.read()

kaiseki_4500_html = '''      <!-- Zigzag 3: Kaiseki 4500 -->
      <div class="zigzag-row">
        <div class="zigzag-image">
          <div class="auto-slider-container">
            <div class="auto-slider-track" id="kaiseki-slider-4500">
              <div class="slider-item">
                <img src="images/sept_main_4500.jpg" alt="‰οΘ—Ώ— 4500‰~" class="slider-image">
              </div>
              <div class="slider-item">
                <img src="images/sept_4500_01_hashizuke.jpg" alt="”Ά•" class="slider-image">
                <div class="slider-caption"><strong>”Ά•</strong>“μ‰Z“¤•… CV ‰Τ•δ R¨ ”ό–΅o`</div>
              </div>
              <div class="slider-item">
                <img src="images/sept_4500_02_zensai.jpg" alt="‘OΨάν" class="slider-image">
                <div class="slider-caption"><strong>‘OΨάν</strong>ƒAƒ“ƒ`ƒ‡ƒrƒ`[ƒY –Β–εΗq ‹e‰Τa‚¦ H“‹›¬‘³–_υi ‹βΗ‹Κqρ‚Ή</div>
              </div>
              <div class="slider-item">
                <img src="images/sept_4500_03_mukouzuke.jpg" alt="ό•" class="slider-image">
                <div class="slider-caption"><strong>ό•</strong>‹Gί‚Μδ‘Ά‚θ ‚ ‚µ‚η‚Άκ®</div>
              </div>
              <div class="slider-item">
                <img src="images/sept_4500_04_yakimono.jpg" alt="Δζ" class="slider-image">
                <div class="slider-caption"><strong>Δζ</strong>HψΌ‹Δ Iκn“cy g—tlQ‰Ο ‹e‰Τ‘εª</div>
              </div>
              <div class="slider-item">
                <img src="images/sept_4500_05_aburamono.jpg" alt="–ϋ•¨" class="slider-image">
                <div class="slider-caption"><strong>–ϋ•¨</strong>—Άπ–έ “μ‹ @ª Β“‚</div>
              </div>
              <div class="slider-item">
                <img src="images/sept_4500_06_shiizakana.jpg" alt="‹­ζ" class="slider-image">
                <div class="slider-caption"><strong>‹­ζ</strong>”’Hφ‚µ ‹βιQ Ig ‘ω “μ‰Z –έ {“χ</div>
              </div>
              <div class="slider-item">
                <img src="images/sept_4500_07_shokuji.jpg" alt="H–" class="slider-image">
                <div class="slider-caption"><strong>H–</strong>“Ψ“χ‚ΖH–μΨ ‚Β‚―‹Ό”</div>
              </div>
              <div class="slider-item">
                <img src="images/sept_4500_08_mizumono.jpg" alt="…•¨" class="slider-image">
                <div class="slider-caption"><strong>…•¨</strong>I‚ιH‚Μƒvƒƒ“</div>
              </div>
            </div>
          </div>
        </div>
        <div class="zigzag-text">
          <div class="zigzag-subtitle">KAISEKI 4500</div>
          <h3 class="zigzag-title">‰οΘ—Ώ—</h3>
          <p class="zigzag-desc">
            ‚¨‹Cy‚Ι‚¨y‚µ‚έ‚Ά‚½‚Ύ‚―‚ι‘S8•i‚Μ‰οΘƒR[ƒX‚Ε‚·B<br>
            ‚²—Fl‚Ζ‚Μƒ‰ƒ“ƒ`‚βƒJƒWƒ…ƒAƒ‹‚Θ‚²‰ƒ‰ο‚Ι‚Ò‚Α‚½‚θ‚ΘAΚ‚θ–L‚©‚Θƒƒjƒ…[‚Ε‚·B
          </p>
          <div class="zigzag-menu">
            ”Ά•@‘OΨάν@ό•@Δζ@–ϋ•¨<br>
            ‹­ζ@H–@…•¨@@<span class="zigzag-price">4,500‰~</span>
          </div>
        </div>
      </div>
'''

new_html = re.sub(r'      <!-- Zigzag 3: Kaiseki 4500 -->.*?      <!-- Zigzag 4: Banquet -->', kaiseki_4500_html + '\n      <!-- Zigzag 4: Banquet -->', html, flags=re.DOTALL)

with open('food_september.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("HTML Replaced successfully.")
