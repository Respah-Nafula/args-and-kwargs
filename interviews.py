# def star(s):
#     for x in range (s):
#         print( ' '*(s-x-1)+ ' *'*(2*x+1))
# star(10)

# a=input('enter a sequence : ')
# b=a[::-1]
# if a==b:
#     print('palindrome')
# else:
#     print("not a palindrome")


#     # def main():
#     #     x,y=100,20
#     #     if x==y:
           
#     #       print(X is greater thany)


from statistics import median


list=[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 10, 20, 68, 8, 40, 45, 1, 5, 53, 45, 17]
print(list)
final=[]
for num in list:
 if num not in final:
    final.append(num)
    print(list)

   #  program to obtain the median of a list of numbers
num=[1,2,3,4,5,6,7]
n=len(num)
if n%2==0:
   i=int(n/2-1)
   j=int(n/2)
   median=(num[i]+num[j])/2
else:
   i=int(n/2)
median=num[i]
print(median)
      