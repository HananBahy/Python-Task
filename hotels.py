import pandas as pd

##all Data
Data = pd.read_csv('7282_1.csv')

#Data with “Hotels” value in “ categories ” column
Hotels_Data = Data[Data.categories=='Hotels']   #dropna(how='any')

#data_columns
cols = Hotels_Data.columns

###Divide data into 2 dataframes  to facilite aggregatiion
df1 = Hotels_Data.loc[:,'address':'province']    #theses columns doesn't change for rows of the same hotel
df2 = Hotels_Data.loc[:,'reviews.date':'reviews.userProvince']   #these change for the same hotel

df2[['name','address']] = Hotels_Data[['name','address']]     #To use these to columns to specify unique hotel


#####there are hotels have more than branch so unique hotel has unique address and name 
   #check 
#df1 = Hotels_Data.loc[:,'address':'province']
#df1.drop_duplicates(keep='last',inplace=True)
#
#df11 = Hotels_Data.loc[:,'address':'province']
#df11.drop_duplicates(['name'],keep='last',inplace=True)
#
#df22 = Hotels_Data.loc[:,'address':'province']
#df22.drop_duplicates(['name','address'],keep='last',inplace=True)

###################################################################
     #then
df1.drop_duplicates(['name','address'],keep='last',inplace=True)

############################################
     ####aggregrate rows for the same hotels#######
df100 = df1[['name','address']].reset_index()
df100.drop('index',axis=1,inplace=True)


cols = list(df2.columns)[:-2]  #don't dupicate (name ,address) as they are added before to df100

for each in cols :
    dfm = (df2.groupby(['name','address'])[each].apply(lambda x: list(set(x)))).reset_index()
    #print('yyyyyyyyyyyyyyyyyyyyyy')
    df100[each] = dfm[each]
    
    ## binding 2 parts of dataframe after aggregation and make each hotel has one row  in both                 ##########################################
df100.drop(['name','address'],axis=1,inplace=True) 

df1.reset_index(inplace=True)
df1.drop('index',axis=1,inplace=True)  
df_final=pd.concat([df1,df100], axis=1, ignore_index=True)
names=dict(zip(range(19),list(df1.columns)+list(df100.columns)))
df_final.rename(columns=names , inplace=True)   #finally , each hotel has only row , having all its data

#############################################################

if __name__ == "__main__":
    df_final.to_pickle('hotels_without_tones.pkl')  #not in csv file to save lists as it is
    ##df_final.to_csv("hotels_without_tones.csv", index=False)
