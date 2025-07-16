import React, { useState, useEffect } from 'react'
import { type ProductRecommendation } from '../questions'
import { getProductName, getProductShortDescription } from '../products-utils'

interface ProductRecommendationsProps {
  recommendations: ProductRecommendation[]
  userProfile: { answers: any[] }
  onProductClick: (productId: string) => void
  previousRecommendations?: ProductRecommendation[]
}

const ProductRecommendations: React.FC<ProductRecommendationsProps> = ({
  recommendations,
  userProfile,
  onProductClick,
  previousRecommendations = []
}) => {
  const [showAllProducts, setShowAllProducts] = useState(false)
  const [highlightedProducts, setHighlightedProducts] = useState<Set<string>>(new Set())

  // Get top 8 recommendations for main section
  const topRecommendations = recommendations.slice(0, 8)
  const additionalRecommendations = recommendations.slice(8)

  // Check for new or updated recommendations and highlight them briefly
  useEffect(() => {
    if (previousRecommendations.length > 0) {
      const currentIds = new Set(recommendations.map(r => r.productId))
      const previousIds = new Set(previousRecommendations.map(r => r.productId))

      const newProducts = recommendations.filter(r => !previousIds.has(r.productId))
      const updatedProducts = recommendations.filter(r => {
        const prev = previousRecommendations.find(p => p.productId === r.productId)
        return prev && Math.abs(prev.score - r.score) > 0.1
      })

      const productsToHighlight = [...newProducts, ...updatedProducts].map(r => r.productId)

      if (productsToHighlight.length > 0) {
        setHighlightedProducts(new Set(productsToHighlight))

        // Remove highlight after 3 seconds
        const timeoutId = setTimeout(() => {
          setHighlightedProducts(new Set())
        }, 3000)

        return () => clearTimeout(timeoutId)
      }
    }
  }, [recommendations, previousRecommendations])

  const isHighlighted = (productId: string) => highlightedProducts.has(productId)

  return (
    <div className="bg-white rounded-xl shadow-lg p-6">
      <div className="mb-6">
        <div className="flex items-center justify-between mb-2">
          <h2 className="text-2xl font-semibold text-gray-900">
            Top Product Recommendations
          </h2>
          <div className="flex items-center gap-4 text-sm text-gray-600">
            <span className="bg-blue-100 text-blue-800 px-3 py-1 rounded-full font-medium">
              {topRecommendations.length} products
            </span>
            {additionalRecommendations.length > 0 && (
              <span className="bg-gray-100 text-gray-700 px-3 py-1 rounded-full font-medium">
                +{additionalRecommendations.length} more
              </span>
            )}
          </div>
        </div>
        <p className="text-gray-600">
          {userProfile.answers.length > 0
            ? `Based on your ${userProfile.answers.length} answer${userProfile.answers.length > 1 ? 's' : ''}`
            : 'Answer questions to see personalized product recommendations'
          }
        </p>
      </div>

      {topRecommendations.length > 0 ? (
        <div className="space-y-6">
          {/* Grid layout for better full-width presentation */}
          <div className="grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
            {topRecommendations.map((recommendation) => (
              <div
                key={recommendation.productId}
                className={`border rounded-lg p-4 hover:shadow-md transition-all duration-300 cursor-pointer bg-white ${isHighlighted(recommendation.productId)
                  ? 'border-blue-300 shadow-lg bg-blue-50'
                  : 'border-gray-200'
                  }`}
                onClick={() => onProductClick(recommendation.productId)}
              >
                <div className="flex flex-col h-full">
                  <div className="flex items-center gap-2 mb-3">
                    <span className="text-xs font-medium text-blue-600 bg-blue-100 px-2 py-1 rounded">
                      {recommendation.category}
                    </span>
                    <span className="text-xs text-gray-500">
                      {recommendation.family}
                    </span>
                    {isHighlighted(recommendation.productId) && (
                      <span className="text-xs font-medium text-blue-600 bg-blue-200 px-2 py-1 rounded animate-pulse">
                        Updated
                      </span>
                    )}
                  </div>

                  <div className="flex-1">
                    <h3 className="font-medium text-gray-900 mb-2 line-clamp-2">
                      {getProductName(recommendation.productId)}
                    </h3>
                    <p className="text-sm text-gray-600 line-clamp-3 mb-3">
                      {getProductShortDescription(recommendation.productId)}
                    </p>
                  </div>

                  <div className="flex items-center justify-between mt-auto">
                    <div className="text-right">
                      <div className="text-lg font-bold text-blue-600">
                        {Math.round(recommendation.score)}
                      </div>
                      <div className="text-xs text-gray-500">Score</div>
                    </div>
                    <div className="inline-flex items-center text-sm text-blue-600 hover:text-blue-800 font-medium transition-colors">
                      <span className="text-xs">View Details</span>
                      <svg className="ml-1 w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                      </svg>
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>

          {/* Additional Products Collapsible Section */}
          {additionalRecommendations.length > 0 && (
            <div className="pt-6 border-t border-gray-200">
              <button
                onClick={() => setShowAllProducts(!showAllProducts)}
                className="w-full flex items-center justify-between p-4 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors"
              >
                <div className="flex items-center gap-3">
                  <span className="font-medium text-gray-900">
                    View All Products
                  </span>
                  <div className="flex items-center gap-2 text-sm text-gray-600">
                    <span className="bg-blue-100 text-blue-800 px-2 py-1 rounded-full font-medium">
                      {topRecommendations.length} shown
                    </span>
                    <span className="bg-orange-100 text-orange-800 px-2 py-1 rounded-full font-medium">
                      {additionalRecommendations.length} additional
                    </span>
                  </div>
                </div>
                <svg
                  className={`w-5 h-5 text-gray-500 transition-transform ${showAllProducts ? 'rotate-180' : ''}`}
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                </svg>
              </button>

              {showAllProducts && (
                <div className="mt-4">
                  <div className="mb-4 flex items-center justify-between">
                    <h3 className="text-lg font-medium text-gray-900">
                      All Recommendations ({recommendations.length} total)
                    </h3>
                    <div className="flex items-center gap-2 text-sm text-gray-600">
                      <span className="bg-green-100 text-green-800 px-2 py-1 rounded-full font-medium">
                        {recommendations.length} products
                      </span>
                    </div>
                  </div>
                  <div className="grid md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
                    {additionalRecommendations.map((recommendation) => (
                      <div
                        key={recommendation.productId}
                        className={`border rounded-lg p-3 hover:shadow-md transition-all duration-300 cursor-pointer bg-white ${isHighlighted(recommendation.productId)
                          ? 'border-blue-300 shadow-lg bg-blue-50'
                          : 'border-gray-200'
                          }`}
                        onClick={() => onProductClick(recommendation.productId)}
                      >
                        <div className="flex flex-col h-full">
                          <div className="flex items-center gap-2 mb-2">
                            <span className="text-xs font-medium text-blue-600 bg-blue-100 px-2 py-1 rounded">
                              {recommendation.category}
                            </span>
                            <span className="text-xs text-gray-500">
                              {recommendation.family}
                            </span>
                            {isHighlighted(recommendation.productId) && (
                              <span className="text-xs font-medium text-blue-600 bg-blue-200 px-2 py-1 rounded animate-pulse">
                                Updated
                              </span>
                            )}
                          </div>

                          <div className="flex-1">
                            <h4 className="text-sm font-medium text-gray-900 mb-2 line-clamp-2">
                              {getProductName(recommendation.productId)}
                            </h4>
                            <p className="text-xs text-gray-600 line-clamp-3 mb-2">
                              {getProductShortDescription(recommendation.productId)}
                            </p>
                          </div>

                          <div className="flex items-center justify-between mt-auto">
                            <div className="text-right">
                              <div className="text-sm font-bold text-blue-600">
                                {Math.round(recommendation.score)}
                              </div>
                              <div className="text-xs text-gray-500">Score</div>
                            </div>
                            <div className="inline-flex items-center text-xs text-blue-600 hover:text-blue-800 font-medium transition-colors">
                              <span>View</span>
                              <svg className="ml-1 w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                              </svg>
                            </div>
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          )}
        </div>
      ) : (
        <div className="text-center py-12">
          <div className="text-gray-400 text-4xl mb-4">📋</div>
          <h3 className="text-lg font-medium text-gray-900 mb-2">
            No recommendations yet
          </h3>
          <p className="text-gray-600">
            Start answering questions to see personalized product recommendations.
          </p>
        </div>
      )}
    </div>
  )
}

export default ProductRecommendations 
