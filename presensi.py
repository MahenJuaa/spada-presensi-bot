import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
from telegram_notifier import send_telegram_message

load_dotenv()

USERNAME = os.getenv("SPADA_USERNAME")
PASSWORD = os.getenv("SPADA_PASSWORD")

PRESENSI_LABELS = [
    "Attendance", "Presensi", "PRESENSI KULIAH",
    "Presensi Kehadiran Mahasiswa", "Presensi disini"
]

def auto_presensi(keterangan=""):
    for attempt in range(3):
        try:
            options = Options()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            driver = webdriver.Chrome(options=options)

            # Login ke SPADA
            driver.get("https://spada.upnyk.ac.id/")
            driver.find_element(By.ID, "username").send_keys(USERNAME)
            driver.find_element(By.ID, "password").send_keys(PASSWORD)
            driver.find_element(By.ID, "loginbtn").click()
            time.sleep(3)

            # Cari link presensi
            found = False
            for label in PRESENSI_LABELS:
                try:
                    presensi_link = driver.find_element(By.PARTIAL_LINK_TEXT, label)
                    presensi_link.click()
                    found = True
                    break
                except NoSuchElementException:
                    continue

            if not found:
                raise Exception("Tidak menemukan link presensi di dashboard")

            time.sleep(2)

            # Klik "Go to activity" atau sejenisnya
            try:
                driver.find_element(By.PARTIAL_LINK_TEXT, "Go to activity").click()
            except NoSuchElementException:
                raise Exception("Tidak menemukan tombol 'Go to activity'")

            time.sleep(2)

            # Klik "Apply for attendance"
            try:
                driver.find_element(By.PARTIAL_LINK_TEXT, "Apply for attendance").click()
            except NoSuchElementException:
                raise Exception("Tidak menemukan tombol 'Apply for attendance'")

            time.sleep(2)

            # Pilih "Present"
            try:
                present_radio = driver.find_element(By.XPATH, "//input[@type='radio' and @value='1']")
                present_radio.click()
            except NoSuchElementException:
                raise Exception("Opsi 'Present' tidak ditemukan")

            # Klik Save changes
            try:
                driver.find_element(By.XPATH, "//input[@type='submit']").click()
            except NoSuchElementException:
                raise Exception("Tombol 'Save changes' tidak ditemukan")

            send_telegram_message(f"✅ Presensi otomatis berhasil!\n📝 {keterangan}")
            driver.quit()
            break

        except Exception as e:
            if attempt == 2:
                send_telegram_message(f"❌ Gagal presensi setelah 3 percobaan\n📝 {keterangan}\nError: {str(e)}")
            time.sleep(2)
            driver.quit()