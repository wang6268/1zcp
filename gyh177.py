article ='''
One morning a fox saw a cock.He thought,"This is my breakfast.''

He came up to the cock and said,"I know you can sing very well.Would you like to sing for me?''The cock was glad.He closed his eyes and began to sing.The fox saw that and caught him in his mouth and carried him away.

People in the field saw the fox.They shouted："Look,look!The fox is carrying our cock away.''

The cock said to the fox,"Mr Fox,do you understand?The people say you are carrying their cock away.Tell them it is yours.Not theirs.''

The fox opened his mouth and said,"The cock is mine,not yours.''Just then the cock ran away from the fox and fled into the tree.
'''

split = article.split()
print(split)
article = article.replace(",","").replace(".","").replace(":","").replace(";","").replace("?","")
exchange = article.lower();
print(exchange)
list = exchange.split()
print(list)
dic = {}
for i in list:
    count = list.count(i)
    dic[i] = count
print(dic)
dic1= sorted(dic.items(),key=lambda d:d[1],reverse= True)
print(dic1)

