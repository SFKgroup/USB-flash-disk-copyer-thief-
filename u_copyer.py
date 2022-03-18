import os,time
path = 'F:\\'
last = ['pptx','.ppt','.vbs','.mp4','.exe','.mp3','.bat','.png','jpeg','.jpg','.doc','docx','.pdf','.xlsx']
save = 'D:\\test\\'
global other,fail,altogether
other = []
fail = 0
altogether = 0
def copy_file(dir_path,root,save_path):
    global other,fail,altogether
    dir_list = []
    dir_st = []
    try:
        os.makedirs(save_path)
    except OSError as e:
        print(save_path+'文件夹已创建')
    #print(os.listdir(dir_path))
    for dirs in os.listdir(dir_path):
        if dirs[-4:] in root:
            #print(dirs)
            result = os.system('copy "' + str(dir_path) + str(dirs) + '" "' + str(save_path) + '" /Y')
            fail = fail + int(result)
            altogether += 1
        elif not('.' in dirs):
            dir_list.append(str(dir_path) + str(dirs) + '\\')
            dir_st.append(str(dirs) + '\\')
        else:
            other.append(str(dirs))
    return dir_list,dir_st

time.sleep(600)
ret,rl = copy_file(path,last,save)
while ret != []:
    n_ret = []
    n_rl = []
    for ret_dir,ret_name in zip(ret,rl):
        #print(ret_dir,ret_name)
        o_ret,o_rl = copy_file(ret_dir,last,save+ret_name)
        #print(o_ret)
        for t,l in zip(o_ret,o_rl):
            n_ret.append(t)
            n_rl.append(l)
    ret = n_ret
    rl = n_rl
    print(n_ret,n_rl)