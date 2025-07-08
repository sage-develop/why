import { useState, useEffect } from 'react'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'

interface ProductDetailProps {
  productId: string
  onBack: () => void
}

interface ProductData {
  title: string
  content: string
  section?: string
}

const ProductDetail = ({ productId, onBack }: ProductDetailProps) => {
  const [productData, setProductData] = useState<ProductData | null>(null)
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    const loadProductData = async () => {
      try {
        setIsLoading(true)
        setError(null)

        // Parse product ID to get filename and section
        const [filename, section] = productId.includes('#')
          ? productId.split('#')
          : [productId, null]

        // Fetch the markdown file
        const response = await fetch(`/products/${filename}`)
        if (!response.ok) {
          throw new Error(`Failed to load product data: ${response.statusText}`)
        }

        const markdownContent = await response.text()

        // If we have a specific section, extract it
        let content = markdownContent
        let title = filename.replace('.md', '').replace(/_/g, ' ').toUpperCase()

        if (section) {
          // Find the specific section in the markdown
          const sectionMatch = markdownContent.match(new RegExp(`## ${section}[^#]*`, 's'))
          if (sectionMatch) {
            content = sectionMatch[0]
            // Extract the product name from the section header
            const titleMatch = content.match(/## \d+\. (.+)/)
            if (titleMatch) {
              title = titleMatch[1]
            }
          }
        }

        setProductData({
          title,
          content,
          section: section || undefined
        })
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to load product data')
      } finally {
        setIsLoading(false)
      }
    }

    loadProductData()
  }, [productId])

  if (isLoading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
        <div className="container mx-auto px-4 py-8">
          <div className="max-w-4xl mx-auto">
            <div className="bg-white rounded-xl shadow-lg p-6">
              <div className="flex items-center justify-center py-12">
                <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
                <span className="ml-3 text-gray-600">Loading product details...</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
        <div className="container mx-auto px-4 py-8">
          <div className="max-w-4xl mx-auto">
            <div className="bg-white rounded-xl shadow-lg p-6">
              <div className="text-center py-12">
                <div className="text-red-500 text-4xl mb-4">⚠️</div>
                <h2 className="text-xl font-semibold text-gray-900 mb-2">Error Loading Product</h2>
                <p className="text-gray-600 mb-6">{error}</p>
                <button
                  onClick={onBack}
                  className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition-colors"
                >
                  Go Back
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    )
  }

  if (!productData) {
    return null
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="container mx-auto px-4 py-8">
        <div className="max-w-4xl mx-auto">
          {/* Header */}
          <div className="bg-white rounded-xl shadow-lg p-6 mb-6">
            <div className="flex items-center justify-between mb-4">
              <button
                onClick={onBack}
                className="flex items-center text-blue-600 hover:text-blue-800 font-medium transition-colors"
              >
                <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
                </svg>
                Back to Recommendations
              </button>
            </div>
            <h1 className="text-3xl font-bold text-gray-900 mb-2">{productData.title}</h1>
            {productData.section && (
              <p className="text-gray-600">Section {productData.section}</p>
            )}
          </div>

          {/* Product Content */}
          <div className="bg-white rounded-xl shadow-lg p-6">
            <div className="prose prose-lg max-w-none prose-headings:text-gray-900 prose-p:text-gray-700 prose-strong:text-gray-900 prose-ul:text-gray-700 prose-li:text-gray-700">
              <ReactMarkdown
                remarkPlugins={[remarkGfm]}
                components={{
                  h1: ({ children }) => <h1 className="text-2xl font-bold text-gray-900 mb-4">{children}</h1>,
                  h2: ({ children }) => <h2 className="text-xl font-semibold text-gray-900 mb-3 mt-6">{children}</h2>,
                  h3: ({ children }) => <h3 className="text-lg font-medium text-gray-900 mb-2 mt-4">{children}</h3>,
                  p: ({ children }) => <p className="text-gray-700 mb-3 leading-relaxed">{children}</p>,
                  ul: ({ children }) => <ul className="list-disc list-inside mb-3 space-y-1">{children}</ul>,
                  ol: ({ children }) => <ol className="list-decimal list-inside mb-3 space-y-1">{children}</ol>,
                  li: ({ children }) => <li className="text-gray-700">{children}</li>,
                  strong: ({ children }) => <strong className="font-semibold text-gray-900">{children}</strong>,
                  em: ({ children }) => <em className="italic text-gray-700">{children}</em>,
                  code: ({ children }) => <code className="bg-gray-100 px-1 py-0.5 rounded text-sm font-mono">{children}</code>,
                  pre: ({ children }) => <pre className="bg-gray-100 p-3 rounded-lg overflow-x-auto mb-3">{children}</pre>,
                  blockquote: ({ children }) => <blockquote className="border-l-4 border-blue-500 pl-4 italic text-gray-600 mb-3">{children}</blockquote>,
                  table: ({ children }) => <table className="w-full border-collapse border border-gray-300 mb-3">{children}</table>,
                  th: ({ children }) => <th className="border border-gray-300 px-3 py-2 bg-gray-50 font-semibold text-left">{children}</th>,
                  td: ({ children }) => <td className="border border-gray-300 px-3 py-2">{children}</td>,
                }}
              >
                {productData.content}
              </ReactMarkdown>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default ProductDetail 
