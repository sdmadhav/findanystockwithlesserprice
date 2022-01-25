import pandas as pd
import pandas_datareader as web

df=pd.read_csv('validcode.csv') //validcode.csv contains list of Security Code of NSE companies find it in folder

df.drop('Unnamed: 0',axis=1,inplace=True)

ls=df['0']

for i in range(len(ls)):
    ls[i]=ls[i]+'.NS'
    print(ls[i])


for i in range(500,len(ls)):
    print(i)
    df=web.DataReader(ls[i],data_source="yahoo",start='2021-01-01',end='2022-01-25')
    des=df.describe()
    mini=des['Low'].min()
    latest=df['Open'][-1]
    if(mini>latest):
        print('Buy')
        print(ls[i])
    else:
        pass
