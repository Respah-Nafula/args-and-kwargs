
# add three nums
def numbers(d,e,f):
    print(d+e+f)
numbers(500,300,400)

# *args(non keyword arguments)
# **kwargs(keyword arguments)

def numbers(*num):
    sum=0
    for i in num:
        sum = sum + i
        print("sum:",sum)
numbers(3,7)
numbers(4,5,8,9)
numbers(7,9,6,5)

def intro(**introduction):
    print("\nData type of argument:",type(introduction))
    for key, value in introduction.items():
        print("{} is {}".format(key,value))
intro(Firstname="Respah",lastname="Love",age=25,phonenumber="0745645342",email="nafres@gmail.com",country="Rwanda")

intro(Firstname="Nafula",Lastnamename="Love",age=28,phonenumber="0757764538",email="naflah@compulynx@gmail.com",country="Kenya")



        
