# topicsimilaritymodel-gravityai
Library to connect to the Topic Similarity Model on [Gravity AI](https://www.gravity-ai.com)

## Installation:

To install from pip, first clone this repository then:

```
pip install .
```

## Quick Example
-----------------

```python
import topicsimilaritymodel_gravityai

gravityai = topicsimilaritymodel_gravityai.Model('http://localhost:80')

response = gravityai.health()
print(response.text)

response = gravityai.addJob(testData)
print(response.text)

response = gravityai.getStatus("7f46ac5d-e398-4ca2-93b3-0531de7ea4b7")
print(response.text)

results = gravityai.getResult("7f46ac5d-e398-4ca2-93b3-0531de7ea4b7")
print(response.text)

response = gravityai.deleteJob("7f46ac5d-e398-4ca2-93b3-0531de7ea4b7")
print(response.text)

```