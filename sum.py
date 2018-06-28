def UniqueSum(int1,int2,int3):
    if (int1 == int2 and int1 == int3):
        int1, int2 ,int3 = 0,0,0
    if (int1 == int2):
        int1, int2 = 0, 0
    if (int1 == int3):
        int1, int3 = 0, 0
    if (int2 ==int3):
        int2, int3 = 0, 0
    return (int1+int2+int3)

print (UniqueSum(5,5,6))

print (UniqueSum(5,5,5))

print (UniqueSum(5,6,6))

print (UniqueSum(1,2,3))


print (UniqueSum(10,5,10))