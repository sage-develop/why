import React from 'react'
import { questions, type Question } from '../questions'
import { useQuestionStore } from '../store'

interface AnswerSummaryProps {
  onQuestionSelect: (questionId: string) => void
  currentQuestionId?: string
}

const AnswerSummary: React.FC<AnswerSummaryProps> = ({ onQuestionSelect, currentQuestionId }) => {
  const { userProfile, getCurrentAnswer } = useQuestionStore()
  const [openCategory, setOpenCategory] = React.useState<string | null>(null)
  const scrollContainerRef = React.useRef<HTMLDivElement>(null)
  const currentQuestionRef = React.useRef<HTMLDivElement>(null)

  // Show questions that have been visited (including skipped ones) plus the current question
  const visitedQuestions = questions.filter(q =>
    userProfile.answers.some(a => a.questionId === q.id) || q.id === currentQuestionId
  )

  // Auto-open category when current question changes
  React.useEffect(() => {
    if (currentQuestionId) {
      const currentQuestion = questions.find(q => q.id === currentQuestionId)
      if (currentQuestion) {
        setOpenCategory(currentQuestion.category)
      }
    }
  }, [currentQuestionId])

  // Auto-scroll to current question when it changes
  React.useEffect(() => {
    if (currentQuestionId && currentQuestionRef.current && openCategory && scrollContainerRef.current) {
      // Small delay to ensure the category is fully expanded
      const timeoutId = setTimeout(() => {
        const container = scrollContainerRef.current
        const targetElement = currentQuestionRef.current

        if (container && targetElement) {
          const containerRect = container.getBoundingClientRect()
          const targetRect = targetElement.getBoundingClientRect()

          // Calculate the scroll position to center the target element
          const targetTop = targetRect.top - containerRect.top
          const containerHeight = containerRect.height
          const targetHeight = targetRect.height

          const scrollTop = container.scrollTop + targetTop - (containerHeight / 2) + (targetHeight / 2)

          container.scrollTo({
            top: scrollTop,
            behavior: 'smooth'
          })
        }
      }, 100)

      return () => clearTimeout(timeoutId)
    }
  }, [currentQuestionId, openCategory])

  const getAnswerText = (questionId: string) => {
    const answer = getCurrentAnswer(questionId)
    if (!answer || answer.selectedOptions.length === 0) return 'Not answered'

    const question = questions.find(q => q.id === questionId)
    if (!question) return 'Unknown'

    const selectedOption = question.options.find(opt => opt.id === answer.selectedOptions[0])
    return selectedOption?.text || 'Unknown'
  }

  const getCategoryQuestions = () => {
    const categories: Record<string, Question[]> = {}
    visitedQuestions.forEach(question => {
      if (!categories[question.category]) {
        categories[question.category] = []
      }
      categories[question.category].push(question)
    })
    return categories
  }

  const formatCategoryName = (category: string) => {
    return category.split('_').map(word =>
      word.charAt(0).toUpperCase() + word.slice(1)
    ).join(' ')
  }

  const handleCategoryToggle = (category: string) => {
    setOpenCategory(openCategory === category ? null : category)
  }

  if (visitedQuestions.length === 0) {
    return (
      <div className="bg-white rounded-xl shadow-lg p-6 h-[600px] flex flex-col">
        <div className="flex-shrink-0 mb-4">
          <h3 className="text-lg font-semibold text-gray-900">
            Questions Summary
          </h3>
        </div>
        <div className="flex-1 flex items-center justify-center">
          <div className="text-center text-gray-500">
            <p>No questions visited yet</p>
            <p className="text-sm">Start answering questions to see your summary here</p>
          </div>
        </div>
      </div>
    )
  }

  const categoryQuestions = getCategoryQuestions()

  return (
    <div className="bg-white rounded-xl shadow-lg p-6 h-[600px] flex flex-col">
      {/* Header Section - Fixed Height */}
      <div className="flex-shrink-0 mb-4">
        <h3 className="text-lg font-semibold text-gray-900">
          Questions Summary
        </h3>
      </div>

      {/* Main Content - Scrollable */}
      <div ref={scrollContainerRef} className="flex-1 overflow-y-auto pr-2">
        <div className="space-y-2">
          {Object.entries(categoryQuestions).map(([category, questions]) => {
            const isOpen = openCategory === category

            // Count answered and total questions in this category
            const answeredInCategory = questions.filter(q => {
              const answer = getCurrentAnswer(q.id)
              return answer && answer.selectedOptions.length > 0 && q.id !== currentQuestionId
            }).length

            return (
              <div key={category} className="border border-gray-200 rounded-lg overflow-hidden">
                <button
                  onClick={() => handleCategoryToggle(category)}
                  className="w-full flex items-center justify-between p-4 bg-gray-50 hover:bg-gray-100 transition-colors text-left"
                  aria-expanded={isOpen}
                  aria-label={`${isOpen ? 'Collapse' : 'Expand'} ${formatCategoryName(category)} category`}
                >
                  <h4 className="font-medium text-gray-900">
                    {formatCategoryName(category)}
                  </h4>
                  <div className="flex items-center space-x-2">
                    <span className="text-sm text-gray-500">
                      {answeredInCategory}/{questions.length} answered
                    </span>
                    <svg
                      className={`w-5 h-5 text-blue-400 transition-transform ${isOpen ? 'rotate-180' : ''}`}
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                    >
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                    </svg>
                  </div>
                </button>

                {isOpen && (
                  <div className="p-4 bg-white border-t border-gray-200">
                    <div className="space-y-2">
                      {questions.map((question) => {
                        const answerText = getAnswerText(question.id)
                        const isSkipped = answerText === 'Not answered'
                        const isCurrentQuestion = question.id === currentQuestionId
                        const hasAnswer = userProfile.answers.some(a =>
                          a.questionId === question.id && a.selectedOptions.length > 0
                        ) && question.id !== currentQuestionId

                        return (
                          <div
                            key={question.id}
                            ref={isCurrentQuestion ? currentQuestionRef : null}
                            className={`flex items-start justify-between p-3 rounded-lg cursor-pointer transition-colors ${isCurrentQuestion
                              ? 'bg-blue-50 border border-blue-200'
                              : hasAnswer
                                ? 'bg-green-50 hover:bg-green-100'
                                : 'bg-gray-50 hover:bg-gray-100'
                              }`}
                            onClick={() => onQuestionSelect(question.id)}
                            role="button"
                            tabIndex={0}
                            onKeyDown={(e) => {
                              if (e.key === 'Enter' || e.key === ' ') {
                                e.preventDefault()
                                onQuestionSelect(question.id)
                              }
                            }}
                            aria-label={`Review answer for: ${question.text}`}
                            aria-current={isCurrentQuestion ? 'true' : undefined}
                          >
                            <div className="flex-1 min-w-0">
                              <div className="text-sm font-medium text-gray-900 truncate">
                                {question.text}
                              </div>
                              <div className={`text-sm mt-1 ${isSkipped
                                ? 'text-gray-500 italic'
                                : hasAnswer
                                  ? 'text-green-600'
                                  : isCurrentQuestion
                                    ? 'text-blue-600'
                                    : 'text-gray-600'
                                }`}>
                                {answerText}
                              </div>
                            </div>
                            <div className="ml-3 text-xs text-gray-400">
                              {question.id}
                            </div>
                          </div>
                        )
                      })}
                    </div>
                  </div>
                )}
              </div>
            )
          })}
        </div>
      </div>
    </div>
  )
}

export default AnswerSummary 
