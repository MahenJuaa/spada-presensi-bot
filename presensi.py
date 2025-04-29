import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from telegram_notifier import send_telegram_message
import time

load_dotenv()

USERNAME = os.getenv("SPADA_USERNAME")
PASSWORD = os.getenv("SPADA_PASSWORD")

def auto_presensi(keterangan=""):
    for attempt in range(3):
        try:
            options = Options()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            driver = webdriver.Chrome(options=options)

            driver.get("https://spada.upnyk.ac.id/")  # Ganti dengan URL asli SPADA

            driver.find_element("id", "username").send_keys(USERNAME)
            driver.find_element("id", "password").send_keys(PASSWORD)
            driver.find_element("id", "loginbtn").click()

            time.sleep(3)

            # Tambahkan logika klik presensi sesuai kebutuhan

            send_telegram_message(f"✅ Presensi otomatis berhasil📝 {keterangan}")
            driver.quit()
            break
        except Exception as e:
            if attempt == 2:
                send_telegram_message(f"❌ Gagal presensi setelah 3 percobaan📝 {keterangan}Error: {str(e)}")
