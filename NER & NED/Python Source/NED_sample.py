import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Define the function to get the Wikipedia URL for an entity
def get_wikipedia_url(entity):
    if entity.label_ in ["PERSON", "ORG", "GPE", "LOC"]:
        # Replace spaces with underscores in entity text for URL
        entity_text = entity.text.replace(" ", "_")
        # Construct the Wikipedia URL for the entity
        return f"https://en.wikipedia.org/wiki/{entity_text}"
    else:
        return None

# Register the 'wikipedia_url' attribute as an extension
spacy.tokens.Span.set_extension("wikipedia_url", getter=get_wikipedia_url)

# Define the text to be analyzed
text = ["Matt ate an apple for breakfast.", "John works at Apple.", 
        "George Washington was the first U.S. President.", "Seattle is in Washington", 
        "David loves working at Amazon.", "Humidity of the Amazon River is very high", 
        "find the restaurant near the Trump Tower"]

for sentence in text:
    doc = nlp(sentence)
    # Iterate over the entities identified in the text
    for ent in doc.ents:
        # Check if the entity is a person, organization and geo-political entity
        if ent.label_ in ["PERSON", "ORG", "GPE", "LOC"]:
            # Print the entity and its Wikipedia URL (if available)
            print(ent.text, ent.label_, ent._.wikipedia_url)
