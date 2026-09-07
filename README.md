# Jenkins Python CI/CD Pipeline

## 📌 Project Overview

This project demonstrates an automated **CI/CD pipeline using Jenkins, GitHub, Python, Docker, and Docker Hub**.

Whenever code is pushed to the GitHub repository, a **GitHub Webhook automatically triggers Jenkins**. Jenkins checks out the latest code, installs dependencies, runs automated tests, builds a Docker image, and pushes the image to Docker Hub.

The project also includes environment-based deployment stages for **DEV, TEST, and PROD**.

---

## 🛠️ Technologies Used

* Jenkins
* Git & GitHub
* Python
* Pytest
* Docker
* Docker Hub
* Linux / Ubuntu
* Jenkinsfile
* GitHub Webhooks

---

## 🔄 CI/CD Workflow

```text
Developer pushes code
        ↓
      GitHub
        ↓
 GitHub Webhook
        ↓
      Jenkins
        ↓
   Checkout Code
        ↓
 Install Dependencies
        ↓
   Run Automated Tests
        ↓
  Application Check
        ↓
   Build Docker Image
        ↓
    Push to Docker Hub
        ↓
 Deploy to Selected Environment
 DEV / TEST / PROD
```

---

## 📂 Project Structure

```text
jenkins-python-cicd/
│
├── app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
└── Jenkinsfile
```

### File Description

| File               | Purpose                                     |
| ------------------ | ------------------------------------------- |
| `app.py`           | Python application                          |
| `test_app.py`      | Automated unit test                         |
| `requirements.txt` | Python dependencies                         |
| `Dockerfile`       | Instructions to build the Docker image      |
| `Jenkinsfile`      | Defines the complete Jenkins CI/CD pipeline |

---

## ⚙️ Jenkins Pipeline Stages

### 1. Build

Jenkins starts the pipeline and prepares the Python application.

### 2. Show Environment

Displays:

* Application name
* Application version
* Selected deployment environment

The pipeline supports:

```text
DEV
TEST
PROD
```

### 3. Install Dependencies

Jenkins creates a Python virtual environment and installs dependencies from:

```text
requirements.txt
```

A virtual environment is used to avoid installing Python packages directly into the system Python environment.

### 4. Automated Tests

The pipeline runs tests using **pytest**.

The testing stage contains parallel branches:

```text
Unit Tests
Application Check
```

This allows independent checks to run at the same time.

### 5. Docker Build

After successful tests, Jenkins builds a Docker image:

```bash
docker build -t jenkins-python-cicd:latest .
```

### 6. Docker Push

The generated Docker image is pushed to Docker Hub so that the image can be stored and used for deployment.

### 7. Deployment

Based on the selected parameter, Jenkins proceeds to the corresponding environment:

```text
DEV
TEST
PROD
```

Only the selected environment's deployment stage is executed.

### 8. Post Actions

The pipeline reports whether execution was successful or failed.

---

## 🔔 GitHub Webhook

A GitHub Webhook is configured to automatically notify Jenkins whenever code is pushed to the repository.

Therefore, instead of manually starting Jenkins every time, the workflow becomes:

```text
Git Push
   ↓
GitHub Webhook
   ↓
Jenkins automatically starts
   ↓
CI/CD Pipeline
```

The Jenkins console shows:

```text
Started by GitHub push by <username>
```

This confirms that the webhook triggered the pipeline.

---

## 🐳 Docker

The application is packaged into a Docker image using the project's `Dockerfile`.

Example:

```bash
docker build -t jenkins-python-cicd:latest .
```

The image is then pushed to Docker Hub.

This makes the application portable and allows the same image to be used across different environments.

---

## 🧪 Testing

The project uses **pytest** for automated testing.

Example test:

```python
def test_greet():
    assert greet() == "Hello from Jenkins webhook CI/CD"
```

If the test fails, Jenkins stops the pipeline and does not continue to Docker build, Docker push, or deployment.

This helps prevent faulty code from moving further through the CI/CD process.

---

## 🎯 Key Learning Outcomes

Through this project, I learned how to:

* Create a Jenkins Declarative Pipeline
* Write and use a Jenkinsfile
* Integrate Jenkins with GitHub
* Configure GitHub Webhooks
* Automate Python dependency installation
* Create Python virtual environments
* Run automated tests with pytest
* Execute parallel Jenkins stages
* Build Docker images from Jenkins
* Push Docker images to Docker Hub
* Use Jenkins parameters for environment selection
* Implement basic CI/CD workflow
* Troubleshoot Jenkins, Docker, Python, and Linux-related issues

---

## 🚀 Project Outcome

The final workflow automates the process from **code commit to container image creation and deployment stages**, reducing manual intervention and demonstrating a practical CI/CD implementation using Jenkins.

---

## 👩‍💻 Author

**Greeshma H**

BCA | Cloud & DevOps | AWS | Linux | Jenkins | Docker | Terraform
