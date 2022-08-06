# this is a script for parsing network logs created by Jeremy West

import re

# network log class
class Log():
    def __init__(self, log):

        logSplit = log.split(' ')

        self.ip         = logSplit[0]
        self.isAdmin    = True if logSplit[2]=='admin' else False
        self.dateTime   = logSplit[3]
        self.reqType    = logSplit[5][1:]
        self.endPoint   = logSplit[6]
        self.protocol   = logSplit[7]
        self.response   = logSplit[8]
        self.browser    = logSplit[11]

        # this regex is used to get the users machine info
        # accounting for inconsitencies in data formatting ("junk extra")
        self.userInfo   = " ".join(re.findall(r'"[^"]*"', log)[-1:][0].split(' ')[1:])

    # a function that returns the member of a log specified
    def getAttribute(self ,attr):
        if attr == "ip":
            return self.ip
        if attr == "isAdmin":
            return self.isAdmin
        if attr == "dateTime":
            return self.dateTime
        if attr == "reqType":
            return self.reqType
        if attr == "endPoint":
            return self.endPoint
        if attr == "protocol":
            return self.protocol
        if attr == "response":
            return self.response
        if attr == "browser":
            return self.browser
        if attr == "userInfo":
            return self.userInfo

def readFile(dir):
    file = open(dir).readlines()
    return file

# a function that returns a hashmap with the key being the attribute specified
def mapByAttribute(attr, logs):
    logMap = dict()
    for log in logs:
        newLog = Log(log)
        if newLog.getAttribute(attr) not in logMap.keys():
            logMap[newLog.getAttribute(attr)] = [newLog]
        else:
            logMap[newLog.getAttribute(attr)] = logMap[newLog.getAttribute(attr)] + [log]
    return logMap
        
# A function that takes a map and an int and returns the keys
# that have been referenced the most
def topNMostOccuring(map, n):
    byCount = []

    for key in map:
        byCount = byCount + [[len(map[key]), key]]
    
    byCount.sort(key=lambda row:row[0], reverse=True)
    
    return byCount[0:n]


if __name__ == "__main__":
    
    # Reading file
    path = "Info/programming-task-example-data.log"
    logList = readFile(path)

    # Creating a hashmap by key
    logIPMap = mapByAttribute('ip', logList)
    logURLMap = mapByAttribute('endPoint', logList)

    # Getting top n most occuring from each hashmap
    top3IP = topNMostOccuring(logIPMap, 3)
    top3Url = topNMostOccuring(logURLMap, 3)

    # Output
    print("\nnumber of unique IP adresses: %2d" % len(logIPMap.keys()))
    print("\ntop 3 most visited urls: \n 1) %s, \n 2) %s, \n 3) %s" % (top3Url[0], top3Url[1] , top3Url[2]))#% max(len(urlList for urlList in logURLMap.values())))
    print("\ntop 3 most active IP's: \n 1) %s, \n 2) %s, \n 3) %s" % (top3IP[0], top3IP[1] , top3IP[2]))#% max(len(urlList for urlList in logURLMap.values())))



    