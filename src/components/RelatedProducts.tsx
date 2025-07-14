import { Product } from '../products'

interface ProductWithId extends Product {
  id: string
}

interface RelatedProductsProps {
  products: ProductWithId[]
  onProductClick: (productId: string) => void
  familyName: string
}

const RelatedProducts = ({ products, onProductClick, familyName }: RelatedProductsProps) => {
  if (products.length === 0) {
    return null
  }

  return (
    <div className="bg-white rounded-xl shadow-lg p-6">
      <h3 className="text-xl font-semibold text-gray-900 mb-4">
        Other {familyName} Products
      </h3>
      <div className="grid gap-4">
        {products.map((product) => (
          <div
            key={product.id}
            className="border border-gray-200 rounded-lg p-4 hover:border-blue-300 hover:shadow-md transition-all cursor-pointer"
            onClick={() => onProductClick(product.id)}
            onKeyDown={(e) => {
              if (e.key === 'Enter' || e.key === ' ') {
                onProductClick(product.id)
              }
            }}
            tabIndex={0}
            role="button"
            aria-label={`View details for ${product.name}`}
          >
            <div className="flex items-start justify-between">
              <div className="flex-1">
                <h4 className="font-medium text-gray-900 mb-1">{product.name}</h4>
                <p className="text-sm text-gray-600 mb-2">{product.description}</p>
                <div className="flex flex-wrap gap-1">
                  {product.tags.slice(0, 3).map((tag, index) => (
                    <span
                      key={index}
                      className="inline-block bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded-full"
                    >
                      {tag}
                    </span>
                  ))}
                  {product.tags.length > 3 && (
                    <span className="inline-block bg-gray-100 text-gray-600 text-xs px-2 py-1 rounded-full">
                      +{product.tags.length - 3} more
                    </span>
                  )}
                </div>
              </div>
              <div className="ml-4 flex-shrink-0">
                <div className="text-xs text-gray-500 bg-gray-100 px-2 py-1 rounded">
                  {product.type}
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

export default RelatedProducts 
