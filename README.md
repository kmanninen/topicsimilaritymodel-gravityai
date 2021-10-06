# topicsimilaritymodel_gravityai
Library to connect to the Topic Similarity Model on [Gravity AI](https://www.gravity-ai.com)
## Use Cases
-----------------

 - Reducing large sets of unknown documents into smaller (manageable and prioritized) sets of related topics.
 - Topic classification
 - Enhancing unstructured data with structured values (great for visualizations) 
## Installation:
-----------------

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

response = gravityai.addJob(inputData)
print(response.text)

response = gravityai.getStatus("7f46ac5d-e398-4ca2-93b3-0531de7ea4b7")
print(response.text)

results = gravityai.getResult("7f46ac5d-e398-4ca2-93b3-0531de7ea4b7")
print(response.text)

response = gravityai.deleteJob("7f46ac5d-e398-4ca2-93b3-0531de7ea4b7")
print(response.text)

```



## Input
-----------------

This model requires three objects as input:

 1. __Training Documents:__ A list of sample texts (typically around 50-100 samples) that best represent the semantic style of the documents being analyzed. For example: If scholarly publications are being analyzed for a particular topic, then the training documents shall be a set of scholarly publications written in a semantically similar manner as the set of unknown scholarly documents that are to be analyzed.

 2. __Topic Text:__ The text of the topic that is the basis for the similarity search. Ideally, this text will contain one or more examples of documents that best convey the desired topic. Copying and pasting text from known documents is encouraged. A good rule of thumb is to remove any Proper Nouns (people names, locations, entities, etc) from this text - unless they are integral to the topic.

 3. __Documents:__ The set of unknown documents to be analyzed. This set shall include: a document id and the text of the document.

Here is a sample JSON Input:

```
{
	"trainingDocs": ["Document Text 1...", "Document Text 2...", "Document Text 3..."],
	"topicText": ["This is the example text of the topic being searched."],
	"documents": [{
		"id": "docID_1",
		"text": "This is the text of docID_1..."
	}, {
		"id": "docID_2",
		"text": "This is the text of docID_2..."
	}]
}
```

## Output
-----------------

This model will return a list of similarity scores for each document.

Here is a sample JSON Output:

```
{
	"documents": [{
		"id": "docID_1",
		"text": "This is the text of docID_1...",
		"similarityScore": 0.8483078479766846
	}, {
		"id": "docID_2",
		"text": "This is the text of docID_2...",
		"similarityScore": 0.9077356457710266
	}]
}
```