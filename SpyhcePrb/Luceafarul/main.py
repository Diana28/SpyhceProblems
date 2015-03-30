# This Python file uses the following encoding: utf-8
'''
Created on Mar 29, 2015

@author: Diana User
'''

def main():
    input = open("Luceafarul.txt",'r') #input file
    output = open("Result.txt",'w') #output file
    text = input.readlines() 
    
    dict = {} # store information in a dictionary of type {letters1: [[word1,countWord1],[word2,countWord2]...],...}

    for line in text: 
        for word in line.split():
            word = word.translate(None,' ,”„.–;?!*"') # delete the characters attached to the words
            word = word.decode('utf-8').lower() # make all words lowercase

            if len(word) == 0: # we are not interested in the empty word
                continue
            
            letters = ''.join(sorted(word))  # get the sorted string formed by the word's letters
            
            """
                If the combination of letters from the word is not among the dictionary's keys, we add it 
            to the dictionary with initial count 1
                Otherwise we look for the word: - if exist we increment its count
                                                - else we add it with initial count 1
            """
            if letters not in dict.keys():
                dict[letters] = [[word,1]]          
                
            else:
                ok = True
                for pair in dict[letters]:
                    if pair[0] == word:
                        pair[1] = pair[1] + 1
                        ok = False
                        break
                if ok == True:
                    dict[letters].append([word,1])

    # display in a file or on the screen
    for item in dict:
        if len(dict[item]) > 1:    
            #print("For the letters '" + item + "' we have " + str(len(dict[item])) + " anagram(s):\n")  
            output.write("For the letters '" + item.encode('utf8') + "' we have " + str(len(dict[item])) + " anagrams:\n")
            sortedList = sorted(dict[item], key = lambda pair:pair[0])
            for pair in sortedList:
                #print("'" + pair[0].encode('utf8') + "' with count = " + str(pair[1]) + "\n")
                output.write("'" + pair[0].encode('utf8') + "' with count = " + str(pair[1]) + "\n")
            #print("-----------------------------------------------\n")
            output.write("-------------------------------------------\n")
            

main()