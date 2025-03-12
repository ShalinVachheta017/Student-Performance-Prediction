# Student Performance Prediction

## Overview

This project leverages machine learning techniques to predict student performance based on various features such as gender, parental education level, and test preparation courses. The goal is to provide educators and stakeholders with insights to identify students who may need additional support.

## Features

- **Data Preprocessing:** Handling missing values, encoding categorical variables, and scaling features.
- **Model Training:** Implementing algorithms like Linear Regression, Decision Trees, and XGBoost.
- **Web Application:** A user-friendly Flask-based web app for real-time predictions.
- **Containerization:** Dockerized application for consistent deployment across environments.

## Getting Started

### Prerequisites

- **Docker:** Ensure Docker is installed. [Installation Guide](https://docs.docker.com/get-docker/)
- **Git:** For cloning the repository. [Installation Guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ShalinVachheta017/Student-Performance-Prediction.git
   cd Student-Performance-Prediction
   ```

2. **Build the Docker image:**
   ```bash
   docker build -t student-performance-app .
   ```

3. **Run the Docker container:**
   ```bash
   docker run -p 5000:5000 student-performance-app
   ```

4. **Access the web application:**
   Open your browser and navigate to `http://localhost:5000/`.

### Usage

- **Home Page(http://127.0.0.1:5000/):** Provides an overview and navigation links.
- **Prediction Page:(http://127.0.0.1:5000/predictdata  )** Input student data to receive performance predictions.

### Project Structure

```
Student-Performance-Prediction/
│
├── src/
│   ├── pipeline/
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   ├── __init__.py
│   └── ...
│
├── templates/
│   ├── index.html
│   └── home.html
│
├── application.py
├── Dockerfile
├── requirements.txt
└── README.md
```

- **`src/`**: Contains the core machine learning pipelines.
- **`templates/`**: HTML templates for the Flask web application.
- **`application.py`**: Main Flask application file.
- **`Dockerfile`**: Instructions to build the Docker image.
- **`requirements.txt`**: Python dependencies.

### Dockerization

The application is containerized using Docker to ensure consistency across different environments. This approach simplifies deployment and scaling.

**Building the Docker Image:**

```bash
docker build -t student-performance-app .
```

**Running the Docker Container:**

```bash
docker run -p 5000:5000 student-performance-app
```

These commands will set up the application in a Docker container, exposing it on port 5000.

### Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
