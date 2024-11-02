# Breast Cancer Diagnosis using Machine Learning

This project provides a web application for breast cancer diagnosis using machine learning techniques. The application allows users to input various medical parameters and receive a prediction of whether the tumor is benign or malignant.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Model](#model)
- [Deployment](#deployment)
- [Screenshots](#screenshots)
- [Video Demonstration](#video-demonstration)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Features
- User-friendly interface built with Streamlit.
- Input various features related to breast cancer.
- Predicts whether the tumor is benign or malignant using a trained machine learning model.

## Technologies Used
- **Streamlit**: For creating the web application.
- **Pandas**: For data manipulation and analysis.
- **Joblib**: For loading the trained machine learning model.
- **NumPy**: For numerical operations.
- **Seaborn & Matplotlib**: For data visualization.
- **Scikit-learn**: For machine learning algorithms.
- **XGBoost**: For implementing the XGBoost model.

## Installation
To run this application, you need to have Python installed on your machine. Follow these steps to set up the project:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/breast-cancer-diagnosis.git
    cd breast-cancer-diagnosis
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and navigate to `http://localhost:8501` to access the application.

3. Input the required features and click on the "Diagnose" button to get the prediction.

## Data
The dataset used in this project is `breast-cancer.csv`, which contains various features related to breast cancer tumors. The model is trained to classify tumors as either benign or malignant based on these features.

## Model
The machine learning model is trained using several classifiers, including Logistic Regression, Decision Trees, Random Forests, and XGBoost. The final model is saved as `model.pkl` using the joblib library.

## Deployment
You can access the deployed web application [here](https://breast-cancer-prediction-model.streamlit.app/).

## Screenshots
Below are some screenshots of the application:

![Application Screenshot 1](https://github.com/user-attachments/assets/17ae0a22-c0d9-46dd-9083-10bcc564a857)
![Application Screenshot 2](https://github.com/user-attachments/assets/9f96452a-636f-486c-88ed-d7e3accf5f79)

## Video Demonstration
Watch a video demonstration of the application [here](https://github.com/user-attachments/assets/9bb35bca-0579-49cb-9413-cdff36402dea) or directly below:

[![Watch the video](https://img.youtube.com/vi/9bb35bca-0579-49cb-9413-cdff36402dea/0.jpg)](https://github.com/user-attachments/assets/9bb35bca-0579-49cb-9413-cdff36402dea)

## Contributing
Contributions are welcome! If you have suggestions for improvements or want to add new features, please fork the repository and create a pull request.

## License
This project is licensed under the MIT License .

## Author
You can connect with me on [LinkedIn](https://www.linkedin.com/in/rufyda-rahma-96b656179/).
