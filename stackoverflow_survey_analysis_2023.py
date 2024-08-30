
import pandas as pd

# Load the dataset
file_path = "/Users/dominikkwiecien/Downloads/stack-overflow-developer-survey-2023/survey_results_public.csv"
df = pd.read_csv(file_path)

# 1. How many respondents completed the survey?
num_respondents = df.shape[0]
print(f"{num_respondents} respondents completed the survey.")

# 2. How many respondents answered all questions?
respondents_answered_all = df.dropna().shape[0]
print(f"{respondents_answered_all} respondents answered all questions.")

# 3. What are the values of central tendency for respondents' work experience?
work_exp = df['WorkExp'].dropna()
central_tendency_work_exp = work_exp.describe()
print("Central tendency measures for work experience:")
print(central_tendency_work_exp)

# 4. How many respondents work remotely?
remote_work_respondents = df[df['RemoteWork'] == 'Fully remote'].shape[0]
print(f"{remote_work_respondents} respondents work remotely.")

# 5. What percentage of respondents program in Python?
python_users = df['LanguageHaveWorkedWith'].str.contains('Python', na=False).sum()
python_usage_percentage = (python_users / num_respondents) * 100
print(f"{python_usage_percentage:.2f}% of respondents program in Python.")

# 6. How many respondents learned programming through online courses?
online_course_learners = df[df['LearnCodeOnlineResources'] == 'Yes'].shape[0]
print(f"{online_course_learners} respondents learned programming through online courses.")

# 7. What is the average and median salary in each country among respondents who program in Python?
python_devs = df[df['LanguageHaveWorkedWith'].str.contains('Python', na=False)]
avg_median_salary_by_country = python_devs.groupby('Country')['ConvertedCompYearly'].agg(['mean', 'median']).dropna()
print("Average and median salary by country for Python developers:")
print(avg_median_salary_by_country)

# 8. What is the education level of the 5 respondents with the highest salaries?
top_5_highest_salaries = df.nlargest(5, 'ConvertedCompYearly')[['EdLevel', 'ConvertedCompYearly']]
print("Education level of the 5 respondents with the highest salaries:")
print(top_5_highest_salaries)
