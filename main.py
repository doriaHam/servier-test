from modules.preparation import run_preparation_pipeline
from modules.processing import run_processing_pipeline
from config import DATASET_DRUGS, DATASETS_MENTION, DATASETS, DATASETS_DESCRIPTION, DATA_REPOSITORY_OUTPUT
#import lib.modules.load

if __name__ == "__main__":

    print('------------------Data preparation--------------------')

    output_datapreparation = run_preparation_pipeline()

    print('------------------Data processing---------------------')

    result = run_processing_pipeline(output_datapreparation)

    print('--------------------END--------------------------------')

    print(result)