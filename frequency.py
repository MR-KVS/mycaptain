def my_freq(data):
    dic={}
    for i in data:
        if i not in dic.keys():
            dic[i]=1
        else:
            dic[i]+=1
    for j in dic:
        print(j +":"+str(dic[j]))

my_freq(input("enter the string:"))