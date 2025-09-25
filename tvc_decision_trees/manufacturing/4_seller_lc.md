# Letter of Credit Products - Seller Decision Tree (Manufacturing)

```mermaid
flowchart TD
    Start@{ label: "Step 4 Manufacturing Seller LC | cond={'is_seller':'true', 'is_lc':'true'}" } --> CheckPacking{"Need pre-shipment working capital?"}
    CheckPacking -- "Yes<br>feat={'needs_preshipment_capital':'true'}" --> ECRAvailable{"Is a government Export Credit Refinancing program available for this transaction?"}
    CheckPacking -- "No<br>feat={'needs_preshipment_capital':'false'}" --> PostShipment["Proceed to<br>Post-shipment"]
    ECRAvailable -- "No<br>feat={'ecr_program_available':'false'}" --> PackingCredit["Packing Credit<br>feat={'is_product':'true'}"]
    ECRAvailable -- "Yes<br>feat={'ecr_program_available':'true'}" --> ECRWant{"Does the client want to use the program (cheaper cost but with eligibility/paperwork)?"}
    ECRWant -- "Yes<br>feat={'wants_ecr_program':'true'}" --> ECRPreShip["Export Credit Refinancing Pre Ship<br>feat={'is_product':'true'}"]
    ECRWant -- "No<br>feat={'wants_ecr_program':'false'}" --> PackingCredit
    ECRPreShip --> PostShipment
    PackingCredit --> PostShipment
    PostShipment --> LCTypeCheck{"What type of LC<br>is the seller using?"}
    LCTypeCheck -- "Sight LC<br>feat={'lc_type':'sight'}" --> SightCalc["Calculate financing gap<br>with Sight LC formula"]
    LCTypeCheck -- "Usance LC<br>feat={'lc_type':'usance'}" --> UsanceCalc["Calculate financing gap<br>with Usance LC formula"]
    SightCalc --> SightFinanceCheck{"Does seller need financing based on gap calculation?"}
    UsanceCalc --> UsanceFinanceCheck{"Does seller need financing based on gap calculation?"}
    SightFinanceCheck -- "Yes<br>feat={'needs_postshipment_financing':'true'}" --> OnshoreCheck{"Need foreign currency funding?"}
    SightFinanceCheck -- "No<br>feat={'needs_postshipment_financing':'false'}" --> SightWait@{ label: "Wait until buyer's bank<br>pays at sight" }
    UsanceFinanceCheck -- "Yes<br>feat={'needs_postshipment_financing':'true'}" --> OnshoreCheckUsance{"Need foreign currency funding?"}
    UsanceFinanceCheck -- "No<br>feat={'needs_postshipment_financing':'false'}" --> UsanceWait@{ label: "Wait until maturity date<br>for buyer's bank to pay" }
    OnshoreCheck -- "Yes<br>feat={'needs_foreign_currency':'true'}" --> OnshoreFC["Onshore Foreign Currency Loan<br>feat={'is_product':'true'}"]
    OnshoreCheck -- "No<br>feat={'needs_foreign_currency':'false'}" --> SightComplete["Transaction completed"]
    OnshoreCheckUsance -- "Yes<br>feat={'needs_foreign_currency':'true'}" --> OnshoreFC2["Onshore Foreign Currency Loan<br>feat={'is_product':'true'}"]
    OnshoreCheckUsance -- "No<br>feat={'needs_foreign_currency':'false'}" --> UsanceComplete@{ label: "Transaction completed<br>at LC maturity when<br>buyer's bank pays" }
    OnshoreFC --> SightCompleteFC["Transaction completed"]
    OnshoreFC2 --> UsanceCompleteFC@{ label: "Transaction completed<br>at LC maturity when<br>buyer's bank pays" }
    SightWait --> SightCompleteWait["Transaction completed"]
    UsanceWait --> UsanceCompleteWait@{ label: "Transaction completed<br>at LC maturity when<br>buyer's bank pays" }

    Start@{ shape: stadium}
    PostShipment@{ shape: rect}
    SightWait@{ shape: rect}
    UsanceWait@{ shape: rect}
    UsanceComplete@{ shape: rect}
    UsanceCompleteFC@{ shape: rect}
    UsanceCompleteWait@{ shape: rect}
     PackingCredit:::productBox
     ECRPreShip:::productBox
     OnshoreFC:::productBox
     OnshoreFC2:::productBox
    classDef productBox fill:#e1f5fe,stroke:#01579b,stroke-width:2px,color:#000
```
