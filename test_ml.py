import pytest
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import fbeta_score, precision_score, recall_score
from ml.model import train_model, compute_model_metrics
from ml.data import process_data

# Dummy dataset for testing
dummy_data = pd.DataFrame(
    {
        "feature_1": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "feature_2": [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        "feature_3": [5, 4, 3, 2, 1, 5, 4, 3, 2, 1],
        "feature_4": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        "label": [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    }
)

categorical_features = ['feature_1', 'feature_2']

# Split and process dummy data
train, test = train_test_split(dummy_data, test_size=0.2, random_state=56)

X_train, y_train, encoder, lb = process_data(train,
                                             categorical_features=categorical_features,
                                             label="label",
                                             training=True)
X_test, y_test, _, _ = process_data(test,
                                    categorical_features=categorical_features,
                                    label="label",
                                    training=False,
                                    encoder=encoder,
                                    lb=lb,)

def test_data_splits():
    """
    # Test if the split and processed training and test datasets have the expected data type and size
    """
    assert isinstance(X_train, np.ndarray)
    assert isinstance(X_test, np.ndarray)
    assert isinstance(y_train, np.ndarray)
    assert isinstance(y_test, np.ndarray)
    assert X_train.shape[0] == .8 * dummy_data.shape[0]
    assert X_test.shape[0] == .2  * dummy_data.shape[0]


def test_train_model():
    """
    # Test if the train_model function returns a GradientBoostingClassifier type
    """
    model = train_model(X_train, y_train)
    assert isinstance(model, GradientBoostingClassifier)


def test_compute_model_metrics():
    """
    # Test if the compute_model_metrics function returns the expected values
    """
    model = train_model(X_test, y_test)
    y_preds = model.predict(X_test)
    precision, recall, fbeta = compute_model_metrics(y_test, y_preds)
    
    # Compute metrics separately
    expected_precision = precision_score(y_test, y_preds)
    expected_recall = recall_score(y_test, y_preds)
    expected_fbeta = fbeta_score(y_test, y_preds, beta=1)

    # Assert the function returns the correct values
    assert precision == expected_precision
    assert recall == expected_recall
    assert fbeta == expected_fbeta
