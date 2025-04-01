# Project: Calories Burned Expectation 🔥

![calories_burned_project](https://github.com/user-attachments/assets/b276b254-b258-467f-8b58-6a57337d906f)


## Index 📋

1. Project Description.
2. Project Access.
3. Functionalities and Applications Demonstration.
4. Technologies used.
5. Acknowledgments.
6. Project Developer.

## 1. Project Description 📚

This project presents a comprehensive analysis of gym members' exercise tracking data obtained from Kaggle. It consists of two main stages:<br><br>

1. Data analysis and modeling performed in *Jupyter Notebook*.<br>
2. Model Deployment in a Desktop Application Environment built in *Visual Studio Code*.<br><br>

The goal of this project is to predict the number of calories a person can burn in a single workout session using historical data and a Linear Regression model. 
The prediction is based on several key features, selected through experimentation as the most relevant for estimating calorie burn.

*⚠️Note: This analysis is limited to the dataset used for training the model. Therefore, the predictions should be interpreted with caution.
This project is intended exclusively for educational purposes, as part of practicing Data Science skills.*

Once the model learns the relationship between these features and the expected calorie burn, a user-friendly desktop application allows individuals to input their personal data 
and obtain an estimate of the calories they might burn during a workout.


## 2. Project Access 📂

There are two options for obtaining the project:

1. Clone the repository used in the command line. You only need to stand on the path you want to clone it and type the following command:
   `git clone https://github.com/ignaciomajo/calories_burned_expectations`

2. Or you can download it directly from the GitHub repository by following these steps in the provided link:
   <p><a href="https://github.com/ignaciomajo/calories_burned_expectation">https://github.com/ignaciomajo/calories_burned_expectation</p>

   The link will take you to the following screen, and do what's indicated on the image:

![download_zip](https://github.com/user-attachments/assets/5fa0c947-9e42-42e7-9552-16f13bcaa3e9)
   
This will download the compressed file `.zip` for you to save it in any path you wish to.

Either way, you should end up with the following files an directories:

![repository](https://github.com/user-attachments/assets/32e744b5-aea2-4a19-81e9-394fcdc3ab97)

* **models**📁: this directory contains the model and the scalaer for deployment, both are implemented in the desktop application to calculate predictions based on the user
  provided by the user.
* **Calories_Burned_Analysis.ipynb**📄: ***Jupyter Notebook*** file containing the full analysis performed on the dataset. *(I suggets to use this environment or a Google Colab
  environment since it has data visualization)*.
* **Calories_Burned_Expectation.py**📄: script that contains the application development. You can run it from an interpreter such as ***Visual Studio Code*** to see the application. In case you want to build the application for distribution, you can run the following code in your command line from the directory you have the project in:<br>

` python -m PyInstaller --onefile --windowed --icon=icon4.png --add-data "models;models" --hidden-import=numpy --hidden-import=numpy.core.multiarray Calories_Burned_Expectations.py`

*Note: make sure you have PyInstaller in your computer*

* **gym_members_excercise_tracking.csv**📄: ***CSV*** file that contains the data used for the analysis.

## 3. Functionalities and Applications Demonstration 📝

<br><br><br><br><br>

## 4. Technologies used 🛠️

* ``
* `Git and GitHub`
* ``
* ``
* ``

## 5. Acknowledgments 🤝

<br><br><br><br><br>

## 6. Project Developer 👷

![imagen-readme](https://github.com/user-attachments/assets/133bc743-0424-4120-a7a6-7245d2f28f8c)

**| Ignacio Majo | Junior Data Scientist | Junior RPA Developer |**
