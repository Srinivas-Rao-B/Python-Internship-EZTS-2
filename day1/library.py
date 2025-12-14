book=input("Enter the book name:")
book_quant=int(input("Enter total number quantities of book:"))
borrow_quant=int(input("Enter how many books user need:"))
if borrow_quant>book_quant:
    print("No sufficient books are there")
    exit()
day=int(input("Enter the submission date:"))
if day==0:
    print("No fine")
if 1<=day<=5:
    print("Fine is 50")
if 6<=day<=10:
    print("Fine is 100")
if 11<=day<=13:
    print("Fine is 150")
if day>13:
    print("Terminate student ID")
print("The remaining books are",book_quant-borrow_quant)