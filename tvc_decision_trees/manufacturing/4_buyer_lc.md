# LC Products Decision Diagram - Buyer (Trust Receipt, P/N & OFCL)

```mermaid
flowchart TD
    Start(["Step 4 Manufacturing Buyer LC | cond={'is_buyer':'true', 'is_lc':'true'}"]) --> Q1{"Is it Sight LC or Usance LC?"}
    Q1 -- "lc_type={'sight'}" --> End1["Calculate financing gap using Sight LC formula"]
    Q1 -- "lc_type={'usance'}" --> End2["Calculate financing gap using Usance LC formula"]
    End1 --> Q2{"Does buyer need financing based on gap calculation?"}
    End2 --> Q2
    Q2 -- "needs_financing={'true'}" --> Q3{"Who has title to the goods on the B/L?"}
    Q3 -- "bl_title_holder={'bank'}" --> P1["Trust Receipt Loan under Letter of Credit | feat={'is_product': 'true'}"]
    Q3 -- "bl_title_holder={'buyer'}" --> P2["P/N under Letter of Credit | feat={'is_product': 'true'}"]
    P1 --> Q4{"Does buyer need foreign currency financing?"}
    P2 --> Q4
    Q4 -- "needs_fx_financing={'true'}" --> P3["Onshore Foreign Currency Loan | feat={'is_product': 'true'}"]
    Q4 -- "needs_fx_financing={'false'}" --> End3["Financing completed - buyer can proceed with trade"]
    P3 --> End4["Financing with OFCL completed - buyer can proceed with trade"]

     P1:::productBox
     P2:::productBox
     P3:::productBox
    classDef productBox fill:#e1f5fe,stroke:#01579b,stroke-width:2px
```
