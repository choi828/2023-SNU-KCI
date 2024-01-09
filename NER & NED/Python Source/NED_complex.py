import spacy
from spacy import displacy
from spacy.tokens import Span
from spacy.vocab import Vocab
from spacy.pipeline import EntityLinker
from spacy.kb import KnowledgeBase
import requests

# Define the text to be analyzed
text = "Apple is looking at buying U.K. startup for $1 billion"

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Add the entity linker to the pipeline
if "entityLinker" not in nlp.pipe_names:
    # Create a new vocab to store the entity linker
    entity_vocab = Vocab()

    # Create a new knowledge base using the Wikidata knowledge graph
    kb = KnowledgeBase(vocab=entity_vocab, entity_vector_length=300)

    # Add entities and aliases to the knowledge base
    kb.set_entities([{"id": "Q312", "label": "Apple"},
                     {"id": "Q8337", "label": "United Kingdom"},
                     {"id": "Q380073", "label": "Startup"}])
    kb.set_aliases(
        [
            {"alias": "Apple Inc.", "entities": [0]},
            {"alias": "the U.K.", "entities": [1]},
            {"alias": "British", "entities": [1]},
            {"alias": "a British", "entities": [1]},
            {"alias": "startup", "entities": [2]},
            {"alias": "a startup", "entities": [2]},
        ]
    )

    # Create a new entity linker using the Wikidata knowledge base
    linker = EntityLinker(
        name="entityLinker",
        vocab=entity_vocab,
        kb=kb,
        entity_vector_length=300,
        default_label="UNKNOWN",
        labels_discard=["MISC"],
        n_sents=5,
        incl_prior=True,
        incl_context=True,
        get_candidates=None,
        get_candidates_batch=None,
        generate_empty_kb=False,
        use_gold_ents=False,
        candidates_batch_size=32,
    )

    # Add the entity linker to the pipeline
    nlp.add_pipe(linker)

# Define the entity labels to search for
entity_labels = ["PERSON", "ORG", "GPE"]

# Apply the spaCy model to the text
doc = nlp(text)

# Iterate over the entities identified in the text
for ent in doc.ents:
    # Check if the entity label is in the list of entity labels to search for
    if ent.label_ in entity_labels:
        # Get the top entity for the entity mention
        entity = linker.predict([ent])[0]
        # Get the Wikipedia URL for the entity
        wikipedia_url = requests.get(f"https://www.wikidata.org/entity/{entity}").json()["sitelinks"]["enwiki"]["url"]
        # Print the entity and its Wikipedia URL
        print(ent.text, wikipedia_url)
