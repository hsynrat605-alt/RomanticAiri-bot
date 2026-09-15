from flask import Flask
import threading
import os

# --- هنا كود البوت مالتك الرومانسي ---
# اذا عندك كود بوت تليجرام خليه هنا
# هذا مثال يخلي السيرفر شغال 24 ساعة

app = Flask(__name__)

@app.route('/')
def home():
    return "RomanticAiri Bot is Alive and Running! ❤️"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    # شغل الفلاسك
    t = threading.Thread(target=run_flask)
    t.start()
    
    # هنا شغل بوت التليجرام مالتك
    print("Bot started...")
    # مثال: 
    # from telegram.ext import Updater
    # updater.start_polling()
