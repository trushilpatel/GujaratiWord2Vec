# Python program to generate word vectors using Word2Vec

from nltk.tokenize import sent_tokenize, word_tokenize
import warnings
import gensim

warnings.filterwarnings(action='ignore')

# DONE
def gujarati_line_with_quote(line):
    """

    :param line: string
        line containing quotation handled separately
    :return: list
        list of line's words
    """
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


# DONE
def pure_gujarati_need_for_data(dataset_file_loc, string_based=0, lines=None):
    """
    if we are using pure_gujarati ( manually generated files ) then these function is helpful

    :param dataset_file_loc: file
        location of file
    :param string_based: {0,1}
    :param lines: integer
        number of lines for training model
    :return: list
        list contains list of sentence's words
        EX: [['a','b'],...]
    """
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


# DONE
def need_for_data_sample(file_loc, string_based, lines=None):
    """

    :param file_loc: file
        file location
    :param string_based: {0,1}
        if 1 then it's a string based else it's file based method for dataset
    :param lines: integer
        number of lines used for model training
    :return: tuple( sample, lines)
        sample: string
            dataset as string
        lines: integer
            number of lines used for generating sample
    """
    # if it's string based
    if string_based is 1:
        sample = input("Enter String ")

    # if it's file based
    else:
        file = open(file_loc, 'rt', encoding="UTF-8")
        # if number of lines not provided
        if lines is None:
            lines = len(file.readlines())
        sample = str()
        file.seek(0, 0)
        for i in range(lines):
            sample += file.readline()

    return sample, lines


# DONE
def need_for_data(file_loc, string_based, lines=None):
    """

    :param file_loc: file
        file location
    :param string_based: {0,1}
        if 1 then it's string based otherwise file based model training
    :param lines: integer, Optional
        number of lines used for model training
    :return: list
        list which conatains list of tokenized words
        Ex. [['a','b','b'],[...]]
    """
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


# DONE
def skip_gram_model(dataset_file_loc, model_name, file_dir_to_save, string_based=0, lines=None, hs=0, pure_gujarati=0):
    """

    :param dataset_file_loc: file
        absolute/ relative location of dataset file
    :param model_name:  string
        name for model
    :param file_dir_to_save: directory path
        file directory to save model
    :param string_based: {0,1}, optional
        want to train on string ( if yes then no need to provide dataset_file_loc )
    :param lines: integer, optional
        how many lines you wanted to train data ( for lines = 100 we use only first 100 lines to train model)
    :param hs: {0, 1}, optional
               If 1, hierarchical softmax will be used for model training.
               If 0, and `negative` is non-zero, negative sampling will be used.
    :param pure_gujarati: is it a pure gujarati file or not
    :return: None
    """
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
    print("At location :" + file_dir_to_save + "\\" + model_name)


# DONE
def cbow(dataset_file_loc, model_name, file_dir_to_save, string_based=0, lines=None, hs=0, pure_gujarati=0):
    """

    :param dataset_file_loc: file
        absolute/ relative location of dataset file
    :param model_name:  string
        name for model
    :param file_dir_to_save: directory path
        file directory to save model
    :param string_based: {0,1}, optional
        want to train on string ( if yes then no need to provide dataset_file_loc )
    :param lines: integer, optional
        how many lines you wanted to train data ( for lines = 100 we use only first 100 lines to train model)
    :param hs: {0, 1}, optional
               If 1, hierarchical softmax will be used for model training.
               If 0, and `negative` is non-zero, negative sampling will be used.
    :param pure_gujarati: is it a pure gujarati file or not
    :return: None
    """

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
    print("At location :" + file_dir_to_save + "\\" + model_name)

# pure_gujarati_need_for_data(r"C:\Users\trush\OneDrive\Desktop\pure_gujarati_corpus\Transformed\civil_transformed.txt",
#                           string_based=1)
