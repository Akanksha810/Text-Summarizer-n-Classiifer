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


def intake() :
        raw_text = "Edgar Allan Poe's C. Auguste Dupin is generally acknowledged as the first detective in fiction and served as the prototype for many that were created later, including Holmes. Conan Doyle once wrote,  Each [of Poe's detective stories] is a root from which a whole literature has developed... Where was the detective story until Poe breathed the breath of life into it?  Similarly, the stories of Émile Gaboriau's Monsieur Lecoq were extremely popular at the time Conan Doyle began writing Holmes, and Holmes' speech and behaviour sometimes follow that of Lecoq. Both Dupin and Lecoq are referenced at the beginning of A Study in Scarlet.Conan Doyle repeatedly said that Holmes was inspired by the real-life figure of Joseph Bell, a surgeon at the Royal Infirmary of Edinburgh, whom Conan Doyle met in 1877 and had worked for as a clerk. Like Holmes, Bell was noted for drawing broad conclusions from minute observations. However, he later wrote to Conan Doyle:  You are yourself Sherlock Holmes and well you know it .Sir Henry Littlejohn, Chair of Medical Jurisprudence at the University of Edinburgh Medical School, is also cited as an inspiration for Holmes. Littlejohn, who was also Police Surgeon and Medical Officer of Health in Edinburgh, provided Conan Doyle with a link between medical investigation and the detection of crime.Other inspirations have been considered. One has been argued to be Maximilien Heller, by French author Henry Cauvain. It is not known if Conan Doyle read Maximilien Heller, but he was fluent in French, and in this 1871 novel (sixteen years before the first adventure of Sherlock Holmes), Henry Cauvain imagined a depressed, anti-social, opium-smoking polymath detective, operating in Paris. Michael Harrison has suggested that a German self-styled  consulting detective  named Walter Scherer may have been the model for Holmes."
        print(nltk_summarizer(raw_text))


intake()
