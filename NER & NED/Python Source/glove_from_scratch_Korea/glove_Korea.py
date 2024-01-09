import numpy as np
from scipy.spatial.distance import cosine

# Define the list of Korean apartment names
apartment_names = ['반포자이', '아크로리버파크', '래미안퍼스티지', '서초그랑자이', '롯데캐슬클래식', '신반포']

# Tokenize the apartment names
tokenized_names = [name.split() for name in apartment_names]

# Create a co-occurrence matrix from the tokenized names
word_counts = {}
for name in tokenized_names:
    for word in name:
        if word not in word_counts:
            word_counts[word] = 0
        word_counts[word] += 1

vocab_size = len(word_counts)
co_occurrence_matrix = np.zeros((vocab_size, vocab_size))

for name in tokenized_names:
    for i, word in enumerate(name):
        for j in range(i - 5, i + 6):
            if j >= 0 and j < len(name) and i != j:
                co_occurrence_matrix[word_counts[word]-1][word_counts[name[j]]-1] += 1

# Train the GloVe model
np.random.seed(0)
embedding_size = 100
word_embeddings = np.random.rand(vocab_size, embedding_size) - 0.5
context_embeddings = np.random.rand(vocab_size, embedding_size) - 0.5
bias = np.random.rand(vocab_size) - 0.5
context_bias = np.random.rand(vocab_size) - 0.5
learning_rate = 0.05
epochs = 50

for epoch in range(epochs):
    cost = 0
    for i in range(vocab_size):
        for j in range(vocab_size):
            x_ij = co_occurrence_matrix[i][j]
            if x_ij > 0:
                weight = (x_ij / 5) ** 0.75
                diff = np.dot(word_embeddings[i], context_embeddings[j]) + bias[i] + context_bias[j] - np.log(x_ij)
                cost += weight * diff ** 2
                word_gradients = weight * diff * context_embeddings[j]
                context_gradients = weight * diff * word_embeddings[i]
                bias_gradients = weight * diff
                context_bias_gradients = weight * diff
                word_embeddings[i] -= learning_rate * word_gradients
                context_embeddings[j] -= learning_rate * context_gradients
                bias[i] -= learning_rate * bias_gradients
                context_bias[j] -= learning_rate * context_bias_gradients
    print("Epoch:", epoch + 1, "Cost:", cost)

# Save the trained model to disk
np.savez('korean_apartment_names_glove.npz', word_embeddings=word_embeddings, context_embeddings=context_embeddings, bias=bias, context_bias=context_bias)

