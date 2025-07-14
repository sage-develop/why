import React from 'react'
import { questions, type Question } from '../questions'
import { useQuestionStore } from '../store'

interface AnswerSummaryProps {
  onQuestionSelect: (questionId: string) => void
}

const AnswerSummary: React.FC<AnswerSummaryProps> = ({ onQuestionSelect }) => {
  const { userProfile, getCurrentAnswer } = useQuestionStore()
  const [showDetails, setShowDetails] = React.useState(false)

  const answeredQuestions = questions.filter(q =>
    userProfile.answers.some(a => a.questionId === q.id)
  )

  const getAnswerText = (questionId: string) => {
    const answer = getCurrentAnswer(questionId)
    if (!answer || answer.selectedOptions.length === 0) return 'Skipped'

    const question = questions.find(q => q.id === questionId)
    if (!question) return 'Unknown'

    const selectedOption = question.options.find(opt => opt.id === answer.selectedOptions[0])
    return selectedOption?.text || 'Unknown'
  }

  const getCategoryQuestions = () => {
    const categories: Record<string, Question[]> = {}
    answeredQuestions.forEach(question => {
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

  if (answeredQuestions.length === 0) {
    return null
  }

  const categoryQuestions = getCategoryQuestions()

  return (
    <div className="bg-white rounded-xl shadow-lg p-6">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-semibold text-gray-900">
          Your Answers Summary
        </h3>
        <button
          onClick={() => setShowDetails(!showDetails)}
          className="text-sm text-blue-600 hover:text-blue-800 transition-colors"
        >
          {showDetails ? 'Hide' : 'Show'} Details
        </button>
      </div>

      <div className="space-y-4">
        {Object.entries(categoryQuestions).map(([category, questions]) => (
          <div key={category} className="border border-gray-200 rounded-lg p-4">
            <h4 className="font-medium text-gray-900 mb-3">
              {formatCategoryName(category)}
            </h4>

            <div className="space-y-2">
              {questions.map((question) => {
                const answerText = getAnswerText(question.id)
                const isSkipped = answerText === 'Skipped'

                return (
                  <div
                    key={question.id}
                    className="flex items-start justify-between p-3 bg-gray-50 rounded-lg cursor-pointer hover:bg-gray-100 transition-colors"
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
                  >
                    <div className="flex-1 min-w-0">
                      <div className="text-sm font-medium text-gray-900 truncate">
                        {question.text}
                      </div>
                      <div className={`text-sm mt-1 ${isSkipped ? 'text-gray-500 italic' : 'text-blue-600'}`}>
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
        ))}
      </div>

      {showDetails && (
        <div className="mt-4 pt-4 border-t border-gray-200">
          <div className="grid grid-cols-2 gap-4 text-sm text-gray-600">
            <div>
              <span className="font-medium">Total Questions:</span> {questions.length}
            </div>
            <div>
              <span className="font-medium">Answered:</span> {answeredQuestions.length}
            </div>
            <div>
              <span className="font-medium">Skipped:</span> {userProfile.answers.filter(a => a.selectedOptions.length === 0).length}
            </div>
            <div>
              <span className="font-medium">Categories:</span> {Object.keys(categoryQuestions).length}
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

export default AnswerSummary 
