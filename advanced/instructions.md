# Advanced Challenge – FairFrame

## 🎯 Goal
Conduct a multi-system fairness audit across all three systems: Loan Risk Estimator, Promotion Recommender, and Customer Service Chatbot.

## 📁 Datasets
- `data/loan_data.csv`
- `data/promotion_data.csv`
- `data/chatbot_output.csv`

## 📝 Tasks
1. Analyze systemic disparities across the three systems:
   - Bias in loan score and approvals
   - Unequal promotion exposure
   - Language model response gaps by identity

2. For the chatbot:
   - Identify biased or less helpful responses by group
   - Create a simple scoring rubric (e.g., 0 = biased, 1 = fair)
   - Score and summarize

3. Discuss interactions between systems (e.g., loan denial + weak support = compounded harm)

## ✅ Deliverable
- Summary notebook or report that includes:
  - Analysis across all systems
  - At least one fairness metric
  - Bias scoring on chatbot examples
  - A short write-up of your findings and reflections
