#!/bin/bash

# chmod +x build.sh

gcloud config set run/region asia-southeast2 && \
gcloud builds submit --config=cloudbuild.yaml && \
gcloud beta run deploy ml-deployment \
  --image='asia-southeast2-docker.pkg.dev/test-docker-405606/ml-deployment/ml-deployment:latest' \
  --port='8080' \
  --allow-unauthenticated \
  --memory='1Gi'