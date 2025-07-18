## Global Markets Product Decision Tree

```
START: Client Assessment
│
├── Does client have FX exposure/risk?
│   ├── NO → Consider Interest Rate products
│   │   └── Does client have Interest Rate risk?
│   │       ├── YES → Interest Rate Swap (IRS)
│   │       └── NO → No Global Markets products needed
│   │
│   └── YES → What is client's FX risk appetite?
│       │
│       ├── WILLING TO TAKE FX RISK → FX Spot
│       │   └── Client Type?
│       │       ├── IMPORTER → FX Spot - Bank Sells
│       │       │   (Client buys foreign currency from bank)
│       │       └── EXPORTER → FX Spot - Bank Buys
│       │           (Client sells foreign currency to bank)
│       │
│       └── WANTS TO HEDGE FX RISK → Choose hedging strategy
│           │
│           ├── Is client certain about the date they require foreign currency?
│           │   ├── YES → FX Forward Contract
│           │   │   └── Client Type?
│           │   │       ├── IMPORTER → FX Forward Contract - Bank Sells
│           │   │       └── EXPORTER → FX Forward Contract - Bank Buys
│           │   │
│           │   └── NO → FX Options
│           │       └── Client Type?
│           │           ├── IMPORTER → FX Call Option
│           │           │   (Right to buy foreign currency)
│           │           └── EXPORTER → FX Put Option
│           │               (NOT AVAILABLE - Contact your RM)
│           │
│           └── Does client also have Interest Rate risk?
│               ├── YES → Cross Currency Swap (CCS)
│               │   (Hedges both FX and Interest Rate risk)
│               └── NO → Use FX products as determined above
```

## Decision Logic Summary

### 1. **FX Spot Products**
- **Use when:** Client is willing to take on FX risk
- **FX Spot - Bank Sells:** For importers who need to buy foreign currency to purchase goods from suppliers
- **FX Spot - Bank Buys:** For exporters who receive foreign currency from customers and need to sell it

### 2. **FX Forward Contract Products**
- **Use when:** Client wants to hedge FX risk AND is certain about the date they require foreign currency
- **FX Forward Contract - Bank Sells:** For importers with future payment obligations
- **FX Forward Contract - Bank Buys:** For exporters with future receivables

### 3. **FX Options**
- **Use when:** Client wants to hedge FX risk BUT is uncertain about the date they require foreign currency
- **FX Call Option:** For importers (right to buy foreign currency)
- **FX Put Option:** NOT AVAILABLE at this bank - advise client to "Contact your RM"

### 4. **Interest Rate Products**
- **Interest Rate Swap (IRS):** For clients with Interest Rate risk who want to hedge
- **Cross Currency Swap (CCS):** For clients with both FX and Interest Rate risk

## Available Products
1. FX Spot - Bank Buys
2. FX Spot - Bank Sells
3. FX Forward Contract - Bank Buys
4. FX Forward Contract - Bank Sells
5. FX Call Option
6. Interest Rate Swap
7. Cross Currency Swap

## Important Notes
- Unlike some other banks, this bank does not provide an FX Put Option
- If a client requires an FX Put Option, they should "Contact your RM"
- Importers typically need to buy foreign currency from the bank
- Exporters typically receive foreign currency and may need to sell it to the bank 