# https://www.geeksforgeeks.org/python-word-embedding-using-word2vec/

# Python program to generate word vectors using Word2Vec

# importing all necessary modules
from nltk.tokenize import sent_tokenize, word_tokenize
import warnings
from nltk.corpus import state_union

warnings.filterwarnings(action='ignore')

import gensim
from gensim.models import Word2Vec

# Reads file
sample = state_union.raw("2005-GWBush.txt").lower()


# Replaces escape character with space
f = sample.replace("\n", " ")


data = []

# iterate through each sentence in the file
for i in sent_tokenize(f):
    temp = []

    # tokenize the sentence into words
    for j in word_tokenize(i):
        temp.append(j.lower())

    data.append(temp)

print(data)

# Create CBOW model
model1 = gensim.models.Word2Vec(data, min_count=1,
                                size=100, window=5)

# Print results
print("Cosine similarity between 'george' " +
     "and 'bush' - CBOW : ",
      model1.similarity('george', 'bush'))

print("Cosine similarity between 'george' " +
     "and 'bush' - CBOW : ",
      model1.similarity('george', 'bush'))

# Create Skip Gram model
model2 = gensim.models.Word2Vec(data, min_count=1, size=100,
                                window=5, sg=1)

# Print results
print("Cosine similarity between 'president' " +
      "and 'bush' - Skip Gram : ",
      model2.similarity('president', 'bush'))

print("Cosine similarity between 'george' " +
      "and 'bush' - Skip Gram : ",
      model2.similarity('george', 'bush'))
