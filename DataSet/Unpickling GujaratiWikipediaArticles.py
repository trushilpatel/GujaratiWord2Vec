import pickle

source = r"C:\Users\trush\OneDrive\Documents\Projects\Python\DataSet\GujaratiWikipediaArticles\\"
destination = r"C:\Users\trush\OneDrive\Documents\Projects\Python\DataSet\Pickled_GujaratiWikipediaArticles\\"


for i in range(31914):
    print("\n" + str(i))
    source_file = open(source + str(i) +".pkl",'rb')
    load = pickle.load(source_file)
    source_file.close()
    print(load)
    destination_file = open(destination + str(i) +".txt",'wt',encoding='UTF-8')
    destination_file.write(load)
    destination_file.close()

