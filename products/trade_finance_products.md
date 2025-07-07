# Trade Finance Products

## 1. Import P/N
- **Description**: This is a generic pre-shipment trade loan specifically structured to 
  finance imports, transactionally supported by a promissory note executed by the borrower. 
  Proceeds of the drawdown are paid directly to the exporter.
- **Family**: Trade
- **Type**: Trade Finance
- **Risk**: Medium to low, if applied to documentary collections and letters of credit where 
  title of the goods can be consigned to the bank.
- **Tags**: imports, financing, foreign currency, credit terms, cash conversion cycle, 
  open account, letter of credit, collections, short term, bridging finance, P-note, 
  shipment, goods clearance, supply chain, trade, purchase finance, pre-shipment
- **Segmentation**: generic, importers
- **Use Case**: working capital financing

## 2. Import P/N under Open Account
- **Description**: This is a generic pre-shipment trade loan specifically structured to 
  finance imports on open account only, transactionally supported by a promissory note 
  executed by the borrower. Proceeds of the drawdown are paid directly to the exporter.
- **Family**: Trade
- **Type**: Trade Finance
- **Risk**: Medium to high, since for open account the underlying goods may be consigned 
  directly to the buyer/importer
- **Tags**: OA (Open Account), imports, P-note, financing, short term, bridging finance, 
  credit, shipment, trade, supply chain, goods clearance, purchase finance, pre-shipment
- **Segmentation**: generic, importers
- **Use Case**: working capital financing

## 3. Export P/N under Open Account
- **Description**: This is a generic post-shipment trade loan specifically structured to 
  finance exports on open account only, transactionally supported by a promissory note 
  executed by the borrower. Proceeds of the drawdown are paid directly to the 
  exporter/borrower.
- **Family**: Trade
- **Type**: Trade Finance
- **Risk**: Medium to high, since for open account the underlying goods may be consigned 
  directly to the buyer/importer and bank has no control. Bank also generally does not 
  have a relationship with the buyer/importer.
- **Tags**: open account, exports, P-note, financing, short term, bridging finance, credit, 
  shipment, trade, supply chain, purchase finance, post-shipment, advance
- **Segmentation**: generic, exporters
- **Use Case**: working capital financing

## 4. Packing Credit
- **Description**: Pre-shipment financing for exporters/sellers against either a letter of 
  credit or purchase order. Percentage of financing is programmable.
- **Family**: Trade
- **Type**: Trade Finance
- **Risk**: Medium to high. Pre-shipment financing is fully dependent on the borrower's 
  ability to complete performance. Once performance is completed, the risk should be 
  lowered since only a collections task remains, if it is against a letter of credit where 
  payment is guaranteed. If it is against a purchase order, the risks may be higher as 
  payment is directly from the buyer.
- **Tags**: open account, purchase order, letter of credit, imports, advance, financing, 
  short term, bridging finance, credit, shipment, trade, supply chain, goods clearance, 
  purchase finance, pre-shipment
- **Segmentation**: generic, importers
- **Use Case**: working capital financing

## 5. Inward Bill for Collection
- **Description**: This is a collections service where the bank only acts as an agent for 
  the exporter to collect payment or acceptance and release trade documents to the 
  importer/buyer
- **Family**: Trade
- **Type**: Services
- **Risk**: Low. No financing risk, only operational risk is involved.
- **Tags**: collections, imports, shipment, trade, supply chain, goods clearance, 
  shipping guarantee
- **Segmentation**: generic, importers
- **Use Case**: trade services

## 6. Import P/N under Bill for Collection
- **Description**: This is a generic pre-shipment trade loan specifically structured to 
  finance imports on import collections only, transactionally supported by a promissory 
  note executed by the borrower. Proceeds of the drawdown are paid directly to the 
  remitting bank on behalf of the exporter.
- **Family**: Trade
- **Type**: Trade Finance
- **Risk**: Medium, since for collections the title documents for the underlying goods are 
  controlled by the banks
- **Tags**: collections, imports, P-note, financing, short term, bridging finance, credit, 
  shipment, trade, supply chain, goods clearance, purchase finance, pre-shipment
- **Segmentation**: generic, importers
- **Use Case**: working capital financing

## 7. Outward Bill for Collection
- **Description**: This is a collections service where the bank only acts as an agent for 
  the exporter send the trade documents to the collecting bank/importer in exchange for 
  payment or acceptance
- **Family**: Trade
- **Type**: Services
- **Risk**: Low. No financing risk, only operational risk is involved.
- **Tags**: collections, exports, shipment, trade, supply chain, goods clearance, 
  shipping guarantee
- **Segmentation**: generic, importers
- **Use Case**: trade services

