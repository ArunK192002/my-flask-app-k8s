# Flask PostgreSQL Kubernetes App

This is a simple Flask web application that connects to a PostgreSQL database, deployed using Kubernetes.

## Table of Contents

- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Database Initialization](#database-initialization)
- [Endpoints](#endpoints)
- [Troubleshooting](#troubleshooting)

## Project Structure

my-flask-k8s/
│
├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── app.py
│   ├── config.py
│   └── models.py
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── secret.yaml
└── .env

## Prerequisites

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Kubernetes: [Install Kubernetes](https://kubernetes.io/docs/tasks/tools/)
- kubectl: [Install kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- Docker Hub account

## Installation

1. **Build the Docker Image:**

   docker build -t your-dockerhub-username/my-flask-app:latest ./app

2. **Push the Docker Image to Docker Hub:**

   docker push your-dockerhub-username/my-flask-app:latest

3. **Apply Kubernetes Manifests:**

   kubectl apply -f k8s/secret.yaml
   kubectl apply -f k8s/deployment.yaml
   kubectl apply -f k8s/service.yaml

## Usage

### Access the Flask Application

Get the external IP of the Flask service and open it in your browser:

kubectl get services

Look for the `EXTERNAL-IP` of the `flask-service` and open it in your browser. It will be something like `http://<EXTERNAL-IP>`.

## Environment Variables

The following environment variables are used by the application and should be set in the `.env` file:

FLASK_ENV=development
DATABASE_URL=postgresql://postgres:postgres@postgres-service/postgres

## Database Initialization

After deploying the services, you need to initialize the database:

1. Open a new terminal and execute the following command to access the running `flask-app` pod:

   kubectl exec -it <flask-app-pod-name> -- /bin/sh

   Replace `<flask-app-pod-name>` with the actual name of the Flask pod. You can get the pod name using:

   kubectl get pods

2. Inside the Flask container, run the following commands to create the tables:

   flask shell
   from models import db
   db.create_all()
   exit()

## Endpoints

- **GET /**: Returns a "Hello, World!" message.
- **GET /users**: Returns a list of users in JSON format.

## Troubleshooting

### Common Issues

- **ModuleNotFoundError**: Ensure all dependencies are listed in `requirements.txt` and rebuild the Docker image.
- **Database Connection**: Verify the `DATABASE_URL` in the `.env` file is correctly configured.

### Checking Logs

Check the logs for the `flask-app` and `postgres` pods using:

kubectl logs <flask-app-pod-name>
kubectl logs <postgres-pod-name>

### Pod Status

Ensure all pods are running without issues:

kubectl get pods

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Flask: [Flask Documentation](https://flask.palletsprojects.com/)
- Kubernetes: [Kubernetes Documentation](https://kubernetes.io/docs/)
- PostgreSQL: [PostgreSQL Documentation](https://www.postgresql.org/docs/)

This `README.md` file provides a clear and structured overview of your Kubernetes project, guiding users through the installation, usage, and troubleshooting steps.
