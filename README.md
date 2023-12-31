# Test ML-Backend-Frontend

## Development mode

Install dependency:

```bash
cd frontend
npm install

cd ../backend
pip install -r requirements.txt
```

Run:

```bash
npm run dev
flask run
```

## Production mode (Docker)

1. Change `Dockerfile`
1. Execute docker compose

```bash
cd frontend
docker compose -f docker-compose.yml up -d

cd ../backend
docker compose -f docker-compose.yml up -d
```

Stops and removes the containers, services, and associated volumes

```bash
docker compose -f docker-compose.yml down --volumes
```

## Production mode (deploy container image to Cloud Run)

1. Change project ID, region, image name, and other specification first on the `build.sh`, `cloudbuild.yaml`, and `Dockerfile`
1. Create Docker repository in the Artifact Registry
1. Execute the bash script

```bash
cd frontend
chmod +x build.sh
./build.sh

cd ../backend
chmod +x build.sh
./build.sh
```
