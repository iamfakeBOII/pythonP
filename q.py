sal = int(input("salary: "))
nsal = 0
if(sal > 0 and sal <= 10000):
    nsal = sal + 0.2*sal + 0.8*sal
elif(sal <= 20000):
    nsal = sal + 0.25*sal + 0.9*sal
elif(sal > 20000):
    nsal = sal + 0.3*sal + 0.95*sal
else:
    print("error")
print("gross: ", nsal)
