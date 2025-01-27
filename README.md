# SpeakX---DevOps-Assignment---LPU-2026
# Mobile Application Backend Deployment in the Cloud 
This repository demonstrates the deployment of a mobile application backend in the cloud using best practices in infrastructure provisioning, application deployment, and CI/CD automation.
This is a endpoint link(Note: It will not work without api key) *https://www.numberpropertyapi.site/number-info?number=3*

Use this code in terminal to access this API APP    -
```curl -H "X-API-KEY: d5b7f6e9-ff8a-4d93-bc6b-bd6fcf3e55bb" "https://www.numberpropertyapi.site/number-info?number=3"```

One of the valid API key is *d5b7f6e9-ff8a-4d93-bc6b-bd6fcf3e55bb*

This api helps to give property of a number you just need to change the number at the end of the code and the api will work


# Cloud Deployment of Mobile Application Backend

This repository contains the code and configurations for deploying a mobile application backend in the cloud. It uses Terraform for Infrastructure as Code (IaC), Docker for containerization, and GitHub Actions for CI/CD.

---

## **Architecture Overview**

### **High-Level Diagram**

### **Components**
1. **Infrastructure**: Provisioned using Terraform.
   - VPC with public and private subnets.
   - ECS Cluster for running the Dockerized backend.
   - Application Load Balancer (ALB) for HTTPS traffic.
2. **Backend**: Simple REST API (Node.js/Python) containerized using Docker.
3. **Secrets Management**: AWS Secrets Manager for securely storing sensitive data.
4. **CI/CD**: GitHub Actions pipeline automating build and deployment processes.

---

