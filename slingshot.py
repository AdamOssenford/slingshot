#!/usr/bin/python
import subprocess
import urllib
import time

# FUNCTIONS
# this takes commands and runs them
def fireAway(command):
  ps = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  output = ps.communicate()[0]
  return output.strip()

def printUrl(url):
  f = urllib.urlopen(url)
  myfile = f.read()
  print(myfile)
  print("Data resides at url " + url + "\n")

#write commands file
def writeCommands(booyah):
  a = open("commands", "w")
  a.write("#!/bin/bash")
  a.write("\n")
  a.write("export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin")
  a.write("\n")
  a.write(booyah + " > /tmp/outfile.txt")
  a.write("\n")
  a.write("curl --upload-file '/tmp/outfile.txt' 'https://paste.c-net.org'")
  a.write("\n")
  a.write("rm /tmp/outfile.txt")
  a.write("\n")
  a.write("exit 1")
  a.close()

#checkin to git
def shitNgit():
  fireAway(git1)
  fireAway(git2)
  fireAway(git3)

# VARIABLES
#github command1
chop = "/usr/local/bin/gh run list -L 1 | awk '{print $NF}' | head -1"
#github command2

git1 = "git add commands"
git2 = "git commit -am 'firing'"
git3 = "git push"


# prompt for commands
print("command blaster")
powpow = raw_input("what command should we run now? ")

# setup correct output for commands files
writeCommands(powpow)

# run git commands 
shitNgit()

print "checked into git\n"
print "getting the log number for this command\n"
time.sleep(3)

this_run = fireAway(chop)
print "found log id " + this_run

next_run = "gh run view " + this_run + " --log-failed | grep 'paste.c-net.org' | awk ' { print $NF } ' | cut -d ':' -f2"

are_we_there_yet = fireAway(next_run)

while are_we_there_yet.__contains__("still in progress"):
	print "still running... sleeping 10 seconds\n"		
	time.sleep(10)
	are_we_there_yet = fireAway(next_run)


print "run complete, getting results for you\n"
time.sleep(2)
printUrl("https:" + fireAway(next_run))
