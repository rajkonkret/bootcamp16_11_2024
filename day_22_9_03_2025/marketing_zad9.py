import numpy as np
import lift_function
import marketing_zad7 as fun
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("marketing_r_bool.csv", sep=",")
df['date_served'] = pd.to_datetime(df['date_served'], format='%m/%d/%y')

email = df[df['marketing_channel'] == 'Email']
print(email.head().to_string())
# 354  a100000526  2018-01-01             Email  personalization       True             Arabic             Arabic   0-18 years          1/1/18           NaN               Email        True
# 358  a100000530  2018-01-05             Email  personalization       True             Arabic             Arabic  19-24 years          1/5/18           NaN               Email        True
# 362  a100000534  2018-01-09             Email  personalization      False            English            English  45-55 years          1/9/18           NaN               Email        True
# 366  a100000538  2018-01-13             Email  personalization       True             Arabic             Arabic  24-30 years         1/13/18       1/23/18               Email       False
# 370  a100000542  2018-01-17             Email  personalization       True            English            English   0-18 years         1/17/18       2/12/18               Email       False

alloc = email.groupby(['variant'])['user_id'].nunique()
print(alloc.head())

alloc.plot(kind="bar")
# plt.title("Personalization test allocation")
# plt.ylabel('# participants')
# plt.show()

subscribers = email.groupby(['user_id', 'variant'])['converted'].max()
print(subscribers.head())

subscribers_df = pd.DataFrame(subscribers.unstack(level=1))
control = subscribers_df['control'].dropna()
print(control.head())

personalization = subscribers_df['personalization'].dropna()
print(personalization.tail())

print("Control conversion rate:", np.mean(control))  # średnia
print("Personalization conversion rate:", np.mean(personalization))
# Control conversion rate: 0.2814814814814815
# Personalization conversion rate: 0.3908450704225352
print(lift_function.lift(control, personalization))