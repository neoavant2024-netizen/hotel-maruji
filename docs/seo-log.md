# SEO 施策ログ（maruji.info）

定期的に SEO 対策を重ねていくための記録。毎回、実施内容と次回候補をここに追記する。
対象キーワードの軸: 「宇都宮 宴会」「宇都宮 大型宴会」「宇都宮 忘年会/新年会」「宇都宮 お祝い（七五三・顔合わせ等）」「宇都宮 おせち」

## 運用ルール

- 施策前に全ページ監査（title/description/canonical/JSON-LD/sitemap 突合）を行う。別端末の並行編集でバグが混入しやすい
- canonical は全ページ「自分自身」を指すこと（コピー元の URL が残る事故が2回発生: food.html→food_august、food_september→food_august、news_osechi→news_sake）
- 新ページ追加時は sitemap.xml への登録とパンくず（BreadcrumbList）を忘れない
- 画像は 1MB 超を目安に圧縮（quality 85・最大1600px）。参照側の ?v= を上げる
- Search Console の sitemap 送信・インデックス登録リクエストはユーザー側の作業

## 2026-11-11 ラウンド1

### バグ修正（検索順位に直結）
- food_september.html: title/description/canonical/OGP が food_august の複製のままだった → 9月（長月）版に修正
- news_osechi/: canonical と og:url が news_sake を指していた → 自分自身に修正（おせち商戦期の致命傷）

### 実施
- sitemap.xml に celebration 系8ページ + food_october/november の計10 URL を追加（欠落ゼロに）
- celebration 全8ページに BreadcrumbList、celebration.html に ItemList（プラン7件）の JSON-LD を追加
- news_distillery/ に Event 構造化データ（11/14 開催・8,000円・限定80名）→ リッチリザルト対象
- news 全8ページの title から「新着情報 - 」接頭辞を外しキーワードを前置、短すぎた description（23〜30字）を具体的な内容（価格・具材・引き渡し日等）で100字前後に拡充
- images/celebration_shichigosan.jpg を 1.7MB→431KB に圧縮（?v=3）

### 現状の構造化データ
- index: Hotel（geo/amenity/sameAs あり）
- banquet/bounenkai/shinnenkai/shaonkai/sotsudan: FAQPage + BreadcrumbList
- plan: BreadcrumbList + ListItem
- celebration 系: BreadcrumbList（+ハブに ItemList）
- news_distillery: Event

## 次回以降のレベルアップ候補（優先順）

1. **news_osechi 本文のテキスト化**: 現在ほぼ画像チラシのみでクロール対象テキストが無い。お品書き・価格・引き渡し日をチラシから正確に転記して本文に追加（恵方巻ページが良い見本）。※実在商品の内容は必ず元データから
2. **celebration 系ページに FAQPage**: 「個室はあるか」「ちゃんちゃんこ貸出」「子ども料金」など。宴会系ページで実績のある型
3. **季節イベントの Event スキーマ運用**: イベント終了後は eventStatus を外す/ページ整理。新イベント告知時に毎回 Event を付ける
4. **食事ページの統廃合検討**: food_august/september など過去月ページが増え続ける。過去月は food.html へ 301 するか「過去の献立」アーカイブ化してキーワード分散を防ぐ
5. **内部リンク強化**: 各プランページ下部に関連プラン相互リンク（忘年会⇔新年会⇔宴会場など）の充実度を点検
6. **PageSpeed 実測**: モバイル実測（Lighthouse）。WebP 化・フォント読み込み最適化の検討
7. **Google ビジネスプロフィール**: 投稿・写真・プラン情報の定期更新（ユーザー側作業。ローカル検索「宇都宮 宴会」に最も効く）
8. **被リンク**: 宇都宮観光系サイト・商工会議所・ぐるなび等への掲載状況確認
