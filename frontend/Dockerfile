FROM node:14.16.1 as base

WORKDIR /code
COPY package*.json /code/

FROM base as production
ENV NODE_ENV=production
RUN npm ci
COPY . /code/
RUN npm run build
EXPOSE 3000
CMD ["node", "./build"]

FROM base as dev
ENV NODE_ENV=development
RUN npm install
COPY . /code/
EXPOSE 3000
EXPOSE 24678
CMD ["npm", "run", "devDocker"]