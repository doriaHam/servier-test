import pandas as pd
from config import DATASETS_MENTION, DATA_REPOSITORY, DATASETS_DESCRIPTION, DATASETS, TITLE_COLUMN
from  unidecode import unidecode
import os

def load_file(file):
    """
    load data 
    """
    if os.path.exists(DATA_REPOSITORY+'/'+file+'.csv'):
        try :
            datafram = pd.read_csv(DATA_REPOSITORY+'/'+file+'.csv', names=DATASETS_DESCRIPTION[file].keys(), header=0)
            return datafram
        except :
            print('the file is not in the correct format !')
    else :
        print('the file does not exist !')

def run_preparation_pipeline() :

    for file_name in DATASETS:
        df = load_file(file_name)
        df = clean_all(df, file_name)
        output_repository = 'data/output_cleaned'
        df.to_csv(output_repository+'/'+file_name+'.csv', index=False)
    return output_repository

def _clean_string_column(df, column_name):
    """
    df : Datafram
    column_name : string
    => Datafram
    """
    df[column_name] = df[column_name].str.strip().str.lower()
    df[column_name] = df[column_name].apply(lambda x : unidecode(str(x)))
    return df[column_name]


def _convert_column_type(df, column_name, column_type):
    """
    df : dataframe
    column_name, column_type : string
    """
    if  column_type == 'date': 
        df[column_name] = pd.to_datetime(df[column_name])
    else:
        df[column_name] = df[column_name].astype(column_type)

    return df[column_name]

def clean_all(df, df_name):
    """
    df : dataframe
    df_name : string
    """
    for column_name, column_type in DATASETS_DESCRIPTION[df_name].items():
        df[column_name] = _convert_column_type(df, column_name, column_type)
        if column_type == 'string':
            df[column_name] = _clean_string_column(df,column_name)
    # clean mention datasets
    if (df_name in DATASETS_MENTION):
        df[TITLE_COLUMN] = df[TITLE_COLUMN].replace('', pd.NA)
        df.dropna(subset=[TITLE_COLUMN], inplace=True)

    return df