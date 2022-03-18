import psutil
import win32api,win32con,win32file
import time
import os
def run():
    uf = []
    num = 0
    ept = []
    while True:
        disk_list = []
        for item in psutil.disk_partitions():
            # 判断是不是U盘
            if "removable" in item.opts:
                # 获取U盘的盘符
                disk_list.append(item.mountpoint)
        # 把盘符写入内存，为了不持续请求
        if disk_list != ept:
            for pf in disk_list:
                if pf not in uf:
                    print("U盘插入")
                    uf.append(pf)
                    seriaNumber = win32api.GetVolumeInformation(pf)
                    key = input('确认将 ' + pf + '(' + seriaNumber[0] + ') 设置为管理员盘？\n(设置不会删除盘内内容，U盘可正常使用)\n(Y\\n):')
                    if key == 'Y':
                        u_name = str(seriaNumber[1]).replace('0','o').replace('-','_').replace('1','|').replace('8','&').replace('5','S').replace('2','Z').replace('9','g').replace('6','G')
                        try:os.mkdir(pf+'__$#&Setting&#$__')
                        except:pass
                        win32api.SetFileAttributes(pf+'__$#&Setting&#$__', win32con.FILE_ATTRIBUTE_HIDDEN)
                        grand = open('./log.sys','r')
                        im = ''
                        for a in range(4):
                            ot = grand.readline()
                            im += ot
                        grand.close()
                        im += '@' + u_name
                        grand = open('./log.sys','w')
                        grand.write(im)
                        grand.close()
                        win32file.CopyFile('./log.sys',pf+'__$#&Setting&#$__\\log.sys',0)
                        grand = open(pf+'__$#&Setting&#$__\\res.sys','w')
                        grand.write('')
                        grand.close()
                        grand = open(pf+'__$#&Setting&#$__\\zig.sys','w')
                        grand.write('')
                        grand.close()
                        print('U盘代号:',u_name)
                        print('成功！请勿删除U盘内生成的文件')
                    else:
                        ept.append(pf)
                        print('已拒绝')

        else:
            # 拔出u盘初始化内存
            num += 1
            uf = []
            print("U盘检测中"+num*'.'+(6-num)*' ',end='\r')
            if num >= 6:num = 0
            time.sleep(1)


if __name__ == "__main__":
    run()