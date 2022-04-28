import pandas as pd
from config import DATASETS_MENTION, TITLE_COLUMN, DATASET_DRUGS,DATA_REPOSITORY_OUTPUT
import json


def run_processing_pipeline(output_repository):

    dfs_mentions = {}
    for mention in DATASETS_MENTION : 
        print (mention)
        dfs_mentions[mention] = pd.read_csv(output_repository+'/'+mention+'.csv', encoding='iso-8859-1')

    df_drugs = pd.read_csv(output_repository+'/'+DATASET_DRUGS+'.csv')
    result = get_articles_mentioned_drugs(dfs_mentions, df_drugs)
    return genrate_json_file(result)

def _get_articles_mentioned_drug(df, drug):
    """
    df : dataframe
    drug : raw
    """
    result = df[df[TITLE_COLUMN].str.contains(drug["drug"])]
    result["drug"] = drug["drug"]
    result["atccode"] = drug["atccode"]
    return result

def _get_articles_mentioned_drugs_type(df_article, df_drugs, type) : 
    """
    df_article, df_drugs : dataframe
    type : string
    """
    result = pd.DataFrame()
    print(type)
    for i, raw in df_drugs.iterrows():
        r=_get_articles_mentioned_drug(df_article, raw)
        result = pd.concat([result,r], ignore_index=True)
    result["type"] = type
    return result

def get_articles_mentioned_drugs (dfs_articles, df_drugs) : 
    """
    param : 
        dfs_articles : dict {type : dataframe}
        df_drugs : dataframe
    return : DataFrame
    """

    result=pd.DataFrame()
    for source, df in dfs_articles.items() : 
        df_type = _get_articles_mentioned_drugs_type(df, df_drugs, source)
        result = pd.concat([result,df_type])
    return result

def genrate_json_file(dataframe):
    """
    save dataframe  into json with foramt : {}
    """
    dataframe["index"] = dataframe.atccode.astype('str') +'-'+ (dataframe.id.astype('str'))
    dataframe.drop(["atccode", "id"], axis=1, inplace=True)
    dataframe.set_index('index', inplace=True)
    result = dataframe.to_dict(orient='index')
    
    with open(DATA_REPOSITORY_OUTPUT+"/reslut.json", "w") as file:
        json.dump(result, file)
    return result, DATA_REPOSITORY_OUTPUT
