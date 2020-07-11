import wave
from os import listdir
from os.path import isfile,join
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
mypath = dir_path + "/vox"
otherpath = dir_path+"/alarm"

words = [f for f in listdir(mypath) if isfile(join(mypath, f))]
words += [f for f in listdir(otherpath) if isfile(join(otherpath, f))]

for i in range(0,len(words)):
    words[i] = words[i][:-4]

sentence = [input("Write sentence: ").lower()]
saidWords = sentence[0].split()

for word in saidWords:
    c = False
    for w in words:
        if w == word:
            c = True
    
    if not c:
        saidWords.remove(word)

data = []
for infile in saidWords:
    w = wave.open(mypath+"/"+infile+".wav",'rb')
    data.append([w.getparams(),w.readframes(w.getnframes())])
    w.close()

output  = wave.open("out.wav",'wb')
output.setparams(data[0][0])

for i in range(0,len(data)):
    output.writeframes(data[i][1])

output.close()