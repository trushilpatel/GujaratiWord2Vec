def gujarati_line_with_quote(line):
    index = 0
    le = 0
    quotes = 0
    final_list = list()
    temp = str()
    for i in range(len(line)):
        le += 1
        if '"' in line[i]:
            quotes += 1
            if quotes == 2:
                temp = line[index:i].strip()
                print("if :", temp)

                if temp is not '':
                    final_list.append(temp)
                quotes = 0
            else:
                temp = line[index:i].split()
                print("else :", temp)
                for j in temp:
                    j_temp = j.strip()
                    if temp is not '':
                        final_list.append(j)

            index = i + 1

    if index < le:
        temp = line[index:le].split()
        for i in temp:
            final_list.append(i.strip())
    for i in final_list:
        print(i)
    print(final_list)
    return final_list


'''
    for i in range(int(len(qi)/2)):
        qi.append([qi[i],qi[i+1]].copy())
    for i in range(int(len(qi)*2/3)):
        qi.pop(0)
    print(qi)
'''

#   for i in qi:


line = 'એલડીઆરપીમાં સિવિલમાં પહેલી શિફ્ટનો સમય "8 થી 2" નો છે'
# line = '"મૌની મોદી" civilમાં "study કરાવે" છે'

gujarati_line_with_quote(line)
