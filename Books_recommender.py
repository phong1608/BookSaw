

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

df_books= pd.read_csv('dataset/books.csv')

def get_stopwords_list(stop_file_path):
    """load stop words """

    with open(stop_file_path, 'r', encoding="utf-8") as f:
        stopwords = f.readlines()
        stop_set = set(m.strip() for m in stopwords)
        return list(frozenset(stop_set))

stopwords = get_stopwords_list('dataset/vietnamese-stopwords.txt')

df_books.head()

df_books['description']

vectorizer = TfidfVectorizer(stop_words=stopwords)
df_books['description'] = df_books['description'].fillna('')
tfidf_matrix = vectorizer.fit_transform(df_books['description'])

consine_sim=linear_kernel(tfidf_matrix,tfidf_matrix)
consine_sim

indexs=pd.Series(df_books.index,index=df_books['name']).drop_duplicates()
indexs

def get_recommendation(title,consine_sim=consine_sim):
  index =indexs[title]
  sim_scores=enumerate(consine_sim[index])
  sim_scores= sorted(sim_scores,key= lambda x: x[1], reverse=True)
  sim_scores= sim_scores[1:5]
  sim_index=[i[0] for i in sim_scores]
  
  recommendation= df_books['name'].iloc[sim_index].tolist()
  return recommendation
