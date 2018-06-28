def blackJack(num1, num2)
    if (int(num1) >21):
        num1 = 0
    if (int(num2) >21):
        num2 = 0
    if(int(num1) > int(num2)):
        return num1
    else:
        return num2