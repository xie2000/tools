#!/usr/bin/python
# Filename : helloworld.py
import os
import shutil
import sys, getopt

opts, args = getopt.getopt(sys.argv[1:], "hp:")
packageName=""

for op, value in opts:
    if op == "-p":
        packageName = value
    elif op == "-h":
        print "-package out java file package name"
        sys.exit()

print "Package->" + packageName

listFiles = os.listdir("./")

if not os.path.exists("./packageOut"):  
	os.makedirs("./packageOut")  

for fileName in listFiles:
	if fileName.endswith("Reply.java"):
		pbName = fileName.replace("Reply.java", "");
		dst = "./packageOut/" + pbName + "Package.java"
		shutil.copyfile("./TemplatePackage.data", dst)

		f = open(dst, "r")
		d = f.read()
		f.close()
		d = d.replace("TAG_PACKAGE", packageName)
		d = d.replace("PBNAME", pbName)
		f = open(dst, "r+")
		f.write(d)
		f.close()
	