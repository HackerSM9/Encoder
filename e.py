try:
        import os,sys,time,marshal
except Exception as F:
        exit("[ModuleErr] %s"%(F))
        
if sys.version[0] in '2':
        exit("[sorry] use python version 3")

# Color
a='\033[1;30m'
r='\033[1;31m'
g='\033[32;1m' 
y='\033[1;33m'
c='\033[1;36m' 
w='\033[1;37m' 
n='\033[0;00m' 
br='\033[91;7m' 

bannerpy3 = """
         {}___ 
{} ___ _  |{}_  {}{}| {}Author  {}:{} HackerSM9
{}| . | | |{}_  {}{}| {}Code    {}:{} Python3
{}|  _|_  |{}___{}{}| {}Version {}:{} v.6.0
{}|_| |___| {}*{} https://github.com/HackerSM9 
""".format(r,y,br,n,y,w,r,w,y,br,n,y,w,r,w,y,br,n,y,w,r,w,y,r,a)

os.system('clear')
try:
    print(bannerpy3)
    print (y+' ['+w+'#'+y+'] '+w+'Example '+y+':'+w+' /sdcard/dfv.py')
    file = input(y+' ['+w+'?'+y+'] '+w+'Input your file location'+y+' :'+w+' ')
    o = file.replace('.py', '')
except KeyboardInterrupt:
    sys.exit()
else:
    try:
        strng = open(file, 'r').read()
    except IOError:
        print (r+'\n ['+w+'!'+r+'] '+r+'[ '+w+'Error '+r+'] '+w+'No such file or directory '+r+': '+w+'"'+dfv+'"\n')
        sys.exit()
    try:
        code = compile(strng,'','exec')
        data = marshal.dumps(code)
    except TypeError:
        print (R + '   ['+W+'!'+R+'] '+R+'[ '+W+'File Encrypted Successfully!\n') 
        sys.exit()

fileout = open(o + '.py', 'w')
fileout.write('# ENCRYPTED By HackerSM9\n')
fileout.write('# https://github.com/HackerSM9\n')
fileout.write('import marshal\n')
fileout.write('exec(marshal.loads(' + repr(data) + '))')
fileout.close()
time.sleep(2) 
print (y+'\n ['+w+'+'+y+'] '+w+'File success to compile   '+y+': ' + w + o + '.py\n')
