from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import re
import difflib

def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()

def string_io( dic, results):
    for i in results:
        number = 0
        j_index = 0
        test_str = re.search(r"\W",i)
        if test_str==None:
            list2 = list(dic.keys())
            result = process.extractOne(i,list2)
            if result == None:
                dic[i] = 1
            else:
                if int(result[1]) > 50:
                    if len(result[0]) >= len(i):
                        num = dic[result[0]]
                        dic.pop(result[0])
                        dic[i] = num+1
                    else:
                        dic[result[0]] += 1
                else:
                    dic[i] = 1
        else:
            for j in dic:
                number2 = string_similar(i,j)
                if number < number2:
                    number = number2
                    j_index = j
            if number > 0.5:
                if len(i) >= len(j_index):
                    dic[j_index] += 1
                else:
                    num = dic[j_index] + 1
                    dic.pop(j_index)
                    dic[i] = num
            else:
                dic[i] =1
def string_io2( dic, dicc):
    for i in dicc:
        number = 0
        j_index = 0
        test_str = re.search(r"\W",i)
        if test_str==None:
            list2 = list(dic.keys())
            result = process.extractOne(i,list2)
            if result == None:
                dic[i] = dicc[i]
            else:
                if int(result[1]) > 50:
                    if len(result[0]) >= len(i):
                        dic[i] = dic[result[0]] +dicc[i]
                        dic.pop(result[0]) 
                    else:
                        dic[result[0]] += dicc[i]
                else:
                    dic[i] = dicc[i]
        else:
            for j in dic:
                number2 = string_similar(i,j)
                if number < number2:
                    number = number2
                    j_index = j
            if number > 0.5:
                if len(i) >= len(j_index):
                    dic[j_index] += dicc[i]
                else:
                    dic[i] = dic[j_index] + dicc[i]
            else:
                dic[i] = dicc[i]