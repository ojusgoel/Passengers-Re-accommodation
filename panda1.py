import pandas as pd
import matplotlib.pyplot as plt


df= pd.read_csv('SCH-ZZ-20231208_035117.csv')
#print(df)

#df.info()
#print(df.describe())

#df[['RECLOC', 'FIRST_NAME', 'LAST_NAME']] 

#print(df['RECLOC'])

#print(df.loc[(df['Sunday']>0) & (df['Monday']>0), "FlightNumber"])


#df.plot.scatter(x="FlightNumber", y="Frequency")
#plt.show()

#print(df.tail(10))

#print(df[["FlightNumber", "Frequency", "AircraftType"]])


#print((df[["FlightNumber", "Frequency", "AircraftType"]]).groupby("AircraftType"))

print(df.sort_values(by="Frequency", ascending=False).head())
