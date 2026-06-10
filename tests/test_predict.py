import sys
sys.path.append('.')

def test_mock():
    """Simple placeholder test - will be replaced with real model test later"""
    assert True

# More advanced test (optional):
# from transformers import pipeline
# 
# def test_model_loads():
#     classifier = pipeline("sentiment-analysis", model="mohdali1/distilbert-imdb-sentiment")
#     result = classifier("This movie was great!")
#     assert result[0]['label'] in ['POSITIVE', 'LABEL_1']
