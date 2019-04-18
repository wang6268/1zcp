#词频统计
from string import punctuation
 
#对文本的每一行计算词频的函数
def processLine(line,wordCounts):
    #用空格替换标点符号
    line=replacePunctuations(line)
    words = line.split()
    for word in words:
        if word in wordCounts:
            wordCounts[word]+=1
        else:
            wordCounts[word]=1
 
def replacePunctuations(line):
    for ch in line :
        #这里直接用了string的标点符号库。将标点符号替换成空格
        if ch in punctuation:
            line=line.replace(ch," ")
        return line
 
def main():
    infile=open("英语文本.txt",'r')
    count=10
    words=[]
    data=[]
 
    # 建立用于计算词频的空字典
    wordCounts={}
    for line in infile:
        processLine(line.lower(), wordCounts)#这里line.lower()的作用是将大写替换成小写，方便统计词频
    #从字典中获取数据对
    pairs = list(wordCounts.items())
    #列表中的数据对交换位置,数据对排序
    items = [[x,y]for (y,x)in pairs]
    items.sort()
    #因为sort()函数是从小到大排列，所以range是从最后一项开始取
    for i in range(len(items) - 1, len(items) - count - 1, -1):
        print(items[i][1] + "\t" + str(items[i][0]))
        data.append(items[i][0])
        words.append(items[i][1])
 
    infile.close()
 
if __name__ == '__main__':
    main()
