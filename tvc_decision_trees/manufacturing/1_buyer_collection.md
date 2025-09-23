# Trade Collection - Buyer Decision Tree (Inward Bill for Collection)

```mermaid
flowchart TD
    A(["Step 1 Manufacturing Buyer Collection"]) --> B@{ label: "The original B/L arrived at buyer's bank<br/>" }
    B --> D["Inward Bill for Collection<br/>feat={is_product: true}"]

    B@{ shape: diamond}
    D:::productBox
    classDef productBox fill:#e1f5fe,stroke:#01579b,stroke-width:2px
```
