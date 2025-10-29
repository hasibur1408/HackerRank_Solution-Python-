def merge_the_tools(string, k):
    # your code goes here
    list1=[]
    for i in range(0,len(string),k):
        list1.append(string[i:i+k])
    for i in list1:
        l=[]
        for j in i:
            if j not in l:
                l.append(j)
        print(''.join(l))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)