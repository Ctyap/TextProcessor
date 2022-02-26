#Assignment 1: Text Processing Part A
#Cooper Yap, CTYAP, 90967488

import re
import sys
from collections import defaultdict 
from collections import OrderedDict



class Tokenize():
    
    #Quadratic Time - O(n^2) performs a linear time operation for each word in the line of text file.
    def tokenize(self, filePath):
        
        #Create a opened file object.
        file_object = open(filePath, encoding = "utf8")
        
        #Create a list that holds accepted tokens
        token_lst = list()
        
        #Iterate each line of text file
        for line in file_object:
            
            #Split each line according to regex pattern: [a-zA-Z0-9_]+
            for word in re.split(r'(\W+)', line):
                
                #Splits words if underscore char found.
                if '_' in word:
                    
                    #Create a list of divided by underscore
                    word_lst = word.split('_')
                    
                    #Add lower case words to token list of alphanumeric.
                    token_lst.extend(split_word.lower() for split_word in word_lst if split_word.isalnum())
                else:  
                    #Check if word is alphanumeric.
                    if word.isalnum():
                        
                        #Add lower case word to list to be independent of capitalization
                        token_lst.append(word.lower())
                    
        return token_lst
    
    
    #Linear Time - O(n) algorithm examines all values of the given dictionary.
    def computeWordFrequencies(self, token_lst):
        
        #Create default dict with int value
        tokenFrequencyDict = defaultdict(int)
        
        #Iterate through list and add to  dictionary
        #Increment dictionary values by 1 if exists
        for token in token_lst:
            tokenFrequencyDict[token] += 1
        
        return tokenFrequencyDict
    
    
    #Time - O(N log2N) as the function uses the sorting algorithm of Python which uses a special version of merge sort.
    def print_frequencies(self, tokenFrequency_dict):
        #Sort dictionary by value and decreasing order
        sorted_dictionary = OrderedDict(sorted(tokenFrequency_dict.items(), key=lambda item: (-item[1], item[0])))
        
        #Print token and count
        for token, count in sorted_dictionary.items():
            print(token + " -> " + str(count))
                             

if __name__ == '__main__':

    #Instantiate Class
    token = Tokenize()
    
    try:
        #Call print method that takes in the token dictionary from sys.argv 
        token.print_frequencies(token.computeWordFrequencies(token.tokenize(sys.argv[1])))
        
        #FilenotFound and IndexError exceptions with custom message.
    except(FileNotFoundError):
        print("File not found.")
    except(IndexError):
        print("Only enter one text file.")
        
        