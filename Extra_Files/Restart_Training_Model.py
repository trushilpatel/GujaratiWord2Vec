# Python program to generate word vectors using Word2Vec

from nltk.tokenize import sent_tokenize, word_tokenize
import warnings
import gensim
from gensim.models import Word2Vec

warnings.filterwarnings(action='ignore')

# from User Defined python file
from utils.Visualize import PCA_based_visualization


def skip_gram_model_restart_training(data_file, model, model_name, start_line, end_line):
    data = need_for_data_restart_training(data_file, start_line, end_line)

    print("\nSKIP GRAM\n" + "=" * 15)
    print("Restarted Training " + model_name + "using Skip Gram ")

    model.train(data,total_examples=model.corpus_count, epochs=1)
    model.save('Trained_models\\' + model_name )
    print("Total Training Time :", model.total_train_time)


def cbow_restart_training(data_file, model, model_name, start_line, end_line):
    data = need_for_data_restart_training(data_file, start_line, end_line)

    print("\nCBOW\n" + "=" * 15)
    print("Restarted Training" + model_name + " using CBOW ")
    model.train(data, min_count=1, size=300, window=5)
    model.save('Trained_models\\' + model_name + '_CBOW.w2v')
    print("Total Training Time :", model.total_train_time)


def need_for_data_restart_training(file_name, start_line, end_line):
    # file : txt file as input
    # lines : number of line for training model
    total_words = int()
    file = open(file_name, 'rt', encoding="UTF-8")
    sample = str()

    for i in range(start_line, end_line + 1):
        sample += file.readline(i)

    f = sample.replace("\n", " ")  # Replaces escape character with space
    data = []

    for i in sent_tokenize(f):  # iterate through each sentence in the file
        temp = []
        for j in word_tokenize(i):  # tokenize the sentence into words
            temp.append(j.lower())
        data.append(temp)
        total_words += len(temp)

    # find total numbers of line in file
    file.seek(0, 0)
    print("\nTotal No of Lines in FILE :", (len(file.readlines())))
    print("Total No of Lines used for training model :", end_line - start_line + 1)
    print("Total No of words used for training model :", total_words)
    return data


def load_model(model_name):
    model = gensim.models.Word2Vec.load('Trained_models\\' + model_name)
    return model


def cosine_similarity(word1, word2, cbow_model, sg_model):
    print("Cosine similarity between " + word1 + " and " + word2 + " - CBOW : ", cbow_model.wv.similarity(word1, word2))
    print("Cosine similarity between " + word1 + " and " + word2 + " - Skip Gram : ",
          sg_model.wv.similarity(word1, word2))


#data @ C:\Users\trush\OneDrive\Documents\Projects\Python\Word2Vec\DataSet\Whole_GujaratiWikipediaArticles.txt
'''
model_name = input("Enter the name of Model : ")
data_file = input("Enter the location of DataSet file : ")
start_line = int(input("Enter the Starting line number : "))
end_line = int(input("Enter the Ending line number : "))
'''
model_name = "5000_SG.w2v"
data_file = r"C:\Users\trush\OneDrive\Documents\Projects\Python\Word2Vec\DataSet\Whole_GujaratiWikipediaArticles.txt"
start_line = 6001
end_line = 7000


# Visualization
# TSNE_based_visualization(model_name + "_SG.w2v")
PCA_based_visualization(gensim.models.Word2Vec.load('Trained_models\\' + model_name ))


#SG_model = gensim.models.Word2Vec.load('Trained_models\\' + model_name)
#CBOW_model = gensim.models.Word2Vec.load('Trained_models\\' + model_name)
#cosine_similarity('ગુજરાત', 'ભારત', CBOW_model, SG_model)


#skip_gram_model_restart_training(data_file,SG_model,model_name, start_line , end_line)

#PCA_based_visualization(gensim.models.Word2Vec.load('Trained_models\\' + model_name ))

'''
print("MOst Similar to ગુજરાત : \n" , SG_model.most_similar("ગુજરાત"),"\n\n")
print("MOst Similar to ગુજરાતનો : \n", SG_model.most_similar("ગુજરાતનો"),"\n\n")
print("MOst Similar to ભારત : \n", SG_model.most_similar("ભારત"),"\n\n")

'''