import spacy
import pandas as pd
import random
import difflib

# df = pd.read_csv('/Users/daewoong/Documents/서울대학교/NLP/연구 및 프로젝트/NER & NED/Geo Questions/newQuestions.csv')
# column = df['A']

# # randomly select ten sentences from the column
# num_sentences = 10
# sample_sentences = random.sample(list(column), num_sentences)

# # convert the selected sentences to a list
# sentence_list = [sentence for sentence in sample_sentences]

# print(sentence_list)

sentence_list = ['방배브라운가아파트와 가까운 지하철역은?', '임광3차아파트와 가까운 지하철역은?', '래미안서초에스티지S 아파트 근처 가장 가까운 지하철역 위치와 거리 3개씩 보여줘', '신번포8차아파트와 유사한 단지 보여줘', '롯데캐슬클래식아파트 실거래가 추이 알려줘', '우면한라 아파트 실거래가 추이 알려줘', '삼호한숲 아파트 평면도 보여줘', '래미안퍼스티지 아파트와 유사한 단지 보여줘', '진흥 아파트 평면도 보여줘', '서초푸르지오써밋 아파트와 유사한 단지 보여줘']

df = pd.read_csv('/Users/daewoong/Documents/서울대학교/NLP/연구 및 프로젝트/NER & NED/Korean word2Vec model/apt_info - apt_info.csv')
column_apt = df['n_apt_title']

apt_list = list(column_apt)


# print(apt_list)

# Load the pre-trained Korean model
nlp = spacy.load('ko_core_news_sm')

for element in sentence_list:
    # Process the text with the NLP pipeline
    doc = nlp(element)
    # Print the recognized entities and their labels
    for ent in doc.ents:
        print('인식된 개체:',ent.text,'|',ent.label_)
        closest_match = difflib.get_close_matches(ent.text, apt_list, n=1)
        if closest_match:
            print("Closest match:", closest_match[0])
        else:
            print("매치된 정보가 없습니다.")
        print('---------------------------------------------')
    
