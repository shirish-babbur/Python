from sys import argv

script, fromfile, tofile = argv

open(tofile,"w").write(open(fromfile).read())

print("All bytes copied...!")
