from utils import Visualize, utility, Train_Model
from pure_Gujarati import Generate_Replace_words_file

print("\n1.  Skip Gram base Train Model "
      "\n2.  CBOW based Train Model "
      "\n3.  Load Model "
      "\n4.  TSNE based visualization "
      "\n5.  PCA based visualization"
      "\n6.  Create CSV file of words and it's vectors"
      "\n7.  Cosine Similarity"
      "\n8.  Distance between vectors"
      "\n9.  Save Vocabulary"
      "\n10. vocabulary size "
      "\n11. Most Similar"
      "\n25. Pure Gujarati LOL"
      "\n0.  Exit")

print("*" * 80)
choice = int(input("Enter Choice : "))
print("-" * 20)

loaded_model = 0

while choice != 0:

    if choice == 1:  # Skip Gram base Train Model
        dataset_file_loc = input("Enter dataset file location : ")
        model_name = input("Enter model name to save model : ")
        file_dir_to_save = input("Enter file directory to save model : ")
        string_based = int(input("Want to insert string instead of file [ 0 for NO, 1 for Yes ] : "))
        pure_gujarati = int(input("file is Pure Gujarati file [ 0 for NO, 1 for Yes ] : "))
        hs = int(input("0 for non-zero, negative sampling and 1 for hierarchical softmax : "))

        Train_Model.skip_gram_model(dataset_file_loc=dataset_file_loc, model_name=model_name,
                                    file_dir_to_save=file_dir_to_save, string_based=string_based, hs=hs,
                                    pure_gujarati=pure_gujarati)

    elif choice == 2:  # CBOW based Train Model
        dataset_file_loc = input("Enter dataset file location : ")
        model_name = input("Enter model name to save model : ")
        file_dir_to_save = input("Enter file directory to save model : ")
        string_based = int(input("Want to insert string instead of file [ 0 for NO, 1 for Yes ] : "))
        hs = int(input("0 for non-zero, negative sampling and 1 for hierarchical softmax : "))
        pure_gujarati = int(input("file is Pure Gujarati file [ 0 for NO, 1 for Yes ] : "))

        Train_Model.cbow(dataset_file_loc=dataset_file_loc, model_name=model_name,
                         file_dir_to_save=file_dir_to_save, string_based=string_based, hs=hs,
                         pure_gujarati = pure_gujarati)

    elif choice == 3:  # Load Model
        file_loc = input("Enter location of file : ")
        model = utility.load_model(file_loc=file_loc)
        loaded_model = 1

    elif choice == 4:  # TSNE based visualization
        if loaded_model == 0:
            print("First Load model")
        else:
            method = input("Which method \"barnes_hut\" or \"exact\" : ")
            vocab_based = int(input("Want to give selected words [ 0 for NO, 1 for Yes ] : "))
            perplexity = int(input("Enter perplexity between 5 and 50 : "))
            learning_rate = int(input("Enter Learning rate in the range [10.0, 1000.0] : "))
            n_iter = int(input("Enter n_iter : "))

            if vocab_based == 1:
                n = int(input("Enter how many words "))

                words = list()
                for i in range(n):
                    w = input()
                    words.append(w)

                Visualize.TSNE_based_visualization(model=model, vocabulary=words, method=method, perplexity=perplexity,
                                                   learning_rate=learning_rate, n_iter=n_iter)

            else:
                Visualize.TSNE_based_visualization(model=model, method=method, perplexity=perplexity,
                                                   learning_rate=learning_rate, n_iter=n_iter)

    elif choice == 5:  # PCA based visualization
        if loaded_model == 0:
            print("First Load model")
        else:
            vocab_based = int(input("Want to give selected words [ 0 for NO, 1 for Yes ] : "))
            if vocab_based == 1:
                n = int(input("Enter how many words "))
                words = list()
                for i in range(n):
                    w = input()
                    words.append(w)

                Visualize.PCA_based_visualization(model=model, vocabulary=words)

            else:
                Visualize.PCA_based_visualization(model=model)

    elif choice == 6:  # Create CSV file of words and it's vectors
        if loaded_model == 0:
            print("First Load model")
        else:
            file_dir = input("Enter location to save file : ")
            file_name = input("Enter file name to save file : ")
            Visualize.create_CSV_file(model=model, file_dir=file_dir, file_name=file_name)

    elif choice == 7:  # Cosine Similarity
        if loaded_model == 0:
            print("First or Load model")
        else:
            word1 = input("Enter first word : ")
            word2 = input("Enter second word : ")
            utility.cosine_similarity(model=model, word1=word1, word2=word2)

    elif choice == 8:  # Distance between vectors
        if loaded_model == 0:
            print("First or Load model")
        else:
            word1 = input("Enter first word : ")
            word2 = input("Enter second word : ")
            utility.vector_distance(model=model, word1=word1, word2=word2)

    elif choice == 9:  # Save Vocabulary
        if loaded_model == 0:
            print("First Load model")
        else:
            file_dir = input("Enter directory to save file : ")
            file_name = input("Enter file name to save file : ")
            utility.vocab_save(model=model, file_dir=file_dir, file_name=file_name)

    elif choice == 10:  # vocabulary size
        if loaded_model == 0:
            print("First Load model")
        else:
            utility.vocab_size(model=model)

    elif choice == 11:  # vocabulary size
        if loaded_model == 0:
            print("First Load model")
        else:
            word = input("Enter the word : ")
            utility.most_similar(model=model, word=word)

    elif choice == 25:  # pure Gujarati user data
        file_loc = input("Enter file location : ")
        save_file_loc = input("Enter file directory to save file : ")
        save_file_name = input("Enter file name to save file :")
        Generate_Replace_words_file.file_transform(file_loc=file_loc, save_file_loc=save_file_loc,
                                                   save_file_name=save_file_name)

    else:
        print("Enter valid choice")

    print("\n" + "*" * 80)
    choice = int(input("Enter Choice : "))

    print("-" * 20)

# loc = C:\Users\trush\OneDrive\Documents\Projects\Python\Word2Vec\SG.w2v
