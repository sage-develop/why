import React, { useState } from 'react'
import { type ProductRecommendation } from '../questions'
import { getProductName, getProductShortDescription } from '../products-utils'

interface ProductRecommendationsProps {
  recommendations: ProductRecommendation[]
  userProfile: { answers: any[] }
  onProductClick: (productId: string) => void
}

const ProductRecommendations: React.FC<ProductRecommendationsProps> = ({
  recommendations,
  userProfile,
  onProductClick
}) => {
  const [showAllProducts, setShowAllProducts] = useState(false)

  // Get top 8 recommendations for main section
  const topRecommendations = recommendations.slice(0, 8)
  const additionalRecommendations = recommendations.slice(8)

  return (
    <div className="bg-white rounded-xl shadow-lg p-6">
      <div className="mb-6">
        <h2 className="text-2xl font-semibold text-gray-900 mb-2">
          Top Product Recommendations
        </h2>
        <p className="text-gray-600">
          {userProfile.answers.length > 0
            ? `Based on your ${userProfile.answers.length} answer${userProfile.answers.length > 1 ? 's' : ''}`
            : 'Answer questions to see personalized product recommendations'
          }
        </p>
      </div>

      {topRecommendations.length > 0 ? (
        <div className="space-y-4">
          {topRecommendations.map((recommendation, index) => (
            <div
              key={recommendation.productId}
              className="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow cursor-pointer"
              onClick={() => onProductClick(recommendation.productId)}
            >
              <div className="flex items-start justify-between mb-2">
                <div className="flex-1">
                  <div className="flex items-center gap-2 mb-1">
                    <span className="text-sm font-medium text-blue-600 bg-blue-100 px-2 py-1 rounded">
                      {recommendation.category}
                    </span>
                    <span className="text-sm text-gray-500">
                      {recommendation.family}
                    </span>
                  </div>
                  <h3 className="font-medium text-gray-900 mb-1">
                    {getProductName(recommendation.productId)}
                  </h3>
                  <p className="text-sm text-gray-600 line-clamp-2">
                    {getProductShortDescription(recommendation.productId)}
                  </p>
                </div>
                <div className="text-right">
                  <div className="text-lg font-bold text-blue-600">
                    {Math.round(recommendation.score)}
                  </div>
                  <div className="text-xs text-gray-500">Score</div>
                </div>
              </div>
              {/* Product Detail Link */}
              <div className="mt-3 pt-3 border-t border-gray-100">
                <div className="inline-flex items-center text-sm text-blue-600 hover:text-blue-800 font-medium transition-colors">
                  <span>View Product Details</span>
                  <svg className="ml-1 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                  </svg>
                </div>
              </div>
            </div>
          ))}

          {/* Additional Products Collapsible Section */}
          {additionalRecommendations.length > 0 && (
            <div className="mt-6 pt-6 border-t border-gray-200">
              <button
                onClick={() => setShowAllProducts(!showAllProducts)}
                className="w-full flex items-center justify-between p-4 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors"
              >
                <span className="font-medium text-gray-900">
                  View All Products ({recommendations.length} total)
                </span>
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
                <div className="mt-4 space-y-3">
                  {additionalRecommendations.map((recommendation) => (
                    <div
                      key={recommendation.productId}
                      className="border border-gray-200 rounded-lg p-3 hover:shadow-md transition-shadow cursor-pointer"
                      onClick={() => onProductClick(recommendation.productId)}
                    >
                      <div className="flex items-start justify-between mb-2">
                        <div className="flex-1">
                          <div className="flex items-center gap-2 mb-1">
                            <span className="text-xs font-medium text-blue-600 bg-blue-100 px-2 py-1 rounded">
                              {recommendation.category}
                            </span>
                            <span className="text-xs text-gray-500">
                              {recommendation.family}
                            </span>
                          </div>
                          <h4 className="text-sm font-medium text-gray-900 mb-1">
                            {getProductName(recommendation.productId)}
                          </h4>
                          <p className="text-xs text-gray-600 line-clamp-2">
                            {getProductShortDescription(recommendation.productId)}
                          </p>
                        </div>
                        <div className="text-right">
                          <div className="text-sm font-bold text-blue-600">
                            {Math.round(recommendation.score)}
                          </div>
                          <div className="text-xs text-gray-500">Score</div>
                        </div>
                      </div>
                      {/* Product Detail Link */}
                      <div className="mt-2 pt-2 border-t border-gray-100">
                        <div className="inline-flex items-center text-xs text-blue-600 hover:text-blue-800 font-medium transition-colors">
                          <span>View Details</span>
                          <svg className="ml-1 w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                          </svg>
                        </div>
                      </div>
                    </div>
                  ))}
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
