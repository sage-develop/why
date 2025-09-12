# Trade Finance Products v3

## Trade Collections

### Sellers - Pre-shipment

#### 16. Packing Credit for Exporters

This is a pre-shipment financing for sellers

- Provides sellers with an upfront loan to prepare and ship goods.
- The seller repays the bank from the buyer’s payment under D/P (pays now) or, if D/A (pays later), from funds received at/after the due date.
- Use when the seller needs **pre-shipment working capital**.
- Useful for large orders, urgent shipments, or when the seller's cash flow is insufficient.
- Enables sellers to take on new orders without waiting for previous payments.
- After selecting this product, the seller can also use other Trade Collection products, including post-shipment options.

### Sellers - Post-shipment

#### 12. Outward Bill for Collection

This is a post-shipment service for sellers

- This is the base Trade Collection product for sellers.
- This product is mandatory when the buyer and seller have agreed to settle the trade using a Trade Collection.
- The bank helps sellers send trade documents to the buyer's bank in exchange for payment.

#### 13. Bill Receivable under Outward Bill for Collection

This is a post-shipment finaning for sellers

- Use when the buyer and seller agreed on **D/A (Documents against Acceptance)**.
- Provides financing immediately after documents are presented, even though payment is deferred until maturity.
- Calculate the financing gap with the D/A formula to know if the seller needs financing.
- If the seller needs financing, choose Bill Receivable under Collection (the bank discounts the accepted draft), if not, wait until maturity for the buyer to pay.
- Use when the seller wants immediate payment after documents are presented under D/A Collection.
- The transaction is completed at maturity when the buyer pays under D/A.

### Buyers - Pre-shipment

#### 10. Inward Bill for Collection

This is a service for buyers.

- This is the base Trade Collection product for buyers.
- This product is mandatory when the buyer and seller have agreed to settle the trade using a Trade Collection.
- The bank helps buyers receive and process collection documents from sellers.
- Use when B/L has arrived at the buyer's bank.
- Can continue choosing other Collection product by determining which payment term **the buyer is using D/P or D/A**.

#### 11. P/N under Bill for Collection (Buyer)

This is a financing for buyers.

- Can be used once the original B/L has been received by the collecting bank handling the documents.
- Use when buyer needs goods but lacks immediate payment capability.
- Must determine whether the collection is **D/P (Documents against Payment) or D/A (Documents against Acceptance)**.
- If the buyer is using D/P, separately calculate the financing gap using the D/P formula.
- If the buyer is using D/A, separately calculate the financing gap using the D/A formula.
- Determine if the buyer needs financing from the financing gap result.
- If financing is needed, the collecting bank may release the B/L using P/N under Bill for Collection (Buyer).
- Continue the flow, with **whose name the original B/L is issued under**, if it's under the bank's name, needs to combine with Endorsement.
- If Shipping Guarantee Issuance is used, the buyer needs to exchange B/L for the shipping guarantee to complete the flow.

#### 18. Shipping Guarantee Issuance

This is a service for buyers.

- When **the buyer's bank haven't yet received the original B/L**, but **the buyer wants to claims the goods immediately**, use Shipping Guarantee Issuance.
- If **the buyer's bank haven't yet received the original B/L** but the buyer doesn't want to claims the goods immediately, continue the base flow
- The buyer uses Shipping Guarantee to claim the goods immediately (not after exchange B/L with the Shipping Guarantee).
- Then wait for the original B/L to arrive, continue the base flow to use Inward Bill for Collection.
- Using Shipping Guarantee Issuance will affect the end of all the flow.
- In other product's flow, if a Shipping Guarantee is issued in the buyer’s name, use it to exchange for the Shipping Guarantee.
- In other product's flow, if a Shipping Guarantee is issued in the buyer’s bank’s name, the buyer must also use Endorsement Services.

#### 19. Endorsement Services

This is a service for buyers.

- Use when the buyer and seller have agreed to settle the trade using a Trade Collection.
- Use when **the B/L is issued under the buyer’s bank’s name** and the buyer needs to claim the goods.
- The buyer’s bank endorses the B/L, transferring ownership of the goods to the buyer.
- Required for the buyer to take delivery when the B/L is not in their name.
- The original B/L must have arrived before this service can be used.

- Make a new decision diagram for seller pre/post-shipment products.
- The buyer is already using the Trade Collection payment method.
- If the buyer can continue choosing other products, continue the flow.
- Consider every single bullet point below each product in @trade_finance_product.v3_collections.md.

## Buyer

- Make a new decision diagram for buyer pre-shipment pro products.
- The buyer is already using the Trade Collection payment method.
- If the buyer can continue choosing other products, continue the flow.

## Seller

- Make new decision diagrams for seller pre-shipment and post-shipment, the flow starts from seller pre-shipment diagram, then continue on post-shipment diagram.
- The seller is already using the Trade Collection payment method.
- If the seller can continue choosing other products, continue the flow.

## Base Prompt

- Consider every single bullet point below each product in @trade_finance_product.v3_collections.md.
- The highlighted sentences must be a decision point.
- If it's the end of the flow, add a sentence to conclude the flow.
- Only the product will be inside the colored box (all the same color). Any box that doesn't say the product's name will have no color.
- In the product box, only put in the full product name, no extra explanation.
- A product should appear once in the decision diagram.
- Combine duplicate decision points if possible.
- Ask one question at a decision point.
