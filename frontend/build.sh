#!/bin/bash

# chmod +x build.sh

gcloud config set run/region asia-southeast2 && \
gcloud builds submit --config=cloudbuild.yaml && \
gcloud beta run deploy ml-frontend \
  --image='asia-southeast2-docker.pkg.dev/test-docker-405606/ml-frontend/ml-frontend:latest' \
  --port='80' \
  --allow-unauthenticated