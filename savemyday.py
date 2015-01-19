filename = "notes.ini"
target = open(filename, 'w')
target.truncate()
target.write("[Notes]\n")
target.write("Directory=c:\\notes\data")
target.close()
print "DONE! %s file was restored successfully." % filename
print "You can close this windows now."
print "Have a nice day!"
