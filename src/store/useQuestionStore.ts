import { create } from 'zustand'
import { questions, type Question, type UserAnswer, type UserProfile, type ProductRecommendation, calculateProductRecommendations } from '../questions'
import { getNextQuestion, updateUserProfile } from '../questions-utils'

interface QuestionState {
  // State
  userProfile: UserProfile
  currentQuestion: Question | null
  recommendations: ProductRecommendation[]
  previousRecommendations: ProductRecommendation[] // Track previous state for changes
  isLoading: boolean
  questionHistory: Question[] // Track all questions for navigation
  currentQuestionIndex: number // Track current position in question flow

  // Actions
  initializeQuestion: () => void
  submitAnswer: (selectedOption: string) => void
  skipQuestion: () => void
  resetAnswers: () => void
  setLoading: (loading: boolean) => void
  navigateToQuestion: (questionId: string) => void
  navigateToPrevious: () => void
  navigateToNext: () => void
  updateAnswer: (questionId: string, selectedOption: string) => void
  removeAnswer: (questionId: string) => void
  getCurrentAnswer: (questionId: string) => UserAnswer | null
  getQuestionProgress: () => number
  getAnsweredQuestions: () => string[]
  getUnansweredQuestions: () => string[]
  getCurrentQuestionIndex: () => number
  getTotalQuestions: () => number
}

