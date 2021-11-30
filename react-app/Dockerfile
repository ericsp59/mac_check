FROM node:13 as node
WORKDIR /react-app
COPY ./react-app/package.json ./package.json
RUN npm install
COPY ./react-app ../../
RUN npm run build --prod

FROM nginx:1.13
WORKDIR /re
COPY --from=node ./react-app/build/ /usr/share/nginx/html
COPY ./react-app/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80