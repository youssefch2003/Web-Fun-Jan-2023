#1
# def Count(x):
#     arr=[]
#     for i in range(x,0,-1):
#         arr.append(i)
#     return arr 
# print(Count(5))

#2
# def calcul(x):
#     print(x[0])
#     return x[1]
# a=calcul([1,2])
# print(a)

#3
# def first_plus_length(k):
#         s = k[0] + len(k)
#         return s

# a = first_plus_length([1,2,3])

# print(a)

#4
# def values_greater_than_second(c):
#     m = []
#     i=0
#     while i<len(c) :
#         if len(c)<2:
#             return False
#         elif(c[2]<c[i]):
#             m.append(i)
#     i=i+1
#     print(len(m))
#     print(m)
#     return len(m) +  m


# a =values_greater_than_second([1,2,3,4,5]) 
# print(a)

#5
def createarray(val,size):
    arr=[]
    len(arr)==size
    for i in range(0,size+1):
        arr[i]==val
    return arr
a = createarray(7,4)
print(a)

