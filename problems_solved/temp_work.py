len1 = raw_input()
len1 = int(len1)
gene = raw_input()
ch_len_start = 0
ch_len_end = 0
steady_gen=1
per_char_len = len1/4
ch_dict = dict()
ch1_dict = dict()
str_len = 0
master_str = ['A','G','T','C']

for ch in gene:
    try :
        if ch in ch_dict.keys():
            ch_dict[ch] += 1
        else:
            ch_dict[ch] = 1
    except:
        pass

if len(ch_dict.keys()) == 4:
    for ch in ch_dict.keys():
        if ch_dict[ch] == per_char_len:
            steady_gen=0
        else:
            steady_gen=1  
            break

    
if steady_gen == 1:
    for ch in gene:
        str_len += 1
        if ch1_dict.has_key(ch):
            if ch1_dict[ch] < per_char_len:
                ch1_dict[ch] += 1
            else:
                if ch_len_start == 0:
                    ch_len_start = str_len -1
                else:
                    ch_len_end = str_len -1                
        else:
            ch1_dict[ch] = 1 
    list_gene = list(gene)
    print (ch_len_end-ch_len_start+1)
else :
    print steady_gen
 
