# LC Buyer Decision Tree - LC Issuance

```mermaid
flowchart TD
    Start["Step 1 Manufacturing Buyer LC"] --> LCIssuance["LC Issuance feat={'is_product': 'true'}"]
    LCIssuance --> Complete["LC Issuance completed - buyer has issued LC to seller"]

    LCIssuance:::productBox
    classDef productBox fill:#e1f5fe,stroke:#01579b,stroke-width:2px,color:#000
```
