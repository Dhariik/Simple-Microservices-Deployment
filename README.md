# Simple-Microservices-Deployment
## Microservices Deployment Guide with Docker and Git
This guide walks through creating a simple microservices application and deploying it using Docker while using Git for version control.

## Project Overview
We’ll build a basic microservices application with two services:
  1. User Service (Python/Flask): Manages user data
  2. Product Service (Node.js/Express): Manages product data

Each service:
  1. Runs in its own container
  2. Has its own internal in-memory data
  3. Communicates via HTTP

## Step-by-Step Guide
### Step 1: Set Up Project Structure
![Image](https://github.com/user-attachments/assets/a891beef-0eb5-4442-b4c5-9e6dda2592ac)

### Step 2: Initialize Git Repository
![Image](https://github.com/user-attachments/assets/0e405d5d-c1e5-44e5-a0fa-53b87174f164)

### Step 3: Create the User Service (Python/Flask)
#### user-service/requirements.txt
![Image](https://github.com/user-attachments/assets/2b61a924-50a4-4da8-9964-2626d5ccb616)

#### user-service/app.py
![Image](https://github.com/user-attachments/assets/8ddf39f1-b2c6-4766-b641-5201e0b5ae23)

#### user-service/Dockerfile
![Image](https://github.com/user-attachments/assets/e0a079e6-9ba2-482d-a0b6-0c7e62faff22)

### Step 4: Create the Product Service (Node.js/Express)
#### product-service/package.json
![Image](https://github.com/user-attachments/assets/64e92b3c-914a-4840-aef8-96daffeaad45)

#### product-service/server.js
![Image](https://github.com/user-attachments/assets/861fb3f4-f86b-4f39-9ac7-2894bed4d270)

#### product-service/Dockerfile
![Image](https://github.com/user-attachments/assets/3bc90c27-a7d2-4f8d-80f8-b335ddc53033)

### Step 5: Create Docker Compose File
![Image](https://github.com/user-attachments/assets/0514ed47-4823-4610-b906-7ae2ae4e5561)

### Step 6: Deploy Locally with Docker
![Image](https://github.com/user-attachments/assets/8135659f-791f-4799-b11f-1e3606452d9e)
![Image](https://github.com/user-attachments/assets/92f24e5b-4b23-48fa-9398-31316923790b)

### Step 7: Testing Your Microservices
#### User Service: http://localhost:5000/users
![Image](https://github.com/user-attachments/assets/593d2eb6-19d5-4a8e-87a7-57d3a98f74e3)

#### Product Service: http://localhost:3000/products
![Image](https://github.com/user-attachments/assets/034b919f-d7f6-4f3e-991c-5e86ed2d3be9)
