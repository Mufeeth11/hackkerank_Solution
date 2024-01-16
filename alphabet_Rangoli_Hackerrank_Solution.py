def print_rangoli(size):
    # your code goes here
    n=size
    formula=(n*2)-1
    upper_line=formula-1
    center_alphabet=chr(97)
    alphabet_list=[]
    upper=[]
    lower_line=2
    upperdiagram=[]
    for x in range(n-1,-1,-1):
        alphabet_list.append(chr(97+x))
    li=alphabet_list[::-1]
    alphabet_list=alphabet_list+li[1:]
    temp=list(alphabet_list)
    for row in range(n-1):
        alphabet_list.pop(len(alphabet_list)//2)
        alphabet_list=alphabet_list[:len(alphabet_list)//2]+alphabet_list[(len(alphabet_list)//2)+1:]
        upper.append(list(alphabet_list))
    upperdiagram=upper[::-1]
    for x in upperdiagram:
        print("-"*upper_line+"-".join(x)+"-"*upper_line)
        upper_line -= 2
    print("-".join(temp))
    for x in upper:
        print("-"*lower_line+"-".join(x)+"-"*lower_line)
        lower_line += 2


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)