# a=20
# b=20
# c=0
# while a/2!=1:
#     a=a/2
#     b += a
#     if a%2 ==1:
#         a-=1
#         c+=1
#     if a/2 == 1:
#         c+=1
# print(b+c)






def qishui(a):
    c=0
    b=a
    while a/2!=1:
        a=a/2
        b += a
        if a%2 ==1:
            a-=1
            c+=1
        if a/2 == 1:
            c+=1
    print(b+c)
    return (b+c)
print(qishui(32))
