import pandas as pd
def load_and_process(rawData1, rawData2):
        df1 = pd.read_csv(rawData1,encoding = 'latin-1')
        df2 = pd.read_csv(rawData2,encoding = 'latin-1')
        df1 = df1.drop(['rgdpe',
                        'country','currency_unit','i_cig','i_xm','i_xr',
                        'i_outlier','i_irr','ccon','cda','cgdpe',
                        'cgdpo','cn','ck','ctfp','rconna','rdana','pl_con','pl_da','pl_gdpo','cor_exp','statcap','csh_c',
                        'csh_i','csh_g','csh_x','csh_m','csh_r','pl_c','pl_i','pl_g','pl_x',
                        'pl_m','pl_n','pl_k','cwtfp','rgdpna','rnna','rkna','rtfpna','rwtfpna','labsh','irr','delta','xr'],axis=1)
        df1 = df1.rename(columns={'rgdpo': 'Output GDP (USD millions)', 'pop' : 'Population (millions)','emp' : 'Number of Employees (millions)',
                                  'avh' : 'Average annual hours worked',
                                  'hc' : 'Human capital index'})
        df2 = df2.drop(['Entity'], axis = 1)
        df2 = df2.rename(columns={'Code':'countrycode','Year' : 'year',
                                  'Days of vacation and holidays for full-time production workers in non-agricultural activities (Huberman & Minns 2007)' : 'Annual Days of Vacation'})
        cleanedData = pd.merge(df1,df2,how = 'left',on = ["countrycode", "year"])
        cleanedData_with_index = cleanedData.set_index("countrycode")
        cleanedData = cleanedData_with_index.drop(['ABW','AGO','AIA','ALB','ARE','ARG','ARM','ATG','AUT','AZE','BDI','BEN','BFA','BGD','BGR','BHR','BHS','BIH',
                                                   'BLR','BLZ','BMU','BOL','BRA','BRB','BRN','BTN','BWA', 'CAF', 'CHE', 'CHL', 'CHN', 'CIV','CMR',
                                                   'COD', 'COG', 'COL', 'COM', 'CPV', 'CRI', 'CUW', 'CYM','CYP','CZE', 'DJI', 'DMA','DOM', 'DZA', 'ECU', 'EGY',
                                                   'EST', 'ETH', 'FIN', 'FJI', 'GAB', 'GEO','GHA', 
                                                   'GIN', 'GMB', 'GNB', 'GNQ', 'GRC', 'GRD', 'GTM','GUY','HKG', 'HND', 'HRV', 'HTI',
                                                   'HUN','IDN','IND','IRN','IRQ', 'ISL', 'ISR', 'JAM', 'JOR', 'JPN', 'KAZ', 'KEN',
                                                   'KGZ', 'KHM', 'KNA', 'KOR', 'KWT', 'LAO', 'LBN', 'LBR', 'LCA','LKA',
                                                   'LSO', 'LTU', 'LUX', 'LVA', 'MAC', 'MAR', 'MDA', 'MDG',
                                                   'MDV', 'MEX', 'MKD', 'MLI', 'MLT', 'MMR', 'MNE', 'MNG', 'MOZ','MRT', 
                                                   'MSR', 'MUS', 'MWI', 'MYS', 'NAM', 'NER', 'NGA', 'NIC','NOR', 'NPL', 'NZL', 'OMN', 'PAK', 'PAN', 
                                                   'PER', 'PHL','POL', 'PRT', 'PRY', 'PSE', 'QAT', 'ROU', 'RUS', 'RWA', 'SAU','SDN', 
                                                   'SEN', 'SGP', 'SLE', 'SLV', 'SRB', 'STP', 'SUR', 'SVK','SVN', 'SWZ', 'SXM', 'SYC', 'SYR', 
                                                   'TCA', 'TCD', 'TGO','THA', 'TJK', 'TKM', 'TTO', 'TUN', 'TUR', 'TWN', 'TZA', 'UGA','UKR', 'URY', 'UZB', 'VCT', 'VEN', 
                                                   'VGB', 'VNM', 'YEM','ZAF', 'ZMB', 'ZWE',], axis = 0)
        cleanedData = cleanedData.reset_index("countrycode")
        cleanedData['Labour Productivity'] = cleanedData['Output GDP (USD millions)'] / (cleanedData['Average annual hours worked'] * cleanedData['Number of Employees (millions)'])
        return cleanedData
