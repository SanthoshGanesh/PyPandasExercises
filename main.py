import pandas as pd
import re
df= pd.read_csv('pokemon_data.csv')
# print(df.head(2))
#print(df.tail(4))
# print(df[['Name','Type 1','HP']])
# print(df.iloc[4])
# for index,row in df.iterrows():
#     print(index,row)

# print(df.loc[df['Type 1']=='Fire'])
# print(df.describe())
# print(df.sort_values('Name',ascending=False))
# print(df.sort_values(['Name','Type 1'],ascending=[False,True]))

# print(df.columns)

# df['Total']=df['HP']+df['Attack']+df['Defense']+df['Sp. Atk']+df['Sp. Def']+df['Speed']
# print(df.head(2))
#  print(df.sort_values('Total'))
# print(df.columns)
# df=df.drop(columns='Total')
# print(df.columns)
#df['Total']=df.iloc[:,4:10].sum(axis=1)
# print(df.head(4))
df['Total']=df.iloc[:,4:10].sum(axis=1)
cols=list(df.columns)
df= df[cols[0:4]+ [cols[-1]]+ cols[4:12]]
 # print(df.head(4))
# print(df.columns)
# df.to_csv('modified_pokemon_data.csv',index=False)
# df.to_excel('modified_pokemon_data.xlsx',index=False)
# df.to_csv('modified_pokemon_data.txt',index=False,sep='\t')

# print(df.columns)



# print(df.loc[(df['Type 1']=='Grass') & (df['Type 2']=='Poison') & (df['HP']>70)])
# new_df= df.loc[(df['Type 1']=='Grass') & (df['Type 2']=='Poison') & (df['HP']>70)]
# new_df.reset_index(drop=1,inplace= True) --> //inplace will help in saving memory by assigning the value to same variable instead of creating a new one
# print(new_df)

# print(df.loc[df['Name'].str.contains('Mega')])
# ~ --> equivalent to !

# re_df=df.loc[df['Type 1'].str.contains('fire|grasS', flags=re.I ,regex=True)]
# print(re_df)

# ee_df=df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I ,regex=True)]
# print(ee_df)

# df.loc[df['Type 1']=='Fire', 'Type 1']='Fire'
# print(df.head(5))

# df.loc[df['Type 1']=='Fire', 'Legendary']=True

# df.loc[df['Total']>400,['Generation','Legendary']]=['T1','T2']

# df.groupby(['Type 1']).mean()
# df.groupby(['Type 1']).mean().sort_values('Defense',ascending=False)
# df.groupby(['Type 1']).count()

# for df in pd.read_csv('pokemon_data.csv',chunksize=5):
#     print("CHUNK")
#     print(df)

# new_df=pd.DataFrame(columns=df.columns)
# for df in pd.read_csv('pokemon_data.csv',chunksize=5):
#     results=df.groupBy(['Type 1']).count()
#
#     new_pdf=pd.concat([new_df,results])
