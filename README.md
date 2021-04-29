#

__Python-Fundamentals-for-Data-Science-S2-20_DSECLPFDS__
Introduction to Python for DataScience - Prof. Partha Sarathy P D

Being a Data Science course, we are using the Anaconda Framework predominantly.

* `conda info --envs` : lists all environments
* `source activate <env name>`: activate an environment
* `source deactivate`: deactivate an environment
* `conda create --name <env name> python=3 astroid babel` : create new environment, specify version of python, and install packages
* `conda env export > environment.yml` : export env dependencies
* `conda env create -f environment.yml` : Import depencendies from .yml file
* `conda env remove --name dseclpfds` : Remove a conda env
* `conda create --name dseclpfds python=3.8` : create an env with python package
* `conda install beautifulsoup4` : install individual packages
* `conda update anaconda=4.6.1` : update anaconda version
* `conda update -n myenv --all` : update all packages in current env
* `conda list` : list all packages installed
* __WINDOWS NOTE: SOURCE is not recognized.__ When deactivating and activating in the anaconda command prompt, skip `source` and just type `deactivate` or `activate` depending on what you are trying to do.
* `conda env remove -n ENV_NAME` : delete environment

__Packages covered:__

1. Numpy
2. Pandas
