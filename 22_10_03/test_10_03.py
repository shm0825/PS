x, y = map(int, input().split())
result = x-y

if (result > 0):
    print(">")
if(result < 0):
    print("<")
if(result == 0):
    print("==")