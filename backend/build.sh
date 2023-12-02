#!/bin/bash

# chmod +x build.sh

gcloud config set run/region asia-southeast2 && \
gcloud builds submit --config=cloudbuild.yaml
