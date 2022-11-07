import pandas as pd
def clean_and_secure(pwt, vac):
    '''
    This method is specific for the penn world table csv and the vacation days csv. It takes the address of both as input with the order being specific.
    '''
    df_pwt = pd.read_csv(pwt, encoding='cp1251') #Penn-world table data
    df_vac = pd.read_csv(vac) #Vacation days data
    df_data = df_pwt[['country', 'year', 'pop', 'rgdpe', 'avh']].dropna()
    df = (
        pd.merge(df_data[df_data['country'].isin(['Australia', 'Belgium', 'Canada', 'Denmark', 'France',
                                                  'Germany', 'Ireland', 'Italy', 'Netherlands', 'Spain','Sweden', 'Switzerland',
                                                  'United Kingdom', 'United States'])], 
                 df_vac.rename(columns = {'Year': 'year', 'Entity': 'country'}), 
                 how='left', 
                 on = ['country', 'year'])
        .fillna(method='ffill')
        .dropna()
        .rename(columns={'Days of vacation and holidays for full-time production workers in non-agricultural activities (Huberman & Minns 2007)': 'vacation days'})
    )
    
    df['gdp per capita'] = df['rgdpe']/df['pop']
    df['productivity'] = df['gdp per capita']/df['avh']
    df['gdp per vac days'] = df['rgdpe']/ df['vacation days']
    df = df[['country', 'year', 'pop', 'avh', 'rgdpe', 'gdp per capita', 'vacation days', 'productivity', 'gdp per vac days']]

    return df

def makeHeatMap(data):
    df_mx = data.corr()
    ht = sns.heatmap(df_mx, annot = True, cmap = 'flare')
    
def getyear(data, start_year):
    new = data[data['Year'] > start_year]
    return new

def getcountry(data, country):
    new = data[data['Entity'] == country] 
    return new