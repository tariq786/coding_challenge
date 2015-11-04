# example of program that calculates the number of tweets cleaned

from collections import Counter

counter_unicode =  Counter()

def tweets_clean_func(filename):
    fw=open('out.txt','w')
    f=open(filename)
    for line in f:
     #   print line
        line_lst = line.split(',"',4)
     #   print line_lst
        time_stamp = line_lst[0]
        time_stamp_val = time_stamp.split(":",1)[1]
        text_field = line_lst[3]
        print text_field
        text_val = text_field.split(":",1)[1]
       # print text_val
        if "\u" in text_val:
            text_val = text_val.decode('unicode_escape').encode('ascii','ignore')
            counter_unicode['unicode'] += 1
        if '\/' in text_val:
            text_val = text_val.replace("\/","/")
#        if "\\" in text_val:
#            text_val = text_val.replace("\\","\")
#        if "\'" in text_val:
#            text_val = text_val.replace("\'","'")
#        if '\"' in text_val:
#            text_val = text_val.replace('\"','"')
#        if "\n" in text_val:
#            text_val = text_val.replace("\n"," ")
#        if "\t" in text_val:
#            text_val = text_val.replace("\t"," ")
        if(text_val != ""):
            fw.write(text_val[1:-2])
            fw.write(" ")
            fw.write("(timestamp: ")
            fw.write(time_stamp_val[1:-1])
            fw.write(")")
            fw.write("\n")
    fw.write("\n")
#    fw.write(counter_unicode['uniqu
    fw.write("%d tweets contained unicode." %(counter_unicode['unicode']))
    fw.close()
    return text_val, counter_unicode
