# example of program that calculates the number of tweets cleaned

from collections import Counter
import re

counter_unicode =  Counter()

#def tweets_clean_func(filename):
fw=open('../tweet_output/f1.txt','w')
f=open("tweets.txt")
for i,line in enumerate(f,1):
    line_lst = line.split(',"',4)
    #print line_lst
    time_stamp = line_lst[0]
    #print time_stamp
    time_stamp_val = time_stamp.split(":",1)[1]
    try:
        text_field = line_lst[3]
        #print text_field
        text_val = text_field.split(":",1)[1]
        #print text_val
        if "\u" in text_val:
            text_val = text_val.decode('unicode_escape').encode('ascii','ignore')
            counter_unicode['unicode'] += 1
        if '\/' in text_val:
            text_val = text_val.replace("\/","/")

        text_val = re.sub(' +',' ',text_val)
        text_val = re.sub('\n+',' ',text_val)
        text_val = re.sub('\t+',' ',text_val)
        #print text_val
        if  text_val != '""':
            fw.write(text_val[1:-1])
            fw.write(" ")
            fw.write("(timestamp: ")
            fw.write(time_stamp_val[1:-1])
            fw.write(")")
            fw.write("\n")

    except IndexError:
        #print "Invalid Line detected on Line %i" %(i)
        pass

fw.write("\n")
fw.write("%d tweets contained unicode." %(counter_unicode['unicode']))
fw.close()

#    return time_stamp, text_val, counter_unicode
