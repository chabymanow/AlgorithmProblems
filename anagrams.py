import re

def anagram(string_1, string_2):
    anagrams = False
    string_1 = re.sub(r"[^a-zA-Z0-9]","",string_1).lower()
    string_2 = re.sub(r"[^a-zA-Z0-9]","",string_2).lower()
    if(len(string_1) == len(string_2)):
        for char in string_1:
            if char in string_2:
                anagrams = True
            else:
                anagrams = False
                break
    else:
        anagrams = False
    
    return anagrams
print("The two words are anagrams: " + str(anagram("Second!$@#", "Second")))