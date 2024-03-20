from pydub import AudioSegment
import os
import glob
#segmentation

#import numpy as np
#import IPython.display as ipd
source=r"D:\carnatic\22_Nadaswaram\wav\*.wav"
lst=glob.glob(source)
print(lst)
for filename in lst:
    songname = filename
    audio = AudioSegment.from_wav(songname) 
    n = len(audio)
    interval = 30 * 1000
    overlap = 0
    start = 0
    end = 0
    flag = 0
    counter=1
    for i in range(0,  n, interval): #2 * n
        if i == 0:
            start = 0
            end = interval  
        else: 
            start = end
            end = start + interval 
        if end >= n: 
            end = n 
            flag = 1
        chunk = audio[start:end] 
        file = filename+str(counter)+'.wav'
        chunk.export(file, format ="wav") 
        print("Processing chunk "+str(counter)+". Start = "+str(start)+" end = "+str(end))
        counter = counter + 1

