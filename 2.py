def chem():
    input_file=open('/home/user/Документы/text1.txt', 'r')
    output_file=open('/home/user/Документы/text2.txt', 'w')
    line=input_file.readline().split()
    c, h, o = int(line[0]), int(line[1]), int(line[2])
    c1=c//2
    h1=h//6
    o1=o//1
    ans=min(c1, h1, o1)
    print(ans)
    output_file.write(str(ans)+'\n')
chem()