import { PRODUCTS } from './products'

// Types for questions and answers
export type AnswerOption = {
  id: string
  text: string
  value: string
  score: number // Base score for this answer
  productRecommendations: string[] // Product IDs that get recommended
  tags: string[] // Tags that get added to user profile
}

export type Question = {
  id: string
  category: string
  subcategory: string
  text: string
  description?: string
  type: 'single' | 'multiple' | 'range' | 'text'
  options: AnswerOption[]
  required: boolean
  order: number
  weight: number // How much this question affects overall scoring
}

export type UserAnswer = {
  questionId: string
  selectedOptions: string[]
  textValue?: string
  answeredAt: Date
}

export type UserProfile = {
  answers: UserAnswer[]
  tags: string[]
  preferences: Record<string, any>
}

export type ProductRecommendation = {
  productId: string
  score: number
  reason: string
  category: string
  family: string
}

// Product scoring weights
const PRODUCT_WEIGHTS = {
  'cash_management': 1.0,
  'trade_finance': 1.2,
  'loans': 1.1,
  'global_markets': 1.3,
  'investments': 0.8,
  'insurance': 0.9,
}

// Question categories and their weights
const CATEGORY_WEIGHTS = {
  'business_overview': 1.0,
  'trade_finance': 1.2,
  'cash_management': 1.1,
  'global_markets': 1.3,
  'lending': 1.0,
}

// Helper function to expand category-level recommendations to individual products
const expandProductRecommendations = (productIds: string[]): string[] => {
  const expandedProducts: string[] = []

  productIds.forEach(productId => {
    if (productId.includes('#')) {
      // Specific product, add as is
      expandedProducts.push(productId)
    } else {
      // Category-level recommendation, expand to all products in that category
      Object.keys(PRODUCTS).forEach(productKey => {
        if (productKey.startsWith(productId + '#')) {
          expandedProducts.push(productKey)
        }
      })
    }
  })

  return expandedProducts
}

