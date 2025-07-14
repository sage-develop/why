import React from 'react'
import { useForm } from 'react-hook-form'
import { type Question } from '../questions'
import { useQuestionStore } from '../store'

interface FormData {
  selectedOption: string
}

interface QuestionSectionProps {
  currentQuestion: Question | null
  isComplete: boolean
  progress: number
  isLoading: boolean
  onSkipQuestion: () => void
}

const QuestionSection: React.FC<QuestionSectionProps> = ({
  currentQuestion,
  isComplete,
  progress,
  isLoading,
  onSkipQuestion
}) => {
  const { register, reset, watch, setValue, formState: { errors } } = useForm<FormData>()
  const {
    navigateToPrevious,
    navigateToNext,
    updateAnswer,
    removeAnswer,
    getCurrentAnswer,
    getCurrentQuestionIndex,
    getTotalQuestions
  } = useQuestionStore()

  const watchedOption = watch('selectedOption')

  // Reset form when question changes and set current answer if exists
  React.useEffect(() => {
    if (currentQuestion) {
      reset()
      const currentAnswer = getCurrentAnswer(currentQuestion.id)
      if (currentAnswer && currentAnswer.selectedOptions.length > 0) {
        setValue('selectedOption', currentAnswer.selectedOptions[0])
      }
    }
  }, [currentQuestion, reset, getCurrentAnswer, setValue])

  // Auto-update recommendations when user changes answer
  React.useEffect(() => {
    if (currentQuestion && watchedOption) {
      const currentAnswer = getCurrentAnswer(currentQuestion.id)
      if (!currentAnswer || currentAnswer.selectedOptions[0] !== watchedOption) {
        // Debounce the update to avoid too many recalculations
        const timeoutId = setTimeout(() => {
          updateAnswer(currentQuestion.id, watchedOption)
        }, 300)

        return () => clearTimeout(timeoutId)
      }
    }
  }, [watchedOption, currentQuestion, updateAnswer, getCurrentAnswer])

  const handleAnswerChange = (optionId: string) => {
    if (currentQuestion) {
      setValue('selectedOption', optionId)
      updateAnswer(currentQuestion.id, optionId)
    }
  }

  const handleClearSelection = () => {
    if (currentQuestion) {
      removeAnswer(currentQuestion.id)
      setValue('selectedOption', '')
    }
  }

  const currentQuestionIndex = getCurrentQuestionIndex()
  const totalQuestions = getTotalQuestions()
  const canNavigatePrevious = currentQuestionIndex > 1
  const canNavigateNext = currentQuestionIndex < totalQuestions

  // Show clear button if there's a saved answer or current selection
  const currentAnswer = currentQuestion ? getCurrentAnswer(currentQuestion.id) : null
  const hasSavedAnswer = currentAnswer?.selectedOptions && currentAnswer.selectedOptions.length > 0
  const hasCurrentSelection = watchedOption && watchedOption.length > 0
  const showClearButton = hasSavedAnswer || hasCurrentSelection

  return (
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

        {/* Navigation Controls */}
        {!isComplete && (
          <div className="flex items-center justify-between mt-4">
            <button
              type="button"
              onClick={navigateToPrevious}
              disabled={!canNavigatePrevious}
              className="flex items-center px-4 py-2 text-sm font-medium text-gray-700 bg-gray-100 rounded-lg hover:bg-gray-200 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
            >
              ← Previous
            </button>

            <div className="text-sm text-gray-500">
              Question {currentQuestionIndex} of {totalQuestions}
            </div>

            <button
              type="button"
              onClick={navigateToNext}
              disabled={!canNavigateNext}
              className="flex items-center px-4 py-2 text-sm font-medium text-gray-700 bg-gray-100 rounded-lg hover:bg-gray-200 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
            >
              Next →
            </button>
          </div>
        )}
      </div>

      {currentQuestion && !isComplete ? (
        <div className="space-y-6">
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
                  {...register('selectedOption')}
                  className="mr-3 text-blue-600 focus:ring-blue-500"
                  onChange={() => handleAnswerChange(option.id)}
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
            {/* Clear Button - show if there's a saved answer or current selection */}
            {showClearButton && (
              <button
                type="button"
                onClick={handleClearSelection}
                disabled={isLoading}
                className="px-4 py-3 border border-red-300 text-red-700 rounded-lg font-medium hover:bg-red-50 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
              >
                Clear
              </button>
            )}
          </div>

          {/* Real-time feedback */}
          {watchedOption && (
            <div className="mt-4 p-3 bg-blue-50 border border-blue-200 rounded-lg">
              <p className="text-sm text-blue-800">
                <span className="font-medium">Live Preview:</span> Your selection will update recommendations in real-time.
              </p>
            </div>
          )}
        </div>
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
  )
}

export default QuestionSection 
