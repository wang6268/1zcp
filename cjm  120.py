fin = open('1.txt') 
lines=fin.readlines()
fin.close()

'''transform the article into word list

'''
def words_list():
    chardigit='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 '
    all_lines = ''
    for line in lines:
        one_line=''
        for ch in line:
            if ch in chardigit:
                one_line = one_line + ch
        all_lines = all_lines + one_line

    return all_lines.split()

'''calculate the total number of article list

s is the article list
'''
def total_num(s):
    return len(s)

'''calculate the occurrence times of every word

t is the article list
'''
def word_dic(t):
    fre_dic = dict()
    for i in range(len(t)):
        fre_dic[t[i]] = fre_dic.get(t[i],0) + 1
    return fre_dic

'''calculate the occurrence times of every word

w is dictionary of the occurrence times of every word
'''
def word_fre(w):
    for key in w:
        w[key] = w[key] / total
    return w

'''sort the dictionary 

v is the frequency of words
'''
def word_sort(v):
    sort_dic = sorted(v.items(), key = lambda e:e[1])
    return sort_dic

'''This is entrance of functions

output is the ten words with the largest frequency
'''
total = total_num(words_list())   
print(word_sort(word_fre(word_dic(words_list())))[-10:])
