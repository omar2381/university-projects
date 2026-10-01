#Using Python Version 3.8.8 on 64-bit windows Machine, on VScode
# to run the program, enter "python3 scrape_and_compare.py" in command line

#imports
from bs4 import BeautifulSoup, SoupStrainer             # V 4.9.3
import requests                                         # V 2.25.1
import seaborn as sb                                    # V 0.11.1
import pandas as pd                                     # V 1.2.1
import urllib.request                                   # V 3.8
from nltk.tokenize import sent_tokenize, word_tokenize  # V 3.5
import gensim                                           # V 3.8.3
from gensim.models import Word2Vec                      # v 3.8.3
import numpy as np

import warnings 
warnings.filterwarnings(action = 'ignore') 

#list of variables
filenames = []          # to contain keyword.txt (and replace ' ' with '_') 
link_names = []         # to contain link name (and replace ' ' with '+')
xlsx_list = []          # list to contain raw keywords from file
pages = []              # list to store '&page=' based on pagenum variable below
links = []              # to contain all the links eg: url + link_name + page 
keyword_len = []        # to contain the length of all the keywords
pagenum = 30            # number of pages to visit
url = 'https://www.bbc.co.uk/search?q='

#early setup, reading excel file, getting variables
keyword_location = ('keywords.xlsx')
raw_keywords = pd.read_excel(keyword_location)
size = raw_keywords.shape
raw_keywords = raw_keywords.columns.ravel()
raw_keywords = raw_keywords[1:]

#creating 2D arrays for the values
keywords = [[] for q in range(int(size[0])+1)]
xlsx = [[-1 for j in range(int(size[0]))] for q in range(int(size[0]))]
xlsx_list.append('keywords')

#filling up all the lists with different forms of the input keywords
for i in range(int(size[0])):
    xlsx_list.append(raw_keywords[i])
    keywords[len(keywords)-1].append(raw_keywords[i].lower())
    link_names.append(raw_keywords[i])
    filenames.append(raw_keywords[i])
    link_names[i] = str(link_names[i]).replace(" ", "+")
    filenames[i] = str(filenames[i]).replace(" ", "_") + ".txt"

#filling up the page numbers i.e. &page=1 - &page=30
for i in range(pagenum):
    pages.append('&page='+str(i+1))


#Problem 1 Begins here:
def download_Data():
    #creating the url's to search by concatination 
    for i in range(len(link_names)):
        for j in range(len(pages)):
            links.append(url+link_names[i]+pages[j])

    websites_visited = 0 #variable to keep track of the number of websites viewed
    
    for i in range(len(links)): #300 links from the 10 keywords * 30 pages

        page = requests.get(links[i])    
        data = page.text
        soup = BeautifulSoup(data,features="html.parser")

        for link in soup.find_all('a'): # making sure the link is valid
            if ('news/' in link.get('href') and 'localnews' not in link.get('href') and 'help' not in link.get('href')): 
                page = requests.get(link.get('href'))
                data = page.text
                for x in range(len(link_names)): #making sure the link is not repeated and checking that the link is valid
                    if (str(link_names[x]) in links[i] and str(keywords[len(keywords)-1][x]) in data.lower() and len(keywords[x]) < 100 and link.get('href') not in keywords[x]): 
                        keywords[x].append(link.get('href'))
                websites_visited = websites_visited + 1 

    print("Number of websites viewed is: "+str(websites_visited))
    for i in range(len(link_names)):
        keyword_len.append(len(keywords[i]))
        print("Length of "+ raw_keywords[i] +" is: "+str(len(keywords[i])))


#Problem 2 Begins here:
def save_data():
    #using the list filenames[i], a .txt file is created for each of the keywords
    for i in range(len(raw_keywords)):
        l = open(filenames[i],'w')
        for j in range(len(raw_keywords)): #write the keywords to the file for the machine learning
            l.write(keywords[len(keywords)-1][j].lower() + " ")
        write_to_file(keywords[i],l) # go to other function
        print(str(filenames[i]) + " has been successfully written to")

