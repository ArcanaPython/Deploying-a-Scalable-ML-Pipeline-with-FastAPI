import pytest
# TODO: add necessary import
import pandas as pd
from ml.model import train_model, compute_model_metrics
from ml.data import apply_label
from sklearn.linear_model import LogisticRegression



# TODO: implement the first test. Change the function name and input as needed
def test_model_type():
    """
    Tests the model is a LogisticRegression sklearn model.
    """
    # Your code here
    X = pd.DataFrame({
        "col1": [1, 2, 3, 4, 5],
        "col2": [1, 1, 0, 0, 1]
    })
    y = [1, 1, 1, 0, 0]

    model = train_model(X, y)

    assert isinstance(model, LogisticRegression)
    


# TODO: implement the second test. Change the function name and input as needed
def test_metric_types():
    """
    Tests that compute_model_metrics returns float datatypes.
    """
    # Your code here
    y_true = [1, 1, 0, 1, 0]
    y_preds = [0, 1, 1, 0, 0]

    precision, recall, f1 = compute_model_metrics(y_true, y_preds)

    assert isinstance(precision, float)
    assert isinstance(recall, float)
    assert isinstance(f1, float)


# TODO: implement the third test. Change the function name and input as needed
def test_inference_labels():
    """
    Tests the string output of the inference label is correct from the 
    numerical input value.
    """
    # Your code here
    assert apply_label([1]) == ">50K"
    assert apply_label([0]) == "<=50K"
