// Auto-generated from markdown files
// Run: node scripts/convertProducts.js

export interface Product {
  name: string
  description: string
  family: string
  type: string
  risk: string
  tags: string[]
  segmentation: string
  useCase: string
  content: string
}

export const PRODUCTS: Record<string, Product> = {
  "cash_management.md#1": {
    "name": "International Outward Fund Transfer",
    "description": "A payment service usually denominated in foreign currency to facilitate",
    "family": "Cash Management",
    "type": "Payments",
    "risk": "High, operational risk related",
    "tags": [
      "foreign currency",
      "cross border",
      "payments",
      "accounts",
      "remittance"
    ],
    "segmentation": "generic, importers, investors",
    "useCase": "payments",
    "content": "the payment of trade and investment transactions."
  },
  "cash_management.md#2": {
    "name": "International Inward Fund Transfer",
    "description": "A payment service usually denominated in foreign currency to facilitate",
    "family": "Cash Management",
    "type": "Collections",
    "risk": "High, operational risk related",
    "tags": [
      "foreign currency",
      "cross border",
      "collections",
      "accounts",
      "remittance"
    ],
    "segmentation": "generic, exporters, investors",
    "useCase": "collections",
    "content": "the payment of trade and investment transactions."
  },
  "cash_management.md#3": {
    "name": "Cash Management Services - Remittance",
    "description": "A generic payment service usually denominated in local and foreign",
    "family": "Cash Management",
    "type": "Payments",
    "risk": "High, operational risk related",
    "tags": [
      "foreign currency",
      "cross border",
      "domestic",
      "payments",
      "accounts",
      "remittance"
    ],
    "segmentation": "generic, importers, investors",
    "useCase": "payments",
    "content": "currency to facilitate the payment of trade and investment transactions."
  },
  "cash_management.md#4": {
    "name": "General Cash Management Services",
    "description": "A generic service usually used to describe services provided to",
    "family": "Cash Management",
    "type": "Payments, Collections, Liquidity Management",
    "risk": "Low, operational risk related",
    "tags": [
      "foreign currency",
      "cross border",
      "payments",
      "collections",
      "accounts",
      "remittance",
      "LM",
      ""
    ],
    "segmentation": "generic, importers, investors, domestic buyers, domestic sellers",
    "useCase": "general services",
    "content": "facilitate accounts, payments, collections and liquidity management to customers.\nliquidity management, sweeps, pooling, netting, notional, EFTs, cheques, cash"
  },
  "cash_management.md#5": {
    "name": "Foreign Currency Deposit Account",
    "description": "A demand deposit account denominated in foreign currency to facilitate",
    "family": "Cash Management",
    "type": "Accounts",
    "risk": "Low",
    "tags": [
      "foreign currency",
      "collections",
      "payments",
      "accounts"
    ],
    "segmentation": "generic, exporters, importers, investors",
    "useCase": "funds management",
    "content": "the payments and collections of trade and investment proceeds."
  },
  "cash_management.md#6": {
    "name": "Liquidity Management Services",
    "description": "A suite of services provided to customers in their management of their",
    "family": "Cash Management",
    "type": "Liquidity Management",
    "risk": "Low",
    "tags": [
      "foreign and local currency accounts",
      "LM",
      "sweeping",
      "zero balance",
      "netting",
      "pooling"
    ],
    "segmentation": "generic",
    "useCase": "funds management",
    "content": "accounts and balances, covering physical sweeps, notional pooling and netting."
  },
  "cash_management.md#7": {
    "name": "Reconciliation Services",
    "description": "A suite of services provided to customers to assist in their management",
    "family": "Cash Management",
    "type": "General",
    "risk": "Low",
    "tags": [
      "foreign and local currency accounts",
      "collections",
      "payments",
      "recon",
      "AP update",
      ""
    ],
    "segmentation": "generic",
    "useCase": "reconciliation",
    "content": "of their accounts, specifically targeting their accounts payables and accounts receivables.\nAR update"
  },
  "global_markets.md#1": {
    "name": "Client Buys Foreign Currency",
    "description": "A service provided to facilitate the exchange of currencies for the",
    "family": "Global Markets",
    "type": "Foreign Exchange",
    "risk": "Low to medium. An exchange of currencies between the bank and customer, with",
    "tags": [
      "foreign exchange",
      "FX",
      "spot",
      "value today",
      "value tomorrow",
      "forwards",
      "options",
      "delivery"
    ],
    "segmentation": "generic, importers, payments",
    "useCase": "foreign currency payments",
    "content": "purpose of making payments.\nthe settlement risk being the difference in currency values. Usually for value today,\ntomorrow and spot transactions, the risk element is small due to the lower volatility\nrisk, whilst forwards and options will carry a higher settlement risk."
  },
  "global_markets.md#2": {
    "name": "Client Sells Foreign Currency",
    "description": "A service provided to facilitate the exchange of currencies for the",
    "family": "Global Markets",
    "type": "Foreign Exchange",
    "risk": "Low to medium. An exchange of currencies between the bank and customer, with",
    "tags": [
      "foreign exchange",
      "FX",
      "spot",
      "value today",
      "value tomorrow",
      "forwards",
      "options",
      "delivery"
    ],
    "segmentation": "generic, exporters, collections",
    "useCase": "foreign currency collections",
    "content": "purpose of making collections.\nthe settlement risk being the difference in currency values. Usually for value today,\ntomorrow and spot transactions, the risk element is small due to the lower volatility\nrisk, whilst forwards and options will carry a higher settlement risk."
  },
  "global_markets.md#3": {
    "name": "FX Spot - Bank Buys",
    "description": "A service provided to facilitate the exchange of currencies for the",
    "family": "Global Markets",
    "type": "Foreign Exchange",
    "risk": "Low to medium. An exchange of currencies between the bank and customer, with",
    "tags": [
      "foreign exchange",
      "FX",
      "spot",
      "value today",
      "value tomorrow",
      "forwards",
      "options",
      ""
    ],
    "segmentation": "generic, exporters, collections",
    "useCase": "foreign currency collections",
    "content": "purpose of making collections in foreign currency.\nthe settlement risk being the difference in currency values. Usually for value today,\ntomorrow and spot transactions, the risk element is small due to the lower volatility\nrisk, whilst forwards and options will carry a higher settlement risk.\ndelivery, hedge"
  },
  "global_markets.md#4": {
    "name": "FX Spot - Bank Sells",
    "description": "A service provided to facilitate the exchange of currencies for the",
    "family": "Global Markets",
    "type": "Foreign Exchange",
    "risk": "Low to medium. An exchange of currencies between the bank and customer, with",
    "tags": [
      "foreign exchange",
      "FX",
      "spot",
      "value today",
      "value tomorrow",
      "forwards",
      "options",
      ""
    ],
    "segmentation": "generic, importers, payments",
    "useCase": "foreign currency payments",
    "content": "purpose of making payments.\nthe settlement risk being the difference in currency values. Usually for value today,\ntomorrow and spot transactions, the risk element is small due to the lower volatility\nrisk, whilst forwards and options will carry a higher settlement risk.\ndelivery, hedge"
  },
  "global_markets.md#5": {
    "name": "FX Forward Contract - Bank Buys",
    "description": "A service provided to facilitate the exchange of currencies for the",
    "family": "Global Markets",
    "type": "Foreign Exchange",
    "risk": "Low to medium. An exchange of currencies between the bank and customer, with",
    "tags": [
      "foreign exchange",
      "FX",
      "spot",
      "value today",
      "value tomorrow",
      "forwards",
      "options",
      ""
    ],
    "segmentation": "generic, exporters, collections",
    "useCase": "foreign currency collections",
    "content": "purpose of making collections in foreign currency on a future date.\nthe settlement risk being the difference in currency values. Usually for value today,\ntomorrow and spot transactions, the risk element is small due to the lower volatility\nrisk, whilst forwards and options will carry a higher settlement risk.\ndelivery, hedge"
  },
  "global_markets.md#6": {
    "name": "FX Forward Contract - Bank Sells",
    "description": "A service provided to facilitate the exchange of currencies for the",
    "family": "Global Markets",
    "type": "Foreign Exchange",
    "risk": "Low to medium. An exchange of currencies between the bank and customer, with",
    "tags": [
      "foreign exchange",
      "FX",
      "spot",
      "value today",
      "value tomorrow",
      "forwards",
      "options",
      ""
    ],
    "segmentation": "generic, importers, payments",
    "useCase": "foreign currency payments",
    "content": "purpose of making payments at a future date.\nthe settlement risk being the difference in currency values. Usually for value today,\ntomorrow and spot transactions, the risk element is small due to the lower volatility\nrisk, whilst forwards and options will carry a higher settlement risk.\ndelivery, hedge"
  },
  "global_markets.md#7": {
    "name": "FX Call Option",
    "description": "A transaction that provides the right to a customer to buy a",
    "family": "Global Markets",
    "type": "Foreign Exchange",
    "risk": "Low to medium. An exchange of currencies between the bank and customer, with",
    "tags": [
      "foreign exchange",
      "FX",
      "spot",
      "value today",
      "value tomorrow",
      "forwards",
      "options",
      ""
    ],
    "segmentation": "generic, importers, payments",
    "useCase": "foreign currency payments",
    "content": "pre-determined amount of foreign currency at a specific rate, on the expiration of an\nagreed date.\nthe settlement risk being the difference in currency values. Usually for value today,\ntomorrow and spot transactions, the risk element is small due to the lower volatility\nrisk, whilst forwards and options will carry a higher settlement risk.\ndelivery, hedge"
  },
  "global_markets.md#8": {
    "name": "FX Put Option",
    "description": "A transaction that provides the right to a customer to sell a",
    "family": "Global Markets",
    "type": "Foreign Exchange",
    "risk": "Low to medium. An exchange of currencies between the bank and customer, with",
    "tags": [
      "foreign exchange",
      "FX",
      "spot",
      "value today",
      "value tomorrow",
      "forwards",
      "options",
      ""
    ],
    "segmentation": "generic, exporters, collections",
    "useCase": "foreign currency collections",
    "content": "pre-determined amount of foreign currency at a specific rate, on the expiration of an\nagreed date.\nthe settlement risk being the difference in currency values. Usually for value today,\ntomorrow and spot transactions, the risk element is small due to the lower volatility\nrisk, whilst forwards and options will carry a higher settlement risk.\ndelivery, hedge"
  },
  "global_markets.md#9": {
    "name": "Interest Rate Swap",
    "description": "A transaction that provides a customer the ability to convert a loan's",
    "family": "Global Markets",
    "type": "Derivatives",
    "risk": "Medium. Requires a settlement of the net interest difference.",
    "tags": [
      "IRS",
      "interest rate swap",
      "swap",
      "hedge"
    ],
    "segmentation": "generic, loans, borrowers",
    "useCase": "loans, local and foreign currency loans",
    "content": "fixed rate to floating rate, or vice-versa."
  },
  "global_markets.md#10": {
    "name": "Cross Currency Swap",
    "description": "A transaction that provides a customer the ability to convert a loan's",
    "family": "Global Markets",
    "type": "Derivatives",
    "risk": "Medium. Requires a settlement of the net interest and FX difference.",
    "tags": [
      "IRS",
      "interest rate swap",
      "swap",
      "hedge",
      "cross currency swap",
      "CCS"
    ],
    "segmentation": "generic, loans, borrowers",
    "useCase": "loans, local and foreign currency loans",
    "content": "fixed rate to floating rate, or vice-versa coupled with a conversion of the loan into\nanother currency."
  },
  "loans.md#1": {
    "name": "Term Loans",
    "description": "A loan facility to finance capital expenditures, usually long term in",
    "family": "Loans",
    "type": "Term",
    "risk": "High, but usually collateralized against guarantees, tangible assets or deposits",
    "tags": [
      "loan",
      "term loan",
      "financing",
      "capex loan"
    ],
    "segmentation": "generic, loans, borrowers",
    "useCase": "long term loans, local and foreign currency",
    "content": "nature. Single drawdown, with fixed repayments until liquidation."
  },
  "loans.md#2": {
    "name": "Revolving Credit",
    "description": "A short loan facility usually to finance working capital. Single",
    "family": "Loans",
    "type": "Term",
    "risk": "High, but usually collateralized against guarantees, tangible assets or deposits",
    "tags": [
      "loan",
      "term loan",
      "RC",
      "revolving credit",
      "financing",
      "working capital financing"
    ],
    "segmentation": "generic, loans, borrowers",
    "useCase": "short term loans, local and foreign currency",
    "content": "drawdown with bullet payment upon maturity but redrawable up to the limit approved once\nexisting loans are repaid."
  },
  "loans.md#3": {
    "name": "Overdrafts",
    "description": "An evergreen reusable loan facility with no maturity date, usually used",
    "family": "Loans",
    "type": "Demand",
    "risk": "High, but usually collateralized against guarantees, tangible assets or deposits",
    "tags": [
      "loan",
      "OD",
      "RC",
      "revolving credit",
      "financing",
      "working capital financing"
    ],
    "segmentation": "generic, loans, borrowers",
    "useCase": "short term loans, local and foreign currency",
    "content": "for working capital financing."
  },
  "trade_finance_products.md#1": {
    "name": "Import P/N",
    "description": "This is a generic pre-shipment trade loan specifically structured to",
    "family": "Trade",
    "type": "Trade Finance",
    "risk": "Medium to low, if applied to documentary collections and letters of credit where",
    "tags": [
      "imports",
      "financing",
      "foreign currency",
      "credit terms",
      "cash conversion cycle",
      ""
    ],
    "segmentation": "generic, importers",
    "useCase": "working capital financing",
    "content": "finance imports, transactionally supported by a promissory note executed by the borrower.\nProceeds of the drawdown are paid directly to the exporter.\ntitle of the goods can be consigned to the bank.\nopen account, letter of credit, collections, short term, bridging finance, P-note,\nshipment, goods clearance, supply chain, trade, purchase finance, pre-shipment"
  },
  "trade_finance_products.md#2": {
    "name": "Import P/N under Open Account",
    "description": "This is a generic pre-shipment trade loan specifically structured to",
    "family": "Trade",
    "type": "Trade Finance",
    "risk": "Medium to high, since for open account the underlying goods may be consigned",
    "tags": [
      "OA (Open Account)",
      "imports",
      "P-note",
      "financing",
      "short term",
      "bridging finance",
      ""
    ],
    "segmentation": "generic, importers",
    "useCase": "working capital financing",
    "content": "finance imports on open account only, transactionally supported by a promissory note\nexecuted by the borrower. Proceeds of the drawdown are paid directly to the exporter.\ndirectly to the buyer/importer\ncredit, shipment, trade, supply chain, goods clearance, purchase finance, pre-shipment"
  },
  "trade_finance_products.md#3": {
    "name": "Export P/N under Open Account",
    "description": "This is a generic post-shipment trade loan specifically structured to",
    "family": "Trade",
    "type": "Trade Finance",
    "risk": "Medium to high, since for open account the underlying goods may be consigned",
    "tags": [
      "open account",
      "exports",
      "P-note",
      "financing",
      "short term",
      "bridging finance",
      "credit",
      ""
    ],
    "segmentation": "generic, exporters",
    "useCase": "working capital financing",
    "content": "finance exports on open account only, transactionally supported by a promissory note\nexecuted by the borrower. Proceeds of the drawdown are paid directly to the\nexporter/borrower.\ndirectly to the buyer/importer and bank has no control. Bank also generally does not\nhave a relationship with the buyer/importer.\nshipment, trade, supply chain, purchase finance, post-shipment, advance"
  },
  "trade_finance_products.md#4": {
    "name": "Packing Credit",
    "description": "Pre-shipment financing for exporters/sellers against either a letter of",
    "family": "Trade",
    "type": "Trade Finance",
    "risk": "Medium to high. Pre-shipment financing is fully dependent on the borrower's",
    "tags": [
      "open account",
      "purchase order",
      "letter of credit",
      "imports",
      "advance",
      "financing",
      ""
    ],
    "segmentation": "generic, importers",
    "useCase": "working capital financing",
    "content": "credit or purchase order. Percentage of financing is programmable.\nability to complete performance. Once performance is completed, the risk should be\nlowered since only a collections task remains, if it is against a letter of credit where\npayment is guaranteed. If it is against a purchase order, the risks may be higher as\npayment is directly from the buyer.\nshort term, bridging finance, credit, shipment, trade, supply chain, goods clearance,\npurchase finance, pre-shipment"
  },
  "trade_finance_products.md#5": {
    "name": "Inward Bill for Collection",
    "description": "This is a collections service where the bank only acts as an agent for",
    "family": "Trade",
    "type": "Services",
    "risk": "Low. No financing risk, only operational risk is involved.",
    "tags": [
      "collections",
      "imports",
      "shipment",
      "trade",
      "supply chain",
      "goods clearance",
      ""
    ],
    "segmentation": "generic, importers",
    "useCase": "trade services",
    "content": "the exporter to collect payment or acceptance and release trade documents to the\nimporter/buyer\nshipping guarantee"
  },
  "trade_finance_products.md#6": {
    "name": "Import P/N under Bill for Collection",
    "description": "This is a generic pre-shipment trade loan specifically structured to",
    "family": "Trade",
    "type": "Trade Finance",
    "risk": "Medium, since for collections the title documents for the underlying goods are",
    "tags": [
      "collections",
      "imports",
      "P-note",
      "financing",
      "short term",
      "bridging finance",
      "credit",
      ""
    ],
    "segmentation": "generic, importers",
    "useCase": "working capital financing",
    "content": "finance imports on import collections only, transactionally supported by a promissory\nnote executed by the borrower. Proceeds of the drawdown are paid directly to the\nremitting bank on behalf of the exporter.\ncontrolled by the banks\nshipment, trade, supply chain, goods clearance, purchase finance, pre-shipment"
  },
  "trade_finance_products.md#7": {
    "name": "Outward Bill for Collection",
    "description": "This is a collections service where the bank only acts as an agent for",
    "family": "Trade",
    "type": "Services",
    "risk": "Low. No financing risk, only operational risk is involved.",
    "tags": [
      "collections",
      "exports",
      "shipment",
      "trade",
      "supply chain",
      "goods clearance",
      ""
    ],
    "segmentation": "generic, importers",
    "useCase": "trade services",
    "content": "the exporter send the trade documents to the collecting bank/importer in exchange for\npayment or acceptance\nshipping guarantee"
  },
  "trade_finance_products.md#8": {
    "name": "Bill Receivable under Outward Bill for Collection",
    "description": "This is a trade loan to finance an outward collection bill, to be",
    "family": "Trade",
    "type": "Financing",
    "risk": "High. Usual financing risk generally with recourse only to the exporter.",
    "tags": [
      "collections",
      "exports",
      "shipment",
      "trade",
      "supply chain",
      "financing",
      "export advance",
      ""
    ],
    "segmentation": "generic, exporters",
    "useCase": "trade financing",
    "content": "liquidated with the proceeds of the collection upon receipt of payment from the\ncollecting bank/importer. Can be with or without recourse financing.\ncash flow easing"
  },
  "trade_finance_products.md#9": {
    "name": "Packing Credit",
    "description": "Pre-shipment financing for importers/sellers against an inward",
    "family": "Trade",
    "type": "Trade Finance",
    "risk": "Medium to high. Pre-shipment financing is fully dependent on the borrower's",
    "tags": [
      "collections",
      "purchase order",
      "letter of credit",
      "imports",
      "advance",
      "financing",
      ""
    ],
    "segmentation": "generic, importers",
    "useCase": "working capital financing",
    "content": "collection bill. Percentage of financing is programmable but usually for the total value\nof the collection bill.\nability to complete performance. Once performance is completed, the risk should be\nlowered since only a collections task remains. However, if the sale is against a letter\nof credit where payment is guaranteed, the collection risk will be small. If it is\nagainst a purchase order, the risks may be higher as payment is directly from the buyer.\nshort term, bridging finance, credit, shipment, trade, supply chain, goods clearance,\npurchase finance, pre-shipment"
  },
  "trade_finance_products.md#10": {
    "name": "Letter of Credit Issuance/Amendment",
    "description": "Issuance of an undertaking by the bank to make payment upon satisfaction",
    "family": "Trade",
    "type": "Trade Services",
    "risk": "Low to medium. A letter of credit is an undertaking by a bank to pay regardless",
    "tags": [
      "purchase order",
      "letter of credit",
      "L/C",
      "imports",
      "advance",
      "financing",
      "short term",
      ""
    ],
    "segmentation": "generic, importers",
    "useCase": "working capital financing",
    "content": "of terms and conditions of a cross border/foreign currency letter of credit\nof whether the applicant is able to make payment or not. As such, principal\nresponsibility to pay still lies with the issuing bank.\nbridging finance, credit terms, shipment, trade, supply chain, goods clearance,\nusance bill"
  },
  "trade_finance_products.md#11": {
    "name": "Domestic Letter of Credit Issuance/Amendment",
    "description": "Issuance of an undertaking by the bank to make payment upon satisfaction",
    "family": "Trade",
    "type": "Trade Services",
    "risk": "Low to medium. A letter of credit is an undertaking by a bank to pay regardless",
    "tags": [
      "purchase order",
      "letter of credit",
      "L/C",
      "imports",
      "advance",
      "financing",
      "short term",
      ""
    ],
    "segmentation": "generic, importers",
    "useCase": "working capital financing",
    "content": "of terms and conditions of a domestic/local currency letter of credit\nof whether the applicant is able to make payment or not. As such, principal\nresponsibility to pay still lies with the issuing bank.\nbridging finance, credit terms, shipment, trade, supply chain, goods clearance,\nusance bill"
  },
  "trade_finance_products.md#12": {
    "name": "Shipping Guarantee Issuance",
    "description": "Bank guarantee issued to a shipping company for the releases of goods,",
    "family": "Trade",
    "type": "Trade Services",
    "risk": "High. A shipping guarantee is an undertaking by a bank to pay the beneficiary",
    "tags": [
      "letter of credit",
      "L/C",
      "collections",
      "imports",
      "goods clearance"
    ],
    "segmentation": "generic, importers",
    "useCase": "working capital financing",
    "content": "in the absence of a bill of lading or transport document, e.g. airway bill.\nregardless of claims value, as the guarantee is issued without a value cap."
  },
  "trade_finance_products.md#13": {
    "name": "Delivery Order Endorsement",
    "description": "A trade service to endorse a title/transport document to an importer for",
    "family": "Trade",
    "type": "Trade Services",
    "risk": "High. An endorsement to the importer will enable the clearance of goods, thus",
    "tags": [
      "letter of credit",
      "L/C",
      "collections",
      "delivery order",
      "D/O",
      "imports",
      "goods clearance"
    ],
    "segmentation": "generic, importers/domestic buyers",
    "useCase": "working capital financing",
    "content": "the purpose of clearing goods.\ncausing the bank to lose control over the goods as collateral. Bank will need to rely on\nother security arrangements to secure the transaction."
  },
  "trade_finance_products.md#14": {
    "name": "Trust Receipt under Letter of Credit",
    "description": "A short term trade loan provided to pay against a letter of credit,",
    "family": "Trade",
    "type": "Trade Financing",
    "risk": "High. A trust receipt loan is provided to an importer with a release of the",
    "tags": [
      "letter of credit",
      "L/C",
      "collections",
      "imports",
      "goods clearance",
      "trust receipt",
      "TR",
      ""
    ],
    "segmentation": "generic, importers",
    "useCase": "working capital financing",
    "content": "whereby the goods are released by the bank under trust to the applicant/importer, for\nthe purpose of sales conversion and proceeds used to repay the LC.\nunderlying goods for the purpose of sales conversion, thus causing the bank to release\nownership of the goods.\ntrade loan, advance, trade financing"
  },
  "trade_finance_products.md#15": {
    "name": "P/N under Domestic Letter of Credit",
    "description": "A trade loan provided against the issuance of a promissory note by the",
    "family": "Trade",
    "type": "Trade Financing",
    "risk": "High. Financing the payment of an LC with an added security of a promissory",
    "tags": [
      "letter of credit",
      "L/C",
      "collections",
      "imports",
      "goods clearance",
      "trade loan",
      ""
    ],
    "segmentation": "generic, importers",
    "useCase": "working capital financing",
    "content": "borrower, for the purpose of paying off a domestic LC.\nnote issued by the borrower.\nfinancing, PN, promissory note, advance"
  },
  "trade_finance_products.md#16": {
    "name": "Letter of Credit Advising/Amendment Advising",
    "description": "Trade service to authenticate and advise the issuance of a letter of",
    "family": "Trade",
    "type": "Trade Services",
    "risk": "Low. Only operational risk of performing authentication of the instrument prior",
    "tags": [
      "letter of credit",
      "L/C",
      "exports",
      "advising",
      "exporters",
      "usance"
    ],
    "segmentation": "generic, exporters",
    "useCase": "working capital financing",
    "content": "credit to a beneficiary\nto advising the beneficiary."
  },
  "trade_finance_products.md#17": {
    "name": "Letter of Credit Confirmation",
    "description": "An undertaking by the bank to pay an exporter on an LC issued by",
    "family": "Trade",
    "type": "Trade Services",
    "risk": "Medium. The undertaking to pay an exporter is predicated on the risk taken on",
    "tags": [
      "letter of credit",
      "L/C",
      "exports",
      "confirmation",
      "sovereign risk",
      "cross border risk",
      ""
    ],
    "segmentation": "generic, exporters",
    "useCase": "working capital financing",
    "content": "another issuing bank once terms and conditions of the LC are complied with\nthe issuing bank. Generally a relatively safe transaction depending on the credit rating\nof the issuing bank.\nbank risk"
  },
  "trade_finance_products.md#18": {
    "name": "Letter of Credit Transferring",
    "description": "A trade service to transfer a letter of credit to a second beneficiary",
    "family": "Trade",
    "type": "Trade Services",
    "risk": "Low. Only operational risk as it is merely a service to transfer the LC to a",
    "tags": [
      "letter of credit",
      "L/C",
      "imports",
      "goods clearance",
      "transfer",
      "transferable LC"
    ],
    "segmentation": "generic, exporters",
    "useCase": "working capital financing",
    "content": "based on the instruction on the LC and of the first beneficiary.\nsecond beneficiary."
  },
  "trade_finance_products.md#19": {
    "name": "Packing Credit",
    "description": "Usually a pre-shipment financing for exporters/sellers against an LC or",
    "family": "Trade",
    "type": "Trade Finance",
    "risk": "Medium to high. Pre-shipment financing is fully dependent on the borrower's",
    "tags": [
      "collections",
      "purchase order",
      "letter of credit",
      "imports",
      "advance",
      "financing",
      ""
    ],
    "segmentation": "generic, importers",
    "useCase": "working capital financing",
    "content": "collection bill. Percentage of financing is programmable but usually for the total value\nof the LC or collection bill.\nability to complete performance. Once performance is completed, the risk should be\nlowered since only a collections task remains. However, if the sale is against a letter\nof credit where payment is guaranteed, the collection risk will be small. If it is\nagainst a purchase order, the risks may be higher as payment is directly from the buyer.\nshort term, bridging finance, credit, shipment, trade, supply chain, goods clearance,\npurchase finance, pre-shipment"
  },
  "trade_finance_products.md#20": {
    "name": "Assignment of Proceeds under Letter of Credit",
    "description": "A service which requires the bank to monitor and make payment of an",
    "family": "Trade",
    "type": "Trade Service",
    "risk": "High. Although this is an operational risk service, the risk is deemed high",
    "tags": [
      "letter of credit",
      "imports",
      "assignment",
      "advance",
      "financing"
    ],
    "segmentation": "generic, importers",
    "useCase": "working capital financing",
    "content": "assigned value of an LC to registered assignees. This can be the full or partial value\nof the LC.\nbecause it exposes the bank to claims if the assignment payment is not correctly made."
  },
  "trade_finance_products.md#21": {
    "name": "Export Bill under Letter of Credit",
    "description": "A collections service provided to claim against a letter of credit. Can",
    "family": "Trade",
    "type": "Trade Service",
    "risk": "Low. Only a service to dispatch the documents presented by the exporter to",
    "tags": [
      "collections",
      "letter of credit",
      "exports",
      "negotiation",
      "acceptance",
      "payment",
      "LC claim"
    ],
    "segmentation": "generic, exporters",
    "useCase": "working capital financing",
    "content": "apply to payment for sight or acceptance in the case of a usance transaction.\nclaim against an LC. Usually there is no need to check the documents for compliance."
  },
  "trade_finance_products.md#22": {
    "name": "Bill Receivable under Letter of Credit",
    "description": "Post-shipment financing for exporters/sellers against a letter of credit",
    "family": "Trade",
    "type": "Trade Finance",
    "risk": "Medium. Post-shipment financing is comforted by the compliance of terms and",
    "tags": [
      "collections",
      "negotiation",
      "discounting",
      "letter of credit",
      "exports",
      "advance",
      ""
    ],
    "segmentation": "generic, exporters",
    "useCase": "working capital financing",
    "content": "once terms and conditions have been complied with.\nconditions of the LC, with payment undertaking by the issuing bank.\nfinancing, short term, bridging finance, credit, post-shipment finance"
  }
};


