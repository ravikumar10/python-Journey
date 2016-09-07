"""
using  os module to get used with various function this module provides.

"""
import os
import string
import time
import sys

def dump(st):
    mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st
    print ("- size:", size, "bytes")
    print ("- owner:", uid, gid)
    print ("- created:", time.ctime(ctime))
    print ("- last accessed:", time.ctime(atime))
    print ("- last modified:", time.ctime(mtime))
    print ("- mode:", oct(mode))
    print ("- inode/dev:", ino, dev)

def replace(file, search_for, replace_with):
    # replace strings in a text file

    back = os.path.splitext(file)[0] + ".bak"
    temp = os.path.splitext(file)[0] + ".tmp"

    try:
        # remove old temp file, if any
        os.remove(temp)
    except os.error:
        pass

    fi = open(file)
    fo = open(temp, "w")

    for s in fi.readlines():
        fo.write(s.replace(search_for, replace_with))

    fi.close()
    fo.close()

    try:
        # remove old backup file, if any
        os.remove(back)
    except os.error:
        pass

    # rename original to backup...
    os.rename(file, back)

    # ...and temporary to original
    os.rename(temp, file)
    try:
        # remove old temp file, if any
        os.remove(back)
    except os.error:
        pass

if __name__ == '__main__':

	#
	# try it out!
	print("Changing the the content of a given file :: \n")
	file = "sample.txt"
	replace(file, "hello", "hello again")

#
# get stats for a file
	print("\nPrinting the File info of a given file :: \n")
	st = os.stat(file)
	print ("stat", file)
	dump(st)
	print

#
# get stats for an open file
	print("\nPrinting the File info of an open file:: \n")

	fp = open(file)
	st = os.fstat(fp.fileno())
	print ("fstat", file)
	dump(st)
#
# running a command in a given OS
	print("\nRunning system command to list the content of the cwd :: \n")
	if os.name == "nt":
		command="dir"
	else :
		command="ls -lrt"	
	os.system(command)
