import json
# example of program that calculates the number of tweets cleaned

def tweets_clean_func(filename):
    f=open(filename)
    for line in f:
        print line
        parsed_line =  json.load(line)
    return parsed_line
