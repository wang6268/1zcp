import re
text = '''Starry starry night
paint your palette blue and grey
look out on a summer's day
with eyes that know the darkness in my soul
Shadows on the hills
sketch the trees and daffodils
catch the breeze and the winter chills
in colors on the snowy linen land'''

#词频统计
def word_count(string):
    if isinstance(string,str):
        new text=sting.strip()
        str_list=re.split('\s+',new_text)
        word_dict={}
        for str_word in str_list:
            if str_word in word_dict.key():#如果key存在则value加1
                word_dict[str_word]=word_dict[str_word]+1
            else:
                word_dict[str_word]=1
        return word_dict
    else:
        raise 'please enter a string'
word=word_count(string=text)
#print(word)

#词频统计按降序排序取前十
word_list=sorted(word.tiems(),key=lambda x:x[1],reverse=True)[0:11]
print(word_list)
