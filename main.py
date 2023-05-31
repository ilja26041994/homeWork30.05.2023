# # 9.14
# x = input('some word')
# result = len(x)
# print(x[result - 1])
# # 9.15
# while True:
#     x = input('some word')
#     x1 = x.find('k')
#     if x1 >= 0:
#         print('k')
#     if x1 < 0:
#         continue
# # 9.16
# while True:
#     x = input('some word')
#     c = (x[1])
#     v = (x[3])
#     if c == v:
#         print('+')
#     else:
#         print('wrong')
# # 9.38 a
# x = input('some word')
# result = len(x)
# cnt = 1
# while True:
#     cnt -= 1
#     if result == 12:
#         print(x[result-8],x[result-7],x[result-6],x[result-5],x[result-4],x[result-3],x[result-2],x[result-1],x[result-12],x[result-11],x[result-10],x[result-9])
#     if cnt ==0:
#         break
# # 9.41
# x = input('some word')
# result = len(x)
# print(x[result*(-1)])
# while True:
#     result -= 1
#     print(x[result*(-1)])
#     if result == 1:
#         break
# # 9.56
# x = input('some word')
# v = str('o')
# result = len(x)
# g = 0
# while True:
#     result -= 1
#     c = (x[result])
#     if c == v:
#         g += 1
#     if result == 0:
#         break
# print(g)
# 9.76 б
x = input('some word')
result = len(x)
cnt = result
x2 = str('e')
while True:
    cnt -= 1
    x1 = x.find('e')
    if x1 == x2:
        break
print(cnt)
# не придумал тоже