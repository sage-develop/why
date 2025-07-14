import React from 'react'
import { type ProductRecommendation } from '../questions'

interface RecommendationChangesProps {
  recommendations: ProductRecommendation[]
  previousRecommendations?: ProductRecommendation[]
}

const RecommendationChanges: React.FC<RecommendationChangesProps> = ({
  recommendations,
  previousRecommendations = []
}) => {
  const [showChanges, setShowChanges] = React.useState(false)

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

  if (!changes || (!changes.added.length && !changes.removed.length && !changes.changed.length)) {
    return null
  }

  return (
    <div className="bg-white rounded-xl shadow-lg p-6">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-semibold text-gray-900">
          Recent Changes
        </h3>
        <button
          onClick={() => setShowChanges(!showChanges)}
          className="text-sm text-blue-600 hover:text-blue-800 transition-colors"
        >
          {showChanges ? 'Hide' : 'Show'} Details
        </button>
      </div>

      <div className="space-y-3">
        {changes.added.length > 0 && (
          <div className="flex items-center text-sm">
            <span className="text-green-600 mr-2">+</span>
            <span className="text-gray-700">
              {changes.added.length} new recommendation{changes.added.length !== 1 ? 's' : ''}
            </span>
          </div>
        )}

        {changes.removed.length > 0 && (
          <div className="flex items-center text-sm">
            <span className="text-red-600 mr-2">-</span>
            <span className="text-gray-700">
              {changes.removed.length} removed recommendation{changes.removed.length !== 1 ? 's' : ''}
            </span>
          </div>
        )}

        {changes.changed.length > 0 && (
          <div className="flex items-center text-sm">
            <span className="text-blue-600 mr-2">↻</span>
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
              <h4 className="font-medium text-green-800 mb-2">New Recommendations:</h4>
              <div className="space-y-1">
                {changes.added.map((rec) => (
                  <div key={rec.productId} className="text-sm text-green-700 bg-green-50 p-2 rounded">
                    {rec.reason}
                  </div>
                ))}
              </div>
            </div>
          )}

          {changes.removed.length > 0 && (
            <div>
              <h4 className="font-medium text-red-800 mb-2">Removed Recommendations:</h4>
              <div className="space-y-1">
                {changes.removed.map((rec) => (
                  <div key={rec.productId} className="text-sm text-red-700 bg-red-50 p-2 rounded">
                    {rec.reason}
                  </div>
                ))}
              </div>
            </div>
          )}

          {changes.changed.length > 0 && (
            <div>
              <h4 className="font-medium text-blue-800 mb-2">Updated Recommendations:</h4>
              <div className="space-y-1">
                {changes.changed.map((rec) => {
                  const prev = previousRecommendations.find(p => p.productId === rec.productId)
                  return (
                    <div key={rec.productId} className="text-sm text-blue-700 bg-blue-50 p-2 rounded">
                      {rec.reason}
                      <span className="ml-2 text-xs">
                        (Score: {prev?.score.toFixed(1)} → {rec.score.toFixed(1)})
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
  )
}

export default RecommendationChanges 
