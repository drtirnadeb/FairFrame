
# ✅ Grading System for FairFrame Challenge

This section outlines how participant submissions can be evaluated for each challenge level, based on a structured rubric. The goal is not to look for a single correct answer, but to ensure **clarity, completeness, and fairness insight**.

---

## 🟢 Beginner Level: EDA & Demographic Comparison

**Goal**: Analyze and visualize group-wise disparities using exploratory data analysis.

| Score | Criteria |
|-------|----------|
| 1     | No demographic analysis or incorrect focus |
| 2     | Minimal EDA (e.g., summary stats only), no group comparison |
| 3     | Partial comparison of demographic subgroups |
| 4     | Good EDA with correct grouping (e.g., caste/gender), some insights |
| 5     | Excellent EDA, key disparities identified and clearly communicated |

**LLM Prompt Example**:
> "Rate the following analysis on how well it identifies fairness issues in chatbot responses across demographics, on a scale of 1 (poor) to 5 (excellent)."

---

## 🟡 Intermediate Level: Fairness Metrics from Classification Models

**Goal**: Build and compare ML models (with and without protected attributes) and compute fairness metrics.

| Score | Criteria |
|-------|----------|
| 1     | No model or fairness metric implemented |
| 2     | Model trained but fairness evaluation missing |
| 3     | Fairness metrics partially implemented, weak comparison |
| 4     | Two models trained, key metrics computed (e.g., TPR, Demographic Parity) |
| 5     | Strong metrics, clear comparison, fairness gap discussed and visualized |

**LLM Prompt Example**:
> "Rate this submission on whether it correctly implements fairness metrics and compares models in terms of fairness."

---

## 🔴 Advanced Level: Chatbot Audit using Rule-based and LLM Rating

**Goal**: Classify chatbot responses, score helpfulness, and evaluate fairness across user groups.

| Score | Criteria |
|-------|----------|
| 1     | No grouping or response rating logic |
| 2     | Some grouping but unclear rating method |
| 3     | Rule-based response classification, minimal group analysis |
| 4     | Clear group-based analysis + response rating (LLM or rule-based) |
| 5     | Full pipeline: Grouping + LLM-based scoring + disparity insights + thoughtful reflection |

**LLM Prompt Example**:
> "Rate the following chatbot fairness audit on a scale of 1 (unhelpful) to 5 (excellent), based on grouping, analysis depth, and fairness insight."

---

## ✅ Summary

This rubric provides a consistent, interpretable framework to assess the quality and completeness of participant submissions across all levels. Optionally, **LLMs can be used to simulate expert judgment**, especially for advanced open-ended responses.

