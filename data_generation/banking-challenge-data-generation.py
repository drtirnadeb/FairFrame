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
n = 100

# ---------------- Loan Risk Estimator Dataset ----------------

genders = np.random.choice(['Male', 'Female'], size=n)
castes = np.random.choice(['General', 'OBC', 'SC/ST'], size=n, p=[0.5, 0.3, 0.2])
religions = np.random.choice(['Hindu', 'Muslim', 'Christian', 'Other'], size=n, p=[0.6, 0.2, 0.1, 0.1])
ages = np.random.randint(21, 61, size=n)
incomes = np.random.randint(30000, 120001, size=n)
accent_scores = np.random.uniform(30, 100, size=n)

# Neutral features
credit_scores = np.random.normal(700, 50, size=n)
num_loans = np.random.poisson(2, size=n)
savings_balances = np.random.randint(1000, 100000, size=n)
years_with_bank = np.random.randint(1, 20, size=n)

# Bias injection
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
    'credit_history_score': credit_scores.round(1),
    'number_of_loans': num_loans,
    'savings_balance': savings_balances,
    'years_with_bank': years_with_bank,
    'loan_score': loan_scores.round(2),
    'approved': approvals
})

# ---------------- Promotion Recommender Dataset ----------------

promo_types = ['Cashback_5%', 'Loan_Plus', 'Premium_Account', 'No_Promo']

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
    'credit_history_score': credit_scores.round(1),
    'years_with_bank': years_with_bank,
    'assigned_promotion': promotion_types
})

# ---------------- Chatbot Dataset ----------------

user_inputs = [
    'I need help resetting my password.',
    'How do I apply for a business loan?',
    'What’s my current balance?'
]
query_types = ['account_help', 'loan_inquiry', 'balance_check']

chatbot_responses = [
    'Please visit our FAQ page.',
    'Sure, I can walk you through that.',
    'We are currently not offering that service.',
    'You can apply through our mobile app.',
    'Please contact customer support.',
    'Let me check that for you...'
]

chatbot_df = pd.DataFrame({
    'user_id': [f'U{i:03d}' for i in range(n)],
    'gender': genders,
    'caste': castes,
    'religion': religions,
    'accent_score': np.random.uniform(30, 100, size=n).round(2),
    'account_age_years': np.random.randint(1, 20, size=n),
    'prev_issues_reported': np.random.poisson(1, size=n),
    'query_type': np.random.choice(query_types, size=n),
    'user_input': np.random.choice(user_inputs, size=n),
    'chatbot_response': np.random.choice(chatbot_responses, size=n)
})


# Save all three to CSV
loan_df.to_csv("/Users/deb/Desktop/Data_science+AI/FairFrame/loan_data.csv", index=False)
promo_df.to_csv("//Users/deb/Desktop/Data_science+AI/FairFrame/promotion_data.csv", index=False)
chatbot_df.to_csv("/Users/deb/Desktop/Data_science+AI/FairFrame/chatbot_output.csv", index=False)
