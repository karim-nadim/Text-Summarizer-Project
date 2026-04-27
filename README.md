# 📝 End-to-End Text Summarizer (NLP & MLOps Pipeline)

Welcome to the **End-to-End Text Summarizer** project! 

This repository contains a production-ready Machine Learning pipeline designed to automatically generate concise summaries of conversational dialogues. It leverages state-of-the-art Natural Language Processing (NLP) models and industry-standard MLOps practices for orchestration, containerization, and automated cloud deployment.

---

## 🚀 Project Overview

The goal of this project is to take conversational text (like chat logs or customer support transcripts) and condense them into meaningful summaries. 

*   **Dataset:** [SAMSum Dataset](https://huggingface.co/datasets/samsum) (Messenger-like dialogues with human-annotated summaries).
*   **Base Model:** Fine-tuned `DistilBART` (Sequence-to-Sequence LM) using Hugging Face Transformers.
*   **Interface:** A RESTful API built with **FastAPI** to trigger training and serve predictions.
*   **Deployment:** Automated via **GitHub Actions** to an **AWS EC2** instance using **Docker** and AWS ECR.

---

## 🛠️ Tech Stack & Tools

*   **Machine Learning & NLP:** PyTorch, Hugging Face (`transformers`, `datasets`, `evaluate`)
*   **Backend & API:** Python 3.11, FastAPI, Uvicorn
*   **MLOps & Orchestration:** DVC (Data Version Control)
*   **Containerization & Deployment:** Docker, AWS ECR, AWS EC2
*   **CI/CD:** GitHub Actions (Automated Linting, Testing, and Deployment)

---

## 🧠 Machine Learning Pipeline Architecture

The core of this project is a highly modular, 4-stage Machine Learning pipeline. Each stage is strictly decoupled, ensuring maintainability and reproducibility.

1.  **Stage 1: Data Ingestion (`data_ingestion.py`)**
    *   Automatically fetches the raw SAMSum dataset from the Hugging Face hub or a remote URL.
    *   Saves the data locally as artifacts for the next stages.
2.  **Stage 2: Data Transformation (`data_transformation.py`)**
    *   Converts human-readable text into machine-readable numerical representations.
    *   Utilizes the DistilBART Tokenizer to process dialogues and summaries into padded/truncated token arrays.
3.  **Stage 3: Model Training (`model_trainer.py`)**
    *   Fine-tunes the pre-trained `DistilBART` sequence-to-sequence model on the tokenized data.
    *   Hyperparameters (Epochs, Batch Size, Weight Decay, etc.) are strictly controlled and easily adjustable via `params.yaml`.
4.  **Stage 4: Model Evaluation (`model_evaluation.py`)**
    *   Evaluates the newly trained model against unseen test data.
    *   Calculates the **ROUGE** score (ROUGE-1, ROUGE-2, ROUGE-L, ROUGE-Lsum) to quantitatively measure the quality of the generated summaries against human references.

---

## ⚙️ Orchestration with DVC (Data Version Control)

Running an entire ML pipeline every time a small change is made is computationally expensive. This project utilizes **DVC** to solve this:

- **Pipeline Tracking:** `dvc.yaml` defines the inputs, dependencies, and outputs of every stage.
- **Smart Execution:** If you run `dvc repro`, DVC automatically detects which stages have changed (e.g., changing a hyperparameter). It will *only* re-run the Model Training and Evaluation stages, entirely skipping Data Ingestion and Transformation to save time and compute resources.
- **DAG Visualization:** Run `dvc dag` in the terminal to visually inspect the pipeline's dependency graph.

---

## 💻 How to Run Locally

Follow these steps to set up the project on your local machine.

### Step 1: Clone the Repository
```bash
git clone https://github.com/karim-nadim/Text-Summarizer-Project.git
cd Text-Summarizer-Project
```

### Step 2: Create a Virtual Environment
It is highly recommended to use Conda for dependency management.
```bash
conda create -n summary python=3.11 -y
conda activate summary
```

### Step 3: Install Requirements
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```
*The FastAPI server will start. Open your browser and navigate to `http://localhost:8080/docs` to interact with the Swagger UI.*

---

## 🌐 API Endpoints & Usage

Once the application is running, you can access the following REST endpoints:

*   `GET /`: Redirects to the FastAPI interactive documentation (Swagger UI).
*   `GET /train`: Triggers the end-to-end `main.py` pipeline. This will execute Data Ingestion, Transformation, Training, and Evaluation sequentially.
*   `POST /predict`: Accepts a text payload, passes it through the fine-tuned DistilBART model, and returns a summarized string.

---

## ☁️ CI/CD & AWS Cloud Deployment

This project features a fully automated Continuous Integration and Continuous Deployment (CI/CD) pipeline built with **GitHub Actions**. Every push to the `main` branch triggers the following workflow:

### 1. Continuous Integration (CI)
*   **Setup:** Provisions an Ubuntu runner and sets up Python 3.11.
*   **Linting:** Runs `flake8` to ensure code quality and adherence to PEP-8 standards.
*   **Testing:** Runs `pytest` to execute unit tests and ensure code reliability.

### 2. Continuous Delivery (CD)
*   **AWS Authentication:** Securely authenticates with AWS using GitHub Secrets.
*   **Dockerization:** Builds a Docker Image of the application.
*   **ECR Push:** Tags and pushes the Docker container to an **Amazon ECR** (Elastic Container Registry) repository.

### 3. Continuous Deployment (CD)
*   **Self-Hosted Runner:** An **Amazon EC2** (Ubuntu) instance listens for successful builds.
*   **Pull & Run:** The EC2 instance automatically pulls the latest Docker image from ECR, stops the old container, and starts the new one, exposing the API to the web on port `8080`.

### Setting up AWS for this project:
If you are forking this repo and want to replicate the AWS deployment, ensure you have:
1.  Created an IAM User with `AmazonEC2FullAccess` and `AmazonEC2ContainerRegistryFullAccess`.
2.  Created an ECR Repository named `textsummarization`.
3.  Launched an EC2 Ubuntu Instance, installed Docker, and configured it as a GitHub Self-Hosted Runner.
4.  Added the following GitHub Repository Secrets:
    *   `AWS_ACCESS_KEY_ID`
    *   `AWS_SECRET_ACCESS_KEY`
    *   `AWS_REGION`
    *   `AWS_ECR_LOGIN_URI`
    *   `ECR_REPOSITORY_NAME`

---

## 📂 Project Structure

```text
Text-Summarizer-Project/
│
├── .github/workflows/main.yaml   # CI/CD Pipeline configuration
├── src/textSummarizer/
│   ├── components/               # Core ML Pipeline steps
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   └── model_evaluation.py
│   ├── pipeline/                 # Pipeline execution scripts
│   ├── utils/                    # Helper functions (e.g., read_yaml)
│   └── logging/                  # Custom logging configuration
│
├── config/config.yaml            # File paths and artifact directories
├── params.yaml                   # Hyperparameters for model training
├── dvc.yaml                      # DVC orchestration graph
├── app.py                        # FastAPI web server and endpoints
├── main.py                       # Pipeline execution entry point
├── Dockerfile                    # Containerization instructions
└── requirements.txt              # Python dependencies
```

---

## 👨‍💻 Author

**Karim Nadim**  
Data Scientist & Machine Learning Engineer  
📧 Email: karim_ossama94@hotmail.com  
🔗 GitHub: karim-nadim
