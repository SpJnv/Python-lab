# import pandas
import pandas as pd

# read the data from csv file
data = pd.read_csv(r"C:\Users\shiva\Downloads\salesdata.csv")

# create dataframe
df = pd.DataFrame(data)

# print first 5 row of file
print(df.head())

# create and print the pivot table
print("\n",pd.pivot_table(df, index=["Item"],values=["Units"],aggfunc="sum", margins=True))


# Output
"""
    Region  Manager   SalesMan          Item  Units  Unit_price  Sale_amt
0     East   Martha  Alexander    Television     95      1198.0  113810.0
1  Central  Hermann     Shelli  Home Theater     50       500.0   25000.0
2  Central  Hermann       Luis    Television     36      1198.0   43128.0
3  Central  Timothy      David    Cell Phone     27       225.0    6075.0
4     West  Timothy    Stephen    Television     56      1198.0   67088.0

               Units
Item               
Cell Phone      278
Desk             10
Home Theater    722
Television      716
Video Games     395
All            2121
"""
