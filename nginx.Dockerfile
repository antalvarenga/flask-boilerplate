FROM --platform=linux/amd64 nginx:latest

WORKDIR /

COPY ./nginx/nginx_default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
EXPOSE 443
