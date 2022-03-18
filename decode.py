import os
import time
import zipfile
import win32file
import psutil
import win32api

def decodes(input_path,output_dir):
    pwd = b'1118184754114511951798881405'
    numbers = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H']
    os.rename(input_path,input_path.split('.')[-2] + '.zip')
    zip_file = zipfile.ZipFile(input_path.split('.')[-2] + '.zip')
    zip_extract = zip_file.extractall('./',pwd=pwd)
    zip_file.close()
    os.remove(input_path.split('.')[-2] + '.zip')
    print('unzipped')
    refile = open(input_path,'r')
    first = True
    Caesar_list = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    while True:
        codes = refile.readline()
        if codes[:1] == '@':
            if not(first):
                out.close()
                first = False
            output_path = output_dir + '\\' + codes[1:].split('|')[0].replace('\n','')
            try:os.mkdir(output_path.replace(output_path.split('\\')[-1],''))
            except:pass
            key = int(codes[1:].split('|')[1].replace('\n',''))
            out = open(output_path,'wb')
        else:
            imformation = codes.replace('\n','')
            for one_B in numbers:imformation = imformation.replace(one_B,Caesar_list[int(numbers.index(one_B)) - key + 16])
            out.write(bytes.fromhex(imformation))
            if codes == '':break
    refile.close()
    out.close()
    print('rezipping...')
    zip_file = zipfile.ZipFile(input_path.split('.')[-2] + '.zip','w')
    zip_file.setpassword(pwd)
    zip_file.write(input_path,compress_type=zipfile.ZIP_DEFLATED)
    zip_file.close()
    os.remove(input_path)
    os.rename(input_path.split('.')[-2] + '.zip',input_path)
    print('Done.')
otpt = './out_put'
try:os.mkdir(otpt)
except:pass
otpath = './provide.sys'
grand = open('./log.sys','r')
back = grand.readlines()
u_name = int(back[4][1:].replace('\n','').replace('o','0').replace('_','-').replace('|','1').replace('&','8').replace('S','5').replace('Z','2').replace('g','9').replace('G','6'))
grand.close()
uf = []
num = 0
while True:
    disk_list = []
    for item in psutil.disk_partitions():
        if "removable" in item.opts:disk_list.append(item.mountpoint)
    if disk_list != []:
        for pf in disk_list:
            if pf not in uf:
                uf.append(pf)
                print("U盘已连接.")
                seriaNumber = win32api.GetVolumeInformation(pf)
                if seriaNumber[1] == u_name:
                    for pth in os.listdir(pf+'__$#&Setting&#$__\\'):
                        if pth[:20] == 'Microsoft_Protection':
                            try:
                                decodes(pf+'__$#&Setting&#$__\\' + pth,otpt)
                                print('文件:' + pf+'__$#&Setting&#$__\\' + pth + '  完成')
                            except:
                                print('\033[0;33;40m文件:' + pf+'__$#&Setting&#$__\\' + pth + '  损坏\033[0m')
                    print('All_Done.')
                else:print('\033[0;33;40m错误的U盘      \033[0m')
    else:
        num += 1
        uf = []
        print("U盘检测中"+num*'.'+(6-num)*' ',end='\r')
        if num >= 6:num = 0
        time.sleep(1)