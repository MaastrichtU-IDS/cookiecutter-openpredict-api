from {{cookiecutter.module_name}}.predict import get_predictions
from {{cookiecutter.module_name}}.train import train_model

input_id = "drugbank:DB00002"

def test_get_predictions():
    predictions = get_predictions(input_id)
    print(predictions)
    assert len(predictions["hits"]) > 0
    assert len(predictions["hits"]) == predictions["count"]


def test_train_model():
    loaded_model = train_model()
    assert loaded_model is not None
    # scores = loaded_model.scores
    # assert 0.80 < scores['precision'] < 0.95
    # assert 0.60 < scores['recall'] < 0.85
    # assert 0.80 < scores['accuracy'] < 0.95
    # assert 0.85 < scores['roc_auc'] < 0.95
    # assert 0.70 < scores['f1'] < 0.85
    # assert 0.75 < scores['average_precision'] < 0.95
