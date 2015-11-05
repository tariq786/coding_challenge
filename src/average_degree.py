# example of program that calculates the average degree of hashtags

import re
import sys
import datetime
from collections import  defaultdict

def diff_times_in_seconds(t1_hr,t1_min,t1_sec, t2_hr,t2_min,t2_sec):
    # caveat emptor - assumes t1 & t2 are python times, on the same day and
    # t2 is after t1
    t1_secs = int(t1_sec) + 60 * ( int(t1_min) + 60*int(t1_hr) )
    t2_secs = int(t2_sec) + 60 * ( int(t2_min) + 60*int(t2_hr) )
    return( t2_secs - t1_secs)

def graph_func(input_filename,temp_filename,output_filename):
    #temp_filename is the output of the 1st program (tweets_cleaned.py)
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
    node_dict = defaultdict(set)
    history_tweets = []
    f3 = open("hash_tags.txt")
    for line_no,line in enumerate(f3,1):
        print line_no,line
        tag_time_list=line.split(" ")
        nodes_list = tag_time_list[0:-3]
        #print nodes_list
        hours,minutes,seconds=tag_time_list[-3:]
        #print hours,minutes,seconds
        history_tweets.append([[int(hours),int(minutes),int(seconds)],nodes_list])
        #logic for adding or deleting u    #first entry is always entered
        #first entry is always entered
        if(line_no == 1):
            for i,item in enumerate(nodes_list):
                for node in nodes_list:
                    if(nodes_list[i] != node):
                        #node_dict[nodes_list[i]].append(node)
                        node_dict[nodes_list[i]].add(node)

            sum_degrees = sum(len(row) for row in node_dict.values())
            print "The rolling average degree is now %.2f" %(float(sum_degrees)/float(len(node_dict.keys())))

        else:
            dt = diff_times_in_seconds(history_tweets[0][0][0],history_tweets[0][0][1],
                                    history_tweets[0][0][2],hours,minutes,seconds
                                    )
            print "dt is " +str(dt)
            if (dt > 60):
            #evict nodes from the import dictionary, remove entry history_tweets list,
            #adding new tweet and then calculate av. degree
                remove_nodes_list = history_tweets[0][1]
                print "remove_nodes_list"
                print remove_nodes_list
                #print "node_dict"
                #print node_dict
                for i,item in enumerate(remove_nodes_list):
                    for remove_node in remove_nodes_list:
                            if(remove_nodes_list[i] != remove_node):
                                print "key is "
                                print remove_nodes_list[i]
                                print "value is"
                                print remove_node
                                try:
                                    node_dict[remove_nodes_list[i]].remove(remove_node)
                                except KeyError:
                                    pass
                history_tweets.pop(0)
                #print "history_tweets (evict)"
                #print history_tweets
                #adding the new tweet
                #print nodes_list
                for i,item in enumerate(nodes_list):
                    for node in nodes_list:
                        if(nodes_list[i] != node):
                            node_dict[nodes_list[i]].add(node)
                sum_degrees = sum(len(row) for row in node_dict.values())
                print "The rolling average degree is now %.2f" %(float(sum_degrees)/float(len(node_dict.keys())))


            else:
            #add the nodes to the dictionary, add to the history_tweets list and
            #calculate av. degree
                #print nodes_list
                #print "history_tweets (after add)"
                #print history_tweets
                for i,item in enumerate(nodes_list):
                    for node in nodes_list:
                        if(nodes_list[i] != node):
                            node_dict[nodes_list[i]].add(node)

                sum_degrees = sum(len(row) for row in node_dict.values())
                print "The rolling average degree is now %.2f" %(float(sum_degrees)/float(len(node_dict.keys())))



if __name__ == '__main__':
    #run from the command prompt like
    #python average_degree.py ./tweet_input/tweets.txt ./tweet_output/ft1.txt ./tweet_output/ft2.txt
    graph_func(sys.argv[1],sys.argv[2],sys.argv[3])
