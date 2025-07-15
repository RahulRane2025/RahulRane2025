d1={"Rahul":67,"Tanushree":98,"Bhargav":97,"Amol":87,"Vipul":77}
name=input("Enter the student's name:")
if name in d1:
    print(f"{name}'s marks:{d1[name]}")
else:
    print(f" Student {name} is not found")
