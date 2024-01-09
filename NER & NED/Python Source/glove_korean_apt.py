import gensim
import numpy as np

# Load the GloVe model
glove_model = gensim.models.KeyedVectors.load_word2vec_format('path/to/glove/model', binary=False)

# List of Korean apartment names
apartment_names = ['반포자이', '아크로리버파크', '래미안퍼스티지', '서초그랑자이', '롯데캐슬클래식', '신반포']

# Preprocess the input
input_text = '신반포2차'
input_tokens = input_text.lower().split()

# Calculate the cosine similarity
max_score = -1
matched_entity = None
for name in apartment_names:
    name_tokens = name.lower().split()
    name_vector = np.mean([glove_model[token] for token in name_tokens if token in glove_model.vocab], axis=0)
    input_vector = np.mean([glove_model[token] for token in input_tokens if token in glove_model.vocab], axis=0)
    cosine_similarity = np.dot(name_vector, input_vector) / (np.linalg.norm(name_vector) * np.linalg.norm(input_vector))
    if cosine_similarity > max_score:
        max_score = cosine_similarity
        matched_entity = name

# Return the matched entity
print('Matched entity:', matched_entity)