# Trade Finance Products v3

## Letter of Credit

### Sellers - Pre-shipment

#### 2. Letter of Credit Advising

This is a pre-shipment service for Sellers

- This is the base LC product for sellers in **international and domestic** trade.
- This product is mandatory when the buyer and seller have agreed to settle the trade using a Letter of Credit.

#### 3. Letter of Credit Confirmation

This is a pre-shipment service for sellers

- First, check if the seller is using a Domestic or International transaction.
- If the seller is doing Domestic transaction, are they worried about a **counterparty risk**, if yes, the seller can use Letter of Credit Confirmation.
- If the seller is doing International transaction, are they worried about a **counterparty sovereign risk**, if yes, the seller can use Letter of Credit Confirmation.
- If the seller has no concern about the counter party risk or counter party sovereign risk, the seller can continue to choose other products.

#### 4. Assignment of Proceeds under Letter of Credit

This is pre-shipment service for sellers

- Use if the seller wants to **redirect payments** to third parties involved in fulfilling the order.
- After selecting this product, the seller can also continue to choose others.

#### 5. Letter of Credit Transferring

For the Seller or trading company that acts as a **middleman** and doesn't actually make the goods.

- Only available if the LC is transferrable.
- If the LC is not transferrable, the seller can consider using Assignment of Proceeds under Letter of Credit instead or pay the supplier directly.
- Suitable for middlemen who do not manufacture or ship goods but want to manage the trade flow and maintain control.
- If the seller is a middleman and chooses this product, the flow ends here.

#### 16. Packing Credit for Exporters

This is a pre-shipment loan for sellers

- Provides sellers with an upfront loan to prepare and ship goods.
- The loan is repaid once the seller receives payment for the goods.
- Use when the seller needs **pre-shipment working capital** to buy raw materials, cover production costs, packaging, or shipment.
- Useful for large orders, urgent shipments, or when the exporter’s cash flow is insufficient.
- Enables exporters to take on new orders without waiting for previous payments.
- After selecting this product, the seller can also use other LC products, including post-shipment options.

<!-- LC Seller Pre-shipment Prompt
<!-- - Make a new decision diagram for seller pre-shipment product @trade_finance_products.v3.md
- Consider every single the bullet points below each product
- The highlighted sentences must be a decision point.
- If its the end of the flow, add a sentence to conclude the flow
- If the seller can continue choosing other product continue the flow
- Only the product will be inside the colored box (all same color) any box that doesn't say product's name will have no color
- The seller is already using LC payment method
- Combine duplicate decision points if possible -->

### Sellers - Post-shipment

#### 8. Export Bill under Letter of Credit

This is a post-shipment service for sellers

- Use when the buyer and seller have agreed to settle the trade using a **Sight LC**.
- The loan is used when the seller wants **immediate payment** under a Sight LC.
- Calculate financing gap with Sight LC formula to know if the seller needs financing.
- If the seller needs financing, choose Export Bill under Letter of Credit (Bank advances funds once docs presented), if not, wait until the buyer's bank pays at sight.
- The bank advances funds once compliant documents are presented then the transaction is completed.

#### 9. Bill Receivable under Letter of Credit

This is a post-shipment loan for sellers

- Use when the buyer and seller agreed on **Usance LC**
- Provides financing immediately after documents are presented, even though payment is deferred until maturity.
- Calculate financing gap with Usance LC formula to know if the seller needs financing.
- If the seller needs financing, choose Bill Receivable under Letter of Credit (Bank discounts usance bill), if not, wait until maturity date for buyer’s bank to pay.
- Use when the seller wants immediate payment after documents are presented under Usance LC.
- Use when the seller wants **post-shipment working capital**.
- The transaction is completed at LC maturity when the buyer’s bank pays.

