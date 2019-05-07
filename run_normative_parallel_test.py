"""
    This function is a motherfunction that executes all parallel normative
    modelling routines. Different specifications are possible using the sub-
    functions.
    ** Input:
        * processing_dir     -> Full path to the processing directory. 
                                This will be the directory which you have   
                                cloned from Rindkind/test_normative_modeling.
        * python_path        -> Full path to the python distribution
        * normative_path     -> Full path to the normative.py
        * job_name           -> Name for the bash script that is the output of
                                this function
        * covfile_path       -> Full path to a .txt file that contains all
                                covariats (subjects x covariates) for the
                                responsefile
        * respfile_path      -> Full path to a .txt that contains all features
                                (subjects x features)
        * batch_size         -> Number of features in each batch
        * memory             -> Memory requirements written as string
                                for example 4gb or 500mb
        * duation            -> The approximate duration of the job, a string
                                with HH:MM:SS for example 01:01:01
        * cv_folds           -> Number of cross validations
        * testcovfile_path   -> Full path to a .txt file that contains all
                                covariats (subjects x covariates) for the
                                testresponse file
        * testrespfile_path  -> Full path to a .txt file that contains all
                                test features
        * log_path           -> Pathfor saving log files
        * binary             -> If True uses binary format for response file
                                otherwise it is text
"""


# run normative parallel - set up the scripts to call the test files-
# setup

import nispat

processing_dir=     '/home/mrstats/triloo/normmod_workspace/test_normative_modeling'
python_path=        '/home/mrstats/triloo//software/anaconda3/bin/python'
normative_path=     '~/software/anaconda3/envs/norm_mod/lib/python3.7site-packages/nips at-0.12-py3.7.egg/nispat/normative.py'
job_name=           'normmod_test_script'
covfile_path=       processing_dir+'/covariates_HC.txt'
respfile_path=      processing_dir+'/features_HC.txt'
testcovfile_path=   processing_dir+'/covariates_allpatients.txt'
testrespfile_path=  processing_dir+'/features_allpatients.txt'
batch_size=         50 
memory=             '4gb'
duration=           '03:00:00'



# run normative modeling test script

nispat.normative_parallel.execute_nm(processing_dir, 
                                     python_path, 
                                     normative_path, 
                                     job_name, 
                                     covfile_path, 
                                     respfile_path, 
                                     batch_size, 
                                     memory, 
                                     duration,
                                     testcovfile_path = testcovfile_path,
                                     testrespfile_path = testrespfile_path
                                     )







