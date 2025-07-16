# Recommendation Tracking Feature

## Overview

The recommendation tracking feature provides real-time feedback to users when their answers change the product recommendations. This helps users understand how their choices impact the suggested products.

## Features

### 1. Notification Banner
- **Auto-dismissing notification**: Shows a blue notification banner in the top-right corner when recommendations change
- **5-second auto-dismiss**: Automatically disappears after 5 seconds
- **Manual dismiss**: Users can click the X button to dismiss immediately
- **Change summary**: Shows the total number of recommendations that changed

### 2. Detailed Changes Panel
- **Collapsible details**: Shows a "Recent Changes" panel below the recommendations
- **Change categories**: 
  - 🟢 **New recommendations** (green)
  - 🔴 **Removed recommendations** (red) 
  - 🔄 **Updated recommendations** (blue)
- **Score tracking**: Shows score changes for updated recommendations
- **Reason display**: Shows why each recommendation was added/removed/updated

### 3. Visual Highlights
- **Product highlighting**: New or updated recommendations get a blue highlight for 3 seconds
- **"Updated" badge**: Shows an "Updated" badge on changed products
- **Smooth transitions**: All changes use smooth CSS transitions

## How It Works

### State Management
The feature uses the existing Zustand store (`useQuestionStore`) which already tracks:
- `recommendations`: Current product recommendations
- `previousRecommendations`: Previous state for comparison

### Change Detection
Changes are detected by comparing:
1. **Added products**: Products in current recommendations but not in previous
2. **Removed products**: Products in previous recommendations but not in current  
3. **Updated products**: Products with score changes > 0.1

### Components

#### RecommendationChanges.tsx
- Main component for displaying changes
- Handles notification banner and detailed changes panel
- Auto-dismiss functionality
- Responsive design with icons and color coding

#### ProductRecommendations.tsx (Enhanced)
- Added highlighting for changed products
- Visual indicators for updated recommendations
- Smooth transitions for better UX

#### HomePage.tsx (Enhanced)
- Integrates RecommendationChanges component
- Manages notification state
- Passes previous recommendations to child components

## Usage

### For Users
1. **Answer questions**: As you answer questions, recommendations update automatically
2. **See notifications**: A blue banner appears when recommendations change
3. **Review changes**: Click "Show Details" in the Recent Changes panel
4. **Spot highlights**: Changed products are highlighted briefly with blue borders

### For Developers
The feature is automatically enabled and requires no additional configuration. The store already tracks previous recommendations, so the feature works out of the box.

## Technical Details

### CSS Animations
```css
@keyframes slide-in-from-top {
  from {
    transform: translateY(-100%);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}
```

### Change Detection Logic
```typescript
const getChanges = () => {
  const currentIds = new Set(recommendations.map(r => r.productId))
  const previousIds = new Set(previousRecommendations.map(r => r.productId))

  const added = recommendations.filter(r => !previousIds.has(r.productId))
  const removed = previousRecommendations.filter(r => !currentIds.has(r.productId))
  const changed = recommendations.filter(r => {
    const prev = previousRecommendations.find(p => p.productId === r.productId)
    return prev && Math.abs(prev.score - r.score) > 0.1
  })

  return { added, removed, changed }
}
```

## Benefits

1. **User Awareness**: Users understand how their choices affect recommendations
2. **Transparency**: Clear visibility into why products are recommended
3. **Engagement**: Interactive feedback keeps users engaged
4. **Trust**: Users can see the system is responding to their inputs
5. **Learning**: Users learn which answers lead to which products

## Future Enhancements

- **Change history**: Track all changes over time
- **Undo functionality**: Allow users to revert answer changes
- **Comparison view**: Side-by-side comparison of old vs new recommendations
- **Export changes**: Allow users to export their recommendation changes
- **Analytics**: Track which changes are most impactful 
