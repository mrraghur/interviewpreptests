from shutil import copyfile
import os

newfile = 'pow_x_n'
oldfile = 'rotatearray'
src = f'./goldFiles/python3/{oldfile}.py'
dst = f'./goldFiles/python3/{newfile}.py'
copyfile(src, dst)

src = f'./testcases/{oldfile}.json'
dst = f'./testcases/{newfile}.json'
copyfile(src, dst)

src = f'./workspace./python3workspace./{oldfile}.py'
dst = f'./workspace./python3workspace./{newfile}.py'
copyfile(src, dst)


########
#populate __init__.py
def py(s):
    if s[-3:] == '.py' and s[:2] != '__':
        return True
    
    return False

fileslist = os.listdir('./goldFiles/python3/')
print(fileslist)

solsNames = list(filter(py,fileslist))

solsImports = ["import sys","sys.path.insert(0,'./goldFiles/python3')",""]
for s in solsNames:
    sol = f"from {s[:-3]} import *"
    solsImports.append(sol)

init = open('./goldFiles/python3/__init__.py','w')
init.write('\n'.join(solsImports))
init.close()
print('\n'.join(solsImports))
# print(solsImports)


fileslist = os.listdir('./workspace/python3workspace/')
print(fileslist)

solsNames = list(filter(py,fileslist))

solsImports = ["import sys","sys.path.insert(0,'./workspace/python3workspace')",""]
for s in solsNames:
    sol = f"from {s[:-3]} import *"
    solsImports.append(sol)

init = open('./workspace/python3workspace/__init__.py','w')
init.write('\n'.join(solsImports))
init.close()
print('\n'.join(solsImports))




