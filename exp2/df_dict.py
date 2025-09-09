import pandas as pd

data = []

n=int(input("Enter the number of employees:"))
for i in range (n):
    nme=input("\nEnter the Name:")
    age=int(input("Enter the Age:"))
    dept=input("Enter the Department:")
    sal=int(input("Enter the Salary:"))

    dict={"Name":nme,"Age":age,"Dept":dept,"Salary":sal}
    data.append(dict)

df= pd.DataFrame(data)
print("\nEmployee DataFrame:\n",df)

print("First row:\n",df.iloc[0])
print("Last row:\n",df.iloc[-1])

print("Average Salary is:",df["Salary"].mean())

df["Bonus"]=df["Salary"]*0.1
print("\nEmployee DataFrame:\n",df)

df = df.drop("Dept",axis = 1)
print("\nEmployee DataFrame:\n",df)

df = df.rename(columns={"Name":"Emp_name"})
print("\nEmployee DataFrame:\n",df)
