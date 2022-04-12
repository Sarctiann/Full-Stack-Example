FROM node:17-alpine

RUN npm install -g serve

WORKDIR /code/frontend

COPY . .

EXPOSE 3000

CMD ["serve", "-s", "build"]