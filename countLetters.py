 nn=0
 na=0
 str=input("Enter the input string:")
 for i in str:
  if i.isalpha()==True:
      na=na+1
  if i.isdigit()==True:
      nn=nn+1
 print("The no of alphabets in given string is ")
 print(na)
 print("The no of numbers in given string is ")
 print(nn)
 print("The no of alphanumerics in given string is ")
 print(na+nn)
