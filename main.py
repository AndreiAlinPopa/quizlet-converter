# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 01:12:47 2020

@author: Andrei
"""
"Interesting repo daddy dre but what does it do?"
"aha very easy! You see it converts quizlet into python dicts"
"quite swagaroni amirite"

import time

def Merge(dict1, dict2):
    '''
    merges two dicts together
    '''
    res = {**dict1, **dict2}
    return res

#----------------------#
# File selection setup #
#----------------------#

path = input("Please enter file path: ")

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
    
    
#------------------------------------------------#
# Who needs SQL when a scuffed database will do! #
#------------------------------------------------#

def input_correction(queryCache):
    response = input("\nAnswer: ")
    try:
        responseValue = queryCache[(int(response)-1)]
        print(responseValue)
        print(finalDict[responseValue])
        time.sleep(3)
    except:
        print("Please enter a valid number")
        time.sleep(1)
        input_correction(queryCache)


def search(query):
    '''
    query: string you are searching for
    returns absolutely nothing
    '''
    queryCache = []
    
    for keys in finalDict.keys():
        if query in keys:
            queryCache.append(keys)
            
    if len(queryCache) == 0:
        print("~~No results found~~")
        time.sleep(1)
    elif len(queryCache) == 1:
        queryCache[0]
        print(finalDict[queryCache[0]])
        time.sleep(3)
    else:
        print("\nDid you mean: \n")
        for i in range(len(queryCache)):
            print(str(i+1) + ". " + queryCache[i])
        input_correction(queryCache)
        
def enterText():
    textEntry = input(str(len(finalDict.keys())) + " Entries available. Search: ")
    search(textEntry)


#---------------#
# Program begin #
#---------------#


while True:
    enterText()
    