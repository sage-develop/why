# Overdraft Decision Tree

# Prompt

Create a non-product decision tree as mermaid code inside non_trade_products.md. Only see Overdraft bullet points in non_trade_product.md file

## Decision Flow

```mermaid
flowchart TD
    Start(["Start: Non-Trade Transaction<br>(Overdraft)"]) --> Context["Context: The client may face cash flow gaps or urgent funding needs unrelated to trade."]

    Context --> Q0{"Does the client have<br>sufficient funds for<br>their business needs?"}
    Q0 -- Yes --> NoLoan["No financing needed"]
    Q0 -- No --> Q1{"Does the client need<br>flexible access to funds<br>for cash flow gaps?"}
    Q1 -- Yes --> Q2{"Do they prefer no fixed<br>repayment schedule?"}
    Q1 -- No --> NotSuitable1["Consider: Term Loan<br>for fixed amounts"]
    Q2 -- Yes --> Warning{"Warning: Will they avoid<br>excessive or long-term<br>usage to prevent high costs?"}
    Q2 -- No --> NotSuitable2["Opportunity: Term Loan<br>with structured payments"]
    Warning -- Yes --> Overdraft["Opportunity: Overdraft<br>✓ Flexible credit facility<br>✓ Interest on used amount only<br>✓ No fixed repayment schedule"]
    Warning -- No --> Caution["Caution: Overdraft may become<br>expensive - consider alternatives<br>or usage guidelines"]
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
