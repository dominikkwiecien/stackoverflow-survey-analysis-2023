
# Stack Overflow Developer Survey 2023 Analysis

This project analyzes the results of the Stack Overflow Developer Survey 2023 using the Python Pandas library. The analysis provides insights into various aspects of the survey, such as the number of respondents, their work experience, remote work preferences, and more. The results are intended to give a comprehensive overview of the developer community's trends and tendencies.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Overview](#project-overview)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run this project locally, you need to have Python installed. Follow these steps:

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    ```
2. Navigate to the project directory:
    ```bash
    cd your-repo-name
    ```
3. Install the required packages:
    ```bash
    pip install pandas
    ```

## Usage

To execute the analysis, open the Jupyter notebook or Google Colab and run the cells step by step. The dataset used in this analysis can be downloaded from the Stack Overflow Developer Survey 2023 website.

Ensure that the dataset is placed in the correct path as specified in the notebook, or update the file path accordingly.

## Project Overview

This project was developed to answer the following questions:

1. **Number of Respondents**: How many people filled out the survey?
2. **Complete Responses**: How many respondents answered all the questions?
3. **Central Tendency Measures for Experience**: What are the values of central tendency for respondents' work experience?
4. **Remote Work**: How many respondents work remotely?
5. **Python Usage**: What percentage of respondents program in Python?
6. **Online Learning**: How many respondents learned programming through online courses?
7. **Average and Median Salary by Country**: What is the average and median salary in each country among respondents who program in Python, grouped by country?
8. **Education Level of Top Earners**: What is the education level of the 5 respondents with the highest salaries?

## Results

### 1. Number of Respondents
```python
import pandas as pd

file_path = "/Users/dominikkwiecien/Downloads/stack-overflow-developer-survey-2023/survey_results_public.csv"
df = pd.read_csv(file_path)

#1. Ilu respondentów wypełniło ankietę?
num_respondents = df.shape[0]
print(f"{num_respondents} respondentów wypełniło ankietę.")
```

### 2. Complete Responses
```python
#2. Ilu respondentów odpowiedziało na wszystkie pytania?
respondents_answered_all = df.dropna().shape[0]
print(f"{respondents_answered_all} respondentów odpowiedziało na wszystkie pytania.")
```

### 3. Central Tendency Measures for Work Experience
```python
#3. Jakie są wartości miar tendencji centralnej dla doświadczenia (WorkExp) respondentów?
work_exp = df['WorkExp'].dropna()
central_tendency_work_exp = work_exp.describe()
print(central_tendency_work_exp)
```

### 4. Remote Work
```python
#4. Ilu respondentów pracuje zdalnie?
remote_work_respondents = df[df['RemoteWork'] == 'Fully remote'].shape[0]
print(f"{remote_work_respondents} respondentów pracuje zdalnie.")
```

### 5. Python Usage
```python
#5. Jaki procent respondentów programuje w języku Python?
python_users = df['LanguageHaveWorkedWith'].str.contains('Python', na=False).sum()
python_usage_percentage = (python_users / num_respondents) * 100
print(f"{python_usage_percentage:.2f}% respondentów programuje w języku Python.")
```

### 6. Online Learning
```python
#6. Ilu respondentów nauczyło się programować poprzez kursy online?
online_course_learners = df[df['LearnCodeOnlineResources'] == 'Yes'].shape[0]
print(f"{online_course_learners} respondentów nauczyło się programować poprzez kursy online.")
```

### 7. Average and Median Salary by Country (for Python Developers)
```python
#7. Jaka jest średnia i mediana wynagrodzenia (ConvertedCompYearly) w każdym kraju wśród respondentów, którzy programują w Pythonie i są pogrupowani według kraju?
python_devs = df[df['LanguageHaveWorkedWith'].str.contains('Python', na=False)]
avg_median_salary_by_country = python_devs.groupby('Country')['ConvertedCompYearly'].agg(['mean', 'median']).dropna()
print(avg_median_salary_by_country)
```

### 8. Education Level of Top Earners
```python
#8. Jaki poziom wykształcenia ma 5 respondentów z najwyższym wynagrodzeniem?
top_5_highest_salaries = df.nlargest(5, 'ConvertedCompYearly')[['EdLevel', 'ConvertedCompYearly']]
print(top_5_highest_salaries)
```

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to fork this repository and create a pull request. Please make sure that your contributions align with the project's objectives and follow the style guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
