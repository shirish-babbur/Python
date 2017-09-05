from sys import argv
from os.path import exists

script, fromfile, tofile = argv

print(f"Copying from {fromfile} to {tofile}.")

# we could do these two on one line, how?
indata = open(fromfile).read()

print(f"the input file is {len(indata)} bytes long.")

print(f"Does the output file exists? {exists(tofile)}")
print("Ready, Hit RETURN to continue, CRTL-C to abort.")
input(">> ")

out_file = open(tofile,"w")
out_file.write(indata)

print("Alright, all done!")

out_file.close()
