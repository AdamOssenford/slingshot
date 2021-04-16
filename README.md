# slingshot

## What is this

Slingshot is a python script that will allow you to send commands to a github repo which then get executed by github actions.  Once the command is executed by github actions it sends the output to a pastebin type site and then provides the output to the terminal along with the pastebin link.  

Using slingshot you can portscan a host without ever directly interacting with it.  This is not limited to just nmap, it can be anything you can dream up.

## Requirements

To use slingshot you will need a few things.  I have only tested on mac os
- git 
- gh command (get it at https://cli.github.com/)
- python
- python modules for subprocess, urllib, time
- a working github account


## how to

make sure to have the gh binary available 
- mine is located in /usr/local/bin/gh so adjust slingshot.py as needed for your environment

visit github and create a repository
copy the Dockerfile, commands, and .github folder from this rep into your repo

if you have additional packages you want available add them to the Dockerfile on the apt-get install line

make sure you have the .github/workflows/dockerimage.yml in your repository

add all items to your github repo
- git add *
- git commit -am "init"
- git push

now from within your local git directory you can execute ./slingshot.py
it will prompt you for a command to run

once you enter a command the following happens
- it writes the command out to the commands file
- runs a git checkin
- pushes to git
- the github actions picks up the Dockerfile and attempts to build the container
- the container calls the commands file
- the commands execute and store to a local txt file
- the txt file is pushed to pastebin
- it exits with status code 1
- slingshot grabs the actions log and pulls out the pastebin url
- slingshot displays the contents of the url and also shows the link to the url

## Disclaimer

I am not responsible for anything you do with this ever.  This is just a proof of concept and should be used for research purposes only