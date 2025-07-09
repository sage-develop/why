import { useEffect, useState } from 'react'
import ProductDetail from './ProductDetail'
import {
  Header,
  ProductRecommendations,
  QuestionSection,
  UserProfileSummary
} from './components'
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
  const [selectedProduct, setSelectedProduct] = useState<string | null>(null)

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
  }, [userProfile.answers])

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
          <Header />

          <div className="grid lg:grid-cols-2 gap-8">
            <QuestionSection
              currentQuestion={currentQuestion}
              isComplete={isComplete}
              progress={progress}
              isLoading={isLoading}
              onAnswerSubmit={handleAnswerSubmit}
              onSkipQuestion={handleSkipQuestion}
            />

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

export default App 