def write_to_file(lst,l):
    #this function recieves the list of articles for a keyword and writes the contents to the .txt file
    for x in range(len(lst)):
        url = str(lst[x]) 
        url = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(url,features = "html.parser") 

        for text in soup(["script", "style"]):
            text.decompose()

        words = list(soup.stripped_strings)
        for i in range(len(words)): 
            try:
                l.write(words[i])
            except UnicodeEncodeError: #to get rid of strange characters such as emoticons
                pass

    l.close()


#Problem 3 Begins here:
def find_dist():
    #to loop about half the matrix 
    for i in range(len(xlsx)):
        for j in range(i,len(xlsx)):
            if (i == j): 
                val = 1.0
            else:
                val = calc_val(i,j)
            xlsx[i][j] = val
            xlsx[j][i] = val
    
    #to insert the Keywords for the distance.xlsx file
    for i in range(len(xlsx_list)-1):
        xlsx[i].insert(0,xlsx_list[i+1])

    data = pd.DataFrame(xlsx)
    data.to_excel('./distance.xlsx', header = xlsx_list, index = False)

def calc_val(i,j):
    # get the file names to open
    f1 = filenames[i]
    f2 = filenames[j]
    # open the files
    f1 = open(f1,'r')
    f2 = open(f2,'r')
    #make the files into strings
    text = f1.read() + f2.read()
    text = text.replace("\n", " ")
    #close the files
    f1.close()
    f2.close()
    #get the keywords to compare the distance of 
    word1 = keywords[len(keywords)-1][i].lower().split()
    word2 = keywords[len(keywords)-1][j].lower().split()

    #to appened the text to a list of lists for the Word2vec Model
    ML = [] 
    for i in sent_tokenize(text): 
        temp = [] 
        for j in word_tokenize(i): 
            temp.append(j.lower()) 
        ML.append(temp)
     
    #creating a model based on the list ML with a size of 1000 to increase accuracy (hopefully no overfitting will occur)
    model = gensim.models.Word2Vec(ML, min_count = 1, size = 1000, window = 5) #and a window of 5 to increase the scope of each word

    temp = 0.00
    k = 1

    try:
        for i in range(len(word1)):
            for j in range(len(word2)):
                if temp > 0:
                    k = 2
                # increamenting temp with the model value and dividing by k so the value doesnt exceed 1 
                temp = float(temp + float(model.similarity(word1[i],word2[j])))/k
    except KeyError: 
        #if there is an error in the model seeing an unkown word, instead of crashing, itll write to the user
        print("error found in " + str(word1) + " and " + str(word2)) 
    
    # as word2vec doesnt care about signs a negative value means nothing and should be converted to positive
    if temp < 0:
        temp = temp * (-1)
    
    #dividing the temp value with the numver of iterations of the loop 
    val = float(temp/((i + j + 1)))

    #return the final value between 0 and 1 
    return val


#Problem 4 Begins here:
def display_data():

    mat_location = ('distance.xlsx')
    mat = pd.read_excel(mat_location)
    mat = mat.drop(mat.columns[[0]], axis=1)
    mat = np.array(mat.values.tolist())

    #set the parameters for the size of the window 
    sb.set(rc={'figure.figsize':(11,7)})
    sb.set(rc={"figure.subplot.left":(0.225)})
    sb.set(rc={"figure.subplot.right":(1)})
    sb.set(rc={"figure.subplot.bottom":(0.35)})
    sb.set(rc={"figure.subplot.top":(0.95)})

    x_axis_labels = raw_keywords # labels for x-axis
    y_axis_labels = raw_keywords # labels for y-axis

    #seaborn Heatmap
    graph = sb.heatmap( mat , annot=True , xticklabels = x_axis_labels , yticklabels = y_axis_labels , linewidths = 0.5, fmt = " .4f", vmin = 0.0, vmax= 1.0)

    graph.invert_yaxis() #invert it to start from the bottom left (increases useability)
    graph = graph.get_figure()
    graph.savefig('./heatmap.png')
    graph.show()
    input("press enter to close the window")


download_Data()
save_data()
find_dist()
display_data()