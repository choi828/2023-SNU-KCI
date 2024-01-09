import numpy as np
from glove_Korea import *
# Load the saved GloVe model
model = np.load('korean_apartment_names_glove.npz')
word_embeddings = model['word_embeddings']
bias = model['bias']

# Define the input word
input_word = '신반포4차아파트'

# Get the index of the input word in the vocabulary
input_word_index = -1
for i, name in enumerate(tokenized_names):
    if input_word in name:
        input_word_index = i
        break

if input_word_index == -1:
    print("Input word not found in vocabulary")
else:
    # Calculate the cosine similarity between the input word and all other words in the vocabulary
    similarities = np.dot(word_embeddings, word_embeddings[input_word_index]) / (np.linalg.norm(word_embeddings, axis=1) * np.linalg.norm(word_embeddings[input_word_index]))

    # Print the top 5 most similar words
    top_indices = similarities.argsort()[::-1][1:6]
    print("Top 5 most similar words to", input_word + ":")
    for i in top_indices:
        print(apartment_names[i])
