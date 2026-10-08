import streamlit as st
import time

st.set_page_config(page_title="Novagenix Platform Live Preview", page_icon="💎", layout="centered")

st.markdown("""
<style>
    .main { background-color: #0e1621; color: #f5f5f5; }
    .stButton>button {
        background-color: #2b5278;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #3b6d9d;
    }
    .chat-bubble {
        background-color: #182533;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 15px;
        border-left: 4px solid #5288c1;
    }
    .console-bubble {
        background-color: #1f1f1f;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 15px;
        border-left: 4px solid #e17055;
        font-family: monospace;
    }
</style>
""", unsafe_allow_html=True)

st.title("💎 Novagenix Platform · Live Preview Simulator")
st.write("Това е интерактивно уеб превю на пълния работен процес в реално време.")

if "step" not in st.session_state:
    st.session_state.step = 1

step = st.session_state.step

if step == 1:
    st.markdown("### 👥 Етап 1 от 10: Меню Verified Vendors в групата")
    st.markdown("""
    <div class="chat-bubble">
    Клиентът влиза в основната група, отваря темата <b>Verified Vendors</b> и вижда акредитираните доставчици.<br><br>
    💡 <i>Системно предимство:</i> Всичко се случва изцяло в Telegram екосистемата, без външни сайтове.
    </div>
    """, unsafe_allow_html=True)
    if st.button("✅ Chat with Novagenix Peptides 🟢"):
        st.session_state.step = 2
        st.rerun()

elif step == 2:
    st.markdown("### 📄 Етап 2 от 10: Автоматичен каталог и запитване")
    st.markdown("""
    <div class="chat-bubble">
    Ботът изпраща ценовата листа и посреща купувача.<br><br>
    💬 <b>Реално съобщение от клиента в чата:</b><br>
    <code>„Здравейте, интересувам се от Ретатрутид 10мг, Тесаморелин 20мг и Мотс-ц 20мг.“</code>
    </div>
    """, unsafe_allow_html=True)
    if st.button("👉 Продължи към уточняването на бройките"):
        st.session_state.step = 3
        st.rerun()

elif step == 3:
    st.markdown("### 💬 Етап 3 от 10: Диалог за бройките и цена")
    st.markdown("""
    <div class="chat-bubble">
    • <b>Вендорът:</b> <i>„Здравейте! По колко бройки от всеки продукт ще желаете?“</i><br>
    • <b>Клиентът:</b> <i>„Моля по 2 бр. от Ретатрутид и Тесаморелин, и 1 бр. от Мотс-ц.“</i><br>
    • <b>Вендорът:</b> <i>„Сумата за тези артикули е общо $1,250.“</i><br>
    • <b>Клиентът:</b> <i>„Перфектно, цената ме устройва.“</i>
    </div>
    """, unsafe_allow_html=True)
    if st.button("👉 Продължи към шипинг адреса"):
        st.session_state.step = 4
        st.rerun()

elif step == 4:
    st.markdown("### 📦 Етап 4 от 10: Събиране на данни за доставка")
    st.markdown("""
    <div class="chat-bubble">
    • <b>Вендорът:</b> <i>„За да ви пусна официална поръчка в системата, моля изпратете ми три имена, телефон и точен адрес за доставка.“</i><br><br>
    • <b>Клиентът изпраща данните:</b><br>
    <code>Григор Петров, тел: +359888123456, гр. Пловдив, ул. Главна 1, ет. 2</code>
    </div>
    """, unsafe_allow_html=True)
    if st.button("👉 Вендорът създава Make offer"):
        st.session_state.step = 5
        st.rerun()

elif step == 5:
    st.markdown("### 📝 Етап 5 от 10: Използване на Make offer и [Edit] бутона")
    st.markdown("""
    <div class="console-bubble">
    🛠 <b>VENDOR CONSOLE</b><br>
    Вендорът натиска системния бутон <b>Make offer</b>, попълва артикулите и адреса.<br><br>
    ⚠️ <b>Ситуация:</b> Клиентът пише: <i>„Чакайте, объркал съм една цифра в телефона!“</i><br>
    ✏️ <b>Решение:</b> Вендорът бързо натиска системния бутон <b>[Edit]</b>, коригира телефона и я пуска наново за секунди.
    </div>
    """, unsafe_allow_html=True)
    if st.button("✅ Преглед на финалната оферта"):
        st.session_state.step = 6
        st.rerun()

