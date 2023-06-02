import sys
n = int(sys.stdin.readline())
dic = {} # 문자열 검색은 딕셔너리가 좋다
for i in range(n):
    root, left, right = sys.stdin.readline().split()
    dic[root] = [left, right]
# print(dic)

def pre(root): # 전위순회
    if root != ".":
        print(root, end = "")
        pre(dic[root][0])
        pre(dic[root][1])
    
def ino(root): # 중위순회
    if root != ".":
        ino(dic[root][0])
        print(root, end = "")
        ino(dic[root][1])
        
def post(root): # 후위순회
    if root != ".":
        post(dic[root][0])
        post(dic[root][1])     
        print(root, end = "")   
        
pre("A")
print()
ino("A")
print()
post("A")