#1
def solution(s):
    stack = []
    flag = True
    
    for _ in s:
        if _ == "(":
            stack.append(_)
        elif _ == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                flag = False
    
    if stack:
        flag = False
    
    return flag


#2 리스트에서 pop() 했을 때 안에 원소가 존재하지 않을 경우 if len(리스트) == 0: X => try/except로 예외처리 O

def is_pair(s):
    st = list()
    for c in s:
        if c == '(':
            st.append(c)

        if c == ')':
            try:
                st.pop()
            except IndexError:
                return False

    return len(st) == 0


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( is_pair("(hello)()"))
print( is_pair("()()()"))
