import pandas as pd
import numpy as np
data = {"Date": ["2024-01-05", "2024-01-07", "2024-01-10", "2024-01-15", "2024-02-01", "2024-02-08", "2024-02-12",
                 "2024-02-20"],
        "Type": ["Income", "Expense", "Expense", "Income", "Income", "Expense", "Expense", "Expense"],
        "Category": ["Salary", "Groceries", "Utilities", "Freelance", "Salary", "Rent", "Entertainment", "Groceries"],
        "Amount": [4000, -150, -90, 500, 4000, -1200, -200, -160]}
df = pd.DataFrame(data)
rez = df[df["Type"] == "Expense"]
#print(rez)

suma=df[df["Type"] == "Income"]["Amount"].sum()
print(suma)

sumae=df[df["Type"] == "Expense"]["Amount"].sum()
print(sumae)

df["balance"]=df["Amount"].cumsum()
print(df["balance"])

grcat=df["Category"].groupby(df["Amount"]).sum()
print(grcat)

grtype=df.groupby('Type')["Amount"].mean()

print(grtype)

desc=df.groupby('Type')["Amount"].sum().reset_index().sort_values("Amount",ascending=False)["Type"]

print(desc)


df1=df[abs(df["Amount"])>300]
print(df1)

df.index = pd.to_datetime(df["Date"])

# Group by year and month
grouped = df.groupby([df.index.year, df.index.month])

# Example: sum Amount by year-month
chelllun= grouped["Amount"].sum()
print(chelllun)


df["coloana"]=abs(df["Amount"])
sorta=df.sort_values("coloana")


print(sorta)


#procent=df[df.groupby("Type")=="Expense"(df["Amount"]*100)/sumae
procent=df[df["Type"]=="Expense"].groupby("Category").sum()
total=procent["Amount"].sum()
result=(procent["Amount"]/total)*100
print(result)