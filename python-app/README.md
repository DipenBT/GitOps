# Flask "Hello World" with Docker + GitHub Actions

A minimal but production-ready Flask application, fully Dockerized, with automated testing on every push using GitHub Actions.

Every time you push code, GitHub automatically:
- Builds the Docker image
- Runs the container
- Hits `http://localhost:8080`
- Shows you the real **"Hello, World!"** output in the workflow logs

GitOps/python-app/
─ app.py
- requirements.txt
- Dockerfile
  - .dockerignore