<!-- LC Seller Post-shipment Prompt -->
<!-- - Make a new seller post-shipment products decision diagram
- Consider all the bullet points below each 'seller - post-shipment' product in @trade_finance_products.v3.md
- If its the end of the flow, add a sentence to conclude the flow
- If the seller can continue choosing other product, let the flow continue
- Only the product will be inside the colored box (all same color) any box that doesn't say product's name will have no color
- In the product box, only put in full product name, no extra explanation
- The seller is already using LC payment method timing is post-shipment
- A product should appear once in the decision diagram.
- Ask one question at a decision point. -->

### Buyers - Pre-shipment

#### 1. Letter of Credit Issuance

This is a pre-shipment service for Buyers

- This is the base LC product for sellers in **international and domestic** trade.
- This product is mandatory when the buyer and seller have agreed to settle the trade using a Letter of Credit.

#### 6. P/N under Letter of Credit (Buyer)

This is financing for buyers.

- Can be used only if the original B/L is already at the buyer's bank.
- The **B/L also needs to be issued under the buyer's name**.
- Must determine if the buyer is using **Sight LC or Usance LC**.
- If the buyer is using Sight LC, separately calculate the financing gap using the Sight LC formula.
- If the buyer is using Usance LC, separately calculate the financing gap using the Usance LC formula.
- Determine if the buyer needs financing from the financing gap result.
- If financing is needed, use P/N under Letter of Credit (Buyer).
- If Shipping Guarantee Issuance is used, the buyer needs to exchange B/L for the shipping guarantee to complete the flow.

#### 7. Trust Receipt Loan under Letter of Credit

This is financing for buyers.

- Can be used only if the original B/L is already at the buyer's bank.
- The **original B/L also needs to be issued under the buyer's bank's name**.
- Must determine if the buyer is using **Sight LC or Usance LC**.
- If the buyer is using Sight LC, separately calculate the financing gap using the Sight LC formula.
- If the buyer is using Usance LC, separately calculate the financing gap using the Usance LC formula.
- Determine if the buyer needs financing from the financing gap result.
- If financing is needed, use Trust Receipt Loan under Letter of Credit.
- After using Trust Receipt Loan under Letter of Credit, the buyer still needs to transfer goods ownership to themselves using Endorsement Services.
- If Shipping Guarantee Issuance is used, the buyer needs to exchange B/L for the shipping guarantee to complete the flow.

#### 18. Shipping Guarantee Issuance

This is a service for buyers.

- Use when **the buyer's bank haven't yet received the original B/L**.
- The buyer uses Shipping Guarantee to claim the goods immediately (not after exchange B/L with the Shipping Guarantee).
- When the original B/L has arrived, continue the flow checking whose name the B/L is issued in.
- Using Shipping Guarantee Issuance will affect the end of all other products' flow.
- If a Shipping Guarantee is issued in the buyer’s name, use it to exchange for the Shipping Guarantee.
- If a Shipping Guarantee is issued in the buyer’s bank’s name, the buyer must also use Endorsement Services.

#### 19. Endorsement Services

This is a service for buyers.

- Note: The buyer’s bank endorses the B/L, transferring ownership of the goods to the buyer.
- The buyer can only claim the goods after the B/L is under the buyer's name.
- The original B/L must have arrived at the buyer's bank before this service can be used.
- Use when the buyer wants to get the ownership of the goods but **the B/L is issued under the buyer’s bank’s name**.
- Can be combined with a Trust Receipt Loan under Letter of Credit if the buyer needs the goods immediately but does not have the cash to pay upfront.

<!-- LC Buyer Pre-shipment Prompt
- Please make a new decision diagram for buyer preshipment product @trade_finance_products.v3.md
- Consider every single the bullet points below each product
- The highlighted sentences must be a decision point.
- If its the end of the flow, add a sentence to conclude the flow
- If the buyer can continue choosing other product continue the flow
- Only the product will be inside the colored box (all same color) any box that doesn't say product's name will have no color
- The buyer is already using LC payment method
- Combine duplicated decision points if possible -->
