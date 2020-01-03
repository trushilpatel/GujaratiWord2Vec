import gensim

import numpy as np
import matplotlib.pyplot as plt

from sklearn.manifold import TSNE

# Load the save model

model = gensim.models.Word2Vec.load('SG.w2v')

print(len(model.wv.vocab))
# Simmilar word Cluster generater
def display_closestwords_tsnescatterplot(model, word):
    arr = np.empty((0, 300), dtype='f')
    word_labels = [word]

    # get close words
    close_words = model.wv.similar_by_word(word)
    print(close_words)
    # add the vector for each of the closest words to the array
    arr = np.append(arr, np.array([model.wv.__getitem__(word)]), axis=0)
    for wrd_score in close_words:
        print("wrd_score : \n",wrd_score)
        wrd_vector = model.wv.__getitem__(wrd_score[0])
        print("wrd vector : \n", wrd_vector)
        word_labels.append(wrd_score[0])
        arr = np.append(arr, np.array([wrd_vector]), axis=0)
    print(arr)

    # find tsne coords for 2 dimensions
    tsne = TSNE(n_components=2, random_state=0)
    np.set_printoptions(suppress=True)
    Y = tsne.fit_transform(arr)
    x_coords = Y[:, 0]

    y_coords = Y[:, 1]
    # display scatter plot
    plt.scatter(x_coords, y_coords)

    for label, x, y in zip(word_labels, x_coords, y_coords):
        plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords='offset points')
    plt.xlim(x_coords.min() + 0.00005, x_coords.max() + 0.00005)
    plt.ylim(y_coords.min() + 0.00005, y_coords.max() + 0.00005)
    #plt.show()

def close(model,vocabulary):
    arr = np.empty((0, 300), dtype='f')
    word_labels = vocabulary

    # get close words
    # add the vector for each of the closest words to the array
    for wrd in word_labels:
        wrd_vector = model.wv.__getitem__(wrd)
        arr = np.append(arr, np.array([wrd_vector]), axis=0)
    print(arr,vocabulary)

    tsne = TSNE(n_components=2, random_state=0)
    np.set_printoptions(suppress=True)
    Y = tsne.fit_transform(arr)
    x_coords = Y[:, 0]

    y_coords = Y[:, 1]
    # display scatter plot
    plt.scatter(x_coords, y_coords)

    for label, x, y in zip(word_labels, x_coords, y_coords):
        plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords='offset points')
    plt.xlim(x_coords.min() + 0.00005, x_coords.max() + 0.00005)
    plt.ylim(y_coords.min() + 0.00005, y_coords.max() + 0.00005)
    plt.show()


#display_closestwords_tsnescatterplot(model, 'a')
close(model,['for','an','a','and'])