FROM nginx:latest
LABEL authors="strumendo"
WORKDIR /etc/nginx

# Copia o arquivo de configuração do Nginx
COPY nginx.conf .

# Expõe a porta 80
EXPOSE 80

# Comando para iniciar o Nginx
CMD ["nginx", "-g", "daemon off;"]