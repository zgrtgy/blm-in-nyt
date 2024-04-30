# -*- coding: utf-8 -*-

#%% import and read csv for NYT db
import pandas as pd
file = pd.read_csv("dir/to/nyt/snippets")

texts = []
raw = []
for x in file["text"]:
        texts.append(x)
        raw.append(x) #keep the raw for comparison

#%% Text clean-up, replace for easy operations, regex for complex
import regex as re

for x in range(len(texts)):
    texts[x] = texts[x].replace("'","") # connect apostrophes
    texts[x] = texts[x].replace("’","") # connect apostrophes
    texts[x] = re.sub(r'[^\w#]', ' ', texts[x], flags=re.MULTILINE) # removes punctuations
    texts[x] = re.sub(r'\s+', ' ', texts[x], flags=re.MULTILINE) # removes newlines
    texts[x] = re.sub(r'\d+', '', texts[x], flags=re.MULTILINE) # removes all numbers
    texts[x] = texts[x].lower() # lowercase
# special rules: separate negative contractions
    texts[x] = texts[x].replace(" aint",' am not')
    texts[x] = texts[x].replace(" isnt",' is not')
    texts[x] = texts[x].replace(" wasnt",' was not')
    texts[x] = texts[x].replace(" arent",' are not')
    texts[x] = texts[x].replace(" werent",' were not')
    texts[x] = texts[x].replace(" doesnt",' does not')
    texts[x] = texts[x].replace(" dont",' do not')
    texts[x] = texts[x].replace(" didnt",' did not')
    texts[x] = texts[x].replace(" havent",' have not')
    texts[x] = texts[x].replace(" hasnt",' has not')
    texts[x] = texts[x].replace(" hadnt",' had not')
    texts[x] = texts[x].replace(" wont",' will not')
    texts[x] = texts[x].replace(" wouldnt",' would not')
    texts[x] = texts[x].replace(" cant",' can not')
    texts[x] = texts[x].replace(" cannot",' can not')
    texts[x] = texts[x].replace(" couldnt",' could not')
    texts[x] = texts[x].replace(" shouldnt",' should not')
    texts[x] = texts[x].replace(" shant",' shall not') 
    texts[x] = texts[x].replace(" mustnt",' must not')
    texts[x] = texts[x].replace(" neednt",' need not')
    texts[x] = texts[x].replace(" mightnt",' might not')
# one more time to account for beginning of sentences
    texts[x] = re.sub("^aint",'am not', texts[x])
    texts[x] = re.sub("^isnt",'is not', texts[x])
    texts[x] = re.sub("^wasnt",'was not', texts[x])
    texts[x] = re.sub("^arent",'are not', texts[x])
    texts[x] = re.sub("^werent",'were not', texts[x])
    texts[x] = re.sub("^doesnt",'does not', texts[x])
    texts[x] = re.sub("^dont",'do not', texts[x])
    texts[x] = re.sub("^didnt",'did not', texts[x])
    texts[x] = re.sub("^havent",'have not', texts[x])
    texts[x] = re.sub("^hasnt",'has not', texts[x])
    texts[x] = re.sub("^hadnt",'had not', texts[x])
    texts[x] = re.sub("^wont",'will not', texts[x])
    texts[x] = re.sub("^wouldnt",'would not', texts[x])
    texts[x] = re.sub("^cant",'can not', texts[x])
    texts[x] = re.sub("^cannot",'can not', texts[x])
    texts[x] = re.sub("^couldnt",'could not', texts[x])
    texts[x] = re.sub("^shouldnt",'should not', texts[x])
    texts[x] = re.sub("^shant",'shall not', texts[x]) 
    texts[x] = re.sub("^mustnt",'must not', texts[x])
    texts[x] = re.sub("^neednt",'need not', texts[x])
    texts[x] = re.sub("^mightnt",'might not', texts[x])
    texts[x] = texts[x].strip() # remove spaces at the beginning and end
    
#%% remove stopwords   
#load stopwords
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords

stop_words = list(stopwords.words("english"))
stop_words.remove("not") 

#tokenize, remove stopwords, drop one character words
texts_tokenized = [i.split() for i in texts] #split into words
texts_sw_removed = [[word for word in i if word not in stop_words] for i in texts_tokenized ] #remove stopwords
texts_cleaned = [[word for word in i if len(word) > 1 and word != "i̇"] for i in texts_sw_removed] # THIS IS NOT AN i ,it's two characters! also remove words with char length<2

#%%re-format as a single string
texts_string = []
for k in texts_cleaned:
   texts_string.append(str(k).replace('[', '').replace(']', '').replace(',', '').replace("'", ""))    

#discard empty strings
texts_string = [x for x in texts_string if x.strip()]

#connect not's to the following word
for x in range(len(texts_string)):
    texts_string[x] = texts_string[x].replace(' not ', ' not-')
    texts_string[x] = re.sub('^not ', 'not-', texts_string[x])

#%% word frequency counter
word_frequency = {}
# for x in texts: #when running on unprocessed text
for x in texts_string:
    for y in x.split():
        if y in word_frequency.keys():
            word_frequency[y] += 1
        else:
            word_frequency[y] = 1

freq_dict_sorted = {k: v for k, v in sorted(word_frequency.items(), key=lambda item: item[1], reverse=True)}

#%% count ngrams (bi and tri) with nltk
import collections
import nltk

counts = collections.Counter() 
for sentence in texts_string:
    sentence = sentence.split()
    counts.update(nltk.everygrams(sentence, min_len = 2, max_len=3))

d = dict(counts)

d_sorted = {str(k).replace("(","").replace(")","").replace(",","").replace("'",""): v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}

#%% save nltk to json
import json

with open("/dir/", "w") as outfile:
    json.dump(d_sorted, outfile)
        