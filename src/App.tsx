import { Routes, Route } from 'react-router-dom'
import { HomePage, ProductDetailPage } from './pages'

function App() {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/product/:productId" element={<ProductDetailPage />} />
    </Routes>
  )
}

export default App 
