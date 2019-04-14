#20161152102 陈绍瑜 第六周上级作业

def get_text():
    f = open('zz.txt','r',encoding='unicode_escape')
    text = f.read().lower()
    for i in '!@#$%^&*()_¯+-;:`~\'"<>=./?,':
        text = text.replace(i,' ')
    return text.split()

ls = get_text()
counts = {}
print(len(ls))
for i in ls:
    counts[i] = counts.get(i,0) + 1

iteams = list(counts.items())
print(iteams)
iteams.sort(key=lambda x:x[1],reverse=True)

for i in iteams[0:10]:
    print(i)
