import { useNavigate } from 'react-router-dom'
import { useQuestionStore } from '../store'
import {
  Header,
  ProductRecommendations,
  QuestionSection,
  UserProfileSummary
} from '../components'

const HomePage = () => {
  const navigate = useNavigate()
  const {
    userProfile,
    currentQuestion,
    recommendations,
    isLoading,
    skipQuestion,
    getQuestionProgress
  } = useQuestionStore()

  const handleSkipQuestion = () => {
    skipQuestion()
  }

  const handleProductClick = (productId: string) => {
    navigate(`/product/${encodeURIComponent(productId)}`)
  }

  // Calculate progress using store method
  const progress = getQuestionProgress()
  const isComplete = progress === 100

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="container mx-auto px-4 py-8">
        <div className="max-w-7xl mx-auto">
          <Header />

          <div className="grid lg:grid-cols-3 gap-8">
            {/* Question Section */}
            <div className="lg:col-span-2">
              <QuestionSection
                currentQuestion={currentQuestion}
                isComplete={isComplete}
                progress={progress}
                isLoading={isLoading}
                onSkipQuestion={handleSkipQuestion}
              />
            </div>

            {/* Sidebar with Navigation and Recommendations */}
            <div className="space-y-6">
              {/* Product Recommendations */}
              <ProductRecommendations
                recommendations={recommendations}
                userProfile={userProfile}
                onProductClick={handleProductClick}
              />
            </div>
          </div>

          <UserProfileSummary userProfile={userProfile} />
        </div>
      </div>
    </div>
  )
}

export default HomePage 
