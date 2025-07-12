# Global Markets

## Notes
- FX Spot transactions are suitable when the client is willing to take on FX risk
- If the client is wants to hedge their FX risk, they should consider either
  an FX Forward or an FX Option
- If the client is considering an FX Forward vs an FX Option: the former is appropriate
  if the client is certain about the date they require the foreign currency. Otherwise,
  they should use an FX Option
- If the client wants to hedge their Interest Rate risk, they should consider
  an IRS or a CCS
- If the client is an importer, they may need to buy foreign currency from the bank
  in order to purchase goods from their suppliers
- If the client is an exporter, they usually receive foreign currency from their
  foreign customers and may need to sell this foreign currency to the bank


## Products
### 1. FX Spot - Bank Buys
### 2. FX Spot - Bank Sells
### 3. FX Forward Contract - Bank Buys
### 4. FX Forward Contract - Bank Sells
### 5. FX Call Option
### 6. FX Put Option
### 7. Interest Rate Swap
### 8. Cross Currency Swap


## Prompt

"""
Input: only this file
Prompt:
Given the notes about some Global Markets products,
give me a decision tree to determine what products 
are suitable for my client
"""
