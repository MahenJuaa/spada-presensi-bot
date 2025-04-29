import schedule
import time
from presensi import auto_presensi

def setup_schedule():
    schedule.every().monday.at("09:00").do(auto_presensi, keterangan="Lapangan A")
    schedule.every().monday.at("12:00").do(auto_presensi, keterangan="Patt.I-3B")
    schedule.every().monday.at("14:30").do(auto_presensi, keterangan="Patt.I-3A")
    schedule.every().tuesday.at("07:00").do(auto_presensi, keterangan="Patt.III-3A")
    schedule.every().tuesday.at("14:30").do(auto_presensi, keterangan="Patt.I-3D")
    schedule.every().wednesday.at("09:30").do(auto_presensi, keterangan="Patt.III-3A")
    schedule.every().wednesday.at("13:00").do(auto_presensi, keterangan="Lab Rancang Bangun Perangkat Lunak")
    schedule.every().wednesday.at("15:00").do(auto_presensi, keterangan="Lab Jaringan")
    schedule.every().thursday.at("07:00").do(auto_presensi, keterangan="Patt.I-3A")
    schedule.every().thursday.at("09:30").do(auto_presensi, keterangan="Patt.I-3B")

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)
