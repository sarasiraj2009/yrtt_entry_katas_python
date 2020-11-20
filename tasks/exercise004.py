# Move the first letter of each word to the end of it, then add "ay" 
# to the end of the word. Leave punctuation marks untouched.

def pig_it(text):

    import string, re
    words = re.sub(fr'([{string.punctuation}])\B', r' \1', text).split()

    for i in range(len(words)):
        word = words[i]
        if word not in string.punctuation:
            word = word[1:]+word[0] + "ay"
            words[i] = word
            
    text = " ".join(words)
    text = re.sub(r' ([^A-Za-z0-9])', r'\1', text)
    
       
    return text