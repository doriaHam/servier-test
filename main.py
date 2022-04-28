from modules.preparation import run_preparation_pipeline
from modules.processing import run_processing_pipeline
#import lib.modules.load

if __name__ == "__main__":

    print('------------------Data preparation--------------------')

    output_datapreparation = run_preparation_pipeline()

    print('------------------Data processing---------------------')

    result = run_processing_pipeline(output_datapreparation)

    print('--------------------END--------------------------------')

    print(result)