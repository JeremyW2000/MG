# this is a script for parsing network logs created by Jeremy West

# Input format example:
#   50.112.00.11 - admin [11/Jul/2018:17:33:01 +0200] "GET /asset.css HTTP/1.1" 200 3574 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6"


import re

# network log class
class Log():
    def __init__(self, log):

        logSplit = log.split(' ')

        self.ip         = logSplit[0]

        self.isAdmin    = True if logSplit[2]=='admin' else False
        self.dateTime   = logSplit[3]
        self.reqType    = logSplit[4][1:]
        self.endPoint   = logSplit[5]
        self.protocol   = logSplit[6]
        self.response   = logSplit[7]
        self.browser    = logSplit[10]
        self.userInfo   = log.split('\"-\" ')[-1]

def readFile(dir):
    file = open(dir).readlines()
    return file

if __name__ == "__main__":
    
    path = "Info/programming-task-example-data.log"

    file = readFile(path)

    


    