import React from 'react'
import { type UserProfile } from '../questions'

interface UserProfileSummaryProps {
  userProfile: UserProfile
}

const UserProfileSummary: React.FC<UserProfileSummaryProps> = ({ userProfile }) => {
  if (userProfile.tags.length === 0) {
    return null
  }

  return (
    <div className="mt-8 bg-white rounded-xl shadow-lg p-6">
      <h3 className="text-lg font-semibold text-gray-900 mb-4">
        Your Business Profile
      </h3>
      <div className="flex flex-wrap gap-2">
        {userProfile.tags.map((tag) => (
          <span
            key={tag}
            className="bg-gray-100 text-gray-700 px-3 py-1 rounded-full text-sm"
          >
            {tag.replace(/_/g, ' ')}
          </span>
        ))}
      </div>
    </div>
  )
}

export default UserProfileSummary 
