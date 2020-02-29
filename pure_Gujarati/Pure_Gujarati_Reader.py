from utils.Train_Model import need_for_data_sample


def gujarati_line_with_quote(line):
    index = 0
    le = 0
    quotes = 0
    final_list = list()
    temp = str()
    for i in range(len(line)):
        le += 1
        if '"' in line[i]:
            temp = line[index:i]
            index = i + 1
            temp = temp.strip()
            if temp is not '':
                final_list.append(temp)
    if index < le:
        final_list.append(line[index:le].strip())

    return final_list


def pure_gujarati_need_for_data(file_loc, string_based=0, lines=None):
    sample, lines = need_for_data_sample(file_loc, string_based, lines)
    f = sample.replace("\n", ".")  # Replaces escape character with space
    L = f.split('.')
    quote = 0
    final_list = list()

    for i in range(len(L)):
        if '"' in L[i]:
            if quote is 2:
                final_list.append(gujarati_line_with_quote(L[i]))
        else:
            if L[i] is not "":
                final_list.append(L[i].split())

    for i in final_list:
        print("final list : ", i)

pure_gujarati_need_for_data(r"C:\Users\trush\OneDrive\Desktop\pure_gujarati_corpus\Transformed\civil_transformed.txt",
                           string_based=1)
