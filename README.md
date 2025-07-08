# Corporate Banking Discovery Tool

A React-based application that helps businesses discover personalized banking solutions through an interactive questionnaire.

## Features

### 🎯 Interactive Questionnaire
- Multi-step question flow with progress tracking
- Dynamic product recommendations based on answers
- Skip optional questions functionality
- Real-time progress updates

### 📊 Product Recommendations
- **Top Recommendations**: Shows the top 8 most relevant products
- **Collapsible All Products**: Expand to see all products ordered by relevance score
- **Smart Product Names**: Clear, descriptive product names instead of technical IDs
- **Product Categories**: Organized by banking categories (Trade Finance, Cash Management, etc.)

### 📄 Product Detail Pages
- **Markdown Rendering**: Full product details rendered from markdown files
- **Rich Content**: Detailed descriptions, risk assessments, and use cases
- **Responsive Design**: Optimized for all screen sizes
- **Easy Navigation**: Back button to return to recommendations

### 🏷️ Business Profile
- **Dynamic Tags**: Automatically generated business profile tags
- **Answer Tracking**: Complete history of user responses
- **Personalization**: Recommendations tailored to business needs

## Product Categories

### Trade Finance
- Import/Export financing solutions
- Letter of Credit services
- Trade document collection
- Shipping guarantees

### Cash Management
- International payment services
- Foreign currency accounts
- Liquidity management
- Reconciliation services

### Lending
- Term loans for capital expenditure
- Revolving credit for working capital
- Overdraft facilities

### Global Markets
- Foreign exchange services
- Currency risk management
- FX forward contracts

### Insurance & Investments
- Trade credit insurance
- Investment advisory services

## Technical Stack

- **React 18** with TypeScript
- **React Hook Form** for form management
- **React Markdown** for content rendering
- **Tailwind CSS** for styling
- **Vite** for build tooling

## Getting Started

1. Install dependencies:
   ```bash
   npm install
   ```

2. Start the development server:
   ```bash
   npm run dev
   ```

3. Open your browser to `http://localhost:5173`

## Project Structure

```
src/
├── App.tsx              # Main application component
├── ProductDetail.tsx     # Product detail page component
├── productUtils.ts       # Product name and URL utilities
└── index.css            # Global styles

products/                 # Markdown product files
├── trade_finance_products.md
├── cash_management.md
├── loans.md
├── global_markets.md
├── insurance.md
└── investments.md

questions.ts              # Question definitions and logic
```

## Product Data

Product information is stored in markdown files with the following structure:

```markdown
# Product Category

## 1. Product Name
- **Description**: Detailed product description
- **Family**: Product family
- **Type**: Product type
- **Risk**: Risk assessment
- **Tags**: Relevant tags
- **Segmentation**: Target segments
- **Use Case**: Primary use cases
```

## Development

### Adding New Products
1. Add product details to the appropriate markdown file in `products/`
2. Update the product mapping in `src/productUtils.ts`
3. Add product recommendations to questions in `questions.ts`

### Customizing Questions
1. Modify question definitions in `questions.ts`
2. Update product recommendation logic
3. Adjust scoring weights as needed

## License

MIT License
