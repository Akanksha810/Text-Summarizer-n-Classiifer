import tkinter as tk                            //importing
from tkinter import *
from tkinter import ttk

##def printtext():
##   global e
##    string = e.get()
##    print(string)


global input1
    
class TS(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        #tk.Tk.iconbitmap(self,default="")
        tk.Tk.wm_title(self,"Text Summarizer")

        container = tk.Frame(self)
        container.pack(side = "top",fill = "both",expand = True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, Raw, Scanned, Doc, Genre, PPT, Output):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky="news")

        frame = StartPage(container,self)

        self.frames[StartPage] = frame

        frame.grid(row=0,column=0,sticky="news")

        self.show_frame(StartPage)

    def show_frame(self,cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg="#149AEB")  
        label = tk.Label(self,text="TEXT SUMMARIZER",font=("@MS PGothic",40,"bold"),bg="#149AEB")
        label.pack(pady=200,padx=100)
        warning = tk.Label(self,text="This is a beta software",bg="#149AEB",font=("Corbel",20))
        warning.pack(pady=50,padx=50)
        button1 = tk.Button(self,text = "Continue",command=lambda:controller.show_frame(PageOne),bg="#FF8E44",font=("calibri",10))
        button1.pack()

class PageOne(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg="#149AEB")

        RawText_Button = tk.Button(self,text = "RAW TEXT",command=lambda:controller.show_frame(Raw))
        RawText_Button.pack(pady=5,padx=5)

        ScannedText_Button = tk.Button(self,text = "SCANNED TEXT",command=lambda:controller.show_frame(Scanned))
        ScannedText_Button.pack(pady=5,padx=5)

        Doc_Button = tk.Button(self,text = "DOCUMENT",command=lambda:controller.show_frame(Doc))
        Doc_Button.pack(pady=5,padx=5)

        PPT_Button = tk.Button(self,text = "PPT",command=lambda:controller.show_frame(PPT))
        PPT_Button.pack(pady=5,padx=5)

        Genre_Button = tk.Button(self,text = "GENRE",command=lambda:controller.show_frame(Genre))
        Genre_Button.pack(pady=5,padx=5)

        Button2 = tk.Button(self,text = "BACK",command=lambda:controller.show_frame(StartPage))
        Button2.pack(pady=5,padx=5)

class Raw(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg="#149AEB")


        e = tk.Text(self, height=20, width=60)
        e.pack()
        e.focus_set()
        
        def retrieve_input():
           input1 = e.get("1.0",'end-1c')
           print(input1)

      
        Button3 = tk.Button(self,text = 'CONTINUE',command=nltk_summarizer(input1))
        Button3.pack(pady=5,padx=5)

        Button4 = tk.Button(self,text = 'BACK',command=lambda:controller.show_frame(PageOne))
        Button4.pack(pady=5,padx=5)

class Scanned(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg="#149AEB")

        Button5 = tk.Button(self,text = 'CONTINUE',command=lambda:controller.show_frame(Output))
        Button5.pack(pady=5,padx=5)

        Button6 = tk.Button(self,text = 'BACK',command=lambda:controller.show_frame(PageOne))
        Button6.pack(pady=5,padx=5)

class Doc(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg="#149AEB")

        Button7 = tk.Button(self,text = 'CONTINUE',command=lambda:controller.show_frame(Output))
        Button7.pack(pady=5,padx=5)

        Button8 = tk.Button(self,text = 'BACK',command=lambda:controller.show_frame(PageOne))
        Button8.pack(pady=5,padx=5)

class PPT(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg="#149AEB")

        Button9 = tk.Button(self,text = 'CONTINUE',command=lambda:controller.show_frame(Output))
        Button9.pack(pady=5,padx=5)

        Button10 = tk.Button(self,text = 'BACK',command=lambda:controller.show_frame(PageOne))
        Button10.pack(pady=5,padx=5)

class Genre(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg="#149AEB")

        Button11 = tk.Button(self,text = 'CONTINUE',command=lambda:controller.show_frame(Output))
        Button11.pack(pady=5,padx=5)

        Button12 = tk.Button(self,text = 'BACK',command=lambda:controller.show_frame(PageOne))
        Button12.pack(pady=5,padx=5)

class Output(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent,bg="#149AEB")

        Button13 = tk.Button(self,text = 'CONTINUE',command=lambda:controller.show_frame(Output))
        Button13.pack(pady=5,padx=5)

        Button14 = tk.Button(self,text = 'BACK',command=lambda:controller.show_frame(PageOne))
        Button14.pack(pady=5,padx=5)




import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq  

def nltk_summarizer(raw_text):
	stopWords = set(stopwords.words("english"))
	word_frequencies = {}  
	for word in nltk.word_tokenize(raw_text):  
	    if word not in stopWords:
	        if word not in word_frequencies.keys():
	            word_frequencies[word] = 1
	        else:
	            word_frequencies[word] += 1

	maximum_frequncy = max(word_frequencies.values())

	for word in word_frequencies.keys():  
	    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

	sentence_list = nltk.sent_tokenize(raw_text)
	sentence_scores = {}  
	for sent in sentence_list:  
	    for word in nltk.word_tokenize(sent.lower()):
	        if word in word_frequencies.keys():
	            if len(sent.split(' ')) < 30:
	                if sent not in sentence_scores.keys():
	                    sentence_scores[sent] = word_frequencies[word]
	                else:
	                    sentence_scores[sent] += word_frequencies[word]



	summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

	summary = ' '.join(summary_sentences)  
	return summary





app = TS()
app.geometry("1600x900")
app.mainloop()
