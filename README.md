# 🚀 Flask App Deployment using Helm & GitHub Actions

This project demonstrates how to deploy a Flask application on a Kubernetes cluster using **Helm** and automate the deployment using **GitHub Actions**.

---

## 📸 Screenshots

### ✅ Deployed App UI
![App Screenshot](screenshots/app.png)

### ⚙️ GitHub Actions Trigger
![Trigger Screenshot](screenshots/trigger.png)

### 📦 Docker Image on Docker Hub
![Docker Image Screenshot](screenshots/image.png)

---

## 📂 Project Structure

```
flask-helm-k8s/
├── flask-chart/             # Helm chart for Flask app
│   ├── templates/           # Helm templates (deployment, service, etc.)
│   └── values.yaml          # Default Helm values
├── Dockerfile               # Docker image definition
├── .github/workflows/
│   └── deploy.yml           # GitHub Actions workflow
└── README.md
```

---

## ⚙️ CI/CD Pipeline Overview

- **Trigger**: Any push to the `master` branch.
- **Build & Deploy**:
  - Connects to Kubernetes cluster using a base64 encoded kubeconfig secret.
  - Uses `helm upgrade --install` to deploy/update the app.
- **Secrets Used**:
  - `KUBECONFIG_DATA` – base64 encoded kubeconfig
  - `DOCKER_USERNAME` & `DOCKER_PASSWORD` – for DockerHub access (if pushing image)

---

## 🚀 Deployment Details

- **Helm Chart Path**: `./flask-chart`
- **Release Name**: `flask-app`
- **Namespace**: `shady-ns` (created if not exists)
- **Docker Image Used**: `shadyemad/flask-helm-app:latest`
- **Service Type**: `NodePort` on port `5000`

```bash
helm upgrade --install flask-app ./flask-chart \
  --namespace shady-ns \
  --create-namespace
```

---

## ✅ GitHub Actions Status

![Deployment Status](https://github.com/shadyemad2/flask-helm-k8s/actions/workflows/deploy.yml/badge.svg)

---

## 📌 Notes

- Make sure to upload the following screenshots in `screenshots/` folder:
  - `app.png` (deployed app UI)
  - `trigger.png` (screenshot of triggered GitHub Actions run)
  - `image.png` (DockerHub image page)

---

## 🧠 Author

**Shady Emad**

> Automating deployments the DevOps way 🚀

