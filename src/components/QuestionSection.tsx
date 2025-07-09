import React from 'react'
import { useForm } from 'react-hook-form'
import { type Question } from '../questions'

interface FormData {
  selectedOption: string
}

interface QuestionSectionProps {
  currentQuestion: Question | null
  isComplete: boolean
  progress: number
  isLoading: boolean
  onAnswerSubmit: (data: FormData) => void
  onSkipQuestion: () => void
}

const QuestionSection: React.FC<QuestionSectionProps> = ({
  currentQuestion,
  isComplete,
  progress,
  isLoading,
  onAnswerSubmit,
  onSkipQuestion
}) => {
  const { register, handleSubmit, reset, formState: { errors } } = useForm<FormData>()

  // Reset form when question changes
  React.useEffect(() => {
    if (currentQuestion) {
      reset()
    }
  }, [currentQuestion, reset])

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
      </div>

      {currentQuestion && !isComplete ? (
        <form onSubmit={handleSubmit(onAnswerSubmit)} className="space-y-6">
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
                onClick={onSkipQuestion}
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
  )
}

export default QuestionSection 
