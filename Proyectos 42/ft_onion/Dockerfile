FROM nginx:latest
COPY nginx-html/index.html /usr/share/nginx/html/index.html
COPY nginx-html/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD nginx -g 'daemon off;'