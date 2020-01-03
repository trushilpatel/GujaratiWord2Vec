from sklearn.manifold import TSNE
import pandas as pd
from sklearn.decomposition import PCA
from matplotlib import pyplot
import matplotlib.font_manager as mfm
import matplotlib.pyplot as plt
import numpy as np

import gensim
from gensim.models.word2vec import Word2Vec
from bokeh.io import output_notebook
from bokeh.plotting import show, figure

# for jupyter notebook
# remove following comment #
# %matplotlib inline

font_path = r"C:\Users\trush\OneDrive\Documents\Projects\Python\Word2Vec\Font\shruti.ttf"
prop = mfm.FontProperties(fname=font_path)

'''
Functions:-
	1	create_CSV_file(model,file_dir, file_name)
			-Library used: from sklearn.manifold import TSNE 
			
			-to create a CSV file of 2D,3D,etc. dimension of vocabulary word
			-file_dir = suitable directory for file 
			-file_name = suitable name for file
			-model = gensim trained Word2Vec model
	
	
	2	PCA_based_visualization(model)
			-Libarary used : from sklearn.decomposition import PCA
							 import matplotlib.pyplot as plt
			
			-model = gensim trained Word2Vec model
			-Principal Component Analysis based Dimension Reduction 
			
			
	3	TSNE_based_visualization(model)
			-Library used: from sklearn.manifold import TSNE , 
							 import matplotlib.pyplot as plt
		
			-model = gensim trained Word2Vec model
			-T-SNE based Dimension Reduction 	
'''


def create_CSV_file(model, file_dir, file_name):
    X = model.wv.__getitem__(model.wv.vocab)
    tsne = TSNE(n_components=2, n_iter=1000)  # 200 is minimum iter; default is 1000
    X_2d = tsne.fit_transform(X)

    # create DataFrame for storing results and plotting
    coords_df = pd.DataFrame(X_2d, columns=['x', 'y'])
    coords_df['token'] = model.wv.vocab.keys()
    coords_df.head()

    coords_df.to_csv(file_dir + "\\" + file_name + '.csv', index=False)
    print("\nCSV file of vocabulary saved successfully...")
    print("At location :" + file_dir + "\\" + file_name + ".csv")

    # coords_df = pd.read_csv(name_of_file + '.csv')
    # return coords_df


def PCA_based_visualization(model, dimension=2, vocabulary=None):  # more work ahead for dimension > 2):
    if vocabulary is None:
        X = model.wv.__getitem__(model.wv.vocab)
        word_labels = [i for i in model.wv.vocab]

    else:
        X = np.empty((0, 300), dtype='f')
        word_labels = vocabulary

        for wrd in word_labels:
            wrd_vector = model.wv.__getitem__(wrd)
            X = np.append(X, np.array([wrd_vector]), axis=0)

        np.set_printoptions(suppress=True)

    pca = PCA(n_components=2)
    result = pca.fit_transform(X)
    x_coords = result[:, 0]
    y_coords = result[:, 1]

    # create a scatter plot of the projection
    pyplot.scatter(x_coords, y_coords)

    for label, x, y in zip(word_labels, x_coords, y_coords):
        plt.text(x, y, s=label, fontproperties=prop)
        # plt.annotate((label), xy=(x, y), xytext=(0, 0), textcoords='offset points')
    plt.xlim(x_coords.min() + 0.00005, x_coords.max() + 0.00005)
    plt.ylim(y_coords.min() + 0.00005, y_coords.max() + 0.00005)
    plt.show()

    pyplot.show()


def TSNE_based_visualization(model, dimension=2, n_iter=1000, vocabulary=None,
                             method='barnes_hut', learning_rate=500,
                             perplexity=30):  # more work ahead for dimension > 2
    if vocabulary is None:
        X = model.wv.__getitem__(model.wv.vocab)
        word_labels = [i for i in model.wv.vocab]

    else:
        X = np.empty((0, 300), dtype='f')
        word_labels = vocabulary

        for wrd in word_labels:
            wrd_vector = model.wv.__getitem__(wrd)
            X = np.append(X, np.array([wrd_vector]), axis=0)

        np.set_printoptions(suppress=True)

    tsne = TSNE(n_components=dimension, n_iter=n_iter, random_state=0, perplexity=perplexity,
                learning_rate=learning_rate,
                method=method)  # 200 is minimum iter; default is 1000
    X_tsne = tsne.fit_transform(X)
    x_coords = X_tsne[:, 0]
    y_coords = X_tsne[:, 1]

    # display scatter plot
    plt.scatter(x_coords, y_coords)

    for label, x, y in zip(word_labels, x_coords, y_coords):
        plt.text(x, y, s=label, fontproperties=prop)
        # plt.annotate((label), xy=(x, y), xytext=(0, 0), textcoords='offset points')
    plt.xlim(x_coords.min() + 0.00005, x_coords.max() + 0.00005)
    plt.ylim(y_coords.min() + 0.00005, y_coords.max() + 0.00005)
    plt.show()


def jupyter_bokeh(file_loc):
    model = gensim.models.Word2Vec.load(file_loc)
    X = model.wv.__getitem__(model.wv.vocab)
    tsne = TSNE(n_components=3, n_iter=1000)  # 200 is minimum iter; default is 1000
    X_2d = tsne.fit_transform(X)

    # create DataFrame for storing results and plotting
    coords_df = pd.DataFrame(X_2d, columns=['x', 'y', 'z'])
    coords_df['token'] = model.wv.vocab.keys()

    _ = coords_df.plot.scatter('x', 'y', figsize=(12, 12), marker='.', s=10, alpha=0.2)
    output_notebook()  # output bokeh plots inline in notebook
    subset_df = coords_df.sample(n=len(X))

    p = figure(plot_width=800, plot_height=800)
    _ = p.text(x=subset_df.x, y=subset_df.y, text=subset_df.token)
    show(p)
