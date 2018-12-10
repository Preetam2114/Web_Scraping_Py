# Web_Scraping_Py :globe_with_meridians:

## Download Python3: :snake:
All my projects in Python 3, which will be replaced by it successor but most probably there shall not be much issue other than chages of syntax the same which we face with python 2.X and 3.X

## To download Python3 
Click the link [here](https://www.python.org/downloads/release/python-371/)

## Installing Jupyter notebook

1. Installing Jupyter using Anaconda and conda
    
    For new users, it's **highly recommend** [installing Anaconda](https://www.continuum.io/downloads). Anaconda conveniently installs Python, the Jupyter Notebook, and other commonly used packages for scientific computing and data science.
   Use the following installation steps:
     Download Anaconda. We recommend downloading Anaconda’s latest Python 3 version (currently Python 3.5).
     
     Install the version of Anaconda which you downloaded, following the instructions on the download page.
     
     Congratulations, you have installed Jupyter Notebook. To run the notebook run the following command in terminal:
     
    ```
     jupyter notebook
    ```
 2. Alternative for experienced Python users: Installing Jupyter with pip
     
     As an existing Python user, you may wish to install Jupyter using Python’s package manager, pip, instead of Anaconda.
    First, ensure that you have the latest pip; older versions may have trouble with some dependencies:
    ```
    pip3 install --upgrade pip
    ```
    Then install the Jupyter Notebook using:
    ```
    pip3 install jupyter
    ```
## Installing Scrapy
Scrapy offers the tool for [download](https://scrapy.org/download/) from its website, as well as instructions for installing Scrapy with third-party installation managers such as pip.

> Because of its relatively large size and complexity, Scrapy is not usually a framework that can be installed in the traditional way with

    pip install Scrapy

>If you’re determined to install Scrapy from pip, using a virtual environment run the following set of codes
    
    $ virtualenv scrapingEnv
    
>This creates a new environment called scrapingEnv, which you must activate to use:
    
    $ cd scrapingEnv/
    $ source bin/activate
    
>This activates the newly created venv all the necessary libraries can be installed here with all the dependencies
including BeautifulSoup

The most highly recommended method is through Anaconda package manager the installation of anaconda is already stated above
After Anaconda is installed, you can install Scrapy by using this command:

    ```
    conda install -c conda-forge scrapy
    ```
