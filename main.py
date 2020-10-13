# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 01:12:47 2020

@author: Andrei
"""

"Interesting repo daddy dre but what does it do?"
"aha very easy! You see it converts quizlet into python dicts"
"quite swagaroni amirite"



path = "C://Users//Andrei//Desktop//security.txt"

def Merge(dict1, dict2):
    '''
    merges two dicts together
    '''
    res = {**dict1, **dict2}
    return res

#---------------------------------------------------#
# Not the most object oriented, but it's only small #
#---------------------------------------------------#


with open(path,"r") as openFile:
    for lines in openFile:
        list1 = lines.split(";")
        #keys + values together
        
list2 = []
for entries in list1:
    list2.append(entries.split("@@"))

#now we convert the list... to a list of dicts!

dictList = []
for lists in list2:
    try:
        listConversion = dict([lists])
        dictList.append(listConversion)
    except:
        pass
    
#now we merge all lists in the dictlist and make a list list. Hold on, that'd just be a list.

finalDict = Merge(dictList[0], dictList[1])        
#gotta make sure it has a dictionary with a start point

for i in range(2, len(dictList)):
    finalDict = Merge(finalDict, dictList[i])
#finalDict is now a full on dictionary with appropriate key values