import time
from datetime import datetime as dt
#Windows host file path
hostsPath= '‪D:/hosts' #r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"

#Add the website you want to block, in this list
websites=["www.youtube.com","youtube.com", "www.facebook.com", "facebook.com"]
while True:
   #Duration during which, website blocker will work
   if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
       print ("Sorry Not Allowed...")
       with open(hostsPath,'r+') as file:
          content = file.read()
          for site in websites:
             if site in content:
                pass
             else:
                file.write(redirect+" "+site+"\n")
   else:
      with open(hostsPath,'r+') as file:
          content = file.readlines()
          file.seek(0)
          for line in content:
             if not any(site in line for site in websites):
                file.write(line)
             file.truncate()
   print ("Allowed access!")
time.sleep(5)

'''
Here I am going to tell scheduling the script in the window since it is somewhat dubious, let start -

Most importantly change the expansion of your script from ".py" to ".pyw".
Now open task scheduler and click on “Create Task” and fill the name of your decision and flag Run with the most elevated benefit.
Now go to triggers, select "At startup" to start the task.
Go to the Action bar and make another activity and give the way/path of your script.
Go to the conditions bar and unflag the power section.
Press ok and your script is scheduled.
Script scheduled is complete now.

Finally, restart your computer and see the result.
'''