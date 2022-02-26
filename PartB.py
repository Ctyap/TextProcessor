#Assignment 1: Text Processing Part B
#Cooper Yap, CTYAP, 90967488

import re
import sys

class Intersection():
    
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
                    
        return set(token_lst)
    
    #O(len(tokenSetA)+len(tokenSetB)) according to Pattis notes 
    def intersection(self, tokenSetA, tokenSetB):
        #Returns a new set with elements that are common to all sets.
        commonTokens = (tokenSetA).intersection(tokenSetB)
        
        #Return number of common tokens
        return len(commonTokens)
        

if __name__ == '__main__':   
    
    #Instantiate Class
    tokenize = Intersection()
    
    try:
            #Retrieve token list of each file
            tokenSetA = tokenize.tokenize(sys.argv[1])
            tokenSetB = tokenize.tokenize(sys.argv[2])
            
            #Call on to get number of common tokens
            numberOfCommonTokens = tokenize.intersection(tokenSetA, tokenSetB)
            
            #Output the common words
            print(numberOfCommonTokens)
            
    #FilenotFound and IndexError exceptions with custom message.
    except(FileNotFoundError):
        print("File not found.")
    except(IndexError):
        print("Only enter two text files to find intersection.")
           
