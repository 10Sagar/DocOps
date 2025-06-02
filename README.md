# DocOps

## Description
A DevOps project to demonstrate CI/CD, Docker, and Cloud Deployment using GitHub Actions and Azure.

## Project Structure

- `app/` - Flask app and unit tests
- `docker/` - Dockerfiles and Compose config
- `scripts/` - Shell scripts for deployment
- `.github/workflows/` - GitHub Actions pipeline

## Run Locally

```bash
docker-compose -f docker/docker-compose.yml up --build