## 8. Bill Receivable under Outward Bill for Collection
- **Description**: This is a trade loan to finance an outward collection bill, to be 
  liquidated with the proceeds of the collection upon receipt of payment from the 
  collecting bank/importer. Can be with or without recourse financing.
- **Family**: Trade
- **Type**: Financing
- **Risk**: High. Usual financing risk generally with recourse only to the exporter.
- **Tags**: collections, exports, shipment, trade, supply chain, financing, export advance, 
  cash flow easing
- **Segmentation**: generic, exporters
- **Use Case**: trade financing

## 9. Packing Credit
- **Description**: Pre-shipment financing for importers/sellers against an inward 
  collection bill. Percentage of financing is programmable but usually for the total value 
  of the collection bill.
- **Family**: Trade
- **Type**: Trade Finance
- **Risk**: Medium to high. Pre-shipment financing is fully dependent on the borrower's 
  ability to complete performance. Once performance is completed, the risk should be 
  lowered since only a collections task remains. However, if the sale is against a letter 
  of credit where payment is guaranteed, the collection risk will be small. If it is 
  against a purchase order, the risks may be higher as payment is directly from the buyer.
- **Tags**: collections, purchase order, letter of credit, imports, advance, financing, 
  short term, bridging finance, credit, shipment, trade, supply chain, goods clearance, 
  purchase finance, pre-shipment
- **Segmentation**: generic, importers
- **Use Case**: working capital financing

## 10. Letter of Credit Issuance/Amendment
- **Description**: Issuance of an undertaking by the bank to make payment upon satisfaction 
  of terms and conditions of a cross border/foreign currency letter of credit
- **Family**: Trade
- **Type**: Trade Services
- **Risk**: Low to medium. A letter of credit is an undertaking by a bank to pay regardless 
  of whether the applicant is able to make payment or not. As such, principal 
  responsibility to pay still lies with the issuing bank.
- **Tags**: purchase order, letter of credit, L/C, imports, advance, financing, short term, 
  bridging finance, credit terms, shipment, trade, supply chain, goods clearance, 
  usance bill
- **Segmentation**: generic, importers
- **Use Case**: working capital financing

## 11. Domestic Letter of Credit Issuance/Amendment
- **Description**: Issuance of an undertaking by the bank to make payment upon satisfaction 
  of terms and conditions of a domestic/local currency letter of credit
- **Family**: Trade
- **Type**: Trade Services
- **Risk**: Low to medium. A letter of credit is an undertaking by a bank to pay regardless 
  of whether the applicant is able to make payment or not. As such, principal 
  responsibility to pay still lies with the issuing bank.
- **Tags**: purchase order, letter of credit, L/C, imports, advance, financing, short term, 
  bridging finance, credit terms, shipment, trade, supply chain, goods clearance, 
  usance bill
- **Segmentation**: generic, importers
- **Use Case**: working capital financing

## 12. Shipping Guarantee Issuance
- **Description**: Bank guarantee issued to a shipping company for the releases of goods, 
  in the absence of a bill of lading or transport document, e.g. airway bill.
- **Family**: Trade
- **Type**: Trade Services
- **Risk**: High. A shipping guarantee is an undertaking by a bank to pay the beneficiary 
  regardless of claims value, as the guarantee is issued without a value cap.
- **Tags**: letter of credit, L/C, collections, imports, goods clearance
- **Segmentation**: generic, importers
- **Use Case**: working capital financing

## 13. Delivery Order Endorsement
- **Description**: A trade service to endorse a title/transport document to an importer for 
  the purpose of clearing goods.
- **Family**: Trade
- **Type**: Trade Services
- **Risk**: High. An endorsement to the importer will enable the clearance of goods, thus 
  causing the bank to lose control over the goods as collateral. Bank will need to rely on 
  other security arrangements to secure the transaction.
- **Tags**: letter of credit, L/C, collections, delivery order, D/O, imports, goods clearance
- **Segmentation**: generic, importers/domestic buyers
- **Use Case**: working capital financing

## 14. Trust Receipt under Letter of Credit
- **Description**: A short term trade loan provided to pay against a letter of credit, 
  whereby the goods are released by the bank under trust to the applicant/importer, for 
  the purpose of sales conversion and proceeds used to repay the LC.
- **Family**: Trade
- **Type**: Trade Financing
- **Risk**: High. A trust receipt loan is provided to an importer with a release of the 
  underlying goods for the purpose of sales conversion, thus causing the bank to release 
  ownership of the goods.
- **Tags**: letter of credit, L/C, collections, imports, goods clearance, trust receipt, TR, 
  trade loan, advance, trade financing
- **Segmentation**: generic, importers
- **Use Case**: working capital financing