const useQuestionStore = create<QuestionState>((set, get) => ({
  // Initial state
  userProfile: {
    answers: [],
    tags: [],
    preferences: {}
  },
  currentQuestion: questions[0],
  recommendations: [],
  previousRecommendations: [],
  isLoading: false,
  questionHistory: [questions[0]],
  currentQuestionIndex: 0,

  // Actions
  initializeQuestion: () => {
    const { userProfile } = get()
    const answeredQuestionIds = userProfile.answers.map(a => a.questionId)
    const nextQuestion = getNextQuestion(answeredQuestionIds)

    set({
      currentQuestion: nextQuestion,
      questionHistory: nextQuestion ? [nextQuestion] : [],
      currentQuestionIndex: 0
    })
  },

  submitAnswer: (selectedOption: string) => {
    const { userProfile, currentQuestion, recommendations } = get()

    if (!currentQuestion) return

    set({ isLoading: true })

    const answer: UserAnswer = {
      questionId: currentQuestion.id,
      selectedOptions: [selectedOption],
      answeredAt: new Date()
    }

    const updatedProfile = updateUserProfile(userProfile, answer)
    const newRecommendations = calculateProductRecommendations(updatedProfile)

    // Get next question
    const answeredQuestionIds = updatedProfile.answers.map(a => a.questionId)
    const nextQuestion = getNextQuestion(answeredQuestionIds)

    // Update question history
    const { questionHistory, currentQuestionIndex } = get()
    const newQuestionHistory = [...questionHistory]
    if (nextQuestion && !newQuestionHistory.find(q => q.id === nextQuestion.id)) {
      newQuestionHistory.push(nextQuestion)
    }

    // Simulate loading delay for better UX
    setTimeout(() => {
      set({
        userProfile: updatedProfile,
        recommendations: newRecommendations,
        previousRecommendations: recommendations,
        currentQuestion: nextQuestion,
        questionHistory: newQuestionHistory,
        currentQuestionIndex: currentQuestionIndex + 1,
        isLoading: false
      })
    }, 500)
  },

  skipQuestion: () => {
    const { userProfile, currentQuestion, recommendations } = get()

    if (!currentQuestion) return

    const answer: UserAnswer = {
      questionId: currentQuestion.id,
      selectedOptions: [],
      answeredAt: new Date()
    }

    const updatedProfile = updateUserProfile(userProfile, answer)
    const newRecommendations = calculateProductRecommendations(updatedProfile)

    // Get next question
    const answeredQuestionIds = updatedProfile.answers.map(a => a.questionId)
    const nextQuestion = getNextQuestion(answeredQuestionIds)

    // Update question history
    const { questionHistory, currentQuestionIndex } = get()
    const newQuestionHistory = [...questionHistory]
    if (nextQuestion && !newQuestionHistory.find(q => q.id === nextQuestion.id)) {
      newQuestionHistory.push(nextQuestion)
    }

    set({
      userProfile: updatedProfile,
      recommendations: newRecommendations,
      previousRecommendations: recommendations,
      currentQuestion: nextQuestion,
      questionHistory: newQuestionHistory,
      currentQuestionIndex: currentQuestionIndex + 1
    })
  },

  navigateToQuestion: (questionId: string) => {
    const { userProfile, currentQuestion, recommendations } = get()

    // If there's a current question and it's unanswered, mark it as skipped
    if (currentQuestion) {
      const currentAnswer = userProfile.answers.find(a => a.questionId === currentQuestion.id)
      if (!currentAnswer || currentAnswer.selectedOptions.length === 0) {
        const skipAnswer: UserAnswer = {
          questionId: currentQuestion.id,
          selectedOptions: [],
          answeredAt: new Date()
        }
        const updatedProfile = updateUserProfile(userProfile, skipAnswer)
        const newRecommendations = calculateProductRecommendations(updatedProfile)

        set({
          userProfile: updatedProfile,
          recommendations: newRecommendations,
          previousRecommendations: recommendations
        })
      }
    }

    const question = questions.find(q => q.id === questionId)
    if (!question) return

    const { questionHistory } = get()
    const newQuestionHistory = [...questionHistory]

    // Add to history if not already present
    if (!newQuestionHistory.find(q => q.id === questionId)) {
      newQuestionHistory.push(question)
    }

    const questionIndex = newQuestionHistory.findIndex(q => q.id === questionId)

    set({
      currentQuestion: question,
      questionHistory: newQuestionHistory,
      currentQuestionIndex: questionIndex
    })
  },

  navigateToPrevious: () => {
    const { userProfile, currentQuestion, recommendations } = get()

    if (!currentQuestion) return

    // If current question is unanswered, mark it as skipped
    const currentAnswer = userProfile.answers.find(a => a.questionId === currentQuestion.id)
    if (!currentAnswer || currentAnswer.selectedOptions.length === 0) {
      const skipAnswer: UserAnswer = {
        questionId: currentQuestion.id,
        selectedOptions: [],
        answeredAt: new Date()
      }
      const updatedProfile = updateUserProfile(userProfile, skipAnswer)
      const newRecommendations = calculateProductRecommendations(updatedProfile)

      set({
        userProfile: updatedProfile,
        recommendations: newRecommendations,
        previousRecommendations: recommendations
      })
    }

    // Find current question index in all questions
    const allQuestionIndex = questions.findIndex(q => q.id === currentQuestion.id)

    if (allQuestionIndex > 0) {
      const previousQuestion = questions[allQuestionIndex - 1]
      set({
        currentQuestion: previousQuestion,
        currentQuestionIndex: allQuestionIndex - 1
      })
    }
  },

  navigateToNext: () => {
    const { userProfile, currentQuestion, recommendations } = get()

    if (!currentQuestion) return

    // If current question is unanswered, mark it as skipped
    const currentAnswer = userProfile.answers.find(a => a.questionId === currentQuestion.id)
    if (!currentAnswer || currentAnswer.selectedOptions.length === 0) {
      const skipAnswer: UserAnswer = {
        questionId: currentQuestion.id,
        selectedOptions: [],
        answeredAt: new Date()
      }
      const updatedProfile = updateUserProfile(userProfile, skipAnswer)
      const newRecommendations = calculateProductRecommendations(updatedProfile)

      set({
        userProfile: updatedProfile,
        recommendations: newRecommendations,
        previousRecommendations: recommendations
      })
    }

    // Find current question index in all questions
    const allQuestionIndex = questions.findIndex(q => q.id === currentQuestion.id)

    if (allQuestionIndex < questions.length - 1) {
      const nextQuestion = questions[allQuestionIndex + 1]
      set({
        currentQuestion: nextQuestion,
        currentQuestionIndex: allQuestionIndex + 1
      })
    }
  },

  updateAnswer: (questionId: string, selectedOption: string) => {
    const { userProfile, recommendations } = get()

    const answer: UserAnswer = {
      questionId,
      selectedOptions: [selectedOption],
      answeredAt: new Date()
    }

    const updatedProfile = updateUserProfile(userProfile, answer)
    const newRecommendations = calculateProductRecommendations(updatedProfile)

    set({
      userProfile: updatedProfile,
      recommendations: newRecommendations,
      previousRecommendations: recommendations
    })
  },

  removeAnswer: (questionId: string) => {
    const { userProfile, recommendations } = get()

    const updatedAnswers = userProfile.answers.filter(a => a.questionId !== questionId)
    const updatedProfile = {
      ...userProfile,
      answers: updatedAnswers
    }

    // Recalculate tags
    const newTags: string[] = []
    updatedAnswers.forEach(answer => {
      const question = questions.find(q => q.id === answer.questionId)
      if (question) {
        answer.selectedOptions.forEach((optionId: string) => {
          const option = question.options.find(o => o.id === optionId)
          if (option) {
            newTags.push(...option.tags)
          }
        })
      }
    })

    updatedProfile.tags = [...new Set(newTags)]
    const newRecommendations = calculateProductRecommendations(updatedProfile)

    set({
      userProfile: updatedProfile,
      recommendations: newRecommendations,
      previousRecommendations: recommendations
    })
  },

  getCurrentAnswer: (questionId: string) => {
    const { userProfile } = get()
    return userProfile.answers.find(a => a.questionId === questionId) || null
  },

  getQuestionProgress: () => {
    const { userProfile } = get()
    return Math.round((userProfile.answers.length / questions.length) * 100)
  },

  getAnsweredQuestions: () => {
    const { userProfile } = get()
    return userProfile.answers.map(a => a.questionId)
  },

  getUnansweredQuestions: () => {
    const { userProfile } = get()
    const answeredQuestionIds = userProfile.answers.map(a => a.questionId)
    return questions.filter(q => !answeredQuestionIds.includes(q.id)).map(q => q.id)
  },

  getCurrentQuestionIndex: () => {
    const { currentQuestion } = get()
    if (!currentQuestion) return 0
    return questions.findIndex(q => q.id === currentQuestion.id) + 1
  },

  getTotalQuestions: () => {
    return questions.length
  },

  resetAnswers: () => {
    set({
      userProfile: {
        answers: [],
        tags: [],
        preferences: {}
      },
      currentQuestion: questions[0],
      recommendations: [],
      previousRecommendations: [],
      questionHistory: [questions[0]],
      currentQuestionIndex: 0
    })
  },

  setLoading: (loading: boolean) => {
    set({ isLoading: loading })
  }
}))

export default useQuestionStore 