// Questions data
export const questions: Question[] = [
  // A. BUSINESS OVERVIEW & SEGMENTATION QUESTIONS
  {
    id: 'A.1.1',
    category: 'business_overview',
    subcategory: 'core_business',
    text: 'What is your core business activity?',
    description: 'Understanding your primary business helps us recommend the most relevant banking solutions.',
    type: 'single',
    required: true,
    order: 1,
    weight: 1.0,
    options: [
      {
        id: 'manufacturing',
        text: 'Manufacturing',
        value: 'manufacturing',
        score: 8,
        productRecommendations: ['trade_finance_products.md#1', 'trade_finance_products.md#4', 'cash_management.md', 'global_markets.md'],
        tags: ['manufacturing', 'imports', 'working_capital']
      },
      {
        id: 'trading_import_export',
        text: 'Trading/Import-Export',
        value: 'trading_import_export',
        score: 9,
        productRecommendations: ['trade_finance_products.md', 'global_markets.md#5', 'cash_management.md'],
        tags: ['trading', 'imports', 'exports', 'fx_exposure']
      },
      {
        id: 'services',
        text: 'Services',
        value: 'services',
        score: 6,
        productRecommendations: ['cash_management.md'],
        tags: ['services', 'domestic']
      },
      {
        id: 'retail_distribution',
        text: 'Retail/Distribution',
        value: 'retail_distribution',
        score: 7,
        productRecommendations: ['trade_finance_products.md#1', 'loans.md', 'cash_management.md'],
        tags: ['retail', 'distribution', 'working_capital']
      }
    ]
  },
  {
    id: 'A.1.2',
    category: 'business_overview',
    subcategory: 'products_services',
    text: 'What are your main products/services?',
    description: 'This helps us understand your supply chain and financing needs.',
    type: 'single',
    required: true,
    order: 2,
    weight: 0.8,
    options: [
      {
        id: 'physical_goods',
        text: 'Physical goods',
        value: 'physical_goods',
        score: 8,
        productRecommendations: ['trade_finance_products.md#12', 'trade_finance_products.md#5'],
        tags: ['physical_goods', 'inventory', 'shipping']
      },
      {
        id: 'digital_services',
        text: 'Digital/Services',
        value: 'digital_services',
        score: 5,
        productRecommendations: ['cash_management.md'],
        tags: ['digital', 'services', 'domestic']
      },
      {
        id: 'commodities',
        text: 'Commodities',
        value: 'commodities',
        score: 9,
        productRecommendations: ['global_markets.md#5', 'trade_finance_products.md'],
        tags: ['commodities', 'fx_exposure', 'bulk_purchases']
      }
    ]
  },
  {
    id: 'A.1.3',
    category: 'business_overview',
    subcategory: 'markets',
    text: 'What are your primary markets?',
    description: 'Your market reach determines the complexity of banking solutions needed.',
    type: 'single',
    required: true,
    order: 3,
    weight: 0.9,
    options: [
      {
        id: 'domestic_only',
        text: 'Domestic only',
        value: 'domestic_only',
        score: 5,
        productRecommendations: ['trade_finance_products.md#11', 'loans.md', 'cash_management.md'],
        tags: ['domestic', 'local_currency']
      },
      {
        id: 'regional',
        text: 'Regional',
        value: 'regional',
        score: 7,
        productRecommendations: ['cash_management.md#1', 'global_markets.md#3', 'trade_finance_products.md'],
        tags: ['regional', 'cross_border', 'fx_exposure']
      },
      {
        id: 'global',
        text: 'Global',
        value: 'global',
        score: 9,
        productRecommendations: ['global_markets.md', 'trade_finance_products.md', 'cash_management.md#5'],
        tags: ['global', 'multi_currency', 'complex_fx']
      }
    ]
  },
  {
    id: 'A.1.4',
    category: 'business_overview',
    subcategory: 'trade_activity',
    text: 'Do you import or export goods/services?',
    description: 'This determines which trade finance solutions are most relevant.',
    type: 'single',
    required: true,
    order: 4,
    weight: 1.1,
    options: [
      {
        id: 'importers',
        text: 'Importers',
        value: 'importers',
        score: 8,
        productRecommendations: ['trade_finance_products.md#1', 'trade_finance_products.md#10', 'trade_finance_products.md#14', 'trade_finance_products.md#12'],
        tags: ['imports', 'trade_finance', 'working_capital']
      },
      {
        id: 'exporters',
        text: 'Exporters',
        value: 'exporters',
        score: 8,
        productRecommendations: ['trade_finance_products.md#3', 'trade_finance_products.md#4', 'trade_finance_products.md#16', 'trade_finance_products.md#7'],
        tags: ['exports', 'trade_finance', 'collections']
      },
      {
        id: 'both',
        text: 'Both',
        value: 'both',
        score: 9,
        productRecommendations: ['trade_finance_products.md', 'global_markets.md#5'],
        tags: ['imports', 'exports', 'complex_trade', 'fx_exposure']
      },
      {
        id: 'neither',
        text: 'Neither',
        value: 'neither',
        score: 4,
        productRecommendations: ['loans.md', 'cash_management.md'],
        tags: ['domestic', 'no_trade']
      }
    ]
  },
  {
    id: 'A.1.5',
    category: 'business_overview',
    subcategory: 'revenue',
    text: 'Annual revenue range',
    description: 'Revenue size helps determine appropriate product complexity and limits.',
    type: 'single',
    required: true,
    order: 5,
    weight: 0.7,
    options: [
      {
        id: 'under_10m',
        text: '< $10M',
        value: 'under_10m',
        score: 5,
        productRecommendations: ['loans.md#3', 'cash_management.md', 'global_markets.md#3'],
        tags: ['small_business', 'basic_services']
      },
      {
        id: '10m_100m',
        text: '$10M-$100M',
        value: '10m_100m',
        score: 7,
        productRecommendations: ['loans.md#2', 'trade_finance_products.md', 'global_markets.md#5'],
        tags: ['medium_business', 'standard_services']
      },
      {
        id: 'over_100m',
        text: '> $100M',
        value: 'over_100m',
        score: 9,
        productRecommendations: ['global_markets.md#9', 'trade_finance_products.md', 'cash_management.md#6'],
        tags: ['large_business', 'complex_services', 'treasury']
      }
    ]
  },

  // B. TRADE FINANCE NEEDS DISCOVERY
  {
    id: 'B.1.1',
    category: 'trade_finance',
    subcategory: 'import_activities',
    text: 'Do you regularly import raw materials, finished goods, or equipment?',
    description: 'This helps determine the type of import financing needed.',
    type: 'single',
    required: false,
    order: 6,
    weight: 1.0,
    options: [
      {
        id: 'raw_materials',
        text: 'Raw materials',
        value: 'raw_materials',
        score: 8,
        productRecommendations: ['trade_finance_products.md#1', 'trade_finance_products.md#4'],
        tags: ['raw_materials', 'imports', 'pre_shipment']
      },
      {
        id: 'finished_goods',
        text: 'Finished goods',
        value: 'finished_goods',
        score: 7,
        productRecommendations: ['trade_finance_products.md#1', 'trade_finance_products.md#14', 'trade_finance_products.md#5'],
        tags: ['finished_goods', 'imports', 'inventory']
      },
      {
        id: 'equipment',
        text: 'Equipment',
        value: 'equipment',
        score: 8,
        productRecommendations: ['loans.md#1', 'trade_finance_products.md#10', 'trade_finance_products.md#13'],
        tags: ['equipment', 'capex', 'term_financing']
      },
      {
        id: 'no_imports',
        text: 'No imports',
        value: 'no_imports',
        score: 2,
        productRecommendations: [],
        tags: ['no_imports']
      }
    ]
  },
  {
    id: 'B.1.2',
    category: 'trade_finance',
    subcategory: 'import_countries',
    text: 'What countries do you import from?',
    description: 'This affects risk assessment and required trade finance instruments.',
    type: 'single',
    required: false,
    order: 7,
    weight: 0.8,
    options: [
      {
        id: 'developed_countries',
        text: 'Developed countries',
        value: 'developed_countries',
        score: 6,
        productRecommendations: ['trade_finance_products.md'],
        tags: ['developed_countries', 'lower_risk']
      },
      {
        id: 'developing_countries',
        text: 'Developing countries',
        value: 'developing_countries',
        score: 8,
        productRecommendations: ['trade_finance_products.md#10'],
        tags: ['developing_countries', 'higher_security']
      },
      {
        id: 'multiple_countries',
        text: 'Multiple countries',
        value: 'multiple_countries',
        score: 9,
        productRecommendations: ['cash_management.md#5', 'global_markets.md#5'],
        tags: ['multiple_countries', 'multi_currency', 'complex_fx']
      }
    ]
  },
  {
    id: 'B.1.3',
    category: 'trade_finance',
    subcategory: 'export_activities',
    text: 'Do you export products to other countries?',
    description: 'This determines export financing and collection services needed.',
    type: 'single',
    required: false,
    order: 8,
    weight: 1.0,
    options: [
      {
        id: 'yes_exports',
        text: 'Yes',
        value: 'yes_exports',
        score: 8,
        productRecommendations: ['trade_finance_products.md#3', 'trade_finance_products.md#4', 'trade_finance_products.md#16', 'trade_finance_products.md#7'],
        tags: ['exports', 'export_financing', 'collections']
      },
      {
        id: 'no_exports',
        text: 'No',
        value: 'no_exports',
        score: 2,
        productRecommendations: [],
        tags: ['no_exports']
      }
    ]
  },
  {
    id: 'B.1.4',
    category: 'trade_finance',
    subcategory: 'transaction_value',
    text: 'Typical import/export transaction value range',
    description: 'Transaction size determines appropriate financing structures.',
    type: 'single',
    required: false,
    order: 9,
    weight: 0.9,
    options: [
      {
        id: 'under_50k',
        text: '< $50K',
        value: 'under_50k',
        score: 5,
        productRecommendations: ['trade_finance_products.md#5'],
        tags: ['small_transactions', 'simple_trade']
      },
      {
        id: '50k_500k',
        text: '$50K-$500K',
        value: '50k_500k',
        score: 7,
        productRecommendations: ['trade_finance_products.md'],
        tags: ['medium_transactions', 'standard_trade']
      },
      {
        id: 'over_500k',
        text: '> $500K',
        value: 'over_500k',
        score: 9,
        productRecommendations: ['trade_finance_products.md', 'trade_finance_products.md#12'],
        tags: ['large_transactions', 'complex_trade', 'guarantees']
      }
    ]
  },
  {
    id: 'B.1.5',
    category: 'trade_finance',
    subcategory: 'payment_methods',
    text: 'How do you currently pay overseas suppliers?',
    description: 'This helps optimize payment and financing solutions.',
    type: 'single',
    required: false,
    order: 10,
    weight: 1.0,
    options: [
      {
        id: 'open_account',
        text: 'Open Account',
        value: 'open_account',
        score: 7,
        productRecommendations: ['trade_finance_products.md#2', 'global_markets.md', 'cash_management.md#1'],
        tags: ['open_account', 'trust_based']
      },
      {
        id: 'letters_of_credit',
        text: 'Letters of Credit',
        value: 'letters_of_credit',
        score: 8,
        productRecommendations: ['trade_finance_products.md#10', 'trade_finance_products.md#14'],
        tags: ['letters_of_credit', 'documentary_trade']
      },
      {
        id: 'collections',
        text: 'Collections',
        value: 'collections',
        score: 7,
        productRecommendations: ['trade_finance_products.md#5', 'trade_finance_products.md#6'],
        tags: ['collections', 'documentary_trade']
      },
      {
        id: 'wire_transfers',
        text: 'Wire transfers',
        value: 'wire_transfers',
        score: 6,
        productRecommendations: ['cash_management.md#1', 'global_markets.md'],
        tags: ['wire_transfers', 'simple_payments']
      }
    ]
  },

  // C. CASH MANAGEMENT NEEDS DISCOVERY
  {
    id: 'C.1.1',
    category: 'cash_management',
    subcategory: 'payment_volume',
    text: 'Monthly international payments volume',
    description: 'This determines the level of cash management services needed.',
    type: 'single',
    required: false,
    order: 11,
    weight: 0.8,
    options: [
      {
        id: 'under_10_payments',
        text: '< 10 payments',
        value: 'under_10_payments',
        score: 4,
        productRecommendations: ['cash_management.md#1'],
        tags: ['low_volume', 'basic_services']
      },
      {
        id: '10_50_payments',
        text: '10-50 payments',
        value: '10_50_payments',
        score: 6,
        productRecommendations: ['cash_management.md#4', 'cash_management.md#5'],
        tags: ['medium_volume', 'cash_management']
      },
      {
        id: 'over_50_payments',
        text: '> 50 payments',
        value: 'over_50_payments',
        score: 8,
        productRecommendations: ['cash_management.md'],
        tags: ['high_volume', 'comprehensive_cash_management']
      }
    ]
  },
  {
    id: 'C.1.2',
    category: 'cash_management',
    subcategory: 'currencies',
    text: 'Currencies typically dealt in',
    description: 'This determines foreign currency and FX services needed.',
    type: 'single',
    required: false,
    order: 12,
    weight: 0.9,
    options: [
      {
        id: 'single_foreign_currency',
        text: 'Single foreign currency',
        value: 'single_foreign_currency',
        score: 6,
        productRecommendations: ['cash_management.md#5', 'global_markets.md#3'],
        tags: ['single_currency', 'basic_fx']
      },
      {
        id: 'multiple_currencies',
        text: 'Multiple currencies',
        value: 'multiple_currencies',
        score: 8,
        productRecommendations: ['cash_management.md#5', 'global_markets.md#5'],
        tags: ['multi_currency', 'complex_fx']
      },
      {
        id: 'local_currency_only',
        text: 'Local currency only',
        value: 'local_currency_only',
        score: 3,
        productRecommendations: ['cash_management.md#4'],
        tags: ['local_currency', 'domestic']
      }
    ]
  },
  {
    id: 'C.1.3',
    category: 'cash_management',
    subcategory: 'foreign_accounts',
    text: 'Maintain foreign currency accounts?',
    description: 'This determines account structure and currency management needs.',
    type: 'single',
    required: false,
    order: 13,
    weight: 0.7,
    options: [
      {
        id: 'yes_foreign_accounts',
        text: 'Yes',
        value: 'yes_foreign_accounts',
        score: 7,
        productRecommendations: ['cash_management.md#5'],
        tags: ['foreign_accounts', 'multi_currency']
      },
      {
        id: 'no_foreign_accounts',
        text: 'No',
        value: 'no_foreign_accounts',
        score: 4,
        productRecommendations: ['global_markets.md', 'global_markets.md#5'],
        tags: ['no_foreign_accounts', 'fx_conversion']
      }
    ]
  },

  // D. GLOBAL MARKETS & HEDGING NEEDS
  {
    id: 'D.1.1',
    category: 'global_markets',
    subcategory: 'fx_exposure',
    text: 'Percentage of revenues/costs in foreign currencies',
    description: 'This determines the level of FX hedging needed.',
    type: 'single',
    required: false,
    order: 14,
    weight: 1.2,
    options: [
      {
        id: 'under_20_percent',
        text: '< 20%',
        value: 'under_20_percent',
        score: 5,
        productRecommendations: ['global_markets.md#3'],
        tags: ['low_fx_exposure', 'basic_fx']
      },
      {
        id: '20_50_percent',
        text: '20-50%',
        value: '20_50_percent',
        score: 7,
        productRecommendations: ['global_markets.md#5'],
        tags: ['medium_fx_exposure', 'hedging']
      },
      {
        id: 'over_50_percent',
        text: '> 50%',
        value: 'over_50_percent',
        score: 9,
        productRecommendations: ['global_markets.md#9', 'global_markets.md#5'],
        tags: ['high_fx_exposure', 'complex_hedging']
      }
    ]
  },
  {
    id: 'D.1.2',
    category: 'global_markets',
    subcategory: 'fx_risk',
    text: 'Exposed to FX rate fluctuations?',
    description: 'This determines hedging strategy requirements.',
    type: 'single',
    required: false,
    order: 15,
    weight: 1.1,
    options: [
      {
        id: 'yes_fx_exposure',
        text: 'Yes',
        value: 'yes_fx_exposure',
        score: 8,
        productRecommendations: ['global_markets.md#5', 'global_markets.md#7'],
        tags: ['fx_exposure', 'hedging_needed']
      },
      {
        id: 'no_fx_exposure',
        text: 'No',
        value: 'no_fx_exposure',
        score: 3,
        productRecommendations: ['global_markets.md#3'],
        tags: ['no_fx_exposure', 'spot_only']
      }
    ]
  },

  // E. LENDING NEEDS DISCOVERY
  {
    id: 'E.1.1',
    category: 'lending',
    subcategory: 'working_capital',
    text: 'Experience seasonal cash flow fluctuations?',
    description: 'This determines working capital financing needs.',
    type: 'single',
    required: false,
    order: 16,
    weight: 1.0,
    options: [
      {
        id: 'yes_seasonal',
        text: 'Yes',
        value: 'yes_seasonal',
        score: 7,
        productRecommendations: ['loans.md#2'],
        tags: ['seasonal', 'working_capital', 'flexible_financing']
      },
      {
        id: 'no_seasonal',
        text: 'No',
        value: 'no_seasonal',
        score: 5,
        productRecommendations: ['loans.md#1'],
        tags: ['stable_cash_flow', 'term_financing']
      }
    ]
  },
  {
    id: 'E.1.2',
    category: 'lending',
    subcategory: 'cash_conversion',
    text: 'Cash conversion cycle duration',
    description: 'This determines the type of working capital financing needed.',
    type: 'single',
    required: false,
    order: 17,
    weight: 1.0,
    options: [
      {
        id: 'under_30_days',
        text: '< 30 days',
        value: 'under_30_days',
        score: 5,
        productRecommendations: ['loans.md#3'],
        tags: ['short_cycle', 'overdrafts']
      },
      {
        id: '30_90_days',
        text: '30-90 days',
        value: '30_90_days',
        score: 7,
        productRecommendations: ['loans.md#2'],
        tags: ['medium_cycle', 'revolving_credit']
      },
      {
        id: 'over_90_days',
        text: '> 90 days',
        value: 'over_90_days',
        score: 8,
        productRecommendations: ['loans.md#1', 'trade_finance_products.md'],
        tags: ['long_cycle', 'term_financing']
      }
    ]
  },
  {
    id: 'E.1.3',
    category: 'lending',
    subcategory: 'working_capital_gaps',
    text: 'Need financing to bridge working capital gaps?',
    description: 'This determines if working capital financing is needed.',
    type: 'single',
    required: false,
    order: 18,
    weight: 1.0,
    options: [
      {
        id: 'yes_working_capital',
        text: 'Yes',
        value: 'yes_working_capital',
        score: 8,
        productRecommendations: ['loans.md#2', 'loans.md#3'],
        tags: ['working_capital_needed', 'gap_financing']
      },
      {
        id: 'no_working_capital',
        text: 'No',
        value: 'no_working_capital',
        score: 3,
        productRecommendations: [],
        tags: ['no_working_capital_needs']
      }
    ]
  },
  {
    id: 'E.2.1',
    category: 'lending',
    subcategory: 'capital_expenditure',
    text: 'Planning major capital investments?',
    description: 'This determines if long-term financing is needed.',
    type: 'single',
    required: false,
    order: 19,
    weight: 1.0,
    options: [
      {
        id: 'yes_capex',
        text: 'Yes',
        value: 'yes_capex',
        score: 8,
        productRecommendations: ['loans.md#1'],
        tags: ['capex', 'term_financing', 'equipment']
      },
      {
        id: 'no_capex',
        text: 'No',
        value: 'no_capex',
        score: 4,
        productRecommendations: ['loans.md#2'],
        tags: ['no_capex', 'working_capital_focus']
      }
    ]
  }
]

