import pandas as pd
import numpy as np

def describeData(df):
    REPORT_NULL = ({
                    'PREDICTORS' : df.shape[1],
                    'SAMPLES': df.shape[0],
                    'FEATURES_NaN' : [feature for feature in df.columns if df[feature].isnull().sum() >= 1],
                    'FEATURES_NUMERICAL' : [feature for feature in df.columns if df[feature].dtypes != 'object'],
                    'FEATURES_CATEGORICAL' : [feature for feature in df.columns if df[feature].dtypes == 'object'],
                    'FEATURES_DISCRETE' : [feature for feature in df.columns if len(df[feature].unique()) <=25],
                    'FEATURES_CONTINOUS' : [feature for feature in df.columns if len(df[feature].unique()) > 25],
                    
                    'REPORT_NULL' : pd.DataFrame({
                                                'NULL_VALUES' : df.isnull().sum(),
                                                'PERCENT_NULL': np.round( df.isnull().mean(), 2 ),
                                                 })
                    
                    
                  })
    return REPORT_NULL

# Look rest of Dataframe with Null values in particular columns
df_energy.loc[(df_energy["eleclink_flow"].isna()) | (df_energy["nsl_flow"].isna()), :]