def solution(p):
    answer = ''

    def isRight(strings):
        stack = []

        for i in range(len(strings)):
            if len(stack) != 0 :
                if stack[-1]=='(' and strings[i]==')':
                    stack.pop()
                else:
                    stack.append(strings[i])
            else:
                stack.append(strings[i])

        if len(stack) == 0:
            return True
        return False

    def braket(strings):
        if isRight(strings) == True:
            return strings
        
        if strings==' ':
            return ' '

        u, v = '',''
        cnt = 0
        for i in range(len(strings)):
            if strings[i] == '(':
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                u = strings[:i+1]
                v = strings[i+1:]
                break

        if isRight(u) == True:
            return u+braket(v)
        else:
            created='(' + braket(v) + ')'
            for i in range(1, len(u)-1):
                if u[i] == ')':
                    created += '('
                else:
                    created += ')'
            return created

    answer = braket(p)

    return answer

if __name__ == '__main__':
    answer = solution("()))((()")
    print(answer)