elif step == 6:
    st.markdown("### 🧾 Етап 6 от 10: Официална оферта")
    st.markdown("""
    <div class="chat-bubble">
    <b>Offer ORD-1042 from Novagenix Peptides</b><br><br>
    ✨ <b>Официална оферта за клиента</b><br>
    ━━━━━━━━━━━━━━━<br>
    📦 <b>Съдържание:</b><br>
    &nbsp;&nbsp;• 2x Retatrutide 10mg<br>
    &nbsp;&nbsp;• 2x Tesamorelin 20mg<br>
    &nbsp;&nbsp;• 1x MOTS-c 20mg<br>
    📍 <b>Адрес:</b> гр. Пловдив, ул. Главна 1 (Коригиран тел: +359888999888)<br>
    ━━━━━━━━━━━━━━━<br>
    <b>Total: $1,250.00 USD</b>
    </div>
    """, unsafe_allow_html=True)
    if st.button("✅ I agree"):
        st.session_state.step = 7
        st.rerun()

elif step == 7:
    st.markdown("### 💳 Етап 7 от 10: Линк за плащане и комисионна")
    st.markdown("""
    <div class="chat-bubble">
    • Вендорът изпраща сигурен линк за плащане.<br>
    • Клиентът плаща и потвърждава в чата: <i>„Готово, платих го!“</i><br>
    • Вендорът натиска системния бутон <b>✅ Paid</b> в служебната тема.<br><br>
    <blockquote>💰 <i>Финансов отчет:</i> Платформата автоматично отчита платформена комисионна (за демото е заложена примерна стойност от <b>10%</b> или <b>$125.00 USD</b>) към твоя панел.</blockquote>
    </div>
    """, unsafe_allow_html=True)
    if st.button("👉 Виж динамиката на иконките в групата"):
        st.session_state.step = 8
        st.rerun()

elif step == 8:
    st.markdown("### 🏷️ Етап 8 от 10: Динамични статуси на темите")
    st.markdown("""
    <div class="chat-bubble">
    Заглавието на темата в групата се променя автоматично на живо:<br><br>
    • 🆕 <code>#1042 · Client Name</code> – Нов клиент (входящ лид).<br>
    • 📦 <code>#1042 · Client Name</code> – Изпратена оферта.<br>
    • 🔒 <code>#1042 · Client Name</code> – Приета оферта от клиента.<br>
    • 🟢 <code>#1042 · Client Name</code> – Успешно платено и затворено!
    </div>
    """, unsafe_allow_html=True)
    if st.button("👉 Виж как работи командата /commission на живо"):
        st.session_state.step = 9
        st.rerun()

elif step == 9:
    st.markdown("### 📊 Етап 9 от 10: Реалният изглед на командата /commission")
    st.markdown("""
    <div class="console-bubble">
    📊 <b>COMMISSION & SALES STATS (NOVAGENIX)</b><br><br>
    📦 Total Locked Offers: 1<br>
    💰 Total Sales Volume: $1,250.00 USD<br>
    💎 Total Commission (10%): $125.00 USD<br>
    ✅ Already Paid: $0.00 USD<br>
    ⏳ <b>Remaining Due (Unpaid):</b> $125.00 USD<br><br>
    ━━━━━━━━━━━━<br>
    📌 <b>UNPAID DEALS BREAKDOWN:</b><br>
    🏷️ <b>Offer:</b> ORD-1042 | 🏢 <b>Vendor:</b> Novagenix Peptides<br>
    👤 <b>Buyer:</b> Григор Петров<br>
    💰 <b>Total:</b> $1,250.00 USD | 💎 <b>Commission:</b> <b>$125.00 USD</b>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🟢 Mark Paid (ORD-1042)"):
        st.session_state.step = 10
        st.rerun()

elif step == 10:
    st.markdown("### 🎉 Етап 10 от 10: Тракинг, доставка и успешен финал")
    st.markdown("""
    <div class="chat-bubble">
    • Вендорът изпраща тракинг номер: <code>BG987654321</code><br>
    • Клиентът получава пратката и пише: <b>„Пратката пристигна, всичко е перфектно, много ви благодаря!“</b><br><br>
    🪄 <b>Голямата картина:</b> Пълна автоматизация, нулеви пропуснати детайли, прозрачни комисионни и доволни клиенти!
    </div>
    """, unsafe_allow_html=True)
    if st.button("🔁 Пусни симулацията отново"):
        st.session_state.step = 1
        st.rerun()
