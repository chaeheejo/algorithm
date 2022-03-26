import sys

def solution():
    inputNum=[]
    for line in sys.stdin:
        try:
            inputNum.append(int(line))
        except:
            break

    for n in inputNum:
        s='1'
        while int(s)%n!=0:
            s+='1'
        print(len(s))

if __name__ == '__main__':
    answer = solution()