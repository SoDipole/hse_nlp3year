import re
import os
import csv

tokens = ''

abbrev_file = open('abbreviations_dict.txt', 'r', encoding = 'utf-8')
abbreviations = abbrev_file.read().split('\n') # keep with .
abbrev_file.close()
abbreviations_masked = [ab.replace('.', '###') for ab in abbreviations]

hyph_file = open('hyphen_dict.txt', 'r', encoding = 'utf-8')
hyphens = hyph_file.read().split('\n') # keep with -
hyph_file.close()
hyphens_masked = [ab.replace('-', '%%%') for ab in hyphens]

punctuation = ['\.', '\,\s', '\"', '\?\!', '\?\?\?', '\!\!\!', '[^\?](\?)[^\?!]', '[^\!\?](\!)[^\!]',
               '[^\d](\:)[^\d]', '\;', '\(', '\)', '…', '—', '-', '©', '[^\d](\/)[^\d]']

doc_id = 1
for root, dirs, files in os.walk('./reviews_clean'):
    for file in files:
        if file.endswith('.txt'):
            f = open(root + '/' + file, 'r', encoding = 'utf-8')
            text = f.read()
            f.close()
            
            text = re.sub('гл. г ', 'гл. г. ', text)
            for i in range(len(abbreviations)):
                text = text.replace(abbreviations[i], abbreviations_masked[i])
            text = re.sub('( г)\.', '\\1###', text)
            
            text = re.sub('\-(то[^А-ЯЁа-яё\w]|нибудь|либо)', '%%%\\1', text)
            text = re.sub('([^А-ЯЁа-яё\w][Пп]о|[^А-ЯЁа-яё\w][Вв]о|[^А-ЯЁа-яё\w][Вв]|[^А-ЯЁа-яё\w][Кк]ое)\-', '\\1%%%', text)
            text = re.sub('([\d])\-([^\d])', '\\1%%%\\2', text)
            for i in range(len(hyphens)):
                text = text.replace(hyphens[i], hyphens_masked[i])
            
            for i in range(len(punctuation)):
                search = punctuation[i]
                punct_in_text = re.findall(search, text)
                
                if punct_in_text:
                    for m in punct_in_text:
                        text = text.replace(m, ' ' + m + ' ')            
            
            words = text.split() # list of tokens
            
            # unite names into one token
            i = 0
            while i + 1 <= len(words) - 1:
                cap_word = '[А-Я]{1}[а-я]+'
                cap_word2 = '[А-Я]{1}[а-я]+ [А-Я]{1}[а-я]+'
                
                x1 = re.findall(cap_word, words[i])      # words[i-1] can't be '.', or can it?
                x2 = re.findall(cap_word, words[i+1])
                if x1:
                    if x2:
                        #print(words[i], words[i+1])
                        words[i] = words[i] + ' ' + words[i+1]
                        words.pop(i+1)
                        
                x3 = re.findall(cap_word2, words[i])
                x4 = re.findall(cap_word, words[i+1])
                if x3:
                    if x4:
                        #print(words[i], words[i+1])
                        words[i] = words[i] + ' ' + words[i+1]
                        words.pop(i+1)

                i += 1

            # naive sentence boundary:
            j = 0
            while j + 2 <= len(words) - 1:
                last_word = '.*?'
                end_sent = '[\.\!\?…]'
                first_word = '[А-Я0-9].*?'

                t1 = re.findall(last_word, words[j])
                t2 = re.findall(end_sent, words[j+1])
                t3 = re.findall(first_word, words[j+2])
                if t1:
                    if t2:
                        if t3:
                            words[j+1] += '</se>'
                j += 1
                
            for i in range(len(words)):
                words[i] = re.sub('###', '.', words[i])
                words[i] = re.sub('%%%', '-', words[i])
                
            token_id = 1
            for x in words:
                fields = str(doc_id) + '\t' + str(token_id) + '\t' + x + '\n'
                tokens += fields
                token_id += 1 
                
            doc_id += 1
            
token_file = open('tokens.txt', 'w', encoding = 'utf-8')
token_file.write(tokens)
token_file.close()
