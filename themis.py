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
for i in range(len(dirList)):
    print(i+1,'. ',dirList[i],sep='')
print()

for curdir in dirList:
    print(' >> Formatting',curdir,'...')
    subdirList = os.listdir(curdir)
    subdirList = list(map(lambda f: f+'/', filter(lambda f: os.path.isdir(curdir+f), subdirList)))
    NumDir = len(str(len(subdirList)))
    print(subdirList)
    print()
    indir = curdir + 'input/'
    outdir = curdir + 'output/'
    os.makedirs(indir)
    os.makedirs(outdir)
    cnt = 0
    for subdir in subdirList:
        subdirPath = curdir + subdir
        if os.path.isdir(subdirPath):
            fileList = os.listdir(subdirPath)
            for curfile in fileList:
                ext = curfile.split('.')[-1].lower()
                if ext == 'inp':
                    newfile = 'input' + str(cnt).zfill(NumDir) + '.txt'
                    os.rename(subdirPath+curfile, subdirPath+newfile)
                    shutil.move(subdirPath+newfile, indir)
                elif ext == 'out': 
                    newfile = 'output' + str(cnt).zfill(NumDir) + '.txt'
                    os.rename(subdirPath+curfile, subdirPath+newfile)
                    shutil.move(subdirPath+newfile, outdir)
        cnt += 1
        shutil.rmtree(subdirPath)