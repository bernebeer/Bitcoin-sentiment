import textrazor

# Get textrazor app key credentials from external file
from dev_settings import *

textrazor.api_key = textrazor_api_key

client = textrazor.TextRazor(extractors=["entities", "topics"])

client.set_cleanup_mode("cleanHTML")

response = client.analyze_url("http://edition.cnn.com/")

for entity in response.entities():
    print(entity.id, entity.relevance_score, entity.confidence_score, entity.freebase_types)