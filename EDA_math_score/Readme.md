# Exploratory data analysis 
The essence of the project is to track the impact of living conditions of students aged 15 to 22 on their academic performance in mathematics, in order to identify students at risk at an early stage.

To determine the parameters of the future model, conduct a exploratory data analysis and compile a report on its results.


## Data Exploration
Let's look at the variables that the dataset contains:

- school — *abbreviation of the school in which the student is studying.*
- sex — *student gender ('F' - female, 'M' - male).*
- age — *student age (15 to 22).*
- address — *student address type ('U' - city, 'R' - out of town).*
- famsize - *family size ('LE3' <= 3, 'GT3'> 3).*
- Pstatus - *status of parents' shared housing ('T' - live together 'A' - separately).*
- Medu - *mother's education (0 - no, 1 - 4 classes, 2 - 5-9 classes, 3 - secondary special or 11 classes, 4 - higher).*
- Fedu - *father's education (0 - no, 1 - 4 classes, 2 - 5-9 classes, 3 - secondary special or 11 classes, 4 - higher).*
- Mjob - *mother's work ('teacher' - teacher, 'health' - healthcare, 'services' - public service, 'at_home' - not working, 'other' - other).*
- Fjob - *father's work ('teacher' - teacher, 'health' - healthcare, 'services' - public service, 'at_home' - not working, 'other' - other).*
- reason - *the reason for choosing a school ('home' - proximity to home, 'reputation' - school reputation, 'course' - educational program, 'other' - other).*
- guardian - *guardian ('mother' - mother, 'father' - father, 'other' - other).*
- traveltime - *travel time to school (1 - <15 min., 2 - 15-30 min., 3 - 30-60 min., 4 -> 60 min.).*
- studytime - *time to study in addition to school per week (1 - <2 hours, 2 - 2-5 hours, 3 - 5-10 hours, 4 -> 10 hours).*
- failures - *the number of extracurricular failures (n, if 1 <= n <3, otherwise 0).*
- schoolsup - *additional educational support (yes or no).*
- famsup - *family educational support (yes or no).*
- paid - *additional paid classes in mathematics (yes or no).*
- activities - *extracurricular activities (yes or no).*
- nursery - *attended kindergarten (yes or no).*
- higher - *wants to get a higher education (yes or no).*
- internet - *internet at home (yes or no).*
- romantic - *in a romantic relationship (yes or no).*
- famrel - *family relationships (from 1 - very poor to 5 - very good).*
- freetime - *free time after school (from 1 - very little to 5 - very much).*
- goout - *spending time with friends (from 1 - very little to 5 - very much).*
- health - *current state of health (from 1 - very poor to 5 - very good).*
- absences - *number of lessons missed.*
- score - *math exam scores.*

## Сonclusion    
So, as a result of EDA for the analysis of the influence of student's living conditions on math scores, the following conclusions were obtained:

- There are not many missing values in the data.

- Outliers were found only in the columns with score, age and absences, which allows us to conclude that the data is quite clean.

- In the columns of famrel, Fedu had values with errors.

- The studytime_granular column is probably a modification of the studytime column. studytime_granular has been deleted.

- Data is not highly correlated.

- The most important parameters that are proposed to be used later to build the model are *age, addres, Medu, Fedu, Mjob, Fjob, traveltime, studytime, failures, schoolsup, famrel, goout, health, absences.*
