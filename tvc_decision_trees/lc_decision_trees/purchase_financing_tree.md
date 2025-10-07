## Prompt

Create a Mermaid decision tree for Trade Finance Purchase by asking the following questions

- Does the client generally finance their purchases?
  If no, then "No opportunity"
- Does the client have a financing gap based on Cash Conversion Cycle?
  If no, then "Not eligible for Purchase Financing"
- Who has the title to the goods on the B/L?
  If the answer if Bank, then Opportunity: Trust Receipt Loan, P/N under Letter of Credit, Invoice Financing
  If the answer is the buyer, then Opportunity: P/N under Letter of Credit, Invoice Financing
  If the answer is not sure, then Opportunity: P/N under Letter of Credit, Invoice Financing

## Decision Tree

```mermaid
%% Trade Finance Purchase Financing Decision Tree
flowchart TD
    Start[Start: Trade Purchase Financing] --> Context[Context: Client is buying goods and may need<br>financing to pay suppliers before<br>receiving payment from their customers]
    Context -->A{Does the client generally finance their purchases?}
    A -->|No| B[No opportunity]
    A -->|Yes| C{Does the client have a financing gap based on Cash Conversion Cycle?}

    C -->|No| D[Not eligible for Purchase Financing]
    C -->|Yes| E{Who has title to the goods?}
    E -->|Bank| F[Opportunity: Trust Receipt Loan, P/N under Letter of Credit, Invoice Financing]
    E -->|Buyer| G[Opportunity: P/N under Letter of Credit, Invoice Financing]
    E -->|Not sure| H[Opportunity: P/N under Letter of Credit, Invoice Financing]
```
