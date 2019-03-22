# Thales-Bert

## Setup

### Virtual Environment

You must first setup a **Python 3.6** virtualenv.
1. Install virtual environments: `pip install virtualenv`.
1. Create the "env" virtual environment in the root of the project: `virtualenv env -p python3`.
1. You may now activate it as needed, and configure the new virtualenv in your IDE: `source env/bin/activate`.
1. Install requirements: `pip install -r requirements.txt.`

### Set up pre-commit hooks
1. Modify your local git configuration to point the correct emplacement of the project hooks
    > Run the following command in the terminal at the project root: 
            
    `git config core.hookspath .githooks`
1. Everytime you create a new commit, you shall see the output of yapf execution which reformats all source files properly. 

### Fine-tuning BERT on the SQuAD dataset in the cloud on a TPU

See the steps 1 and 2 in the cloud directory's [README.md](cloud_scripts/README.md).

You may skip this step if a member of your team already did this step, as it is compute-intensive and costly.

### Download the fine-tuned BERT's weights for local CPU usage of the model

See the steps 3, 4 and 5 in the cloud directory's [README.md](cloud_scripts/README.md). Basically, you need to download the trained BERT model and place it at some place under the `./thales-bert-gcp-bucket` directory here.

### Run tests

Once install, verify your installation by running tests within the virtualenv using the command `./run_tests.sh` when placed in the root of the project.

### Enjoy

You can now run the main, such as by doing `python main.py`, to use the Question-Answering chatbot.
