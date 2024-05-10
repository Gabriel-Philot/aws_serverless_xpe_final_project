# STEP BY STEP DEV GUIDE [API / Databases]

> [!Note]
> Goal here its to dev a framework that have some basic feacutres of good sofware developements pratices

Do the steps below for making the use of the same modules and methods already defined, to gain speed
and making the use of testing and logging your aplication.


## Workspace configuration

* (1) Create the new dir, and copy the dev_model.files files, in to the new dir dev folder.


    * path example - > `mkdir root_project_repo/path_{resource}/path_{application}/dev`

* (2) If the project its to improve other resource, bring the raw code for the dev folder (for documentation). Then if the project its about a new ETL prococess, just use the notebook or script model.

* (3) Change the variables in config_model.py

* (4) Do your job!

## TESTING/DEPLOY for test ENV

After your good runs on local tests , its time to test it in the aws -> dev lighthouse enviroment

* (6) Preparing for Zip

    * Create new dir path example - > `mkdir root_project_repo/path_{resource}/path_{application}/deploy_test`

    * Copy `lambda_function_model.py` from `root_project_repo/path_lambda/resources` & remove the _model of the name.

        * Make the changes into it 

    * Coppy other */resources/* modules into the dir.
        * Dont forget to change config_model.py to config.py and use de _dev values
        * pay atention to the `import config` in the lambda_function.py

* (7) Zip command "terminal method"

    * First cd into the {prod_dir}

> *windows*

`
Compress-Archive -Path prod -DestinationPath lambda.zip

`
for exemple here:

Compress-Archive -Path "C:\Users\martigx68\projects\path\deploy_test\\*" -DestinationPath "C:\Users\martigx68\projects\path\lambda.zip"


> *linux

`
with cd go to resources external_libs creat or update the zip

    * creating 
    pip install requests -t {dir} (new 3party modules)
    zip -r lambda_base.zip .
    then this file u will add the custom modules in the lambda deploy dir.
    with the following command.
    zip -g ghactivity-downloader.zip lambda_function.py download.py .....
    then add new custom modules ass weell.

`


* (8) Upload via Scrpit or manually (`root_project_repo/resources`) into AWS

* (9) Quick check in the AWS console if the files are the same and test it.

* (10) Validate if the files of the ingestion wil be working.