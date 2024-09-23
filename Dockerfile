
#Base image seçiyorum 
FROM python:3.11

#Uygulama dizini seçiyorum 
WORKDIR /app

#Uygulamanın çalışması için gerekli paketlerin kurulması için bir dosya oluşturdum
COPY requirements.txt .

#Gerekli Dosyaları indirdim
RUN pip install --no-cache-dir -r requirements.txt

#Uygulamanın çalışması için gerekli olan tkinter paketini ubuntu için indirdim
RUN apt-get update && apt-get install -y python3-tk

#Uygulamanın dosyasını çalışmasını istediğim yere kopyaladım
COPY python_proje.py  /app/python_proje.py:

#Uygulamanın çalışması için gerekli komutu girdim 
CMD ["python","python_proje.py"]

