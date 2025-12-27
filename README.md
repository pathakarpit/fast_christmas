# Fast Christmas: Production-Grade ML Inference Service
Fast Christmas is a high-performance, containerized microservice built to deliver real-time car price predictions through a robust FastAPI backend. The project demonstrates a full-lifecycle engineering approach, from an automated machine learning pipeline to secure, observable deployment in a microservices environment.

## Engineering Highlights
Automated ML Pipeline & Persistence: Developed a structured training workflow using Scikit-Learn pipelines, incorporating ColumnTransformer for automated numerical scaling and categorical encoding. The final Random Forest Regressor is persisted via joblib for seamless integration into the inference service.

### High-Performance Caching: 
Optimized API latency by implementing a Redis caching layer. The service intelligently caches prediction results based on input feature hashes, significantly reducing redundant compute cycles for recurring queries.

### Enterprise-Grade Security: 
Architected a dual-layer security model utilizing JWT (JSON Web Tokens) for user session management and custom Header-based API Key validation for secure service-to-service communication.

### Full-Stack Observability: 
Integrated a comprehensive monitoring suite using Prometheus and Grafana. The service exports real-time performance metrics via prometheus-fastapi-instrumentator and includes custom logging middleware to track request/response lifecycles.

### Microservices Architecture: 
Fully containerized using Docker and Docker Compose, orchestrating the API, Redis, Prometheus, and Grafana into a cohesive, scalable backend.

### Resilient Design: 
Implemented global exception handling and structured Pydantic data validation to ensure API stability and consistent error reporting (500-series handling).

## Tech Stack
### Backend: 
Python 3.12, FastAPI, Pydantic, Uvicorn.

### Machine Learning: 
Scikit-Learn (Random Forest), Pandas, Joblib.

### Data & Infrastructure: 
Redis (Caching), Docker, Docker Compose.

### DevOps & Monitoring: 
Prometheus, Grafana, Starlette Middleware.

### Security: 
Python-Jose (JWT), Dotenv.

---

## Getting Started (Local)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/fastapi-project.git
cd fastapi-project
```

### 2. Set Environment Variables

```bash
API_KEY=demo-key
JWT_SECRET_KEY=your-secret
REDIS_URL=redis://localhost:6379
```

### 3. Build and Run via Docker

```bash
docker-compose up --build
```

### 4. Access Interfaces

- FastAPI Docs: http://localhost:8000/docs
- FastAPI Metrics: http://localhost:8000/metrics
- Prometheus UI: http://localhost:9090
- Grafana UI: http://localhost:3000

---
