import json

fl_dict = open('freeling_to_GS.json', 'r', encoding = 'utf-8')
d = json.load(fl_dict)
fl_dict.close()

fl_file = open('test_ana.txt', 'r', encoding = 'utf-8')
text = fl_file.read()
fl_file.close()

final = open('result.txt', 'w', encoding = 'utf-8')

text = text.split('\n')

for x in text:
    line = x.split(' ')
    if len(line) < 4:
        final.write('\n')
    else:
        new_line_l = [line[0],line[1]]
        new_tag_l = []
        old_tag = line[2]
# ------------------ADJECTIVES:------------------
        if old_tag[0] == 'A': 
            new_line_l.append('A')
            if old_tag[1] in d['A']['case']:
                new_tag_l.append(d['A']['case'][old_tag[1]])
                
            if old_tag[2] in d['A']['num']:
                new_tag_l.append(d['A']['num'][old_tag[2]])

            if old_tag[3] in d['A']['gen']:
                new_tag_l.append(d['A']['gen'][old_tag[3]])            
            
            if old_tag[5] in d['A']['form']:
                new_tag_l.append(d['A']['form'][old_tag[5]])

            if old_tag[6] in d['A']['degree']:
                new_tag_l.append(d['A']['degree'][old_tag[6]])      

# ------------------ADVERBS:------------------
        elif old_tag[0] == 'D':
            new_line_l.append('ADV')
            
            if old_tag[1] in d['ADV']['degree']:
                new_tag_l.append(d['ADV']['degree'][old_tag[1]])

# ------------------SPRO:------------------
        elif old_tag[0] == 'E':
            new_line_l.append('SPRO')
            
            if old_tag[1] in d['SPRO']['case']:
                new_tag_l.append(d['SPRO']['case'][old_tag[1]])
                
            if old_tag[2] in d['SPRO']['num']:
                new_tag_l.append(d['SPRO']['num'][old_tag[2]])

            if old_tag[3] in d['SPRO']['gen']:
                new_tag_l.append(d['SPRO']['gen'][old_tag[3]])            
            
            if old_tag[5] in d['SPRO']['person']:
                new_tag_l.append(d['SPRO']['person'][old_tag[5]])         

# ------------------NOUNS:------------------
        elif old_tag[0] == 'N':
            new_line_l.append('S')
            if old_tag[1] != 'P':
                if old_tag[2] in d['S']['case']:
                    new_tag_l.append(d['S']['case'][old_tag[2]])
                    
                if old_tag[3] in d['S']['num']:
                    new_tag_l.append(d['S']['num'][old_tag[3]])
    
                if old_tag[4] in d['S']['gen']:
                    new_tag_l.append(d['S']['gen'][old_tag[4]])       

# ------------------APRO:------------------
        elif old_tag[0] == 'R':
            new_line_l.append('APRO')

            if old_tag[1] in d['APRO']['case']:
                new_tag_l.append(d['APRO']['case'][old_tag[1]])
                
            if old_tag[2] in d['APRO']['num']:
                new_tag_l.append(d['APRO']['num'][old_tag[2]])

            if old_tag[3] in d['APRO']['gen']:
                new_tag_l.append(d['APRO']['gen'][old_tag[3]])                

# ------------------VERBS:------------------
        elif old_tag[0] == 'V':
            new_line_l.append('V')
            
            if old_tag[1] in d['V']['mood']:
                new_tag_l.append(d['V']['mood'][old_tag[1]])
                
            if old_tag[2] in d['V']['num']:
                new_tag_l.append(d['V']['num'][old_tag[2]])

            if old_tag[3] in d['V']['gen']:
                new_tag_l.append(d['V']['gen'][old_tag[3]])            
        
            if old_tag[4] in d['V']['tense']:
                new_tag_l.append(d['V']['tense'][old_tag[4]])            
        
            if old_tag[5] in d['V']['person']:
                new_tag_l.append(d['V']['person'][old_tag[5]])

            if old_tag[7] in d['V']['voice']:
                new_tag_l.append(d['V']['voice'][old_tag[7]])     

# ------------------PARTICIPLES:------------------

        elif old_tag[0] == 'Q':
            #print(old_tag)
            new_line_l.append('V')
            new_tag_l.append('partcp')
            
            if old_tag[1] in d['V']['mood']:
                new_tag_l.append(d['V']['mood'][old_tag[1]])
                
            if old_tag[2] in d['V']['num']:
                new_tag_l.append(d['V']['num'][old_tag[2]])

            if old_tag[3] in d['V']['gen']:
                new_tag_l.append(d['V']['gen'][old_tag[3]])            
        
            if old_tag[4] in d['V']['tense']:
                new_tag_l.append(d['V']['tense'][old_tag[4]])            
        
            if old_tag[5] in d['V']['person']:
                new_tag_l.append(d['V']['person'][old_tag[5]])

            if old_tag[7] in d['V']['voice']:
                new_tag_l.append(d['V']['voice'][old_tag[7]])

# ------------------ANUM:------------------

        elif old_tag[0] == 'Y':
            new_line_l.append('ANUM')
            
            if old_tag[1] in d['ANUM']['case']:
                new_tag_l.append(d['ANUM']['case'][old_tag[1]])
                
            if old_tag[2] in d['ANUM']['num']:
                new_tag_l.append(d['ANUM']['num'][old_tag[2]])

            if old_tag[3] in d['ANUM']['gen']:
                new_tag_l.append(d['ANUM']['gen'][old_tag[3]])      

# ------------------NUM:------------------

        elif old_tag[0] == 'Z':
            new_line_l.append('NUM')
            
            if old_tag[1] in d['NUM']['case']:
                new_tag_l.append(d['NUM']['case'][old_tag[1]])
                
            if old_tag[2] in d['NUM']['num']:
                new_tag_l.append(d['NUM']['num'][old_tag[2]])

            if old_tag[3] in d['NUM']['gen']:
                new_tag_l.append(d['NUM']['gen'][old_tag[3]])      
                
        elif old_tag[0] == 'B':
            new_line_l.append('PR') 
            
        elif old_tag[0] == 'C':
            new_line_l.append('CONJ')
            
        elif old_tag[0] == 'T':
            new_line_l.append('PART') 
            
        elif old_tag[0] in ['J','I']:
            new_line_l.append('INTJ')     
        
        elif old_tag[0] == 'P':
            new_line_l.append('ADVPRO')         
        
        else:
            new_line_l.append('')

        if len(new_tag_l) == 0:
            new_line_l.append('')                        
        else:
            new_line_l.append(','.join(new_tag_l))
            
        final.write('\t'.join(new_line_l) + '\n')

final.close()