import { getProductFamily, getProductCategory } from './products-utils'

// Core recommendation calculation logic
export const calculateProductRecommendations = (userProfile: UserProfile): ProductRecommendation[] => {
  const productScores: Record<string, number> = {}
  const productReasons: Record<string, string[]> = {}

  // Calculate scores based on answers
  userProfile.answers.forEach(answer => {
    const question = questions.find(q => q.id === answer.questionId)
    if (!question) return

    answer.selectedOptions.forEach(optionId => {
      const option = question.options.find(o => o.id === optionId)
      if (!option) return

      // Add base score
      const baseScore = option.score * question.weight * CATEGORY_WEIGHTS[question.category as keyof typeof CATEGORY_WEIGHTS] || 1

      // Expand product recommendations (handle category-level recommendations)
      const expandedProducts = expandProductRecommendations(option.productRecommendations)

      // Add product recommendations
      expandedProducts.forEach(productId => {
        const family = getProductFamily(productId)
        const weight = PRODUCT_WEIGHTS[family as keyof typeof PRODUCT_WEIGHTS] || 1
        const score = baseScore * weight

        if (!productScores[productId]) {
          productScores[productId] = 0
          productReasons[productId] = []
        }

        productScores[productId] += score
        productReasons[productId].push(`${question.text}: ${option.text}`)
      })
    })
  })

  console.log('Product scores:', productScores)
  // Convert to array and sort by score
  const recommendations: ProductRecommendation[] = Object.keys(productScores).map(productId => ({
    productId,
    score: productScores[productId],
    reason: productReasons[productId].join('; '),
    category: getProductCategory(productId),
    family: getProductFamily(productId)
  }))

  return recommendations.sort((a, b) => b.score - a.score)
} 
