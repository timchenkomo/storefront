FROM nginx:1.17.8-alpine
COPY . /app
ENTRYPOINT [ "/app/entrypoint.sh" ]
CMD ["nginx", "-g", "daemon off;"]