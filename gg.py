#type fliping difrent typs like int,str,float cant be combind if u dont translate it 
age = 16 #int
his_age = 15.5 #float
your_age = "17" #str

print(float(age))
print(str(his_age))
print(int(your_age))

print(type(age))
print(type(his_age))
print(type(your_age))

age = float(age)
his_age = str(his_age)
your_age = int(your_age)

print(type(age))
print(type(his_age))
print(type(your_age))
