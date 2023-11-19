FROM node:lts AS build
WORKDIR /app
COPY . /app
ENV VITE_BASE_URL https://ml-deployment-5upxjnapxq-et.a.run.app/
RUN npm install
RUN npm run build

FROM nginx:alpine AS run
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx","-g", "daemon off;"]