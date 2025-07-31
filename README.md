# 🚀 Flask App Deployment using Helm & GitHub Actions

This project demonstrates how to deploy a Flask application on a Kubernetes cluster using **Helm** and automate the deployment using **GitHub Actions**.

<img width="942" height="539" alt="hellllllllllllllllllllllllm" src="https://github.com/user-attachments/assets/519c5378-a438-4572-889d-4f29cdd369af" />

---

## 📸 Screenshots

### ✅ Deployed App UI

<img width="1907" height="903" alt="flask-app" src="https://github.com/user-attachments/assets/f825cb97-798e-49f7-8c91-74f45c895c2c" />

### ⚙️ GitHub Actions Trigger

<img width="1780" height="834" alt="trigger-action" src="https://github.com/user-attachments/assets/20e1ae0e-7b8a-4831-bf87-ae7a4c94686b" />

### 📦 Docker Image on Docker Hub

<img width="1290" height="550" alt="image" src="https://github.com/user-attachments/assets/e13bea44-e631-443d-93f7-f4755d42e9c4" />

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

## 🧠 Author

**Shady Emad**

> Automating deployments the DevOps way 🚀

