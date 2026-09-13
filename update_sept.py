import re

with open('food_september.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace title
html = html.replace('葉月会席料理（2026年8月）', '長月会席料理（2026年9月）')
html = html.replace('葉月の会席', '長月の会席')

# Define new menus
menu_6500 = '''            <div class="auto-slider-track" id="kaiseki-slider-6500">
              <div class="slider-item">
                <img src="images/august_main_new_6500.jpg" alt="会席料理 6500円" class="slider-image">
              </div>
              <div class="slider-item">
                <img src="images/august_6500_01_hashizuke.jpg" alt="箸附" class="slider-image">
                <div class="slider-caption"><strong>箸附</strong>胡桃ムース 美味出汁ジュレ 零余子 栗 木の実 いくら</div>
              </div>
              <div class="slider-item">
                <img src="images/august_6500_02_zensai.jpg" alt="前菜七種" class="slider-image">
                <div class="slider-caption"><strong>前菜七種</strong>アンチョビチーズ 鳴門杏子 菊花和え 秋刀魚小袖棒寿司 銀杏玉子寄せ 鮎甘露煮 雲丹チーズ</div>
              </div>
              <div class="slider-item">
                <img src="images/august_6500_03_mukouzuke.jpg" alt="椀物" class="slider-image">
                <div class="slider-caption"><strong>椀物</strong>土瓶蒸し 清汁仕立て 松茸 茸 鶏肉 白身 銀杏 三つ葉 酢橘</div>
              </div>
              <div class="slider-item">
                <img src="images/august_6500_04_aizakana.jpg" alt="向附" class="slider-image">
                <div class="slider-caption"><strong>向附</strong>季節の御造り あしらい一式</div>
              </div>
              <div class="slider-item">
                <img src="images/august_6500_05_yakimono.jpg" alt="焼肴" class="slider-image">
                <div class="slider-caption"><strong>焼肴</strong>甘鯛若狭焼 栗麩田楽 紅葉人参艶煮 菊花大根</div>
              </div>
              <div class="slider-item">
                <img src="images/august_6500_06_takiawase.jpg" alt="煮物" class="slider-image">
                <div class="slider-caption"><strong>煮物</strong>牛頬肉柔か煮 馬鈴薯芋 パプリカ 青味 針葱 友地餡</div>
              </div>
              <div class="slider-item">
                <img src="images/august_6500_07_aburamono.jpg" alt="油物" class="slider-image">
                <div class="slider-caption"><strong>油物</strong>里芋餅 南京 蓮根 青唐</div>
              </div>
              <div class="slider-item">
                <img src="images/august_6500_08_sunomono.jpg" alt="強肴" class="slider-image">
                <div class="slider-caption"><strong>強肴</strong>白秋蒸し 銀餡 蟹身 茸 南瓜 餅 鶏肉</div>
              </div>
              <div class="slider-item">
                <img src="images/august_6500_09_shokuji.jpg" alt="食事" class="slider-image">
                <div class="slider-caption"><strong>食事</strong>豚肉と秋野菜 つけ蕎麦</div>
              </div>
              <div class="slider-item">
                <img src="images/august_6500_10_mizumono.jpg" alt="水物" class="slider-image">
                <div class="slider-caption"><strong>水物</strong>栗香る秋のプリン</div>
              </div>
            </div>'''

menu_5500 = '''            <div class="auto-slider-track" id="kaiseki-slider-5500">
              <div class="slider-item">
                <img src="images/august_main_new_5500.jpg" alt="会席料理 5500円" class="slider-image">
              </div>
              <div class="slider-item">
                <img src="images/august_5500_01_hashizuke.jpg" alt="箸附" class="slider-image">
                <div class="slider-caption"><strong>箸附</strong>胡桃ムース 美味出汁ジュレ 零余子 栗 木の実 いくら</div>
              </div>
              <div class="slider-item">
                <img src="images/august_5500_02_zensai.jpg" alt="前菜五種" class="slider-image">
                <div class="slider-caption"><strong>前菜五種</strong>アンチョビチーズ 鳴門杏子 菊花和え 秋刀魚小袖棒寿司 銀杏玉子寄せ</div>
              </div>
              <div class="slider-item">
                <img src="images/august_5500_03_mukouzuke.jpg" alt="向附" class="slider-image">
                <div class="slider-caption"><strong>向附</strong>季節の御造り あしらい一式</div>
              </div>
              <div class="slider-item">
                <img src="images/august_5500_04_aizakana.jpg" alt="焼肴" class="slider-image">
                <div class="slider-caption"><strong>焼肴</strong>秋鮭西京焼 栗麩田楽 紅葉人参艶煮 菊花大根</div>
              </div>
              <div class="slider-item">
                <img src="images/august_5500_05_yakimono_v2.jpg" alt="煮物" class="slider-image">
                <div class="slider-caption"><strong>煮物</strong>牛頬肉柔か煮 馬鈴薯芋 パプリカ 青味 針葱 友地餡</div>
              </div>
              <div class="slider-item">
                <img src="images/august_5500_06_takiawase_v2.jpg" alt="油物" class="slider-image">
                <div class="slider-caption"><strong>油物</strong>里芋餅 南京 蓮根 青唐</div>
              </div>
              <div class="slider-item">
                <img src="images/august_5500_07_aburamono_v2.jpg" alt="強肴" class="slider-image">
                <div class="slider-caption"><strong>強肴</strong>白秋蒸し 銀餡 蟹身 茸 南瓜 餅 鶏肉</div>
              </div>
              <div class="slider-item">
                <img src="images/august_5500_08_sunomono_v2.jpg" alt="食事" class="slider-image">
                <div class="slider-caption"><strong>食事</strong>豚肉と秋野菜 つけ蕎麦</div>
              </div>
              <div class="slider-item">
                <img src="images/august_5500_09_shokuji_v2.jpg" alt="水物" class="slider-image">
                <div class="slider-caption"><strong>水物</strong>栗香る秋のプリン</div>
              </div>
            </div>'''

menu_4500 = '''            <div class="auto-slider-track" id="kaiseki-slider-4500">
              <div class="slider-item">
                <img src="images/august_main_new_4500.jpg" alt="会席料理 4500円" class="slider-image">
              </div>
              <div class="slider-item">
                <img src="images/august_4500_01_hashizuke.jpg" alt="箸附" class="slider-image">
                <div class="slider-caption"><strong>箸附</strong>南瓜豆腐　海老 花穂 山葵 美味出汁</div>
              </div>
              <div class="slider-item">
                <img src="images/august_4500_02_zensai.jpg" alt="前菜五種" class="slider-image">
                <div class="slider-caption"><strong>前菜五種</strong>アンチョビチーズ 鳴門杏子 菊花和え 秋刀魚小袖棒寿司 銀杏玉子寄せ</div>
              </div>
              <div class="slider-item">
                <img src="images/august_4500_03_mukouzuke.jpg" alt="向附" class="slider-image">
                <div class="slider-caption"><strong>向附</strong>季節の御造り あしらい一式</div>
              </div>
              <div class="slider-item">
                <img src="images/august_4500_04_aizakana.jpg" alt="焼肴" class="slider-image">
                <div class="slider-caption"><strong>焼肴</strong>秋鮭西京焼 栗麩田楽 紅葉人参艶煮 菊花大根</div>
              </div>
              <div class="slider-item">
                <img src="images/august_4500_05_yakimono.jpg" alt="油物" class="slider-image">
                <div class="slider-caption"><strong>油物</strong>里芋餅 南京 蓮根 青唐</div>
              </div>
              <div class="slider-item">
                <img src="images/august_4500_06_takiawase.jpg" alt="強肴" class="slider-image">
                <div class="slider-caption"><strong>強肴</strong>白秋蒸し 銀餡 蟹身 茸 南瓜 餅 鶏肉</div>
              </div>
              <div class="slider-item">
                <img src="images/august_4500_07_aburamono.jpg" alt="食事" class="slider-image">
                <div class="slider-caption"><strong>食事</strong>豚肉と秋野菜 つけ蕎麦</div>
              </div>
              <div class="slider-item">
                <img src="images/august_4500_08_shokuji.jpg" alt="水物" class="slider-image">
                <div class="slider-caption"><strong>水物</strong>栗香る秋のプリン</div>
              </div>
            </div>'''

# Replace slider blocks
html = re.sub(r'            <div class="auto-slider-track" id="kaiseki-slider-6500">.*?            </div>', menu_6500, html, flags=re.DOTALL)
html = re.sub(r'            <div class="auto-slider-track" id="kaiseki-slider-5500">.*?            </div>', menu_5500, html, flags=re.DOTALL)
html = re.sub(r'            <div class="auto-slider-track" id="kaiseki-slider-4500">.*?            </div>', menu_4500, html, flags=re.DOTALL)

# Replace summary text for 6500
html = re.sub(
    r'箸附　前菜七種　向附　合肴　焼肴　焚き合わせ<br>\s*油物　酢の物　食事　水物',
    '箸附　前菜七種　椀物　向附　焼肴　煮物<br>油物　強肴　食事　水物',
    html
)

# Replace summary text for 5500
html = re.sub(
    r'箸附　前菜五種　向附　焼肴　焚き合わせ<br>\s*油物　酢の物　食事　水物',
    '箸附　前菜五種　向附　焼肴　煮物<br>油物　強肴　食事　水物',
    html
)

# Replace summary text for 4500
html = re.sub(
    r'箸附　前菜五種　向附　合肴　焼肴　焚き合わせ<br>\s*油物　食事　水物',
    '箸附　前菜五種　向附　焼肴　油物<br>強肴　食事　水物',
    html
)


with open('food_september.html', 'w', encoding='utf-8') as f:
    f.write(html)
