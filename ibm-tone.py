# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 22:20:14 2019

@author: Hanan Bahy1
"""

import json
from ibm_watson import ToneAnalyzerV3
from ibm_watson import ApiException
from collections import Counter
import pandas as pd

try:
    # Invoke a Tone Analyzer method
    tone_analyzer = ToneAnalyzerV3(version='2017-09-21',
                                    iam_apikey= "Ipna9t1L3kTsaMUp0dywjPG5I_6fZ8c-frG7y6X9Qa0b",
                                    url= "https://gateway-lon.watsonplatform.net/tone-analyzer/api")

except ApiException as ex:
    print("Method failed with status code " + str(ex.code) + ": " + ex.message)



hotels = pd.read_pickle("hotels_without_tones.pkl")

reviews =  hotels['reviews.text']


###utterance_analyses 
Tones=[]
for review in reviews :  #hotel by hotel 
    
    utterances =[ {"text":each ,"user":"person"} for each in review]
         
    try:
        tone_analysis= tone_analyzer.tone_chat(utterances).get_result()
    #print(json.dumps(tone_analysis, indent=2))
    except ApiException as ex:
        print("failed " + str(ex.code) + ": " + ex.message)
        Tones.append({"Not Found"})
        continue

    
    #parser the result
    sentences_tone = tone_analysis['utterances_tone'] 
    
    dict_t ={}
    
    #for 1 hotel  #in case of   .ton_chat(.........)     #the most correct as descriped
    for sentence in sentences_tone :
        for tone in sentence['tones'] :
           
            if  tone['tone_id']  not in dict_t.keys() :
                dict_t[tone['tone_id']] =[1, tone['score']]        #counter
                
            else :
                dict_t[tone['tone_id']][0] += 1        #counter
                dict_t[tone['tone_id']][1] += tone['score']   #sum of scores
                
    tone_review ={item : dict_t[item][1]/dict_t[item][0] for item in dict_t}
    if list(tone_review.keys()) != [] :  #not empty
        Tones.append(tone_review)
    else:
        Tones.append({"Not Found"})
        print("there's no Tones")
    
        
    
    #print(tone_review)

hotels['Tone'] =pd.Series(Tones)   #To add final data
#save..............

if __name__ == "__main__":
    hotels.to_pickle("hotels_with_tones.pkl")
    hotels.to_csv("hotels_with_tones.csv", index=False)
    

    
