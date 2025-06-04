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

This projectlog.md to document workflow and git commands











