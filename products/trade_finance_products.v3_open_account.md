# Trade Finance Products v3

## Trade Collections

### Sellers - Pre-shipment

- none

### Sellers - Post-shipment

#### 15. P/N under Open Account (Seller)

This is a post-shipment financing for sellers

- Use when the seller doesn’t want to wait until due date, they can go to their bank for immediate financing using P/N under Open Account (Seller).

### Buyers - Pre-shipment

#### 14. P/N under Open Account - Buyer

This is a pre-shipment financing for buyers.

- Use P/N under Open Account - Buyer if the buyer can’t pay the seller on due date.

## Buyer

- Make new decision diagram for buyer products.
- The buyer is already using the Open Account payment method.
- If the buyer can continue choosing other products, continue the flow.

## Seller

- Make new decision diagram for seller post-shipment products.
- The seller is already using the Open Account payment method.
- If the seller can continue choosing other products, continue the flow.

## Base Prompt

- Consider every single bullet point below each product in @trade_finance_product.v3_open_account.md.
- The highlighted sentences must be a decision point.
- If it's the end of the flow, add a sentence to conclude the flow.
- Only the product will be inside the colored box (all the same color). Any box that doesn't say the product's name will have no color.
- In the product box, only put in the full product name, no extra explanation.
- A product should appear once in the decision diagram.
- Combine duplicate decision points if possible.
- Ask one question at a decision point.
