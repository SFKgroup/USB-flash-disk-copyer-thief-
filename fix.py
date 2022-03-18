import os
input_path = input('input_path:')
output_dir = input('output_dir:')
numbers = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H']
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