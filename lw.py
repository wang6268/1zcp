#获取单词函数定义
def getTxt():
    txt = open('hamlet.txt').read()
    txt = txt.lower()
    for ch in '!"@#$%^&*()+,-./:;<=>?@[\\]_`~{|}': #替换特殊字符
        txt.replace(ch, ' ')
    return txt
#1.获取单词
hamletTxt = getTxt()

#2.切割为列表格式
txtArr = hamletTxt.split()

#3.遍历统计
counts = {}
for word in txtArr:
    counts[word] = counts.get(word, 0) + 1

#4.转换格式，方便打印，将字典转换为列表
countsList = list(counts.items())
countsList.sort(key=lambda x:x[1], reverse=True)#按次数从大到小排序

#5.打印
for i in range(10):
    word, count = countsList[i]
    print('{0:<10}{1:>5}'.format(word,count))
