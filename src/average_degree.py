# example of program that calculates the average degree of hashtags

import re
import sys
import datetime
from collections import  defaultdict
import tweets_cleaned

#input_filename = sys.argv[1]
#output_filename = sys.argv[2]

#f1   = open(input_filename)
#fw  = open(output_filename,"w")

def graph_func(input_filename,temp_filename,output_filename):
    #Calling 1st script
    tweets_cleaned.clean_func(input_filename,temp_filename)

    f = open(temp_filename)
    f2 = open("hash_tags.txt","w")
    for line in f:
        hash_tag = re.findall(r"#[0-9a-zA-Z.-]+", line)
        hash_tag = [i.lower() for i in hash_tag]
        if hash_tag != []:
            match = re.search(r'\d{2}:\d{2}:\d{2}', line)
            var_time=datetime.datetime.strptime(match.group(), '%H:%M:%S').time()
            #print var_time.hour, var_time.minute,var_time.second
            for item in hash_tag:
                f2.write(item)
                f2.write(" ")
            f2.write(str(var_time.hour))
            f2.write(" ")
            f2.write(str(var_time.minute))
            f2.write(" ")
            f2.write(str(var_time.second))
            f2.write("\n")
    f2.close()

    #get Hashtags with timestamp
    node_dict = defaultdict(list)
    f3 = open("hash_tags.txt")
    for line in f3:
        tag_time_list=line.split(" ")
        nodes_list = tag_time_list[1:-3]
        hour,minutes,second=tag_time_list[-3:]
        for i,item in enumerate(nodes_list):
            for node in nodes_list:
                if(nodes_list[i] != node):
                    node_dict[nodes_list[i]].append(node)
        print node_dict

    #create twitter graph


if __name__ == '__main__':
    graph_func(sys.argv[1],sys.argv[2],sys.argv[3])

