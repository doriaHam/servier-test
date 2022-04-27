

DATA_REPOSITORY = 'data'
DATA_REPOSITORY_OUTPUT = 'data/output'
DATASETS = ['clinical_trials', 'drugs', 'pubmed']

DATASETS_DESCRIPTION = {'clinical_trials' : {'id':'string', 'title':'string', 'date':'date', 'journal':'string'},
                        'pubmed' : {'id':'string', 'title':'string', 'date':'date', 'journal':'string'},
                        'drugs' : {'atccode':'string', 'drug':'string'}
                    }               
DATASETS_MENTION = ['clinical_trials', 'pubmed']
DATASET_DRUGS = 'drugs'
TITLE_COLUMN = 'title'
