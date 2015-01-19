import os
#kill notes (versions)
os.system("taskkill  /im notes.exe")
os.system("taskkill  /im notes2.exe")
os.system("taskkill  /im nlnotes.exe")

#Rewrite notes.ini
filename = "notes.ini"
target = open(filename, 'w')
target.truncate()
target.write("[Notes]\n")
target.write("Directory=c:\\notes\data")
target.close()

#Confirmation
print "DONE! %s file was restored sucesfully." % filename
print "You can close this windows now."
print "Have a nice day!"