## 15. P/N under Domestic Letter of Credit
- **Description**: A trade loan provided against the issuance of a promissory note by the 
  borrower, for the purpose of paying off a domestic LC.
- **Family**: Trade
- **Type**: Trade Financing
- **Risk**: High. Financing the payment of an LC with an added security of a promissory 
  note issued by the borrower.
- **Tags**: letter of credit, L/C, collections, imports, goods clearance, trade loan, 
  financing, PN, promissory note, advance
- **Segmentation**: generic, importers
- **Use Case**: working capital financing

## 16. Letter of Credit Advising/Amendment Advising
- **Description**: Trade service to authenticate and advise the issuance of a letter of 
  credit to a beneficiary
- **Family**: Trade
- **Type**: Trade Services
- **Risk**: Low. Only operational risk of performing authentication of the instrument prior 
  to advising the beneficiary.
- **Tags**: letter of credit, L/C, exports, advising, exporters, usance
- **Segmentation**: generic, exporters
- **Use Case**: working capital financing

## 17. Letter of Credit Confirmation
- **Description**: An undertaking by the bank to pay an exporter on an LC issued by 
  another issuing bank once terms and conditions of the LC are complied with
- **Family**: Trade
- **Type**: Trade Services
- **Risk**: Medium. The undertaking to pay an exporter is predicated on the risk taken on 
  the issuing bank. Generally a relatively safe transaction depending on the credit rating 
  of the issuing bank.
- **Tags**: letter of credit, L/C, exports, confirmation, sovereign risk, cross border risk, 
  bank risk
- **Segmentation**: generic, exporters
- **Use Case**: working capital financing

## 18. Letter of Credit Transferring
- **Description**: A trade service to transfer a letter of credit to a second beneficiary 
  based on the instruction on the LC and of the first beneficiary.
- **Family**: Trade
- **Type**: Trade Services
- **Risk**: Low. Only operational risk as it is merely a service to transfer the LC to a 
  second beneficiary.
- **Tags**: letter of credit, L/C, imports, goods clearance, transfer, transferable LC
- **Segmentation**: generic, exporters
- **Use Case**: working capital financing

## 19. Packing Credit
- **Description**: Usually a pre-shipment financing for exporters/sellers against an LC or 
  collection bill. Percentage of financing is programmable but usually for the total value 
  of the LC or collection bill.
- **Family**: Trade
- **Type**: Trade Finance
- **Risk**: Medium to high. Pre-shipment financing is fully dependent on the borrower's 
  ability to complete performance. Once performance is completed, the risk should be 
  lowered since only a collections task remains. However, if the sale is against a letter 
  of credit where payment is guaranteed, the collection risk will be small. If it is 
  against a purchase order, the risks may be higher as payment is directly from the buyer.
- **Tags**: collections, purchase order, letter of credit, imports, advance, financing, 
  short term, bridging finance, credit, shipment, trade, supply chain, goods clearance, 
  purchase finance, pre-shipment
- **Segmentation**: generic, importers
- **Use Case**: working capital financing

## 20. Assignment of Proceeds under Letter of Credit
- **Description**: A service which requires the bank to monitor and make payment of an 
  assigned value of an LC to registered assignees. This can be the full or partial value 
  of the LC.
- **Family**: Trade
- **Type**: Trade Service
- **Risk**: High. Although this is an operational risk service, the risk is deemed high 
  because it exposes the bank to claims if the assignment payment is not correctly made.
- **Tags**: letter of credit, imports, assignment, advance, financing
- **Segmentation**: generic, importers
- **Use Case**: working capital financing

## 21. Export Bill under Letter of Credit
- **Description**: A collections service provided to claim against a letter of credit. Can 
  apply to payment for sight or acceptance in the case of a usance transaction.
- **Family**: Trade
- **Type**: Trade Service
- **Risk**: Low. Only a service to dispatch the documents presented by the exporter to 
  claim against an LC. Usually there is no need to check the documents for compliance.
- **Tags**: collections, letter of credit, exports, negotiation, acceptance, payment, LC claim
- **Segmentation**: generic, exporters
- **Use Case**: working capital financing

## 22. Bill Receivable under Letter of Credit
- **Description**: Post-shipment financing for exporters/sellers against a letter of credit 
  once terms and conditions have been complied with.
- **Family**: Trade
- **Type**: Trade Finance
- **Risk**: Medium. Post-shipment financing is comforted by the compliance of terms and 
  conditions of the LC, with payment undertaking by the issuing bank.
- **Tags**: collections, negotiation, discounting, letter of credit, exports, advance, 
  financing, short term, bridging finance, credit, post-shipment finance
- **Segmentation**: generic, exporters
- **Use Case**: working capital financing 