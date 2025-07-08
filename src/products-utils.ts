import { PRODUCTS, type Product } from './products'

export const getProduct = (productId: string): Product | undefined => {
  return PRODUCTS[productId]
}

export const getProductName = (productId: string): string => {
  const product = PRODUCTS[productId]
  return product ? product.name : productId
}

export const getProductDescription = (productId: string): string => {
  const product = PRODUCTS[productId]
  return product ? product.description : ''
}

export const getProductShortDescription = (productId: string): string => {
  const product = PRODUCTS[productId]
  if (!product) return productId

  return `${product.name} - ${product.description}`
}

export const getProductCategory = (productId: string): string => {
  const product = PRODUCTS[productId]
  if (!product) return 'Other'

  switch (product.family.toLowerCase()) {
    case 'trade':
      return 'Trade Finance'
    case 'cash management':
      return 'Cash Management'
    case 'loans':
      return 'Lending'
    case 'global markets':
      return 'Global Markets'
    case 'insurance':
      return 'Insurance'
    case 'investments':
      return 'Investments'
    default:
      return product.family || 'Other'
  }
}

export const getProductFamily = (productId: string): string => {
  const product = PRODUCTS[productId]
  if (!product) return 'other'

  switch (product.family.toLowerCase()) {
    case 'trade':
      return 'trade_finance'
    case 'cash management':
      return 'cash_management'
    case 'loans':
      return 'loans'
    case 'global markets':
      return 'global_markets'
    case 'insurance':
      return 'insurance'
    case 'investments':
      return 'investments'
    default:
      return 'other'
  }
} 
