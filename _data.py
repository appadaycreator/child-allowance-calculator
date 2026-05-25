TITLE = '児童手当計算ツール【2024年改正対応】所得・年齢別に試算'
DESCRIPTION = '2024年10月改正版の児童手当を所得・子どもの年齢・人数で試算。所得制限撤廃・高校生延長対応。月額・年額を自動計算します。'
DESCRIPTION_SHORT = '2024年改正対応・子どもの年齢と人数から児童手当額を自動計算...'
COLOR1 = '#F0FDF4'
COLOR2 = '#DCFCE7'
COLOR_BTN = '#16A34A'
FOOTER_LINKS = [('https://appadaycreator.com/household-budget-analyzer/', '家計簿診断ツール'), ('https://appadaycreator.com/kids-activity-finder/', '子ども習い事診断'), ('https://appadaycreator.com/coupon-discount-calculator/', '割引クーポン計算ツール')]

CUSTOM_CSS = ""

MAIN_HTML = """<div class="card">
  <h2 style="font-size:18px;font-weight:700;margin-bottom:12px;">👶 児童手当 試算ツール（2024年10月改正対応）</h2>
  <p style="color:#666;font-size:14px;margin-bottom:16px;">子どもの人数・年齢を入力して受給額を計算します（所得制限なし）</p>
  <label>子ども1人目の年齢</label>
  <select id="age1">
    <option value="">-- 選択 --</option>
    <option value="0">0〜2歳（月15,000円）</option>
    <option value="3">3歳〜小学生（第1・2子：月10,000円）</option>
    <option value="3b">3歳〜小学生（第3子以降：月15,000円）</option>
    <option value="jhs">中学生（月10,000円）</option>
    <option value="hs">高校生（月10,000円）</option>
    <option value="none">18歳超・対象外</option>
  </select>
  <label>子ども2人目の年齢（いる場合）</label>
  <select id="age2">
    <option value="none">いない</option>
    <option value="0">0〜2歳</option>
    <option value="3">3歳〜小学生（第2子）</option>
    <option value="3b">3歳〜小学生（第3子以降）</option>
    <option value="jhs">中学生</option>
    <option value="hs">高校生</option>
  </select>
  <label>子ども3人目の年齢（いる場合）</label>
  <select id="age3">
    <option value="none">いない</option>
    <option value="0">0〜2歳</option>
    <option value="3b">3歳〜小学生（第3子以降）</option>
    <option value="jhs">中学生</option>
    <option value="hs">高校生</option>
  </select>
  <label>4人目以降（いる場合・第3子以降扱い）</label>
  <select id="age4">
    <option value="0">いない</option>
    <option value="1">1人（月15,000円）</option>
    <option value="2">2人（月30,000円）</option>
    <option value="3">3人以上（月45,000円）</option>
  </select>
  <button class="btn" style="margin-top:20px;" onclick="calc()">計算する →</button>
</div>
<div class="result" id="result">
  <div class="card" style="text-align:center;">
    <div style="font-size:13px;color:#888;margin-bottom:4px;">月額合計</div>
    <div class="result-value" id="r-month"></div>
    <div style="font-size:13px;color:#888;">年額: <strong id="r-year"></strong></div>
    <div id="r-detail" style="text-align:left;margin-top:16px;font-size:13px;color:#555;line-height:2;"></div>
    <div style="background:#F0FDF4;border-radius:10px;padding:12px;margin-top:12px;font-size:12px;color:#555;text-align:left;">
      ※2024年10月改正：所得制限撤廃・高校生（18歳年度末）まで延長・第3子以降3万円。<br>
      ※実際の支給額は市区町村で確認してください。
    </div>
    <button class="btn" style="margin-top:16px;" onclick="location.reload()">もう一度計算</button>
  </div>
</div>"""

JS_CODE = """const AMOUNT = {{
  '0':15000,'3':10000,'3b':15000,'jhs':10000,'hs':10000,'none':0
}};
function calc() {{
  const ages=[document.getElementById('age1').value, document.getElementById('age2').value, document.getElementById('age3').value].filter(v=>v&&v!=='none');
  const extra=parseInt(document.getElementById('age4').value)||0;
  if(!ages[0]){{alert('1人目の年齢を選択してください');return;}}
  let total=0, detail='';
  ages.forEach((age,i)=>{{
    const amt=AMOUNT[age]||0;
    total+=amt;
    const label=`子ども${{i+1}}人目`;
    detail+=`<div>${{label}}: <strong>${{amt.toLocaleString()}}円/月</strong></div>`;
  }});
  if(extra>0){{
    const extraAmt=extra*15000;
    total+=extraAmt;
    detail+=`<div>4人目以降: <strong>${{extraAmt.toLocaleString()}}円/月</strong></div>`;
  }}
  document.getElementById('r-month').textContent=total.toLocaleString()+'円/月';
  document.getElementById('r-year').textContent=(total*12).toLocaleString()+'円';
  document.getElementById('r-detail').innerHTML=detail;
  document.getElementById('result').classList.add('show');
  document.getElementById('result').scrollIntoView({{behavior:'smooth'}});
}}"""
