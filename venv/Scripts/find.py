import os,sys,re


name=None
path=None
abs=None
some_directory=(sys.argv[1] if len(sys.argv)>1 else ".")

ls=os.listdir(some_directory)

i=2
while i<len(sys.argv):
    x=sys.argv[i]
    if x=="-name":
        x=sys.argv[i+1]
        name=re.compile(x)


    i+=1
def iteracja(directory):
    ls=os.listdir(directory)
    for j in ls:
        j=os.path.join(directory,j)
        if os.path.isdir(j):
            iteracja(j)


