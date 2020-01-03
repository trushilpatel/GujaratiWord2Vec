from Words_Combination_Generator import factorial_word_selection


def dollar(replace_string):  # dollar for the replacing word line
    replace = replace_string.split(";")
    temp_final = dict()

    for j in replace:
        temp = j.split("=")
        for k in range(len(temp)):
            temp[k] = temp[k].strip()
        temp_final[temp[0]] = temp[1]

    return temp_final


def statements(statement_string):  # statements between "$" and "#"
    temp = statement_string.split(";")
    temp = temp[0:len(temp) - 1]
    return temp


def write_replace_word_file(save_file_loc, save_file_name, final_replace_list, final_statement_list):
    file = open(save_file_loc + "\\" + save_file_name + ".txt", 'wt', encoding="UTF-8")

    # main data added as it is
    for i in final_statement_list:
        for j in i:
            file.writelines(j)
            file.write("\n")
        file.write("\n")
    file.write("\n")

    # adding replaced sentences
    temp = str()
    for i in range(len(final_statement_list)):
        main_words = list(final_replace_list[i].keys())
        fact_word_selection = factorial_word_selection(main_words)

        for j in fact_word_selection:
            for k in j:
                for sen in range(len(final_statement_list[i])):
                    line = final_statement_list[i][sen]
                    for l in k:
                        line = line.replace(l, final_replace_list[i].get(l))
                    file.writelines(line)
                    file.write("\n")
                file.write("\n")
    file.close()


def dollar_hashtag(replace_list, statement_list):
    final_replace_list = list()
    final_statement_list = list()
    # print(len(replace_list),len(statement_list))

    for i in range(len(replace_list)):  # length of replace_list and statement_list is same
        final_replace_list.append(dollar(replace_list[i]))
        final_statement_list.append(statements(statement_list[i]))

    # packing tuple
    return final_replace_list, final_statement_list


def file_transform(file_loc, save_file_loc, save_file_name):
    file = open(file_loc, 'rt', encoding="UTF-8")
    print()
    le = len(file.readlines())
    print("Total lines before Transformation : ", le)
    file.seek(0, 0)

    statement_list = list()
    replace_list = list()
    temp = str()

    for i in range(le):
        line = file.readline().strip()
        try:
            if '$' in line[0]:
                # print(line)
                replace_list.append(line.strip("$"))
            elif '#' in line[0]:
                statement_list.append(temp)
                temp = str()
            else:
                temp += line
        except:
            pass

    # unpacking tuple
    final_replace_list, final_statement_list = dollar_hashtag(replace_list, statement_list)

    write_replace_word_file(save_file_loc, save_file_name, final_replace_list, final_statement_list)

    file = open(save_file_loc + "\\" + save_file_name + ".txt", 'rt', encoding="UTF-8")
    print()
    le = len(file.readlines())
    print("Total lines After Transformation : ", le)
