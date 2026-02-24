import os

def build_cyclone_os():
    html_content = """
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>ROUED CYCLONE V24 - SOVEREIGN EDITION</title>
        <style>
            :root { --gold: #ffd700; --green: #00ff41; --bg: #000; --red: #ff3131; --cyan: #00f2ff; --dark: #0a0a0a; }
            * { box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
            body { background: var(--bg); color: #fff; font-family: 'Courier New', monospace; margin: 0; padding: 5px; height: 100vh; overflow: hidden; border: 4px solid var(--gold); display: flex; flex-direction: column; }
            
            /* القائمة العلوية */
            .nav-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 4px; margin-bottom: 5px; }
            .nav-btn { background: #111; border: 1px solid var(--gold); color: var(--gold); padding: 10px 2px; font-size: 0.65rem; text-align: center; border-radius: 4px; cursor: pointer; font-weight: bold; }

            /* الشاشة الرئيسية - مع تقليص الارتفاع المطللوب */
            .main-frame { flex-grow: 1; border: 2px solid var(--green); background: rgba(0, 20, 0, 0.1); border-radius: 10px; position: relative; overflow: hidden; display: flex; flex-direction: column; margin-bottom: 1.2cm; }
            #display-content { flex-grow: 1; padding: 10px; overflow-y: auto; font-size: 0.8rem; color: var(--green); }
            
            /* النوافذ المنبثقة السيادية */
            .modal { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: var(--bg); z-index: 1000; display: none; padding: 15px; border-radius: 8px; overflow-y: auto; }
            .modal-header { display: flex; justify-content: space-between; border-bottom: 1px solid var(--gold); padding-bottom: 10px; margin-bottom: 10px; }

            /* التارمينال */
            .terminal-input-area { display: flex; align-items: center; gap: 5px; background: #000; padding: 5px; border-top: 1px solid var(--green); }
            #main-input { flex-grow: 1; background: transparent; border: none; color: var(--green); outline: none; font-family: monospace; }

            /* واجهات الأدوات المتقدمة */
            .drone-ctrl { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; text-align: center; }
            .radar-screen { width: 150px; height: 150px; border: 2px solid var(--green); border-radius: 50%; margin: 10px auto; position: relative; background: radial-gradient(circle, #003300 0%, #000 70%); }
            .radar-sweep { width: 100%; height: 100%; border-left: 2px solid var(--green); position: absolute; animation: sweep 4s linear infinite; transform-origin: center; }
            @keyframes sweep { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }

            /* الأزرار والمدخلات */
            .action-btn { background: var(--gold); color: #000; border: none; padding: 8px; font-weight: bold; border-radius: 4px; cursor: pointer; margin-top: 5px; width: 100%; }
            .input-box { width: 100%; background: #111; border: 1px solid var(--cyan); color: #fff; padding: 8px; margin: 5px 0; border-radius: 4px; }
            
            .mic-btn { font-size: 1.8rem; cursor: pointer; transition: 0.3s; }
            .mic-on { color: var(--red); text-shadow: 0 0 10px var(--red); }
            
            /* الورشة والروابط السفلية */
            .footer { position: fixed; bottom: 5px; width: calc(100% - 10px); display: grid; grid-template-columns: repeat(4, 1fr); gap: 4px; }
            .f-item { background: #001a00; border: 1px solid var(--green); color: var(--green); font-size: 0.6rem; text-align: center; padding: 5px 0; border-radius: 3px; }
        </style>
    </head>
    <body>
        <div class="nav-grid">
            <div class="nav-btn" onclick="openMod('sindi')">🏢 سندي</div>
            <div class="nav-btn" onclick="openMod('links')">🖇️ الروابط</div>
            <div class="nav-btn" onclick="openMod('box')">📦 الصندوق</div>
            <div class="nav-btn" onclick="openMod('repo')">📁 المستودع</div>
            <div class="nav-btn" onclick="location.reload()">🛠️ الورشة</div>
        </div>

        <div class="main-frame">
            <div id="display-content">
                <div style="color:var(--gold)">[SYSTEM] ROUED CYCLONE V24 ACTIVE...</div>
                <div id="logs">>> بانتظار إشارة القائد.. البيئة مربوطة بـ Termux.</div>
            </div>
            
            <div id="mod-sindi" class="modal">
                <div class="modal-header"><span>🏢 مكتب سندي روت</span><button onclick="closeMod()">X</button></div>
                <label>مفتاح الحياة (API Key):</label>
                <input type="password" id="api-key" class="input-box" placeholder="أدخل المفتاح أو أمر الاستدعاء...">
                <button class="action-btn" onclick="sysLog('تم مزامنة مفتاح الحياة مع النواة')">🔑 تفعيل المفتاح السيادي</button>
                <hr>
                <div style="text-align:center;">
                    <p id="sindi-status">سندي: بانتظار صوتك يا قائد...</p>
                    <span id="mic-icon" class="mic-btn" onclick="startVoice()">🎤</span>
                </div>
                <button class="action-btn" style="background:var(--green)" onclick="sysLog('نظام الحماية: نشط')">🔐 قفل التطبيق بالبصمة</button>
            </div>

            <div id="mod-links" class="modal">
                <div class="modal-header"><span>🖇️ فحص الثغرات</span><button onclick="closeMod()">X</button></div>
                <input type="text" id="target-url" class="input-box" placeholder="أدخل رابط الهدف...">
                <div style="display:grid; grid-template-columns: 1fr 1fr; gap:5px;">
                    <button class="action-btn" onclick="runScan('ROUED')">تارمينال الرائد</button>
                    <button class="action-btn" onclick="runScan('TERMUX')">تارمينال Termux</button>
                </div>
                <div id="scan-res" style="margin-top:10px; color:var(--cyan); font-size:0.7rem;"></div>
            </div>

            <div id="mod-box" class="modal">
                <div class="modal-header"><span>📦 الصندوق الأسود</span><button onclick="closeMod()">X</button></div>
                <div class="nav-grid">
                    <div class="nav-btn" onclick="showTool('drone')">🚁 درون</div>
                    <div class="nav-btn" onclick="showTool('radar')">📡 رادار</div>
                    <div class="nav-btn" onclick="showTool('sat')">🛰️ ساتليت</div>
                    <div class="nav-btn" onclick="showTool('scan')">🛡️ ماسح</div>
                </div>
                <div id="tool-view" style="margin-top:10px; border-top:1px solid #333; padding-top:10px;"></div>
            </div>

            <div class="terminal-input-area">
                <span style="color:var(--gold); font-weight:bold;">#~:</span>
                <input type="text" id="main-input" placeholder="root@roued: execute_command..." onkeypress="handleTerm(event)">
                <button onclick="sysLog('جاري تحميل الأدوات...')">📥</button>
            </div>
        </div>

        <div class="footer">
            <div class="f-item" onclick="openMod('repo')">📥 تنزيل أدوات</div>
            <div class="f-item">GITHUB</div>
            <div class="f-item">APPILIX</div>
            <div class="f-item">PORT:8080</div>
        </div>

        <script>
            function openMod(id) { 
                document.querySelectorAll('.modal').forEach(m => m.style.display = 'none');
                document.getElementById('mod-' + id).style.display = 'block'; 
            }
            function closeMod() { document.querySelectorAll('.modal').forEach(m => m.style.display = 'none'); }

            function sysLog(msg) {
                const logs = document.getElementById('display-content');
                logs.innerHTML += `<div><span style="color:var(--gold)">[SYSTEM]</span> ${msg}</div>`;
                logs.scrollTop = logs.scrollHeight;
            }

            function handleTerm(e) {
                if(e.key === 'Enter') {
                    const val = e.target.value;
                    sysLog(`root@roued: ${val}`);
                    if(val === 'clear') document.getElementById('display-content').innerHTML = '';
                    e.target.value = '';
                }
            }

            // نظام الروابط
            function runScan(type) {
                const url = document.getElementById('target-url').value;
                if(!url) return alert('أدخل الهدف أولاً');
                const res = document.getElementById('scan-res');
                res.innerHTML = `[+] تشغيل ${type}...<br>[>] فحص الثغرات لـ ${url}<br>[*] جاري سحب البيانات...`;
                setTimeout(() => { res.innerHTML += `<br><span style="color:var(--green)">[DONE] لم يتم العثور على حماية صلبة.</span>`; }, 2000);
            }

            // نظام الصوت - سندي
            function startVoice() {
                const mic = document.getElementById('mic-icon');
                mic.classList.toggle('mic-on');
                const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
                recognition.lang = 'ar-SA';
                recognition.onresult = (event) => {
                    const text = event.results[0][0].transcript;
                    sysLog(`قائدي قال: ${text}`);
                    mic.classList.remove('mic-on');
                };
                recognition.start();
            }

            // أدوات الصندوق الأسود
            function showTool(name) {
                const view = document.getElementById('tool-view');
                if(name === 'drone') {
                    view.innerHTML = `<h4>🎮 تحكم الدرون</h4><div class="drone-ctrl">
                        <button class="action-btn">↖️</button><button class="action-btn">⬆️</button><button class="action-btn">↗️</button>
                        <button class="action-btn">⬅️</button><button class="action-btn" onclick="alert('REC START')">📷</button><button class="action-btn">➡️</button>
                        <button class="action-btn">↙️</button><button class="action-btn">⬇️</button><button class="action-btn">↘️</button>
                    </div>`;
                } else if(name === 'radar') {
                    view.innerHTML = `<h4>📡 رادار حي</h4><input class="input-box" placeholder="رقم أو رابط للملاحقة..."><div class="radar-screen"><div class="radar-sweep"></div></div>`;
                } else if(name === 'sat') {
                    view.innerHTML = `<h4>🛰️ إتصال ساتليت</h4><input class="input-box" placeholder="+213..."><div style="display:flex; gap:5px;"><button class="action-btn" style="background:var(--green)">إتصال</button><button class="action-btn" style="background:var(--red)">قطع</button></div><p>📍 موقعك: 31.62° N, -2.21° W</p>`;
                } else if(name === 'scan') {
                    view.innerHTML = `<h4>🛡️ حماية المؤسسة</h4><input class="input-box" placeholder="حسابي/موقعي..."><button class="action-btn" onclick="alert('Alarm Set')">🖲️ تفعيل الإنذار</button>`;
                }
            }
        </script>
    </body>
    </html>
    """
    with open('index.html', 'w', encoding='utf-8') as f: f.write(html_content)
    print("🌪️ تم تحديث إعصار V24 السيادي! التارمينال مضبوط، الصندوق مفعل، وسندي تستمع لك الآن.")

if __name__ == "__main__": build_cyclone_os()
