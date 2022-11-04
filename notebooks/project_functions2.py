import pandas as pd

def load_and_process(rawFile1, rawFile2):
    df1 = pd.read_csv(rawFile1,encoding='cp1251')
    df2 = pd.read_csv(rawFile2,encoding='cp1251')
    df_clean = pd.merge(df1[['countrycode', 'country', 'currency_unit', 'year', 'rgdpe',
       'pop', 'emp', 'avh', 'hc',  'cn', 'ctfp']], df2.rename(columns={"Code":"countrycode"
       , "Days of vacation and holidays for full-time production workers in non-agricultural activities (Huberman & Minns 2007)":"vac"
       , "Year":"year"}),how='left', on=["countrycode", "year"]).fillna(method='ffill')
    df_clean = df_clean[df_clean["country"] == df_clean["Entity"]].drop(["Entity"], axis=1)
    df_clean['prod'] = 2*df_clean['rgdpe']/(df_clean['avh'] * df_clean['emp'])
    return df_clean