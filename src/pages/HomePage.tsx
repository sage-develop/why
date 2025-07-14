import { useNavigate } from 'react-router-dom'
import { useQuestionStore } from '../store'
import {
  AnswerSummary,
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
    getQuestionProgress,
    navigateToQuestion
  } = useQuestionStore()

  const handleProductClick = (productId: string) => {
    navigate(`/product/${encodeURIComponent(productId)}`)
  }

  const handleQuestionSelect = (questionId: string) => {
    navigateToQuestion(questionId)
  }

  // Calculate progress using store method
  const progress = getQuestionProgress()

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="container mx-auto px-4 py-8">
        <div className="max-w-7xl mx-auto">
          <Header />

          {/* First Row: Question Section and Answer Summary - Fixed Height */}
          <div className="grid lg:grid-cols-3 gap-8 mb-8 h-[600px]">
            {/* Question Section */}
            <div className="lg:col-span-2 h-full">
              <QuestionSection
                currentQuestion={currentQuestion}
                progress={progress}
                isLoading={isLoading}
              />
            </div>

            {/* Answer Summary */}
            <div className="lg:col-span-1 h-full">
              <AnswerSummary
                onQuestionSelect={handleQuestionSelect}
                currentQuestionId={currentQuestion?.id}
              />
            </div>
          </div>

          {/* Second Row: Product Recommendations */}
          <div className="mb-8">
            <ProductRecommendations
              recommendations={recommendations}
              userProfile={userProfile}
              onProductClick={handleProductClick}
            />
          </div>

          <UserProfileSummary userProfile={userProfile} />
        </div>
      </div>
    </div>
  )
}

export default HomePage 
