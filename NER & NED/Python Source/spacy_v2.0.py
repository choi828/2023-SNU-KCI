from nltk import word_tokenize, pos_tag, ne_chunk

sentence = "Daewoong is studying at Seoul National University"
# 토큰화 후 품사 태깅
tokenized_sentence = pos_tag(word_tokenize(sentence))
print(tokenized_sentence)

# 개체명 인식
ner_sentence = ne_chunk(tokenized_sentence)
print(ner_sentence)