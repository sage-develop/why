# LC Transfer vs Back-to-Back LC Decision Tree

```mermaid
flowchart TD
    Start(["Step 1 Manufacturing Seller LC"]) --> Q1{"Is seller a middleman who doesn't make goods?"}
    Q1 -- "Yes feat={'is_middleman': 'true'}" --> Q2{"Is LC transferable?"}
    Q1 -- "No feat={'is_middleman': 'false'}" --> End1["Not applicable - seller produces own goods"]
    Q2 -- "Yes feat={'lc_transferable': 'true'}" --> Q3{"Want to transfer LC to supplier?"}
    Q2 -- "No feat={'lc_transferable': 'false'}" --> P1["Back-to-Back LC feat={'is_product': 'true'}"]
    Q3 -- "Yes feat={'wants_transfer': 'true'}" --> P2["Transferable LC
feat={'is_product': 'true'}"]
    Q3 -- "No feat={'wants_transfer': 'false'}" --> Q4{"Need more control OR different LC terms?"}
    Q4 -- "Yes feat={'needs_control': 'true'}" --> P1
    Q4 -- "No feat={'needs_control': 'false'}" --> End2["Use standard LC processes"]
    P2 --> End3["LC transferred to supplier"]
    P1 --> End4["New LC issued to supplier using original LC as security"]

    P1:::productBox
    P2:::productBox
    classDef productBox fill:#e1f5fe,stroke:#01579b,stroke-width:2px,color:#000
```
