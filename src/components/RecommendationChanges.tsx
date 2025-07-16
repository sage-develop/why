import React, { useState } from 'react'
import { PRODUCTS } from '../products'
import { type ProductRecommendation } from '../questions'

interface RecommendationChangesProps {
  recommendations: ProductRecommendation[]
  previousRecommendations?: ProductRecommendation[]
}

const RecommendationChanges: React.FC<RecommendationChangesProps> = ({
  recommendations,
  previousRecommendations = [],
}) => {
  const [showChanges, setShowChanges] = useState(false)

  // Compare current recommendations with previous ones
  const getChanges = () => {
    if (!previousRecommendations.length) return null

    const currentIds = new Set(recommendations.map(r => r.productId))
    const previousIds = new Set(previousRecommendations.map(r => r.productId))

    const added = recommendations.filter(r => !previousIds.has(r.productId))
    const removed = previousRecommendations.filter(r => !currentIds.has(r.productId))
    const changed = recommendations.filter(r => {
      const prev = previousRecommendations.find(p => p.productId === r.productId)
      return prev && Math.abs(prev.score - r.score) > 0.1
    })

    return { added, removed, changed }
  }

  const changes = getChanges()

  // If no changes, don't render anything
  if (!changes || (!changes.added.length && !changes.removed.length && !changes.changed.length)) {
    return null
  }

  return (
    <>

      <div className="bg-white rounded-xl shadow-lg p-6">
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center gap-3">
            <h3 className="text-lg font-semibold text-gray-900">
              Recent Changes
            </h3>
            <div className="flex items-center gap-2">
              {changes.added.length > 0 && (
                <span className="bg-green-100 text-green-800 text-xs px-2 py-1 rounded-full font-medium">
                  +{changes.added.length}
                </span>
              )}
              {changes.removed.length > 0 && (
                <span className="bg-red-100 text-red-800 text-xs px-2 py-1 rounded-full font-medium">
                  -{changes.removed.length}
                </span>
              )}
              {changes.changed.length > 0 && (
                <span className="bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded-full font-medium">
                  ↻{changes.changed.length}
                </span>
              )}
            </div>
          </div>
          <button
            onClick={() => setShowChanges(!showChanges)}
            className="text-sm text-blue-600 hover:text-blue-800 transition-colors flex items-center gap-1"
            aria-label={showChanges ? 'Hide change details' : 'Show change details'}
          >
            {showChanges ? 'Hide' : 'Show'} Details
            <svg
              className={`w-4 h-4 transition-transform ${showChanges ? 'rotate-180' : ''}`}
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
            </svg>
          </button>
        </div>

        <div className="space-y-3">
          {changes.added.length > 0 && (
            <div className="flex items-center text-sm">
              <span className="text-green-600 mr-2 font-medium">+</span>
              <span className="text-gray-700">
                {changes.added.length} new recommendation{changes.added.length !== 1 ? 's' : ''}
              </span>
            </div>
          )}

          {changes.removed.length > 0 && (
            <div className="flex items-center text-sm">
              <span className="text-red-600 mr-2 font-medium">-</span>
              <span className="text-gray-700">
                {changes.removed.length} removed recommendation{changes.removed.length !== 1 ? 's' : ''}
              </span>
            </div>
          )}

          {changes.changed.length > 0 && (
            <div className="flex items-center text-sm">
              <span className="text-blue-600 mr-2 font-medium">↻</span>
              <span className="text-gray-700">
                {changes.changed.length} updated recommendation{changes.changed.length !== 1 ? 's' : ''}
              </span>
            </div>
          )}
        </div>

        {showChanges && (
          <div className="mt-4 pt-4 border-t border-gray-200 space-y-3">
            {changes.added.length > 0 && (
              <div>
                <h4 className="font-medium text-green-800 mb-2 flex items-center gap-2">
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                  </svg>
                  New Recommendations:
                </h4>
                <div className="space-y-1">
                  {changes.added.map((rec) => {
                    const product = PRODUCTS[rec.productId]
                    return (
                      <div key={rec.productId} className="text-sm text-green-700 bg-green-50 p-2 rounded border border-green-200">
                        {product ? product.name : rec.productId}
                      </div>
                    )
                  })}
                </div>
              </div>
            )}

            {changes.removed.length > 0 && (
              <div>
                <h4 className="font-medium text-red-800 mb-2 flex items-center gap-2">
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M20 12H4" />
                  </svg>
                  Removed Recommendations:
                </h4>
                <div className="space-y-1">
                  {changes.removed.map((rec) => {
                    const product = PRODUCTS[rec.productId]
                    return (
                      <div key={rec.productId} className="text-sm text-red-700 bg-red-50 p-2 rounded border border-red-200">
                        {product ? product.name : rec.productId}
                      </div>
                    )
                  })}
                </div>
              </div>
            )}

            {changes.changed.length > 0 && (
              <div>
                <h4 className="font-medium text-blue-800 mb-2 flex items-center gap-2">
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                  </svg>
                  Updated Recommendations:
                </h4>
                <div className="space-y-1">
                  {changes.changed.map((rec) => {
                    const prev = previousRecommendations.find(p => p.productId === rec.productId)
                    const product = PRODUCTS[rec.productId]
                    return (
                      <div key={rec.productId} className="text-sm text-blue-700 bg-blue-50 p-2 rounded border border-blue-200">
                        {product ? product.name : rec.productId}
                        <span className="ml-2 text-xs bg-blue-100 px-2 py-1 rounded">
                          Score: {prev?.score.toFixed(1)} → {rec.score.toFixed(1)}
                        </span>
                      </div>
                    )
                  })}
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </>
  )
}

export default RecommendationChanges 
