"""
a) Write a function getVowels that takes in an utterance as argument and returns the vowels (‘A’, ‘E’, ‘I’, ‘O’, ‘U’) in uppercase. Sort your list according to the sequence of the alphabets in your vowels.

b) Write the function countChars that takes in an utterance and a character as arguments, and call the function to return the number of occurrence of the character value in the utterance.

"""


def getVowels(text):                              # Part a)
    text = text.upper()
    text_len = len(text)
    new_list =[]
    
    for x in range(0,text_len):
        if text[x] =="A" or text[x] =="E" or text[x] =="I" or text[x] =="O" or text[x] =="U":
            new_list.append(text[x])
                   
    new_list.sort()
    return (new_list)

 
print(getVowels("machine learning"))
print(getVowels("image classification"))


def countChars(utterance, character):              # Part b)
    tot_char = utterance.count(character)
    return(tot_char)

print()
print(countChars("It's going to be interesting to see how society deals with artificial intelligence, but it will definitely be cool.", "a"))

print(countChars("Some people call this artificial intelligence, but the reality is this technology will enhance us. So instead of artificial intelligence, I think we'll augment our intelligence.", "i"))


            
    

