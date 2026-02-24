import os

file_path = 'index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. تحديث وظيفة openMod لتشمل محتوى الورشة والمستودع المطور
updated_logic = """
            function openMod(type) {
                exit.style.display = 'block';
                termBar.style.display = 'none';
                if(type === 'work') {
                    display.innerHTML = `
                        <h3 style="color:var(--gold)">🛠️ الورشة (تطبيقات حية)</h3>
                        <div style="background:#fff; color:#000; padding:10px; border-radius:5px; margin-bottom:10px; font-family:sans-serif;">
                            <div style="border-bottom:1px solid #ccc; font-weight:bold; padding-bottom:5px;">> ROUED V24 payload.SYSTEM</div>
                            <div style="display:flex; justify-content:space-between; align-items:center; padding:8px; border:1px solid #ddd; margin-top:5px; background:#f9f9f9;">
                                <span>Al siccrat<br><small style="color:blue;">//rravetapload.zip</small></span>
                                <button style="background:#28a745; color:white; border:none; padding:5px 12px; border-radius:4px; font-weight:bold;">تحميل</button>
                            </div>
                            <div style="display:flex; justify-content:space-between; align-items:center; padding:8px; border:1px solid #ddd; margin-top:5px; background:#f9f9f9;">
                                <span>Emdlterenur<br><small style="color:blue;">//roued_apps payload.zip</small></span>
                                <button style="background:#28a745; color:white; border:none; padding:5px 12px; border-radius:4px; font-weight:bold;">تحميل</button>
                            </div>
                        </div>
                        <div style="background:#fff; color:#000; padding:10px; border-radius:5px; font-family:sans-serif;">
                             <div style="font-weight:bold; border-bottom:1px solid #ccc;">< ROUTINE V24 APULCX 1SSTH</div>
                             <div style="background:#eee; padding:10px; font-size:0.75rem; margin-top:5px; border-left:4px solid var(--gold);">
                                Flaskmad_apps.zip fWi/=-11890 = mxlapi20 sesthial paylon197
                             </div>
                        </div>`;
                } else if(type === 'repo') {
                    display.innerHTML = `
                        <h3 style="color:var(--cyan)">📁 المستودع (ملفات الثغرات)</h3>
                        <div style="border:2px solid var(--gold); padding:15px; background:rgba(255,215,0,0.05); border-radius:8px;">
                            <p style="color:var(--gold); font-weight:bold;">[✔] تم فتح المستودع السيادي</p>
                            <p style="color:#fff;">[+] ملفات الثغرات المكتشفة: <b>CVE-2026-X</b></p>
                            <p style="color:var(--green)">[*] اسم الحساب المكتشف: <b>الـمـفـتـح</b></p>
                            <hr style="border:0; border-top:1px solid var(--gold);">
                            <p style="font-size:0.8rem;">>> جاري مزامنة البيانات مع مكتب سندي...</p>
                        </div>`;
                } else if(type === 'box') {
"""

# 2. إضافة واجهة التارمينال والأزرار المدمجة في الأسفل
terminal_html = """
        <div style="position: fixed; bottom: 0; left: 0; width: 100%; background: #000; border-top: 2px solid var(--gold); z-index: 2000;">
            <div style="display: flex; align-items: center; gap: 5px; background: rgba(0,255,65,0.05); padding: 8px;">
                <span style="color: var(--gold); font-weight: bold; font-size: 0.8rem;">:root@roued:~#</span>
                <input type="text" id="final-input" style="flex-grow: 1; background: transparent; border: none; color: var(--green); outline: none; font-family: monospace; font-size: 0.9rem;" placeholder="أدخل أمراً للرائد أو ترمكس...">
            </div>
            <div style="display: grid; grid-template-columns: repeat(6, 1fr); gap: 2px; padding: 3px; background: #0a0a0a;">
                <div style="background:#1a1a1a; color:var(--cyan); padding:12px 0; text-align:center; font-size:0.7rem; border-radius:4px;" onclick="addT('ESC')">ESC</div>
                <div style="background:#1a1a1a; color:var(--cyan); padding:12px 0; text-align:center; font-size:0.7rem; border-radius:4px;" onclick="addT('TAB')">TAB</div>
                <div style="background:#1a1a1a; color:var(--cyan); padding:12px 0; text-align:center; font-size:0.7rem; border-radius:4px;" onclick="addT('CTRL')">CTRL</div>
                <div style="background:#1a1a1a; color:var(--cyan); padding:12px 0; text-align:center; font-size:0.7rem; border-radius:4px;" onclick="addT('ALT')">ALT</div>
                <div style="background:#1a1a1a; color:var(--cyan); padding:12px 0; text-align:center; font-size:0.7rem; border-radius:4px;" onclick="addT('UP')">↑</div>
                <div style="background:var(--gold); color:#000; padding:12px 0; text-align:center; font-size:0.7rem; border-radius:4px; font-weight:bold;" onclick="sendT()">ENTER</div>
            </div>
        </div>
        <script>
            function addT(k){ document.getElementById('final-input').value += k + " "; document.getElementById('final-input').focus(); }
            function sendT(){
                let i = document.getElementById('final-input');
                let d = document.getElementById('display-content');
                if(i.value){
                    d.innerHTML += `<div><span style="color:var(--gold)"># ${i.value}</span></div>`;
                    if(i.value.toLowerCase()==='help') d.innerHTML += '<div style="color:var(--cyan)">[!] الأنظمة متصلة: سندي، الدرون، الرادار.</div>';
                    i.value = ''; d.scrollTop = d.scrollHeight;
                }
            }
            document.getElementById('final-input').addEventListener('keypress', (e)=>{if(e.key==='Enter') sendT();});
        </script>
"""

# استبدال المنطق القديم بالجديد
if "function openMod(type) {" in content:
    content = content.replace("function openMod(type) {", updated_logic)

if "</body>" in content:
    content = content.replace("</body>", terminal_html + "</body>")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ اكتملت المهمة! تم دمج الورشة، المستودع، التارمينال، والأزرار كما في الصورة تماماً.")
