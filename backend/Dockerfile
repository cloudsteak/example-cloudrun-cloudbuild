# Hivatalos, pehelysúlyú Python futtatókörnyezet használata
FROM python:3.11-slim

# Munkakönyvtár beállítása a konténeren belül
WORKDIR /app

# Függőségek másolása és telepítése
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# A teljes alkalmazás kódjának másolása
COPY . .

# A gunicorn használata a webszerver futtatásához
# A $PORT változót a Cloud Run automatikusan biztosítja
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app