import gensim


def load_model(file_loc):
    model = gensim.models.Word2Vec.load(file_loc)
    print("\nModel successfully loaded...")
    return model


def cosine_similarity(model, word1, word2):
    print("Cosine similarity between " + word1 + " and " + word2 + " - CBOW : ",
          model.wv.similarity(word1, word2))


def vector_distance(model, word1, word2, type_of_model=None):
    d = model.wv.distance(word1, word2)
    print(type_of_model, " Distance between " + word1 + " and " + word2 + " : ", d)
    return d


def vocab_save(model, file_dir, file_name):
    file = open(file_dir + "\\" + file_name + ".txt", 'wt', encoding='UTF-8')
    for i in model.wv.vocab:
        file.writelines(i + "\n")
    file.close()
    print("\nVocabulary saved successfully...")
    print("At location :" + file_dir + "\\" + file_name + ".txt")


def vocab_size(model):
    count = int()
    for i in model.wv.vocab:
        count += 1
    print("Total Vocabulary :", count)


def most_similar(model, word):
    print("Most Similar to " + word + " : \n", model.wv.most_similar(word))
