# import pandas as pd
import pandas as pd

# reading the data from file
data = pd.read_csv(r"C:\Users\shiva\Downloads\salesdata.csv")

# creating the dataframe of the file
df = pd.DataFrame(data)

# printing first 5 row of the file
print(df.head())

# creating and printing the pivot table
print("\n",pd.pivot_table(df, index=["Region", "Manager", "SalesMan"], values=["Sale_amt"], aggfunc="sum"))


# Output
"""
    Region  Manager   SalesMan          Item  Units  Unit_price  Sale_amt
0     East   Martha  Alexander    Television     95      1198.0  113810.0
1  Central  Hermann     Shelli  Home Theater     50       500.0   25000.0
2  Central  Hermann       Luis    Television     36      1198.0   43128.0
3  Central  Timothy      David    Cell Phone     27       225.0    6075.0
4     West  Timothy    Stephen    Television     56      1198.0   67088.0

                            Sale_amt
Region  Manager SalesMan           
Central Douglas John       124016.0
        Hermann Luis       206373.0
                Shelli      33698.0
                Sigal      125037.5
        Marth   Steven      14000.0
        Martha  Steven     185690.0
        Timothy David      140955.0
East    Douglas Karen       48204.0
        Martha  Alexander  236703.0
                Diana       36100.0
West    Douglas Michael     66836.0
        Timothy Stephen     88063.0
"""
