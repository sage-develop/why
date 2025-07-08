import { questions, type Question, type UserAnswer, type UserProfile } from './questions'

// Helper functions
export const getNextQuestion = (answeredQuestions: string[]): Question | null => {
  const unansweredQuestions = questions.filter(q => !answeredQuestions.includes(q.id))
  return unansweredQuestions.length > 0 ? unansweredQuestions[0] : null
}

export const updateUserProfile = (profile: UserProfile, answer: UserAnswer): UserProfile => {
  const updatedAnswers = profile.answers.filter(a => a.questionId !== answer.questionId)
  updatedAnswers.push(answer)

  // Update tags based on new answer
  const question = questions.find(q => q.id === answer.questionId)
  const newTags: string[] = []

  if (question) {
    answer.selectedOptions.forEach((optionId: string) => {
      const option = question.options.find(o => o.id === optionId)
      if (option) {
        newTags.push(...option.tags)
      }
    })
  }

  const updatedTags = [...new Set([...profile.tags, ...newTags])]

  return {
    ...profile,
    answers: updatedAnswers,
    tags: updatedTags
  }
}

export const getQuestionProgress = (answeredQuestions: string[]): number => {
  return Math.round((answeredQuestions.length / questions.length) * 100)
}

export const getQuestionsByCategory = (category: string): Question[] => {
  return questions.filter(q => q.category === category).sort((a, b) => a.order - b.order)
}

export const getCategoryQuestions = (): Record<string, Question[]> => {
  const categories: Record<string, Question[]> = {}
  questions.forEach(question => {
    if (!categories[question.category]) {
      categories[question.category] = []
    }
    categories[question.category].push(question)
  })

  // Sort questions by order within each category
  Object.keys(categories).forEach(category => {
    categories[category].sort((a, b) => a.order - b.order)
  })

  return categories
} 
