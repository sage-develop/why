import { useEffect, useState } from 'react'
import { useForm } from 'react-hook-form'
import {
  calculateProductRecommendations,
  questions,
  type ProductRecommendation,
  type Question,
  type UserAnswer,
  type UserProfile
} from './questions'
import {
  getNextQuestion,
  getQuestionProgress,
  updateUserProfile
} from './questions-utils'
import ProductDetail from './ProductDetail'
import {
  getProductName,
  getProductShortDescription
} from './products-utils'

interface FormData {
  selectedOption: string
}

function App() {
  const [userProfile, setUserProfile] = useState<UserProfile>({
    answers: [],
    tags: [],
    preferences: {}
  })
  const [currentQuestion, setCurrentQuestion] = useState<Question | null>(questions[0])
  const [recommendations, setRecommendations] = useState<ProductRecommendation[]>([])
  const [isLoading, setIsLoading] = useState(false)
  const [showAllProducts, setShowAllProducts] = useState(false)
  const [selectedProduct, setSelectedProduct] = useState<string | null>(null)

  const { register, handleSubmit, reset, formState: { errors } } = useForm<FormData>()

  // Update recommendations when user profile changes
  useEffect(() => {
    if (userProfile.answers.length > 0) {
      const newRecommendations = calculateProductRecommendations(userProfile)
      console.log(newRecommendations)
      setRecommendations(newRecommendations)
    }
  }, [userProfile])

  // Get next question when current question is answered
  useEffect(() => {
    const answeredQuestionIds = userProfile.answers.map(a => a.questionId)
    const nextQuestion = getNextQuestion(answeredQuestionIds)
    setCurrentQuestion(nextQuestion)

    if (nextQuestion) {
      reset() // Reset form for new question
    }
  }, [userProfile.answers, reset])

  const handleAnswerSubmit = (data: FormData) => {
    if (!currentQuestion) return

    setIsLoading(true)

    const answer: UserAnswer = {
      questionId: currentQuestion.id,
      selectedOptions: [data.selectedOption],
      answeredAt: new Date()
    }

    const updatedProfile = updateUserProfile(userProfile, answer)
    setUserProfile(updatedProfile)

    // Simulate loading delay for better UX
    setTimeout(() => {
      setIsLoading(false)
    }, 500)
  }

  const handleSkipQuestion = () => {
    if (!currentQuestion) return

    const answer: UserAnswer = {
      questionId: currentQuestion.id,
      selectedOptions: [],
      answeredAt: new Date()
    }

    const updatedProfile = updateUserProfile(userProfile, answer)
    setUserProfile(updatedProfile)
  }

  const handleProductClick = (productId: string) => {
    setSelectedProduct(productId)
  }

  const handleBackToRecommendations = () => {
    setSelectedProduct(null)
  }

  const progress = getQuestionProgress(userProfile.answers.map(a => a.questionId))
  const isComplete = progress === 100

  // Get top 8 recommendations for main section
  const topRecommendations = recommendations.slice(0, 8)
  const additionalRecommendations = recommendations.slice(8)

  // If a product is selected, show the product detail page
  if (selectedProduct) {
    return (
      <ProductDetail
        productId={selectedProduct}
        onBack={handleBackToRecommendations}
      />
    )
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="container mx-auto px-4 py-8">
        <div className="max-w-6xl mx-auto">
          {/* Header */}
          <div className="text-center mb-8">
            <h1 className="text-4xl font-bold text-gray-900 mb-2">
              Corporate Banking Discovery
            </h1>
            <p className="text-lg text-gray-600">
              Answer a few questions to discover the best banking solutions for your business
            </p>
          </div>

          <div className="grid lg:grid-cols-2 gap-8">
            {/* Question Section */}
            <div className="bg-white rounded-xl shadow-lg p-6">
              <div className="mb-6">
                <div className="flex items-center justify-between mb-4">
                  <h2 className="text-2xl font-semibold text-gray-900">
                    {isComplete ? 'All Questions Completed!' : 'Current Question'}
                  </h2>
                  <div className="text-sm text-gray-500">
                    {progress}% Complete
                  </div>
                </div>

                {/* Progress Bar */}
                <div className="w-full bg-gray-200 rounded-full h-2">
                  <div
                    className="bg-blue-600 h-2 rounded-full transition-all duration-300"
                    style={{ width: `${progress}%` }}
                  />
                </div>
              </div>

              {currentQuestion && !isComplete ? (
                <form onSubmit={handleSubmit(handleAnswerSubmit)} className="space-y-6">
                  <div>
                    <h3 className="text-xl font-medium text-gray-900 mb-2">
                      {currentQuestion.text}
                    </h3>
                    {currentQuestion.description && (
                      <p className="text-gray-600 mb-4">
                        {currentQuestion.description}
                      </p>
                    )}
                  </div>

                  <div className="space-y-3">
                    {currentQuestion.options.map((option) => (
                      <label
                        key={option.id}
                        className="flex items-center p-4 border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-50 transition-colors"
                      >
                        <input
                          type="radio"
                          value={option.id}
                          {...register('selectedOption', { required: 'Please select an option' })}
                          className="mr-3 text-blue-600 focus:ring-blue-500"
                        />
                        <span className="text-gray-900">{option.text}</span>
                      </label>
                    ))}
                  </div>

                  {errors.selectedOption && (
                    <p className="text-red-600 text-sm">
                      {errors.selectedOption.message}
                    </p>
                  )}

                  <div className="flex gap-3 pt-4">
                    <button
                      type="submit"
                      disabled={isLoading}
                      className="flex-1 bg-blue-600 text-white py-3 px-6 rounded-lg font-medium hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                    >
                      {isLoading ? 'Processing...' : 'Continue'}
                    </button>

                    {!currentQuestion.required && (
                      <button
                        type="button"
                        onClick={handleSkipQuestion}
                        disabled={isLoading}
                        className="px-6 py-3 border border-gray-300 text-gray-700 rounded-lg font-medium hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
                      >
                        Skip
                      </button>
                    )}
                  </div>
                </form>
              ) : (
                <div className="text-center py-8">
                  <div className="text-green-600 text-6xl mb-4">✓</div>
                  <h3 className="text-xl font-medium text-gray-900 mb-2">
                    All questions completed!
                  </h3>
                  <p className="text-gray-600">
                    Your personalized product recommendations are ready below.
                  </p>
                </div>
              )}
            </div>

            {/* Product Recommendations Section */}
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
                      onClick={() => handleProductClick(recommendation.productId)}
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
                              onClick={() => handleProductClick(recommendation.productId)}
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
          </div>

          {/* User Profile Summary */}
          {userProfile.tags.length > 0 && (
            <div className="mt-8 bg-white rounded-xl shadow-lg p-6">
              <h3 className="text-lg font-semibold text-gray-900 mb-4">
                Your Business Profile
              </h3>
              <div className="flex flex-wrap gap-2">
                {userProfile.tags.map((tag) => (
                  <span
                    key={tag}
                    className="bg-gray-100 text-gray-700 px-3 py-1 rounded-full text-sm"
                  >
                    {tag.replace(/_/g, ' ')}
                  </span>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}

export default App 
