#词频统计 刘娅

import os 
import re 
from collections import Counter 
from tkinter import filedialog 
from tkinter import * 
class DirectionDocWordCounter:
    def __init__(self):
        marginx = 5
        marginy = 5
        window = Tk()
        window.title("词频统计器")
        self.dirPath = StringVar()
        self.dirPath.set("选择要打开的文件夹")
        frame1 = Frame()
        frame1.pack(padx=marginx, pady=(marginy, 0))
        Entry(frame1, width=50, textvariable=self.dirPath).pack(side=LEFT)
        Button(frame1, text="选择文件夹", command=self.openDir).pack(side=LEFT, padx=(marginx, 0))
        Button(width=60, text="词频统计结果如下:", command=self.doCalculate).pack(padx=marginx, pady=(10,0))
        frame2 = Frame()
        frame2.pack(padx=marginx, pady=(marginy, marginy),expand=True,fill=Y)
        self.retText = Text(frame2, width=58, height=20, bg="white")
        scrollbar = Scrollbar(frame2,orient=VERTICAL,bg="black")
        self.retText.pack(side=LEFT,expand=True,fill=Y)
        scrollbar.pack(side=LEFT,expand=True,fill=Y)
        self.retText.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.retText.yview)
        window.mainloop()
    def openDir(self):
        self.dirPath.set(filedialog.askdirectory() + "/")
    def doCalculate(self):
        self.countDocWordsInDir(self.dirPath.get())
    def getFileCounter(self, filepath):
        file = open(filepath, "r", encoding="gbk")
        text = file.read()
        pattern = "[A-Za-z]+"
        wordlist = re.findall(pattern, text)
        counter = Counter(wordlist)
        return counter
    def countDocWordsInDir(self, dirpath):
        flist = os.listdir(dirpath)
        mcounter = Counter()
        for name in flist:
            if name.endswith(".txt"):
                docpath = dirpath + name 
                counter = self.getFileCounter(docpath)
                mcounter += counter
        resList = mcounter.most_common()
        
        for item in resList:
            self.retText.insert(END, str(item) + "\n")
if __name__ == '__main__':
    DirectionDocWordCounter()
    pass
