import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\nagen\OneDrive\Desktop\Elevate Labs Internship\Data Analysis on CSV Files\Data.csv")
print(df.head()) #first five rows
print(df.tail()) #last five rows
print(df.info())
print(df.describe())
print(df.columns)   # calls all the columns
print(df.shape)  #returnd rows and colums count



print(df.isnull().sum())  # it returnds the missing values sum
df=df.fillna(35)        #replaces empty with value
print(df)


df['Total']=df['Social']+df['Science']+df['English']+df['Hindi']+df['Telugu']+df['Maths']  #adds new total column and add total marks
print(df)

Highest=df['Total'].sort_values(ascending=False)
print(Highest)

df.plot(kind='bar')
plt.title("Marks")
plt.xlabel("Students")
plt.show()


df.plot(kind='pie')
plt.title("Students_Marks")
plt.xlabel("Students")
plt.show()



