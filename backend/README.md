# Improvement Logs
* 2024-01-26: use Edge inprivate mode, reorganze the folder structure
* 2021-04-20: added standalone Chrome browser
* 2019-12-06: For some components with non-editable start date, skip  inputting start date. Continue to parse in other input areas. Don't log  into error logs.

# Install the program

1. Install [Miniconda (Python)](https://docs.conda.io/en/latest/miniconda.html)  on your local machine. You can access conda via the console, to make sure it's properly installed please run `conda -V` to display the version, and run `python -V` to display the version.

2. Create new virtual environment. Open Anaconda Prompt and run (taken an example of python 3.10):

    ```conda create --name selenium_env python==3.12 –y```

3.  Once it's created you can activate it by running: ```conda activate selenium_env```

4. Go to the current directory, run ```pip install -r requirements.txt``` under the activated virtual environment

5. Setup environment variables for Windows System. Typical path is :C:\Users\user_ID\AppData\Local\Continuum\miniconda3\envs\selenium_env

6. To show hidden files in Windows OS:

![show hidden files](images/screenshots2.PNG)

7. The current design is to download the latest ***Edge Webdriver*** automatically when running the program, no need to manually download the webdriver.

# To Run the program

1. Fill in template.xlsx with validated data, double check, and save.

2. Fill in the AiM login username and password in the command line window, note that the password won't be shown on the screen. Click enter and the program will continue.

   ![CMD login screenshots](images/screenshots1.PNG)
3. template excel file should always starts with "template" and ends with "xlsx", e.g. template339.xlsx
4. template excel file should be saved in "input" file, and will be moved to "archived" folder once processed.
5. Input folder should only have 1 excel file

 

# Important Notes for Users

1. Please do not change any file names.
2. Please do not change the layout of excel templates, i.e. adding columns, deleting columns, changing column names, etc.
3. Please make sure the input value is valid.
4. Always check the error logs.txt after the program finishes. The program should continue running while logging the error.
5. If there are any questions or improvement suggestions, feel free to contact IIM team.