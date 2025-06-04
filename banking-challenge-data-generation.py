#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 16:30:17 2025

@author: deb
"""

import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Number of users
n = 100

# --- Loan Risk Estimator Dataset ---

# Gender, caste, religion distributions
genders = np.random.choice(['Male', 'Female'], size=n)
castes = np.random.choice(['General', 'OBC', 'SC/ST'], size=n, p=[0.5, 0.3, 0.2])
religions = np.random.choice(['Hindu', 'Muslim', 'Christian', 'Other'], size=n, p=[0.6, 0.2, 0.1, 0.1])
ages = np.random.randint(21, 61, size=n)
incomes = np.random.randint(30000, 120001, size=n)
accent_scores = np.random.uniform(30, 100, size=n)  # higher = more "standard" accent

# Inject bias: SC/ST and Muslim applicants get slightly lower loan scores
base_loan_scores = np.random.normal(loc=70, scale=10, size=n)
loan_bias = np.array([-5 if c == 'SC/ST' else 0 for c in castes]) + \
            np.array([-4 if r == 'Muslim' else 0 for r in religions])
loan_scores = np.clip(base_loan_scores + loan_bias, 0, 100)
approvals = (loan_scores > 60).astype(int)

loan_df = pd.DataFrame({
    'user_id': [f'U{i:03d}' for i in range(n)],
    'gender': genders,
    'caste': castes,
    'religion': religions,
    'age': ages,
    'income': incomes,
    'accent_score': accent_scores.round(2),
    'loan_score': loan_scores.round(2),
    'approved': approvals
})

# --- Promotion Recommender Dataset ---

# Define promotion types
promo_types = ['Cashback_5%', 'Loan_Plus', 'Premium_Account', 'No_Promo']

# Exposure bias: General caste + high income more likely to get high-value promos
def assign_promo(caste, income):
    if caste == 'General' and income > 80000:
        return np.random.choice(['Loan_Plus', 'Premium_Account'], p=[0.5, 0.5])
    elif caste == 'SC/ST' or income < 50000:
        return np.random.choice(['Cashback_5%', 'No_Promo'], p=[0.7, 0.3])
    else:
        return np.random.choice(promo_types)

promotion_types = [assign_promo(c, i) for c, i in zip(castes, incomes)]

promo_df = pd.DataFrame({
    'user_id': loan_df['user_id'],
    'gender': genders,
    'caste': castes,
    'religion': religions,
    'income': incomes,
    'assigned_promotion': promotion_types
})

# --- Chatbot Responses Dataset ---

chatbot_data = [
    {'user_id': 'U001', 'user_input': 'I need help resetting my password.',
     'user_profile': 'Female, SC/ST, accent_score=35', 'chatbot_response': 'Please visit our FAQ page.'},
    {'user_id': 'U002', 'user_input': 'I need help resetting my password.',
     'user_profile': 'Male, General, accent_score=95', 'chatbot_response': 'Sure, I can walk you through that.'},
    {'user_id': 'U003', 'user_input': 'How do I apply for a business loan?',
     'user_profile': 'Muslim, Male, accent_score=40', 'chatbot_response': 'We are currently not offering that service.'},
    {'user_id': 'U004', 'user_input': 'How do I apply for a business loan?',
     'user_profile': 'Hindu, Female, accent_score=90', 'chatbot_response': 'You can apply through our mobile app.'},
    {'user_id': 'U005', 'user_input': 'What’s my current balance?',
     'user_profile': 'Christian, SC/ST, accent_score=38', 'chatbot_response': 'Please contact customer support.'},
    {'user_id': 'U006', 'user_input': 'What’s my current balance?',
     'user_profile': 'General, Male, accent_score=88', 'chatbot_response': 'Let me check that for you...'}
]

chatbot_df = pd.DataFrame(chatbot_data)

# Save all three to CSV
loan_df.to_csv("/Users/deb/Desktop/Data_science+AI/FairFrame/loan_data.csv", index=False)
promo_df.to_csv("//Users/deb/Desktop/Data_science+AI/FairFrame/promotion_data.csv", index=False)
chatbot_df.to_csv("/Users/deb/Desktop/Data_science+AI/FairFrame/chatbot_output.csv", index=False)
