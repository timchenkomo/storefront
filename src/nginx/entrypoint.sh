#!/bin/sh
cp /app/nginx.${ENV}.conf /etc/nginx/conf.d/default.conf
nginx -g 'daemon off;'
