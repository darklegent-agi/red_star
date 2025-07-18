# KOMINTERN

This repository contains a skeleton implementation for the KOMINTERN project.
It is a minimal proof-of-concept for a planning and management platform based on
AI methods, using Flask and MongoDB.

## Structure

- `app/` – application package with placeholders for strategy planning and task
  management.
- `docker-compose.yml` – configuration for running MongoDB via Docker.
- `requirements.txt` – Python dependencies.

## Running locally

1. Start MongoDB:

   ```bash
   docker-compose up -d
   ```

2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python -m flask --app app run
   ```
