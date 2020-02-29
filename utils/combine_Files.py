from os import listdir
from os.path import join

"""
    it merges all different files into single file
"""


def choice():
    print("*" * 30)
    print("Press 1 : to enter DataSet path \nElse press any number \n")

    return int(input("Enter your choice : "))


def createWholeDataSetFile():
    """

    :return: nothing it just save the file as whole_database.txt in same folder
    """
    if choice() == 1:
        # it takes dataset folder path which contains all separate file needs to merge
        path = input("Enter the DataSet path : ")
    else:
        path = "../pure_Gujarati/pure_gujarati_corpus/Transformed"

    create_file = open("../pure_Gujarati/pure_gujarati_corpus/Transformed/combined_dataset.txt", "w", encoding="utf8")

    for file in listdir(path):

        temp_file = open(join(path, file), "r", encoding="utf8")
        create_file.write(temp_file.read())
        temp_file.close()

    create_file.close()


if __name__ == "__main__":
    createWholeDataSetFile()
    #open_whole_dataset_file = open("whole_dataset.txt", "r", encoding="utf8")
    #print(len(open_whole_dataset_file.readlines()))
