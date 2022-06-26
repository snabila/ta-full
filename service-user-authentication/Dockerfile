FROM node:14-alpine as base

WORKDIR /code
COPY package*.json /code/

FROM base as production
ENV NODE_ENV=production
RUN npm ci
COPY . /code/
CMD ["npm", "run", "start"]

FROM base as dev
ENV NODE_ENV=development
RUN npm install -g nodemon && npm install
COPY . /code/
CMD ["npm", "run", "dev"]