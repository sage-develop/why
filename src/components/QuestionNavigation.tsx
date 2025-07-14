import React from 'react'
import { questions } from '../questions'
import { useQuestionStore } from '../store'

interface QuestionNavigationProps {
  currentQuestionId: string
  onQuestionSelect: (questionId: string) => void
}

const QuestionNavigation: React.FC<QuestionNavigationProps> = ({
  currentQuestionId,
  onQuestionSelect
}) => {
  const { getCurrentAnswer, getAnsweredQuestions } = useQuestionStore()
  const answeredQuestions = getAnsweredQuestions()

  const getQuestionStatus = (questionId: string) => {
    const isAnswered = answeredQuestions.includes(questionId)
    const isCurrent = questionId === currentQuestionId

    if (isCurrent) return 'current'
    if (isAnswered) return 'answered'
    return 'unanswered'
  }

  const getQuestionIcon = (status: string) => {
    switch (status) {
      case 'current':
        return '🔵'
      case 'answered':
        return '✅'
      case 'unanswered':
        return '⭕'
      default:
        return '⭕'
    }
  }

  const getQuestionClass = (status: string) => {
    const baseClasses = 'flex items-center p-3 rounded-lg cursor-pointer transition-all duration-200 text-sm'

    switch (status) {
      case 'current':
        return `${baseClasses} bg-blue-100 border-2 border-blue-500 text-blue-900 font-medium`
      case 'answered':
        return `${baseClasses} bg-green-50 border border-green-200 text-green-800 hover:bg-green-100`
      case 'unanswered':
        return `${baseClasses} bg-gray-50 border border-gray-200 text-gray-600 hover:bg-gray-100`
      default:
        return `${baseClasses} bg-gray-50 border border-gray-200 text-gray-600`
    }
  }

  return (
    <div className="bg-white rounded-xl shadow-lg p-6">
      <h3 className="text-lg font-semibold text-gray-900 mb-4">
        Question Navigation
      </h3>

      <div className="space-y-2 max-h-96 overflow-y-auto">
        {questions.map((question) => {
          const status = getQuestionStatus(question.id)
          const icon = getQuestionIcon(status)
          const className = getQuestionClass(status)
          const currentAnswer = getCurrentAnswer(question.id)

          return (
            <div
              key={question.id}
              className={className}
              onClick={() => onQuestionSelect(question.id)}
              role="button"
              tabIndex={0}
              onKeyDown={(e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                  e.preventDefault()
                  onQuestionSelect(question.id)
                }
              }}
              aria-label={`Navigate to question: ${question.text}`}
            >
              <span className="mr-3 text-lg">{icon}</span>
              <div className="flex-1 min-w-0">
                <div className="font-medium truncate">
                  {question.text}
                </div>
                {currentAnswer && (
                  <div className="text-xs text-gray-500 mt-1">
                    Answer: {question.options.find(opt => opt.id === currentAnswer.selectedOptions[0])?.text || 'Skipped'}
                  </div>
                )}
              </div>
            </div>
          )
        })}
      </div>

      <div className="mt-4 pt-4 border-t border-gray-200">
        <div className="flex items-center justify-between text-sm text-gray-600">
          <div className="flex items-center space-x-4">
            <div className="flex items-center">
              <span className="mr-2">🔵</span>
              <span>Current</span>
            </div>
            <div className="flex items-center">
              <span className="mr-2">✅</span>
              <span>Answered</span>
            </div>
            <div className="flex items-center">
              <span className="mr-2">⭕</span>
              <span>Unanswered</span>
            </div>
          </div>
          <div className="text-right">
            <div className="font-medium">
              {answeredQuestions.length} / {questions.length}
            </div>
            <div className="text-xs text-gray-500">Questions answered</div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default QuestionNavigation 
