
#BASIC GITHUB COMMANDS--POWERSHELL TERMINAL

#STEP 1:LOGIN--gh auth login

#STEP 2:INITIALIZE--git init
#starts up the repo in github

#STEP 3:STAGE--git add . ("." stages all in current folder. "filename" for specific files)
#chooses which files you want for the save point
#--git reset (undoes stage)

#STEP 4:CONFIRM--git status
#verify it worked

#STEP 5:COMMIT--git commit -m "message"
#creates save point(snapshot) locally w/message

#STEP 6:REPOSITORY--git remote add origin <url>
#CREATE REPO IN GITHUB FIRST
#connects your local repo to repo in github 

#STEP 7:PUSH--git push *(if 1st time: git push -u origin master)
#--master or main? check using --branch
#uploads commit to github

#STEP 8:PULL--git pull
#downloads latest from github

print("testing basic steps")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~