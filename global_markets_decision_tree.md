## Global Markets Product Decision Tree

```
START: Client Assessment
│
├── Does client have FX exposure?
│   ├── NO → Consider Interest Rate products if applicable
│   │   └── Does client have Interest Rate risk?
│   │       ├── YES → Interest Rate Swap (IRS)
│   │       └── NO → No Global Markets products needed
│   │
│   └── YES → Continue to FX Assessment
│       │
│       ├── What is client's risk appetite for FX?
│       │   ├── WILLING TO TAKE FX RISK → FX Spot
│       │   │   ├── Client Type?
│       │   │   │   ├── IMPORTER → FX Spot - Bank Sells
│       │   │   │   └── EXPORTER → FX Spot - Bank Buys
│       │   │
│       │   └── WANTS TO HEDGE FX RISK → Choose hedging strategy
│       │       │
│       │       ├── Is client certain about the date they require FX?
│       │       │   ├── YES → FX Forward
│       │       │   │   ├── Client Type?
│       │       │   │   │   ├── IMPORTER → FX Forward - Bank Sells
│       │       │   │   │   └── EXPORTER → FX Forward - Bank Buys
│       │       │   │
│       │       │   └── NO → FX Options
│       │       │       ├── Client Type?
│       │       │       │   ├── IMPORTER → FX Call Option (right to buy)
│       │       │       │   └── EXPORTER → FX Put Option (right to sell)
│       │
│       └── Does client also have Interest Rate risk?
│           ├── YES → Cross Currency Swap (CCS)
│           └── NO → Use FX products as determined above
```

## Decision Logic Summary

### 1. **FX Spot Products**
- **Use when:** Client willing to take FX risk
- **FX Spot - Bank Sells:** For importers needing foreign currency
- **FX Spot - Bank Buys:** For exporters selling foreign currency

### 2. **FX Forward Products**
- **Use when:** Client wants to hedge FX risk and is certain about the date they require foreign currency
- **FX Forward - Bank Sells:** For importers with future payment obligations
- **FX Forward - Bank Buys:** For exporters with future receivables

### 3. **FX Options**
- **Use when:** Client wants to hedge FX risk but uncertain about the date they require foreign currency
- **FX Call Option:** For importers (right to buy foreign currency)
- **FX Put Option:** For exporters (right to sell foreign currency)

### 4. **Interest Rate Products**
- **Interest Rate Swap (IRS):** For clients with pure interest rate risk
- **Cross Currency Swap (CCS):** For clients with both FX and interest rate risk
