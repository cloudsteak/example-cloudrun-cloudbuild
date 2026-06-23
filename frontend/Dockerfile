FROM nginx:alpine

# Másoljuk a HTML fájlt az Nginx alapértelmezett könyvtárába
COPY index.html /usr/share/nginx/html/

# Trükk a Cloud Runhoz: Az Nginx alapértelmezett 80-as portját lecseréljük a dinamikus $PORT változóra indításkor
CMD sed -i 's/listen[: ]*80;/listen '"$PORT"';/' /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'