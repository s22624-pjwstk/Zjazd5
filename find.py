import os,sys,re


name=None
path=None
abs=False
some_directory=(sys.argv[1] if len(sys.argv)>1 else ".")

ls=os.listdir(some_directory)

i=2
while i<len(sys.argv):
    x=sys.argv[i]
    if x=="-name":
        x=sys.argv[i+1]
        name=re.compile(x)
        i+=1
    elif x=="-abs":
        abs=True


    i+=1
def iteracja(directory):
    ls=[]
    for j in os.listdir(directory):
        j=os.path.join(directory,j)
        ls.append(j)
        if os.path.isdir(j):
            ls.extend(iteracja(j))
    return ls

a=iteracja(some_directory)

for each in a:
    dir,file=os.path.split(each)
    if not name.search(file):
        continue
    if abs:
        each=os.path.abspath(each)
    print(each)