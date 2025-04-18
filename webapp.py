import streamlit as st
from halaman_led import halaman_led
from halaman_upload import halaman_upload_file
from halaman_dht11 import halaman_dht11
from halaman_buzzer import halaman_buzzer
from halaman_servo import halaman_servo 
from halaman_motor_dc import halaman_motor_dc
from halaman_oled import halaman_oled
from halaman_tm1637 import halaman_tm1637
from halaman_ldr import halaman_ldr
from halaman_trim import halaman_trim
from halaman_button import halaman_button
from halaman_chatbot import halaman_chatbot
from halaman_deteksi_sensor_dan_penjelasan import halaman_deteksi_sensor_dan_penjelasan
from halaman_kit_esp32 import halaman_kit_esp32
from halaman_ntc import halaman_ntc
from halaman_tilt import halaman_tilt
from halaman_ds18s20 import halaman_ds18s20
from halaman_tsop1838 import halaman_tsop1838
from halaman_tcrt5000 import halaman_tcrt5000

# Konfigurasi halaman
st.set_page_config(page_title="EduKit Web App", page_icon="💡", layout="centered")

# Sidebar navigasi
st.sidebar.title("📚 Menu Navigasi")
menu = st.sidebar.radio("Pilih Halaman", [
    "📤 halaman_kit_esp32",
    "🔎 Penjelasan LED", 
    "🌡 Penjelasan DHT11", 
    "🔔 Penjelasan Buzzer", 
    "⚙️ Penjelasan Servo", 
    "🔄 Penjelasan Motor DC",
    "🖥️ Penjelasan OLED Display",
    "⏱️ Penjelasan TM1637",
    "🔆 Penjelasan Sensor LDR",
    "🎚️ Penjelasan Potensiometer Trim",
    "🔘 Penjelasan Push Button",
    "🌡 Penjelasan NTC",
    "📐 Penjelasan Tilt Sensor",
    "🌡 Penjelasan DS18S20",
    "📡 Penjelasan TSOP1838",
    "📡 Penjelasan TCR5000",
    "🔎 Penjelasan Object Detection",
    "📤 Upload File ke ESP32",
    "🤖 Chatbot"

])

# ====================
# MAIN LOGIC
# ====================
if menu == "📤 halaman_kit_esp32":
    halaman_kit_esp32()
elif menu == "🔎 Penjelasan LED":
    halaman_led()
elif menu == "📤 Upload File ke ESP32":
    halaman_upload_file()
elif menu == "🌡 Penjelasan DHT11":
    halaman_dht11()
elif menu == "🔔 Penjelasan Buzzer":
    halaman_buzzer()
elif menu == "⚙️ Penjelasan Servo":
    halaman_servo()
elif menu == "🔄 Penjelasan Motor DC":
    halaman_motor_dc()
elif menu == "🖥️ Penjelasan OLED Display":
    halaman_oled()
elif menu == "⏱️ Penjelasan TM1637":
    halaman_tm1637()
elif menu == "🔆 Penjelasan Sensor LDR":
    halaman_ldr()
elif menu == "🎚️ Penjelasan Potensiometer Trim":
    halaman_trim()
elif menu == "🔘 Penjelasan Push Button":
    halaman_button()
elif menu == "🌡 Penjelasan NTC":
    halaman_ntc()
elif menu == "📐 Penjelasan Tilt Sensor":
    halaman_tilt()
elif menu == "🌡 Penjelasan DS18S20":
    halaman_ds18s20()
elif menu == "📡 Penjelasan TSOP1838":
    halaman_tsop1838()
elif menu == "📡 Penjelasan TCR5000":
    halaman_tcrt5000()
elif menu == "🔎 Penjelasan Object Detection":
    halaman_deteksi_sensor_dan_penjelasan()
elif menu == "🤖 Chatbot":
    halaman_chatbot()
