
# Stack Overflow Developer Survey 2023 Analysis

This project analyzes the results of the Stack Overflow Developer Survey 2023 using the Python Pandas library. The analysis provides insights into various aspects of the survey, such as the number of respondents, their work experience, remote work preferences, and more. The results are intended to give a comprehensive overview of the developer community's trends and tendencies.

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
- **89,184** respondents filled out the survey.
  ```python
  num_respondents = df.shape[0]
  print(f"{num_respondents} respondentów wypełniło ankietę.")
  ```

### 2. Complete Responses
- **0** respondents answered all the questions.
  ```python
  respondents_answered_all = df.dropna().shape[0]
  print(f"{respondents_answered_all} respondentów odpowiedziało na wszystkie pytania.")
  ```

### 3. Central Tendency Measures for Work Experience
- The work experience of respondents varies significantly:
  - **Mean**: 11.4 years
  - **Median**: 9.0 years
  - **Minimum**: 0 years
  - **Maximum**: 50 years

  ```python
  work_exp = df['WorkExp'].dropna()
  central_tendency_work_exp = work_exp.describe()
  print(central_tendency_work_exp)
  ```

### 4. Remote Work
- **30,566** respondents work remotely.
  ```python
  remote_work_respondents = df[df['RemoteWork'] == 'Fully remote'].shape[0]
  print(f"{remote_work_respondents} respondentów pracuje zdalnie.")
  ```

### 5. Python Usage
- **34.6%** of respondents program in Python.
  ```python
  python_users = df['LanguageHaveWorkedWith'].str.contains('Python', na=False).sum()
  python_usage_percentage = (python_users / num_respondents) * 100
  print(f"{python_usage_percentage:.2f}% respondentów programuje w języku Python.")
  ```

### 6. Online Learning
- **27,974** respondents learned programming through online courses.
  ```python
  online_course_learners = df[df['LearnCodeOnlineResources'] == 'Yes'].shape[0]
  print(f"{online_course_learners} respondentów nauczyło się programować poprzez kursy online.")
  ```

### 7. Average and Median Salary by Country (for Python Developers)
- The analysis revealed that Python developers' salaries vary widely across different countries. For example:
  - **United States**: Mean salary - $118,844, Median salary - $100,000
  - **Germany**: Mean salary - $69,000, Median salary - $61,000

  ```python
  python_devs = df[df['LanguageHaveWorkedWith'].str.contains('Python', na=False)]
  avg_median_salary_by_country = python_devs.groupby('Country')['ConvertedCompYearly'].agg(['mean', 'median']).dropna()
  print(avg_median_salary_by_country)
  ```

### 8. Education Level of Top Earners
- The top 5 highest-paid respondents have the following education levels:
  - **3** with Professional degrees (JD, MD, Ph.D., etc.)
  - **1** with a Bachelor’s degree
  - **1** with Primary/elementary school education

  ```python
  top_5_highest_salaries = df.nlargest(5, 'ConvertedCompYearly')[['EdLevel', 'ConvertedCompYearly']]
  print(top_5_highest_salaries)
  ```
