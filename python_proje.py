import tkinter as tk
from tkinter import messagebox
import requests
#.
def hava_durumu_al(sehir, api_anahtari):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_anahtari}&units=metric"
        cevap = requests.get(url)
        veri = cevap.json()
        
        if veri.get("cod") == 200:
            hava_durumu = veri["weather"][0]["description"]
            sicaklik = veri["main"]["temp"]
            nem_orani = veri["main"]["humidity"]
            ruzgar_hizi = veri["wind"]["speed"]
            sonuc = f"Hava Durumu: {hava_durumu}\nSıcaklık: {sicaklik}°C\nNem Oranı: {nem_orani}%\nRüzgar Hızı: {ruzgar_hizi} m/s"
            messagebox.showinfo("Hava Durumu", sonuc)
        else:
            messagebox.showerror("Hata", f"Şehir bulunamadı! Hata kodu: {veri['cod']}")
    except Exception as e:
        messagebox.showerror("Hata", f"Hata oluştu: {str(e)}")

def hava_durumu_tahmini_al(sehir, api_anahtari):
    try:
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={sehir}&appid={api_anahtari}&units=metric"
        cevap = requests.get(url)
        veri = cevap.json()
        
        if veri.get("cod") == "200":
            tahminler = veri.get("list", [])
            if tahminler:
                tahmin_metni = ""
                for tahmin in tahminler:
                    tarih = tahmin["dt_txt"]
                    hava_durumu = tahmin["weather"][0]["description"]
                    sicaklik = tahmin["main"]["temp"]
                    tahmin_metni += f"Tarih: {tarih}, Hava Durumu: {hava_durumu}, Sıcaklık: {sicaklik}°C\n"
                messagebox.showinfo("Hava Durumu Tahminleri", tahmin_metni)
            else:
                messagebox.showerror("Hata", "Hava durumu tahmini bulunamadı!")
        else:
            messagebox.showerror("Hata", f"Şehir bulunamadı! Hata kodu: {veri['cod']}")
    except Exception as e:
        messagebox.showerror("Hata", f"Hata oluştu: {str(e)}")

def get_weather():
    sehir = entry.get()
    api_anahtari = "your_api_key_here"  # OpenWeatherMap API anahtarını buraya girin
    hava_durumu_al(sehir, api_anahtari)

def get_forecast():
    sehir = entry.get()
    api_anahtari = "your_api_key_here"  # OpenWeatherMap API anahtarını buraya girin
    hava_durumu_tahmini_al(sehir, api_anahtari)

# Ana uygulama penceresi oluşturma
root = tk.Tk()
root.title("Hava Durumu Uygulaması")

# Etiket ve giriş kutusu oluşturma
label = tk.Label(root, text="Şehir:")
label.pack(pady=10)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Butonlar oluşturma
weather_button = tk.Button(root, text="Hava Durumu Al", command=get_weather)
weather_button.pack(pady=10)
forecast_button = tk.Button(root, text="Hava Durumu Tahminleri Al", command=get_forecast)
forecast_button.pack(pady=5)

# Uygulamayı başlatma
root.mainloop()
