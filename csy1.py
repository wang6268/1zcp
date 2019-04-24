# 20161152102 陈绍瑜 第三周上机作业
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

#define MAXLEN 30


struct wordcount//定义一个结构体Wordcount
{
    char *word;
    int count;
    struct wordcount *next;
};

struct wordcount *head,*wc,*sort,*headsort;
char buff[MAXLEN];
char *zs_c;//buf[]数组用来存放英文字母
int buff_count=0, isfinded;

int main()
{
    FILE *fp;
    char ch;
    int i;
    int k;
    char filename[20];
    printf("请输入文件名：\n");
    scanf("%s",filename);
    if ((fp=fopen(filename,"r"))==NULL) 
    {
        printf("不能打开该文件!\n");
        exit(0);
    }
    
    while ((ch=fgetc(fp))!=EOF)//读取英文文本中的内容
        if (isalpha(ch))
        {
            buff[buff_count++]=tolower(ch);//判断是否为字母若果是则把它放到数组Buff[]
            if (buff_count>=MAXLEN)
            {
                printf("单词长度超过最大限度!\n");//判断单词的长度是否超过最长限度
                fclose(fp);
                return -1;
            }
        }
        else
        {
            //若果不是字母，且buff[]中没有单词的话则把其放到Wordcount link中
            if (buff_count!=0)
            {
                
                buff[buff_count]='\0';
                wc=head;
                isfinded=0;
                while (wc)//如果有的话则计数加1
                {
                    if (strcmp(wc->word,buff)==0)
                    {
                        wc->count=wc->count+1;
                        isfinded=1;
                        break;
                    }
                    else
                        wc=wc->next;
                }
            
                if (isfinded==0) 
                {
                    zs_c=(char *)malloc(buff_count);
                    if (zs_c==0)
                    {
                        printf("错误!: zs_c !\n");
                        fclose(fp);
                        exit(0);
                    }
                    memcpy(buff,zs_c,buff_count);
                    wc=(struct wordcount *)malloc(sizeof(struct wordcount));
                    if (wc==0)
                    {
                        printf("分配有误！\n");
                        fclose(fp);
                        exit(0);
                    }
                    wc->word=zs_c;
                    wc->count=1;
                    wc->next=head;
                    head=wc;
                }
                buff_count=0;
            }
        
    }
    fclose(fp);
    
    if (head)//对单词进行排序
    {
        sort=head->next;
        head->next=0;
        while (sort)
        {
            wc=sort;
            sort=sort->next;
            if ((wc->count) > (head->count))
            {
                wc->next=head->next;
                head=wc;
            }
            else
            {
                headsort=head;
                while ((headsort->next) && (headsort->next->count > wc->count ))//交换进行排序
                {
                     headsort->count=headsort->next->count;
                     wc->next->count=headsort->next->count;
                     wc->next->count=headsort->count;
                     headsort->word=headsort->next->word;
                     wc->next->word=headsort->next->word;
                     wc->next->word=headsort->word;
                     
                }
                    
            }
        }
    }

    
    while (head)//对结果进行输出
    {
        wc=head;
        head=head->next;
        printf("序号\t单词\t频率\n");
        for(i=1;i<11;i++)
            printf("NO%d\t%s\t %d\n",i,wc->word,wc->count);
    }

    return 0;
}
