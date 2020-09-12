# Get the covariates and construct the dataset

def get_dataset():
    
# Covariate 1: Functioning of Government (FOG) index by Freedom House

    FOG = pd.read_excel('FOG index 2003-2018.xlsx',sheet_name="FIW2010") 
    FOG = FOG.iloc[:, : 10].drop(columns=["Country/Territory",'Status','PR Rating','CL Rating','A Aggr', 'B Aggr'], axis=1)
    FOG =FOG.rename(columns={"C Aggr":"FOG"}) 

# Covariate 2: Corruption
    corruption=pd.read_excel("World Governance Indicators, control of corruption 2018.xlsx", sheet_name="COC")
    df =FOG.merge(corruption, on="Country", how="left")

# Covariate 3: Regularoty Quality
    regqual=pd.read_excel("World Governance Indicators, control of corruption 2018.xlsx", sheet_name="REG")

    df=df.merge(regqual,on="Country", how="left")

# Covariate 4: Government Effectiveness
    gov_eff=pd.read_excel("World Governance Indicators, control of corruption 2018.xlsx", sheet_name="GOV")

    df=df.merge(gov_eff,on="Country", how="left")

# Covariate 5: Polity IV from Teytelbom
    polityIV = pd.read_excel("polityIV.xls", sheet_name="2010")
    df = df.merge(polityIV, on="Country", how='left')

# Covariate 6: EU dummy 
    EU = pd.read_excel("EU.xlsx")
    df = df.merge(EU,left_on="Country", right_on="country", how="left")
    df.EU = df.EU.fillna(0)
    df.EU = df.EU.astype(int)
    df = df.drop("country",axis=1)


# Covarite 7: Gallup on Environmental Awareness  
    
    gallup = pd.read_excel('Gallup on Environmental Awareness 2010.xlsx') 
    gallup = gallup.rename(columns={2010:"Gallup"})
    gallup = gallup.drop(2008,axis=1)
    gallup['country'] = gallup['country'].replace(["Slovakia", "Kyrgyzstan"] , ["Slovak Republic", "Kyrgyz Republic"])
    df = df.merge(gallup, left_on= "Country", right_on= "country", how="left" )
     

# France, Switzerland and Norway etc. is missing in Gallup 2010 dataset.

# Imputing  manually from 2007 / 2008

    df.loc[[2,5,21,87,89,65,39,34,86]] ["Gallup"] =  [93, 97,95,49,54,30,88,91,22] 
    df = df.drop("country", axis=1)

# Covarite 8: Social Trust % in others from World values survey
    trust = pd.read_excel("self trust.xls") 
    df = df.merge(trust, on="Country", how='left')

# Covarite 9: vulnerability index from David Wheeler
    vul = pd.read_excel("vulnerability.xls", sheet_name="Sheet1")
    df= df.merge(vul, on="Country", how="left")

# Covarite 10: GDP in billion dollars from the World Bank
    GDP = pd.read_excel("GDP.xlsx")
    df= df.merge(GDP,left_on="Country", right_on= "country" , how='left')

# Covarite 11: GDP per capita
    GDP_pc = pd.read_excel("GDPpercap.xls", sheet_name="2010")
    df= df.merge(GDP_pc, on="Country", how="left")


# Covarite 12/ 13: Renewables as total cons. and electricity output # 2000 or 2015 Worldbank 
    renewable = pd.read_excel('Renewables.xlsx', sheet_name="Sheet2")
    df=df.merge(renewable,on="Country", how="left")

# Covarite 14: gas and oil rents % GDP # Minx and Lamb # kendim gas ve oil icin topladim Worldbank
    gas_oil_rent = pd.read_excel("gas and oil rents.xls", sheet_name="2010")
    df = df.merge(gas_oil_rent, on="Country", how='left')
    df = df.drop(["gas","oil"],axis=1)

#  Covarite 15: coal rents % GDP 
    coal_rent = pd.read_excel("coal.xls", sheet_name="2010")
    df = df.merge(coal_rent, on="Country", how='left')

# Covarite 16: coal in % electricity production
    coal_elec = pd.read_excel("elect from coal.xls", sheet_name="2010")
    df = df.merge(coal_elec, on="Country", how='left')

# Covarite 17: Fossil % GDP
    fossil = pd.read_excel('fossilGDP.xlsx')
    fossil =fossil.rename(columns={2010:'fossil_GDP'})
    df = df.merge(fossil, on="Country", how='left')

    df = df.drop("country", axis=1)
    df.drop(["Add A", "Year"], axis=1, inplace=True)
    return df
