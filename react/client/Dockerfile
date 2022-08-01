FROM node:latest
RUN npm install --global pm2 && apt-get update && apt-get install -y iputils-ping
WORKDIR /react
COPY . .

RUN npm install && npm run build

EXPOSE 3000



CMD [ "pm2-runtime", "npm", "--", "start" ]

# CMD [ "npm", "run", "start" ]