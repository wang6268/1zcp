import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox as mBox
 
#获取原文内容
def getText(DIR):
    txt=open(DIR,'r').read()
    return txt
    txt.close()
 
#打开文件
def __opendir():
    srcText.delete('1.0', tk.END) # 先删除所有
        
    # 打开文件夹对话框
    fname = filedialog.askopenfilename(filetypes=( ("Text file", "*.txt*"),("HTML files", "*.html;*.htm")))
    entryvar.set(fname) # 设置变量entryvar，等同于设置部件Entry
        
    if not fname:
        mBox.showwarning('警告', message='未选择文件夹！')  # 弹出消息提示框
 
    #显示需要统计的文本
    Txt=getText(fname)
    srcText.insert(tk.END, Txt)
            
    srcText.update()
    
#手动输入文件名时回车键触发      
def srcEnter(event=None):
    
    fname=DirEntry.get()
    if not fname:
        mBox.showwarning('警告', message='请选择文件！')  # 弹出消息提示框
        
    Txt=getText(fname)
    srcText.insert(tk.END, Txt)
            
    srcText.update()
 
#词频统计
def wordFrequence():
    fname=DirEntry.get()
    if not fname:
        mBox.showwarning('警告', message='请选择文件！')  # 弹出消息提示框
 
    txt=getText(fname)
    
    #对原文进行小写，标点符号转换处理
    txt=txt.lower()
    for ch in '!"#$%&*()+,.-;:<=>?@[]\^_{}|`':
        txt=txt.replace(ch,' ')
 
    #词频统计
    words=txt.split()
    counts={} #用空字典存储统计结果
    for word in words:
        counts[word]=counts.get(word,0)+1
 
    #词频排序
    items=list(counts.items())
    items.sort(key=lambda x:x[1],reverse=True)
 
    #输出排序结果
    num=0
    for i in range(len(counts)):
        word,count=items[i]
        num=i*count+num
 
 
    dstText.insert(tk.END, '单词种类：')
    dstText.insert(tk.END, str(len(items)))
    dstText.insert(tk.END, '\n')
    dstText.insert(tk.END, '单词总数：')
    dstText.insert(tk.END, str(num))
    dstText.insert(tk.END, '\n')
    dstText.insert(tk.END, '词频排序如下:\n')
    dstText.insert(tk.END, '#word:\t\t#counts:\n')
 
    for i in range(len(counts)):
        word,count=items[i]
        dstText.insert(tk.END, word)
        dstText.insert(tk.END, '\t\t')
        dstText.insert(tk.END, count)
        dstText.insert(tk.END, '\n')
 
def savefile():
    # 打开文件夹对话框
    dirname = filedialog.askdirectory() 
    outvar.set(dirname) # 设置变量entryvar，等同于设置部件Entry
        
    if not dirname:
        mBox.showwarning('警告', message='请选择保存位置！')  # 弹出消息提示框
 
    fname=dirname+'\词频统计结果.txt'
    outfile = open(fname, "w")
    outfile.writelines(dstText.get(1.0,tk.END))
    outfile.close()
    mBox.showinfo('词频统计', '统计结果保存成功！')
 
def dstEnter(event=None):
    dirname=outvar.get()
    if not dirname:
        mBox.showwarning('警告', message='请选择保存位置！')  # 弹出消息提示框
    fname=dirname+'\词频统计结果.txt'
    outfile = open(fname, "w")
    outfile.writelines(dstText.get(1.0,tk.END))
    outfile.close()
    mBox.showinfo('词频统计', '统计结果保存成功！')
    
# Create instance
win = tk.Tk()   
 
# Add a title       
win.title("词频统计GUI")
 
# Disable resizing the GUI
win.resizable(0,0)
 
 
#---------------窗口控件介绍------------------#
 
#打开文件对话框
SelDirButton = ttk.Button(win, command=__opendir, text='选择文件目录：')
SelDirButton.grid(row=0, column=0,sticky=tk.W,pady=3,padx=3)
 
#文件的目录显示    
entryvar = tk.StringVar() 
DirEntry=ttk.Entry(win, width=30,textvariable=entryvar)
DirEntry.grid(row=1, column=0,sticky=tk.W,pady=3,padx=3)
DirEntry.bind('<Return>', func=srcEnter)
 
#文件内容的显示
srcText = scrolledtext.ScrolledText(win,width=30,height=30)#内容输出框
srcText.grid(row=2, column=0,columnspan=1,sticky=tk.W,pady=3,padx=3)
 
#词频统计按钮
CalcuButton = ttk.Button(win, command=wordFrequence, text='词频统计')
CalcuButton.grid(row=0, column=1,sticky=tk.W,pady=3,padx=3)
 
#统计结果显示
dstText = scrolledtext.ScrolledText(win,width=30,height=30)#内容输出框
dstText.grid(row=2, column=1,columnspan=2,sticky=tk.W,pady=3,padx=3)
 
#保存文件按钮
SavefileButton = ttk.Button(win, command=savefile, text='统计结果保存到：')
SavefileButton.grid(row=0, column=2,sticky=tk.W,pady=3,padx=3)
 
#保存文件目录
outvar = tk.StringVar() 
saveEntry=ttk.Entry(win, width=30,textvariable=outvar)
saveEntry.grid(row=1, column=1,columnspan=2,sticky=tk.W,pady=3,padx=3)
saveEntry.bind('<Return>', func=dstEnter)
 
     
#======================
# Start GUI
#======================
