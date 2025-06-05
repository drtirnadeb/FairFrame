# Project Log – FairFrame

## 🗓️ Date: June 4, 2025

### ✅ Initial Setup
- Created local project folder: `FairFrame/`
- Initialized Git repo:
  `git init`

*  Created and connected remote repo:

  `git remote add origin https://github.com/drtirnadeb/FairFrame.git`

  * Renamed branch to main:

    ```git branch -M main
    git push -u origin main
    ```

### 🏗️ Folder Structure Setup

Created folders: beginner/, intermediate/, advanced/

Added .gitkeep files to ensure folders tracked by Git

Committed folder structure:
```
mkdir -p beginner/data intermediate/data advanced/data
touch beginner/.gitkeep ...
git add .
git commit -m "Add folder structure"
```

### 🧪 Dataset Generation

Created synthetic datasets using script:

`loan_data.csv`

`promotion_data.csv`

`chatbot_output.csv`

* Script location:

`data_generation/banking-challenge-data-generation.py`

* Injected bias by lowering loan scores for Muslim/SC-ST applicants and modifying promotion exposure by caste/income.

## Git Pushes
Merged local main with remote main after initial push error:

```
git pull origin main --allow-unrelated-histories
git commit -m "Merge README from remote"
git push -u origin main
```

## 🧹 Cleanup
Moved CSVs into appropriate /data/ subfolders for each level

Removed root-level CSVs after verification


## 📦 Data Organization & Folder Sync (Post-Setup)
Verified all synthetic CSV files were correctly placed in:

`beginner/data/: loan_data.csv`

`intermediate/data/: loan_data.csv, promotion_data.csv`

`advanced/data/: loan_data.csv, promotion_data.csv, chatbot_output.csv`

Removed duplicate CSVs from project root to maintain clean structure.

Confirmed file visibility on GitHub after push:

``` 
git add .
git commit -m "Reorganize data files into respective challenge folders"
git push
```

## 🔄 GitHub Sync (Pull to Local)
Pulled latest changes from GitHub to update local folder:

`git pull origin main`
Resolved merge via terminal editor (:wq in Vim) after auto-prompt.

## 📝 Project Documentation
Added:

README.md with overview and challenge structure

instructions.md for each challenge level (still expanding)


## 📘 Notebook & Instructions Sync 

## ✅ Added Jupyter notebooks to each challenge level:
- `beginner/loan_bias_eda.ipynb`: Visual EDA and caste-level approval analysis
- `intermediate/intermediate_fairness_analysis.ipynb`: Model comparison with and without protected attributes + fairness metric templates

## ✅ Added instruction files:
- `beginner/instructions.md`: Outlines protected vs. neutral attributes and suggested visualizations
- `intermediate/instructions.md`: Structured walkthrough of modeling, metrics, and promotion task

## 🌀 GitHub Sync:
- Pulled latest remote changes (instructions + structure) to local:  
  `git pull origin main`
- Moved notebook to correct folder:  
  `mv intermediate_fairness_analysis.ipynb intermediate/`
- Committed and pushed updates:  
  ```
  git add intermediate/intermediate_fairness_analysis.ipynb beginner/loan_bias_eda.ipynb
  git commit -m "Add beginner and intermediate level notebooks"
  git push origin main
  ```

### 🔴 Advanced Challenge & Evaluation Finalization

✅ **Added Advanced Notebook Example**  
- `advanced/Advanced_Fairness_Analysis.ipynb`  
  Demonstrates chatbot response bias audit using both rule-based and LLM-based helpfulness scoring. Built on top of previous modeling and fairness analysis work.

✅ **Added Advanced Instructions**  
- `advanced/instructions.md`  
  Details the full scope of the advanced challenge, including:
  - Using LLMs to score chatbot response helpfulness
  - Group-wise fairness comparison based on demographic attributes

✅ **Created Grading Rubric**  
- `grading_rubric.md`  
  Structured rubric for evaluating participant submissions across all challenge levels (Beginner, Intermediate, Advanced).  
  Includes:
  - Scoring guide (1–5 scale)
  - Criteria per task level
  - Optional LLM-based grading prompts

✅ **Final GitHub Sync and README Update**  
- Pulled latest changes:
  ```
  git pull origin main
  git add advanced/Advanced_Fairness_Analysis.ipynb advanced/instructions.md grading_rubric.md
  git commit -m "Add advanced notebook, instructions, and grading rubric"
  git push origin main
  ```

  
✅ **Updated README.md:**

Included all challenge levels (Beginner → Advanced)

Linked to the grading rubric

Highlighted LLM-based chatbot fairness audit















