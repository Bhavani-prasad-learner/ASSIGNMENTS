dict_data={'alice':86,'don':99,'kevin':56,'bob':100}
stname=input("enter the name of the student :")
if stname in dict_data:
    print (stname,"'s marks:",dict_data[stname])
else:
    print("student not found")