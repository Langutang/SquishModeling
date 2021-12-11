# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 12:50:49 2021

@author: John Lang
"""
#importing libraries
import random
import pandas as pd
import numpy as np
import names
import re

#making sample selections for fake data
gender = ['m','f','t/u']

circumstance = ['anxiety', 'depression', 'bipolar', 'adhd', 'dissociattion',
                'eating_disorder', 'paranoia', 'ptsd', 'psychosis', 'schizophrenia',
                'personality_disorder', 'OCD', 'autism', 'identity_issues']

interests = ['photography', 'sports', 'radio', 'podcast', 'travel', 'yoga',
             'dance', 'art', 'acting', 'theatre', 'music', 'programming', 
             'reading', 'music', 'cooking', 'biking', 'video_games', 'animals', 
             'foreign_language', 'writing', 'exercise', 'blogs', 'activism']

environment = ['work','school','relationship','financial','spiritual','sexual',
               'physical','other']

#creating empty lists to pass random samples to
names_list = []
gender_list = []
circumstance_list = []
interest_list = []
environment_list = []
age_list = []

#random sampling
for i in range(5000):
    fake_names = names.get_full_name()
    names_list.append(fake_names)

for i in range(5000):
    fake_gender = np.random.choice(gender, 1, p=[0.45, 0.45, 0.1])
    gender_list.append(np.array2string(fake_gender))
    
for i in range(5000):
    fake_circumstance = random.sample(circumstance, 2)
    #fake_circumstance1 = np.random.choice(circumstance, 1, p=[0.15, 0.15, 0.05,
     #                                                        0.1,0.05,0.05,
      #                                                       0.05,0.05,0.05,
       #                                                      0.05,0.05,0.05,
        #                                                     0.05,0.1])
    circumstance_list.append(str(fake_circumstance)) 

for i in range(5000):
    fake_interest = random.sample(interests, 3)
    #fake_interest1 = np.random.choice(interests, 1)
    interest_list.append(str(fake_interest))
    
for i in range(5000):
    fake_environment = np.random.choice(environment, 1)
    environment_list.append(np.array2string(fake_environment))
    
for i in range(5000):
    fake_age = random.randint(18, 65)
    age_list.append(fake_age)

# Creating the DataFrame, here I have added the attribute 'name' for identifying the record.
df = pd.DataFrame({
    'name' : names_list,    
    'sex' : gender_list,    
    'interest' : interest_list,   
    'circumstance' : circumstance_list,
    'environment':environment_list,
    'age' : age_list,    
})

#data cleansing
df['name'] = df['name'].astype('string')
df['interest'] = df['interest'].astype('string')
df['circumstance'] = df['circumstance'].astype('string')
df['sex'] = df['sex'].astype('string').map(lambda x: re.sub(r'\W+', '', x))
df['environment'] = df['environment'].astype('string').map(lambda x: re.sub(r'\W+', '', x))
# split column and add new columns to df
df[['interest1', 'interest2', 'interest3']] = df['interest'].str.split(',', expand=True)
df[['circumstance1', 'circumstance2']] = df['circumstance'].str.split(',', expand=True)
df.drop(['interest','circumstance'], axis=1 ,inplace=True)


df['interest1'] = df['interest1'].map(lambda x: re.sub(r'\W+', '', x))
df['interest2'] = df['interest2'].map(lambda x: re.sub(r'\W+', '', x))
df['interest3'] = df['interest3'].map(lambda x: re.sub(r'\W+', '', x))
df['circumstance1'] = df['circumstance1'].map(lambda x: re.sub(r'\W+', '', x))
df['circumstance2'] = df['circumstance2'].map(lambda x: re.sub(r'\W+', '', x))

model_dataframe = pd.get_dummies(df, prefix=['interest1', 'interest2', 'interest3',
                                             'circumstance1', 'circumstance2'], 
                                 columns=['interest1', 'interest2', 'interest3',
                                             'circumstance1', 'circumstance2'])

