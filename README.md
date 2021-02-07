# Medical-Analysis
A Django App to allow interpretation and visualization of global medical data.

Data Pulled From

https://www.kaggle.com/utkarshxy/who-worldhealth-statistics-2020-complete

As a software Engineer I am trying to gain a larger breadth of programming knowledge and trying to learn to integrate different parts of software to create a complete system. I am also trying to learn new methods of interpreting data through open source software.

This a piece of software that took the https://www.kaggle.com/utkarshxy/who-worldhealth-statistics-2020-complete dataset containing 52 different csvs of data with thousands of rows each and pushes it to a firestore database using python (specically pandas). I then uses this database as the source of my data in a django app that allows visualization of the data and lets you choose any report in the database and view the data in a dataframe and graph. The app will then display the average, max and min values. You can filter by country and date range (2000-2020) or view all data.

Steps to run the software:
1. clone the repo
2. install anaconda (https://docs.anaconda.com/anaconda/install/)
3. run `conda create --name myenv --file spec-file.txt` to create the conda env
4. cd into django1 then into medicalAnalysis
5. run `python manage.py migrate` in the terminal
6. run `python manage.py createsuperuser` in the terminal then create a user
7. run `python manage.py runserver` in the terminal than click on the development server link that pops up
8. log in using the credentials you created
9. click on the Medical Analysis tab in the corner
10. select your date range to query by
11. select country to query by.
12. select which report you want to use
13. view the mean, max and min of the data or interpret it yourself with the interactive graph and dataframe.

The specific purpose of this project was to learn get solid information from data through python and visualization. I also thought as an extra challenge to use the firestore database. And since I have experience with Django I thought it would be cool to bring the code to life and connect the database to a django app rather than just a text based app.

[Software Demo Video](https://youtu.be/XnJg7uGMXBo)

# Relational Database

Database used: sqllite3
The database I created just has one table currently, the food_prices table:
food_prices:
- id integer PRIMARY KEY
- cm_name text NOT NULL - name of the good
- adm0_name text NOT NULL - name of the country
- um_name text NOT NULL - name of the unit of measurment
- mp_year text NOT NULL - year of the data
- mp_price integer NOT NULL - price of the data, average to create a single price unit

# Development Environment

For an exact copy of the env I used, See the spec-file.txt which allows you to recreate the conda env.

Language and tools used:
- Python
- Django
- Pyviz Panel
- Pandas
- Holoviews
- Holoviz
- Numpy
- datetime
- jupyter lab

# Useful Websites

* [dataset](https://www.kaggle.com/utkarshxy/who-worldhealth-statistics-2020-complete)
* [conda env]https://medium.com/@cbrannen/importing-data-into-firestore-using-python-dce2d6d3cd51(https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
* [pandas docs](https://pandas.pydata.org/docs/)
* [pyviz panel](https://panel.holoviz.org/)
* [hv plots](https://hvplot.holoviz.org/index.html)
* [firestore and pandas tutorial](https://medium.com/@cbrannen/importing-data-into-firestore-using-python-dce2d6d3cd51)

# Future Work

* Use more graphs and find new ways to plot the data
* Add in an upload csv button to store directly to firestore
* Create new queries
* Style the site more
