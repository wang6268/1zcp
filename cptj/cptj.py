article ='''
.
A Lifelong Career
As food is to the body, so is learning to the mind. Our bodies grow and muscles
develop with the intake of adequate nutritious food. Likewise, we should keep
learning day by day to maintain our keen mental power and expand our intellectual
capacity. Constant learning supplies us with inexhaustible fuel for driving us
to sharpen our power of reasoning, analysis, and judgment. Learning incessantly
is the surest way to keep pace with the times in the information age, and an
infallible warrant of success in times of uncertainty.
Once learning stops, vegetation sets in. It is a common fallacy to regard school
as the only workshop for the acquisition of knowledge. On the contrary, learning
should be a never-ending process, from the cradle to the grave. With the world
ever changing so fast, the cease from learning for just a few days will make a
person lag behind. What's worse, the animalistic instinct dormant deep in our
subconsciousness will come to life, weakening our will to pursue our noble ideal,
sapping our determination to sweep away obstacles to our success and strangling
our desire for the refinement of our character. Lack of learning will inevitably
lead to the stagnation of the mind, or even worse, its fossilization, Therefore,
to stay mentally young, we have to take learning as a lifelong career
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
