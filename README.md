# Census Income Prediction with ML Pipeline and FastAPI

This project demonstrates the development of a scalable machine learning pipeline, using FastAPI for model deployment. The pipeline trains a classification model on census data to predict whether an individual earns more than \$50K annually. The project includes data preprocessing, model training, performance monitoring on data slices, unit testing, and RESTful API deployment.

## Project Overview

### Key Features:
- **Data Preprocessing**: Clean and process census data using Python, ensuring readiness for model training.
- **Model Training**: Develop a machine learning model to classify income levels using scikit-learn.
- **Performance Monitoring**: Evaluate the model's performance on specific data slices, such as different education levels or work classes.
- **Unit Testing**: Implement tests to verify data integrity and model accuracy.
- **API Deployment**: Deploy the model using FastAPI, enabling real-time predictions via HTTP requests.

### Tools and Libraries:
- **Python**: Core programming language for data processing, model training, and API development.
- **scikit-learn**: Machine learning library used to build and train the model.
- **FastAPI**: Framework for creating the RESTful API and serving the machine learning model.
- **GitHub Actions**: Continuous integration (CI) setup to automatically run tests and ensure code quality.
- **pytest & flake8**: Testing and linting tools for ensuring code robustness and compliance with Python standards.
- **Pandas**: Used for handling and processing the Census Bureau dataset.
- **Conda/virtualenv**: Environment management to ensure consistency in dependencies.

## Project Steps:

1. **Data Exploration and Preprocessing**:
   - Load the Census dataset (`data/census.csv`).
   - Preprocess the data using functions in `ml/data.py`, ensuring proper formatting for training.
   
2. **Model Development**:
   - Train a classification model using `train_model.py`. The model predicts income based on features such as education, occupation, and age.
   - The pipeline includes training, testing, and saving the model for future inference.
   
3. **Model Evaluation**:
   - Evaluate model performance using standard metrics (Precision, Recall, F1-Score).
   - Implement performance tracking for specific data slices using the `performance_on_categorical_slice` function, generating insights for each unique categorical feature.
   
4. **Unit Testing**:
   - Test core components of the machine learning pipeline, including model training and prediction logic, using `test_ml.py`.
   
5. **API Deployment**:
   - Develop a RESTful API with FastAPI (`local_api.py`) that allows external users to interact with the trained model.
   - Implement GET and POST requests for API interactions.
   
6. **CI/CD**:
   - Set up GitHub Actions to automate testing and ensure code quality by running `pytest` and `flake8` on each push.

## Conclusion
This project demonstrates a full machine learning workflow, from data preprocessing to model deployment via a RESTful API. It showcases proficiency in Python, machine learning, API development, and best practices in CI/CD. The combination of model accuracy monitoring and real-time prediction through API calls makes it a scalable solution for production environments.

## License

[License](LICENSE.txt)
