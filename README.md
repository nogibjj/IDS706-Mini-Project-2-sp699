![Python N Pandas CI](https://github.com/nogibjj/Suim-Park-Mini-Project-2/actions/workflows/cicd.yml/badge.svg)
# IDS-706-Data-Engineering :computer:

### Mini Project 2</br>
Mini project 2 repository contains Dockerfile, Github Actions, Makefile, README.md, requirements.txt, main.py and test_main.py.

The files included in the second mini project are as follows:

* `Makefile`: Installed the packages listed in the requirements.txt file, and configured the files to run properly and manage them as needed.</br>

* `Dockerfile`: Contains all the commands a user could call on the command line to assemble an image.</br>

* `README.md`: Shows what content was added and tested in Mini Project 2.</br>

* `requirements.txt`: Added the pandas and matplotlib package with specific version, which is 2.1.0 and 3.7.1.</br></br>
<img src="https://github.com/suim-park/Mini-Project-2/assets/143478016/f80ed434-7d9c-47be-ad7d-079b71d1440c.png" width="150" height="65"/></br>

* `githubactions`: Tested the code created using pandas to ensure that Git Actions runs properly. The test in 'test.py' checks that the number of rows and columns in the data match, so it confirms that the test has passed.</br></br>
<img src="https://github.com/suim-park/Mini-Project-2/assets/143478016/08cc6065-1234-4a72-a991-a61cebd88d69.png" width="670" height="500"/></br>

* `main.py`</br>
: Here is the additional content added to main.py before performing the tests.
1. First, used the pandas package to load data from 'Statistics_Test.csv.' Calculated the Mean, Median, and Standard Deviation of Age and added code to display these values to see the statistics for the ages of the people in the data.</br></br>
<img src="https://github.com/nogibjj/Suim-Park-Mini-Project-2/assets/143478016/d9a81603-ba95-46d4-89a0-85c5bb707ec4.png" width="650" height="300"/></br>
2. To verify and test main.py, added a function to calculate the rows and columns of the data.</br></br>
<img src="https://github.com/nogibjj/Suim-Park-Mini-Project-2/assets/143478016/5696be40-7fde-4701-9dc5-632568112007.png" width="280" height="200"/></br>
3. To visualize the distribution of the data's Age, created a Histogram. Added labels to each axis and a title to make it easy for users to understand the graph at a glance. Additionally, used blue color for the graph and white color for separation to enhance visibility.</br></br>
<img src="https://github.com/nogibjj/Suim-Park-Mini-Project-2/assets/143478016/3819bb4c-e034-4687-8327-c82a22fd108c.png" width="540" height="170"/></br>
4. Added the people() and create_hist() functions to display statistics and a histogram.</br>
<img src="https://github.com/nogibjj/Suim-Park-Mini-Project-2/assets/143478016/5a70b08c-f796-414f-9f1a-c418a7e897f2.png" width="120" height="50"/></br>
* `test_main.py`</br>
: This is the code for testing 'main.py'. It checks if the code is functioning correctly by using the number of rows and columns in the data.</br>
<img src="https://github.com/nogibjj/Suim-Park-Mini-Project-2/assets/143478016/3cf056b1-2fbe-419d-80c5-dcff3cd27708.png" width="250" height="350"/></br>

------------------------

* Summary of data</br>
  : The results of the statistical analysis of the 'Statistics_Test.csv' data and the information about the Age histogram can be found in the following summary. I created the summary using Markdown in a Jupyter Notebook, and you can access it by clicking **[here](https://github.com/nogibjj/Suim-Park-Mini-Project-2/blob/main/Summary.ipynb)**.</br></br>
  :exclamation: ***Jupyter Notebook cannot be opened directly on GitHub, so you must install the program and check it after installation.***
