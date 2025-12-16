# AskVBC – Intelligent Attribution & Delegation Chatbot

AskVBC is a demonstration chatbot designed to help business analysts and
business stakeholders understand **Aetna CVS VBC attribution and delegation
decisions** using plain English questions.

The chatbot translates natural language questions into:
- BigQuery data lookups
- Business-rule reasoning
- Simple, explainable answers

This project is built for **demonstration and learning purposes** and mirrors
how real healthcare analytics organizations design explainable AI systems.

---

## 🔍 Example Questions AskVBC Can Answer

- Why was member 101 delegated to OAKST_VT?
- Why was member 102 directly attributed?
- What rule caused a member to be delegated?
- Compare attribution outcomes for two members
- What happens if a provider is out-of-state?

---

## 🧠 How AskVBC Thinks (High-Level)

1. Understands user intent (WHY / WHAT / COMPARE)
2. Identifies the member or entity involved
3. Queries BigQuery tables for factual data
4. Applies business rules from documented logic
5. Responds in clear, non-technical English

---

## 🏗️ Architecture Overview

