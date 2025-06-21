# Medical Insurance Price Prediction

![Project Demo](https://drive.google.com/uc?id=1m3Mj4DXNAgCuYWRSgxzcbPF0o9rheMaC)

## Introduction

This project is a web application that predicts medical insurance costs for individuals based on their personal attributes. It features an interactive, user-friendly interface where users can input their information—such as age, sex, BMI, and smoking habits—to receive an instant price estimate. The project combines a robust machine learning model with a responsive web front-end to provide a seamless user experience.

## Project Goals

*   **Predictive Accuracy:** To build and deploy a reliable machine learning model that accurately predicts medical insurance charges.
*   **User Experience:** To create an intuitive and responsive web interface that makes it easy for users to get predictions.
*   **Educational Tool:** To serve as a demonstration of a full-stack machine learning application, from data analysis and model training to deployment.
*   **Transparency:** To provide users with information about the dataset and the factors that influence insurance costs.

## Technologies Used

This project is built with a combination of data science and web development technologies:

| Category          | Technology / Library | Version    |
| ----------------- | -------------------- | ---------- |
| **Backend**       | Flask                | (latest)   |
| **ML & Data**     | NumPy                | `1.23.5`   |
|                   | Pandas               | `1.5.3`    |
|                   | Scikit-learn         | `1.2.2`    |
|                   | SciPy                | `1.10.1`   |
| **ML Models**     | XGBoost              | `1.7.3`    |
|                   | LightGBM             | `3.3.5`    |
|                   | CatBoost             | `1.1.1`    |
| **Visualization** | Matplotlib           | `3.7.1`    |
|                   | Seaborn              | `0.12.2`   |
|                   | Plotly               | `5.13.1`   |
| **Explainability**| SHAP                 | `0.41.0`   |
| **Frontend**      | HTML, CSS, JavaScript|            |


## Dataset

The model is trained on the **"Medical Cost Personal Datasets"** from Kaggle. This dataset contains 1,338 observations with the following attributes:

*   **`age`**: Age of the primary beneficiary.
*   **`sex`**: Gender of the beneficiary (female, male).
*   **`bmi`**: Body Mass Index, a measure of body fat.
*   **`children`**: Number of children/dependents covered by the insurance.
*   **`smoker`**: Whether the person is a smoker (yes, no).
*   **`region`**: The beneficiary's residential area in the US (northeast, southeast, southwest, northwest).
*   **`charges`** (Target): Individual medical costs billed by health insurance.

The complete data analysis and visualization can be found in the `Visualisations (EDA).ipynb` notebook.

## Model

The prediction model is an XGBoost Regressor. 
- The target variable (`charges`) was log-transformed (`log(x+1)`) to handle its skewness, a common practice for price prediction. 
- The categorical features (`sex`, `smoker`, `region`) were converted into a numerical format for the model.

## How It Works

### Model Training Workflow

The entire process of building the predictive model is detailed in the project's Jupyter Notebooks and follows these steps:

![Model Training Workflow](https://drive.google.com/uc?id=1xtPPDI__XNsiX0zbxq4u8C8DrcvVPOwB)

1.  **Data Collection:** The process begins by loading the medical insurance dataset.
2.  **Exploratory Data Analysis (EDA):** The dataset is thoroughly analyzed to understand feature distributions, correlations, and initial patterns. This is covered in `Visualisations (EDA).ipynb`.
3.  **Data Preprocessing:**
    *   **Handling Missing Values & Outliers:** The data is cleaned by addressing any missing values and handling outliers.
    *   **Feature Transformation:** The target variable (`charges`) is log-transformed to handle its skewness.
    *   **Encoding:** Categorical features like `sex`, `smoker`, and `region` are converted into numerical formats.
4.  **Data Splitting:** The dataset is split into an 80% training set and a 20% testing set.
5.  **Model Selection:** Ten different regression models were evaluated, including `Random Forest`, `XGBoost`, `LightGBM`, and `Linear Regression`.
6.  **Model Training:** The models are trained on the preprocessed data. Hyperparameter tuning and K-Fold cross-validation are used to optimize performance.
7.  **Model Evaluation:** Models are evaluated using a comprehensive set of metrics: MSE, RMSE, MAE, MAPE, R², Adjusted R², and the best cross-validation score.
8.  **Best Model Selection:** The model with the best performance (XGBoost) is selected for deployment.
9.  **Model Interpretability:** SHAP (SHapley Additive exPlanations) analysis is used to understand the model's predictions and explain the impact of each feature on the final insurance price prediction.


## Why It Matters

Understanding potential healthcare costs is crucial for financial planning. This tool provides a quick and accessible way for individuals to get a data-driven estimate of their medical insurance expenses. For developers and data scientists, this project serves as a practical, end-to-end example of how to build and deploy a machine learning model as a web service.

## How to Run This Project Locally

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/lalith-kumar-raju/Medical-Insurance-Price-Prediction.git
    cd Medical-Insurance-Price-Prediction
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask application:**
    ```bash
    python app.py
    ```

5.  Open your web browser and go to `http://127.0.0.1:5000/` to use the application.

## ✍️ Author

Made with ❤️ by **Lalith kumar raju Somalaraju**.

Connect with me:

*   [<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />](https://github.com/lalith-kumar-raju)
*   [<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/lalith-kumar-raju-somalaraju/)
*   [<img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" />](https://www.instagram.com/_lalith_kumar_raju_/)
*   [<img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" />](mailto:ssivaprasadraju1978@gmail.com)

--- 