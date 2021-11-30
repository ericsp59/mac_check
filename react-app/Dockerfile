FROM node:13 as node
WORKDIR /react-app
COPY ./react-app/package.json ./package.json
RUN npm install
COPY . ../../
RUN npm run build

FROM nginx:1.13
COPY --from=node ./react-app/build/ /usr/share/nginx/html
COPY ./react-app/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80