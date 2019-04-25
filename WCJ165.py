article ='''
Big data analytics and business analytics
by Duan, Lian; Xiong, Ye
Over the past few decades, with the development of automatic identification, data capture and storage technologies, 
people generate data much faster and collect data much bigger than ever before in business, science, engineering, education and other areas. 
Big data has emerged as an important area of study for both practitioners and researchers. 
It has huge impacts on data-related problems. 
In this paper, we identify the key issues related to big data analytics and then investigate its applications specifically related to business problems.
'''

split = article.split()
print(split)

#使用空格替换标点符号
article = article.replace(",","").replace(".","").replace(":","").replace(";","").replace("?","")


#大写字母转换成小写字母
exchange = article.lower();
print(exchange)

#生成单词列表
list = exchange.split()
print(list)

#生成词频统计
dic = {}
for i in list:
    count = list.count(i)
    dic[i] = count
print(dic)

#排除特定单词
word = {'and','the','with','in','by','its','for','of','an','to'}
for i in word:
    del(dic[i])
print(dic)

#排序
dic1= sorted(dic.items(),key=lambda d:d[1],reverse= True)
print(dic1)

#输出词频最大的前十位单词
for i in range(10):
    print(dic1[i])
