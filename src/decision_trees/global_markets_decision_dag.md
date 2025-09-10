flowchart TD
    Start["Client Consultation"] --> ClientType{"What is the client's<br/>business activity?"}
    
    ClientType --> Importer["Importer<br/>(Needs to buy foreign currency)"]
    ClientType --> Exporter["Exporter<br/>(Receives foreign currency)"]
    ClientType --> Both["Both Importer & Exporter"]
    
    Both --> NaturalHedge{"Do foreign currency<br/>payments and receipts<br/>cancel out?"}
    NaturalHedge -->|Yes| NoFXNeeded["Natural hedge exists<br/>No FX products needed"]
    NaturalHedge -->|No| NetPosition["Determine net FX position"]
    
    NetPosition --> Importer
    NetPosition --> Exporter
    
    Importer --> CurrencyCheck1{"Is required currency<br/>supported?<br/>(Major currencies + MYR, KRW, VND)"}
    Exporter --> CurrencyCheck2{"Is received currency<br/>supported?<br/>(Major currencies + MYR, KRW, VND)"}
    
    CurrencyCheck1 -->|No| NotSupported1["Currency not supported<br/>Cannot provide service"]
    CurrencyCheck2 -->|No| NotSupported2["Currency not supported<br/>Cannot provide service"]
    
    CurrencyCheck1 -->|Yes| ImporterFlow["Need to buy foreign currency"]
    CurrencyCheck2 -->|Yes| ExporterFlow["Need to sell foreign currency"]
    
    ImporterFlow --> HedgeDecision1{"Want to hedge<br/>FX volatility/risk?"}
    ExporterFlow --> HedgeDecision2{"Want to hedge<br/>FX volatility/risk?"}
    
    HedgeDecision1 -->|No| FXSpotBuy["FX Spot - Bank Sells<br/>(Client buys foreign currency)"]
    HedgeDecision2 -->|No| FXSpotSell["FX Spot - Bank Buys<br/>(Client sells foreign currency)"]
    
    HedgeDecision1 -->|Yes| HedgeProportion1{"What proportion<br/>to hedge?"}
    HedgeDecision2 -->|Yes| HedgeProportion2{"What proportion<br/>to hedge?"}
    
    HedgeProportion1 --> PartialHedge1["Partial hedging<br/>needed"]
    HedgeProportion1 --> FullHedge1["Full hedging<br/>needed"]
    
    HedgeProportion2 --> PartialHedge2["Partial hedging<br/>needed"]
    HedgeProportion2 --> FullHedge2["Full hedging<br/>needed"]
    
    PartialHedge1 --> FXSpotBuy
    PartialHedge1 --> HedgeProduct1{"Certain about date<br/>and amount?"}
    
    PartialHedge2 --> FXSpotSell
    PartialHedge2 --> HedgeProduct2{"Certain about date<br/>and amount?"}
    
    FullHedge1 --> HedgeProduct1
    FullHedge2 --> HedgeProduct2
    
    HedgeProduct1 -->|Yes| FXForwardSell["FX Forward Contract<br/>Bank Sells"]
    HedgeProduct1 -->|No| FXCallOption["FX Call Option<br/>(Right to buy foreign currency)"]
    
    HedgeProduct2 -->|Yes| FXForwardBuy["FX Forward Contract<br/>Bank Buys"]
    HedgeProduct2 -->|No| FXPutOption["FX Put Option<br/>(Right to sell foreign currency)"]
    
    Start --> IRCheck{"Does client want to<br/>hedge Interest Rate risk?"}
    IRCheck -->|Yes| IRProduct{"Interest rate<br/>hedging needed"}
    IRCheck -->|No| IRComplete["No IR hedging needed"]
    
    IRProduct --> CurrencyMatch{"Same currency as<br/>FX exposure?"}
    CurrencyMatch -->|Yes| IRS["Interest Rate Swap<br/>(Single currency)"]
    CurrencyMatch -->|No| CCS["Cross Currency Swap<br/>(Multi-currency)"]
    
    classDef startNode fill:#4CAF50,stroke:#2E7D32,stroke-width:3px,color:#fff
    classDef decisionNode fill:#2196F3,stroke:#1565C0,stroke-width:2px,color:#fff
    classDef productNode fill:#FF9800,stroke:#E65100,stroke-width:2px,color:#fff
    classDef endNode fill:#9C27B0,stroke:#6A1B9A,stroke-width:2px,color:#fff
    classDef warningNode fill:#F44336,stroke:#C62828,stroke-width:2px,color:#fff
    
    class Start startNode
    class ClientType,NaturalHedge,CurrencyCheck1,CurrencyCheck2,HedgeDecision1,HedgeDecision2,HedgeProportion1,HedgeProportion2,HedgeProduct1,HedgeProduct2,IRCheck,CurrencyMatch decisionNode
    class FXSpotBuy,FXSpotSell,FXForwardSell,FXForwardBuy,FXCallOption,FXPutOption,IRS,CCS productNode
    class NoFXNeeded,IRComplete endNode
    class NotSupported1,NotSupported2 warningNode
