import gensim


def load_model(file_loc):
    """

    :param file_loc: file location
        trained model file
    :return: object of given file
    """
    model = gensim.models.Word2Vec.load(file_loc)
    print("\nModel successfully loaded...")
    return model


def cosine_similarity(model, word1, word2):
    """

    :param model: word2vec model
    :param word1: string
    :param word2: string
    :return: None
    """
    print("Cosine similarity between " + word1 + " and " + word2 + " - CBOW : ",
          model.wv.similarity(word1, word2))


def vector_distance(model, word1, word2, type_of_model=None):
    """

    :param model: word2vec model
    :param word1: string
    :param word2: string
    :param type_of_model: {CBOW,SkipGram}, Optional
    :return: integer
        distance between two words in given model
    """
    d = model.wv.distance(word1, word2)
    print(type_of_model, " Distance between " + word1 + " and " + word2 + " : ", d)
    return d


def vocab_save(model, file_dir, file_name):
    """

    :param model: word2vec model
    :param file_dir: directory path to save file
    :param file_name: file name
    :return: None
    """
    file = open(file_dir + "\\" + file_name + ".txt", 'wt', encoding='UTF-8')
    for i in model.wv.vocab:
        file.writelines(i + "\n")
    file.close()
    print("\nVocabulary saved successfully...")
    print("At location :" + file_dir + "\\" + file_name + ".txt")


def vocab_size(model):
    """

    :param model: word2vec Mode
    :return: integer
    """
    count = int()
    for i in model.wv.vocab:
        count += 1
    print("Total Vocabulary :", count)
    return count


def most_similar(model, word):
    """

    :param model: word2vec model
    :param word: string
        word who's similar words we are finding
    :return:
    """
    print("Most Similar to " + word + " : \n", model.wv.most_similar(word))
