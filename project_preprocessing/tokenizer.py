import re
import os
import csv

tokens = ''

abbrev_file = open('abbreviations.txt', 'r', encoding = 'utf-8')
abbreviations = abbrev_file.read().split() # keep with .
abbreviations_masked = [ab.replace('.', '###') for ab in abbreviations]

punctuation = ['\.', '\,\s', '\"', '\?\!', '\?\?\?', '\!\!\!', '[^\?](\?)[^\?!]', '[^\!\?](\!)[^\!]',
               '[^\d](\:)[^\d]', '\;', '\(', '\)', '…', '—', '©', '[^\d](\/)[^\d]']

doc_id = 1
for root, dirs, files in os.walk('./reviews_clean'):
    for file in files:
        if file.endswith('.txt'):
            f = open(root + '/' + file, 'r', encoding = 'utf-8')
            text = f.read()
            
            for i in range(len(abbreviations)):
                text = text.replace(abbreviations[i], abbreviations_masked[i])
            
            for i in range(len(punctuation)):
                search = punctuation[i]
                punct_in_text = re.findall(search, text)
                
                if punct_in_text:
                    for m in punct_in_text:
                        text = text.replace(m, ' ' + m + ' ')
            
            for i in range(len(abbreviations)):
                text = text.replace(abbreviations_masked[i], abbreviations[i])            
            
            words = text.split() # list of words
                             # separates names like 'James M. Cain'
            token_id = 1
            for x in words:
                fields = str(doc_id) + '\t' + str(token_id) + '\t' + x + '\n'
                tokens += fields
                
                token_id += 1 
                
            doc_id += 1
            
token_file = open('tokens.txt', 'w', encoding = 'utf-8')
token_file.write(tokens)
f.close()


