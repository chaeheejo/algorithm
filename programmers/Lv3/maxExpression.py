from itertools import permutations

def solution(expression):
    answer = 0
    
    priority = list(permutations(['-','+','*'],3))
    
    def calculate(priority,n,expression):
        if n==3:
            return str(eval(expression))
        elif priority[n]=='-':
            s=eval('-'.join([calculate(priority,n+1,e) for e in expression.split('-')]))
        elif priority[n]=='+':
            s=eval('+'.join([calculate(priority,n+1,e) for e in expression.split('+')]))
        else:
            s=eval('*'.join([calculate(priority,n+1,e) for e in expression.split('*')]))
        return str(s)
    
    for p in priority:
        val=int(calculate(p,1,expression))
        answer=max(answer,abs(val))
        
    return answer
