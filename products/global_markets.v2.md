# Global Markets

## Notes
- When the client needs to buy or sell a foreign currency, the base case is
  that they will do so using FX Spot transactions
- However, if they wish to hedge the FX volatility or
  directional risk, they should consider an FX Forward or an FX Option
- Some clients may only want to partially hedge their FX exposure. We must ask
  the proportion that they wish to hedge
- If the client is considering an FX Forward vs an FX Option: 
  the FX Forward is appropriate if the client is certain about 
  the date and amount of the foreign currency they require.
  Otherwise, they should use an FX Option
- If the client wants to hedge their Interest Rate risk, 
  they should consider an IRS or a CCS
- If the client is an importer, they may need to buy foreign currency 
  from the bank in order to purchase goods from their suppliers
- If the client is an exporter, they usually receive foreign currency 
  from their foreign customers and may need to sell this foreign currency 
  to the bank
- If the client is both an exporter and an importer, the foreign currency 
  that they pay and receive may cancel out each other and form a natural 
  hedge. So they won't need to use any of these FX products
- When we have identified an FX product to use, determine the actual
  currency required. Only some foreign currencies are supported by the bank.

## Assumptions about this bank and their clients
- Assume that we are working for a bank and clients whose local currency is MYR
- The bank only supports the major currencies + MYR, KRW and VND

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