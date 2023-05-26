
# La imagen base que usaremos desde docker hub
FROM debian:latest

# Instalamos los servicios y paquetes que usaremos
RUN apt-get update && apt-get install -y \
    openssh-server \
    sudo \
    nginx \
    tor 

# Archivos de configuracion copiados a los directorios del contenedor
COPY index.nginx-debian.html /var/www/html
COPY nginx.conf /etc/nginx/nginx.conf
COPY torrc /etc/tor
COPY sshd_config /etc/ssh
COPY gemas.jpg /var/www/html/gemas.jpg
COPY fondo-universo.jpg /var/www/html/fondo-universo.jpg

# Creamos usuario y grupo para el SSH
# RUN userdel -r jperez-2 || true
RUN useradd -ms /bin/bash -d /home/jperez-2 -G sudo jperez-2
RUN echo "jperez-2:password" | chpasswd

# Creamos el directorio ssh en el contenedor
RUN mkdir home/jperez-2/.ssh && \
    chmod 700 /home/jperez-2/.ssh

# Copiamos la clave publica ssh y cambiamos los permisos
COPY id_rsa.pub /home/jperez-2/.ssh/authorized_keys
RUN chown jperez-2:jperez-2 -R /home/jperez-2/.ssh && \
    chmod 600 /home/jperez-2/.ssh/authorized_keys

EXPOSE 80 4242
# Usamos nginx y ssh de manera predeterminada nada mas lanzar el contenedor
CMD ["nginx", "-g", "daemon off;"]

# Los puertos que usaremos, el 80 para el tor y el 4242 para el ssh

# Abrimos manualmente SSH y Tor:
# > service tor start
# > service ssh start