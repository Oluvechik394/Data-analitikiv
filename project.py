import pandas as pd
import matplotlib.pyplot as plt

# Дані 
data = {
    'Посада': ['Data Analyst', 'Senior Data Analyst', 'Junior Data Analyst', 'Data Scientist', 'Data Engineer'],
    'Заробітна плата': [50000, 70000, 40000, 80000, 75000],
    'Опис роботи': ['Analyze data', 'Lead data analysis', 'Support data analysis', 'Develop models', 'Manage data pipelines'],
    'Рейтинг роботодавця': [4.5, 4.0, 3.5, 4.8, 4.4],
    'Чисельність працівників': [200, 150, 100, 300, 250],
    'Сектор економіки': ['Tech', 'Finance', 'Healthcare', 'Tech', 'Finance'],
    'Конкуренти': ['Company A', 'Company B', 'Company C', 'Company D', 'Company E'],
    'Легко відгукнутися на вакансію': [True, False, True, False, True],
    'Локація': ['Kyiv', 'Lviv', 'Kharkiv', 'Kyiv', 'Odesa'],
    'Досвід роботи': ['2 years', '5 years', '1 year', '3 years', '4 years'],
    'Освіта': ['Bachelor', 'Master', 'Bachelor', 'PhD', 'Master'],
    'Навички': ['SQL, Python', 'SQL, Python, R', 'Excel, SQL', 'Python, Machine Learning', 'SQL, Python, Spark'],
    'Тип зайнятості': ['Full-time', 'Full-time', 'Part-time', 'Full-time', 'Full-time'],
    'Компанія': ['Company 1', 'Company 2', 'Company 3', 'Company 4', 'Company 5'],
    'Дата публікації': ['2023-01-01', '2023-01-15', '2023-02-01', '2023-02-15', '2023-03-01'],
    'Інші': ['Details 1', 'Details 2', 'Details 3', 'Details 4', 'Details 5']
}

# DataFrame
df = pd.DataFrame(data)

# Сортування
df = df.sort_values(by='Рейтинг роботодавця', ascending=False)

# Виведення рядків таблиці
print(df.head())

# Описова статистика
print(df.describe())

# Гістограма заробітної плати 
df['Заробітна плата'].hist(color='skyblue', edgecolor='black', bins=5)
plt.title('Розподіл Заробітної Плати')
plt.xlabel('Заробітна Плата')
plt.ylabel('Частота')
plt.grid(axis='y', alpha=0.75)
plt.show()

print(df[['Рейтинг роботодавця', 'Заробітна плата']].corr())

# Середня заробітна плата за навичками
df['Навички'] = df['Навички'].str.split(', ')
skills_salary = df.explode('Навички').groupby('Навички')['Заробітна плата'].mean()
print(skills_salary)

# Стовпчаста діаграма середньої зарплати за навичками
skills_salary.plot(kind='bar', color='lightgreen', edgecolor='black')
plt.title('Середня Зарплата за Навичками')
plt.xlabel('Навички')
plt.ylabel('Середня Зарплата')
plt.show()

# Точковий графік заробітної плати який залежить рейтингу роботодавця з назвами навичок
plt.scatter(df['Рейтинг роботодавця'], df['Заробітна плата'], color='blue')
plt.title('Залежність Заробітної Плати від Рейтингу Роботодавця')
plt.xlabel('Рейтинг Роботодавця (1 - найгірший, 5 - найкращий)')
plt.ylabel('Заробітна Плата')
plt.grid(True)


for i in range(len(df)):
    skills = df['Навички'][i]
    skill = skills[i % len(skills)]
    if df['Рейтинг роботодавця'][i] != 4.4 or df['Заробітна плата'][i] != 75000:
        plt.text(df['Рейтинг роботодавця'][i], df['Заробітна плата'][i], skill, fontsize=9, ha='right')


plt.scatter(4.2, 70000, color='blue')
plt.text(4.2, 70000, 'R', fontsize=9, ha='right')
plt.scatter(4.4, 75000, color='blue')
plt.text(4.4, 75000, 'Spark', fontsize=9, ha='right')
plt.show()
