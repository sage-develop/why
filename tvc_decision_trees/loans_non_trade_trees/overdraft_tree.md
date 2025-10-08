# Overdraft Decision Tree

# Prompt

Create a non-product decision tree as mermaid code inside this file. Only see OD - Overdraft key points in this 'loan_non_trade_tree.md' file

## Decision Flow

```mermaid
flowchart TD
    Start@{ label: "Start: Non-Trade Transaction<br style=\"--tw-scale-x:\">(Overdraft Ver.1)" } -- <br> --> Context["Context: Non-trade payment may create short-term cash-flow gaps<br>requiring temporary funding support."]
    Context --> Q1{"Does the client have sufficient funds for their business needs?"}
    Q1 -- Yes --> End1["No non-trade financing opportunity"]
    Q1 -- No --> Q2{"What type of non-trade<br>payment is needed?"}
    Q2 -- "Operating expenses<br>(e.g., salaries, rent, utilities)" --> Q4{"Does the client want to preserve<br>cash for daily operations?"}
    Q2 -- "Equipment /<br>services down payment /<br>other business needs <br>(e.g., insurance, maintenance)" --> Q3{"Is this payment urgent?"}
    Q2 -- Tax or government<br>obligations --> OD1["Opportunity: Overdraft<br>(mandatory compliance payment)"]
    Q2 -- Debt repayment /<br>installment due --> Q5{"Is refinancing available or preferred?"}
    Q3 -- Yes --> OD3["Opportunity: Overdraft<br>(bridge urgent payment)"]
    Q3 -- No --> Q4
    Q4 -- Yes --> OD2["Opportunity: Overdraft<br>(cash-flow preservation)"]
    Q4 -- No --> End2["No non-trade financing opportunity"]
    Q5 -- Yes --> End3["Opportunity: Refinancing or restructuring"]
    Q5 -- No --> OD5["Opportunity: Overdraft<br>(bridge short-term repayment)"]

    Start@{ shape: stadium}
     OD1:::Sky
     OD3:::Sky
     OD2:::Sky
     OD5:::Sky
    classDef Sky stroke-width:1px, stroke-dasharray:none, stroke:#374D7C, fill:#E2EBFF, color:#374D7C
```

## Decision Logic

This decision tree is based on the key characteristics of Overdraft facilities:

### Key Questions Based on Overdraft Features:

1. **Cash Flow Fluctuations**: Does the client experience day-to-day cash flow variations?
2. **Flexibility Needs**: Do they need maximum flexibility in accessing and repaying funds?
3. **Unexpected Expenses**: Are there unforeseen costs that need immediate coverage?
4. **Interest Preference**: Do they want to pay interest only on amounts actually used?
5. **Repayment Flexibility**: Can they repay when funds are available rather than on fixed schedules?
6. **Usage Discipline**: Will they use the facility responsibly to avoid high long-term costs?

### Overdraft Suitability Indicators:

✓ **Ideal for clients who need:**

- Automatic short-term loans through current account
- Interest only on overdrawn amounts
- Flexible drawdown and repayment timing
- Management of cash flow fluctuations
- Coverage for unexpected expenses

⚠️ **Caution for clients who might:**

- Use excessively or for long periods
- Accumulate expensive interest and fees
- Need structured repayment schedules

---

## Product Details

### OD - Overdraft

Definition:
A flexible, short-term credit facility that allows customers to withdraw more than the available balance in their current account, up to a pre-approved limit.

Key Points:

- Acts as an automatic short-term loan through the current account.
- Interest applies only on the overdrawn amount, not the entire limit.
- Funds can be drawn and repaid anytime within the approved limit.
- No fixed repayment schedule — repay when funds are available.
- Ideal for managing day-to-day cash flow fluctuations and unexpected expenses.
- If used excessively or for long periods, interest and fees can become expensive.

✓ Flexible credit facility
✓ Interest on used amount only
✓ No fixed repayment schedule
