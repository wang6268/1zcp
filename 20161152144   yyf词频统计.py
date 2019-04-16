#20161152144
#词频统计
import string

words_freq={ }

f=open("英文.txt")

for line in f:
#间类似于twenty-one的单词分为两个单词
#分词
    words=line.replace("-"," ").split()
    for word in words:
    #去掉单词前后的标点符号
        word=word.strip(string.punctuation)
        #所有单词不区分大小写，全部转成小写
        word=word.lower()
        #统计，以字典存储
        if word in words_freq:
            words_freq[word]+=1
        else:
            words_freq[word]=1
freq_words=[]
for word,freq in words_freq.items():
    freq_words.append((freq,word))
freq_words.sort(reverse=True)
for freq,word in freq_words[:10]:
    print(word,freq)
