import os
import shutil

dirList = os.listdir()
print('List of current folder')
for f in dirList:
    if os.path.isdir(f): print('-d--',f)
    else: print('-f--',f)
dirList = list(map(lambda f: f+'/', filter(lambda f: os.path.isdir(f), dirList)))
print()
print('Dirs which are going to be formatted:')
print()
for i in range(len(dirList)):
    print(i+1,'. ',dirList[i],sep='')

for curdir in dirList:
    print(' >> Formatting',curdir,'...')
    indir = curdir+'input/'
    outdir = curdir+'output/'
    os.makedirs(indir)
    os.makedirs(outdir)

    fileList = os.listdir(curdir)
    for curfile in fileList:
        shutil.move(curdir+curfile,curdir+curfile.split('.')[0])

    fileList = os.listdir(indir)
    for curfile in fileList:
        newfile = ''.join(curfile.split('.'))+'.txt'
        os.rename(indir+curfile,indir+newfile)

    fileList = os.listdir(outdir)
    for curfile in fileList:
        newfile = ''.join(curfile.split('.'))+'.txt'
        os.rename(outdir+curfile,outdir+newfile)

print()
print('Formatted!')