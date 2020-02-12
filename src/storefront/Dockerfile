FROM node:13.7.0-alpine3.11 as build
WORKDIR /app
COPY package.json package-lock.json ./
ENV HOST 0.0.0.0
RUN npm install

FROM build
COPY . .
CMD [ "npm", "run", "dev" ]
