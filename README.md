# DevOps assignment-2

**Author:** Chetan Balugu

## Project overview
This repository contains a small demo Flask web application (ticket booking mockup) and all files needed to demonstrate a full CI/CD workflow using Git, Docker, Jenkins, and Kubernetes.

## Repo structure
```
DevOps-assignment-2/
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/index.html
├── Dockerfile
├── Jenkinsfile
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
└── README.md
```

## How to run locally
1. Create a Python virtualenv and run the app locally:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r app/requirements.txt
   python app/app.py
   ```
   Then open http://localhost:5000

## Docker
Build and run locally:
```bash
docker build -t devops-assignment-2:local -f Dockerfile .
docker run -p 5000:5000 devops-assignment-2:local
```

## Jenkins pipeline (high-level)
The included `Jenkinsfile` shows a declarative pipeline with stages:
- Checkout
- Build Image (docker build)
- Unit Test (smoke test by running container + curl)
- Push to Docker Hub (requires `dockerhub-creds` credential in Jenkins)
- Deploy to Kubernetes (requires `kubectl` configured on the Jenkins agent)

**Notes about Jenkins setup**:
- Create credentials in Jenkins (username/password) with id `dockerhub-creds` for pushing to Docker Hub.
- If you want to enable Docker Hub push, set `DOCKERHUB_REPO` environment variable in the pipeline config to `yourusername/devops-assignment-2`.

## Kubernetes
Apply manifests:
```bash
# ensure image in deployment.yaml points to a pushed image (replace YOUR_DOCKERHUB_USERNAME)
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```
Then access NodeIP:30080 (or use port-forwarding).

## GitFlow branching strategy
Suggested workflow:
- `main` branch holds production-ready code
- `develop` branch for integration
- `feature/<name>` branches for new features
- `release/*` and `hotfix/*` as needed

## What to submit (for evaluation)
- Push the entire repository to GitHub under the name `DevOps assignment-2`
- Include screenshots of: Docker image build, Jenkins pipeline run, Kubernetes pods running, Service access (placeholders below)
- Detailed commands and configuration steps used (above and in-line comments)

## Screenshots (add after you run things)
1. Docker build screenshot: `screenshots/docker-build.png`
2. Jenkins pipeline run screenshot: `screenshots/jenkins-pipeline.png`
3. Kubernetes pods: `screenshots/k8s-pods.png`
4. App in browser: `screenshots/app-running.png`

## Author
Chetan Balugu
