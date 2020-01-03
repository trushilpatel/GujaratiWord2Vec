# Python program to generate word vectors using Word2Vec

from nltk.tokenize import sent_tokenize, word_tokenize
import warnings
import gensim

warnings.filterwarnings(action='ignore')


def gujarati_line_with_quote(line):
    index = 0
    le = 0
    quotes = 0
    final_list = list()
    temp = str()
    for i in range(len(line)):
        le += 1
        if '"' == line[i]:
            quotes += 1
            if quotes == 2:
                temp = line[index:i].strip()

                if temp is not '':
                    final_list.append(temp)
                quotes = 0
            else:
                temp = line[index:i].split()
                for j in temp:
                    j_temp = j.strip()
                    if temp is not '':
                        final_list.append(j)
            index = i + 1

    if index < le:
        temp = line[index:le].split()
        for i in temp:
            final_list.append(i.strip())
    return final_list


def pure_gujarati_need_for_data(dataset_file_loc, string_based=0, lines=None):
    sample, lines = need_for_data_sample(dataset_file_loc, string_based, lines)
    f = sample.replace("\n", ".")  # Replaces escape character with space
    L = f.split('.')

    final_list = list()

    for i in range(len(L)):
        if '"' in L[i]:
            final_list.append(gujarati_line_with_quote(L[i]))
        else:
            if L[i] is not "":
                final_list.append(L[i].split())
    return final_list


def need_for_data_sample(file_loc, string_based, lines=None):
    if string_based is 0:
        file = open(file_loc, 'rt', encoding="UTF-8")
        if lines is None:
            lines = len(file.readlines())
        sample = str()
        file.seek(0, 0)
        for i in range(lines):
            sample += file.readline()
    else:
        sample = input("Enter String ")
    return sample, lines


def need_for_data(file_loc, string_based, lines=None):
    sample, lines = need_for_data_sample(file_loc, string_based, lines=lines)
    f = sample.replace("\n", " ")  # Replaces escape character with space
    data = []
    total_words = int()

    for i in sent_tokenize(f):  # iterate through each sentence in the file
        temp = []
        for j in word_tokenize(i):  # tokenize the sentence into words
            temp.append(j.lower())
        data.append(temp)
        total_words += len(temp)

    # find total numbers of line in file
    file = open(file_loc, 'rt', encoding="UTF-8")
    print("\nTotal No of Lines in FILE :", (len(file.readlines())))
    print("Total No of Lines used for training model :", lines)
    print("Total No of words used for training model :", total_words)
    return data


def skip_gram_model(dataset_file_loc, model_name, file_dir_to_save, string_based=0, lines=None, hs=0, pure_gujarati=0):
    if pure_gujarati is 1:
        data = pure_gujarati_need_for_data(dataset_file_loc=dataset_file_loc, lines=lines, string_based=string_based)
    else:
        data = need_for_data(dataset_file_loc, lines=lines, string_based=string_based)

    print("\nSKIP GRAM\n" + "=" * 15)
    print("Training Model using Skip Gram ")
    sg_model = gensim.models.Word2Vec(data, min_count=1, size=300, window=5,
                                      sg=1, workers=1, hs=hs)  # add worker in argument for multi threading
    sg_model.save(file_dir_to_save + '\\' + model_name)  # to save the trained model
    print("\nTotal Training time : ", sg_model.total_train_time)
    print("SKIP GRAM MODEL saved successfully...")
    print("At location :" + file_dir_to_save + "\\" + model_name )


def cbow(dataset_file_loc, model_name, file_dir_to_save, string_based=0, lines=None, hs=0, pure_gujarati=0):
    if pure_gujarati is 1:
        data = pure_gujarati_need_for_data(dataset_file_loc=dataset_file_loc, lines=lines, string_based=string_based)
    else:
        data = need_for_data(dataset_file_loc, lines=lines, string_based=string_based)

    print("\nCBOW\n" + "=" * 15)
    print("Training Model using CBOW ")

    cbow_model = gensim.models.Word2Vec(data, min_count=1, size=300,
                                        window=5, workers=1, hs=hs)  # workers for multithreading
    cbow_model.save(file_dir_to_save + '\\' + model_name)  # to save the trained model

    print("\nTotal Training Time :", cbow_model.total_train_time)
    print("CBOW MODEL saved successfully...")
    print("At location :" + file_dir_to_save + "\\" + model_name )

# pure_gujarati_need_for_data(r"C:\Users\trush\OneDrive\Desktop\pure_gujarati_corpus\Transformed\civil_transformed.txt",
#                           string_based=1)
