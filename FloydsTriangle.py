n = int(input("Enter the number of rows:"))
p = 1
print("Floyd's Triangle")
for i in range(n):
  for j in range(i+1):
    print(p,end = ' ')
    p+=1
  print()
