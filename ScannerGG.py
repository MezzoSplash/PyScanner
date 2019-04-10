#!/usr/bin/env python3

import subprocess
import os

def onePing(ipinput):
    #check if input is a string first
    if type(ipinput) != str:
        return "not correct, try again"
    # make the command, split input
    doPing = "ping -c 1 {}".format(ipinput).split()
    #print result and hide output of subprocess
    result = subprocess.run(doPing, stdout=subprocess.DEVNULL)
    returncode = result.returncode
    
    return returncode, result


def main():
    i = 1
    while i < 101:
        #build command
        ipStart = "192.168.56.{}".format(str(i))
        doPingS = "ping -c 1 {}".format(ipStart).split()
        #return output from doPingS
        returnCode, output = onePing(ipStart)
        #check returncodes, and output because own output is hidden
        if returnCode == 0:
            print("the ip {} is up".format(output.args[-1]))
        elif returnCode == 1:
            print("the ip {} is not up".format(output.args[-1]))
        
        i+=1
        
main()
