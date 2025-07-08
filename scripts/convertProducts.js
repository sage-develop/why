import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Function to parse markdown content and extract product information
const parseProductMarkdown = (content, filename) => {
  const products = [];
  const lines = content.split('\n');
  let currentProduct = null;
  let inProductSection = false;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim();
    
    // Check for product section headers (## 1. Product Name)
    const sectionMatch = line.match(/^## (\d+)\. (.+)$/);
    if (sectionMatch) {
      // Save previous product if exists
      if (currentProduct) {
        products.push(currentProduct);
      }
      
      const sectionNumber = sectionMatch[1];
      const productName = sectionMatch[2];
      
      currentProduct = {
        id: `${filename}#${sectionNumber}`,
        name: productName,
        section: sectionNumber,
        filename: filename,
        description: '',
        family: '',
        type: '',
        risk: '',
        tags: [],
        segmentation: '',
        useCase: '',
        content: ''
      };
      
      inProductSection = true;
      continue;
    }

    // If we're in a product section, collect information
    if (currentProduct && inProductSection) {
      // Check for end of product section (next ## or end of file)
      if (line.startsWith('##') && i > 0) {
        inProductSection = false;
        continue;
      }

      // Parse product details
      if (line.startsWith('- **Description**:')) {
        currentProduct.description = line.replace('- **Description**:', '').trim();
      } else if (line.startsWith('- **Family**:')) {
        currentProduct.family = line.replace('- **Family**:', '').trim();
      } else if (line.startsWith('- **Type**:')) {
        currentProduct.type = line.replace('- **Type**:', '').trim();
      } else if (line.startsWith('- **Risk**:')) {
        currentProduct.risk = line.replace('- **Risk**:', '').trim();
      } else if (line.startsWith('- **Tags**:')) {
        const tagsStr = line.replace('- **Tags**:', '').trim();
        currentProduct.tags = tagsStr.split(',').map(tag => tag.trim());
      } else if (line.startsWith('- **Segmentation**:')) {
        currentProduct.segmentation = line.replace('- **Segmentation**:', '').trim();
      } else if (line.startsWith('- **Use Case**:')) {
        currentProduct.useCase = line.replace('- **Use Case**:', '').trim();
      } else if (line && !line.startsWith('-')) {
        // Add to content if it's not a metadata line
        currentProduct.content += line + '\n';
      }
    }
  }

  // Add the last product
  if (currentProduct) {
    products.push(currentProduct);
  }

  return products;
};

// Function to generate TypeScript content
const generateTypeScriptContent = (allProducts) => {
  const productMap = {};
  
  allProducts.forEach(product => {
    productMap[product.id] = {
      name: product.name,
      description: product.description,
      family: product.family,
      type: product.type,
      risk: product.risk,
      tags: product.tags,
      segmentation: product.segmentation,
      useCase: product.useCase,
      content: product.content.trim()
    };
  });

  return `// Auto-generated from markdown files
// Run: node scripts/convertProducts.js

export interface Product {
  name: string;
  description: string;
  family: string;
  type: string;
  risk: string;
  tags: string[];
  segmentation: string;
  useCase: string;
  content: string;
}

export const PRODUCTS: Record<string, Product> = ${JSON.stringify(productMap, null, 2)};

export const getProduct = (productId: string): Product | undefined => {
  return PRODUCTS[productId];
};

export const getProductName = (productId: string): string => {
  const product = PRODUCTS[productId];
  return product ? product.name : productId;
};

export const getProductDescription = (productId: string): string => {
  const product = PRODUCTS[productId];
  return product ? product.description : '';
};

export const getProductShortDescription = (productId: string): string => {
  const product = PRODUCTS[productId];
  if (!product) return productId;
  
  return \`\${product.name} - \${product.description}\`;
};

export const getProductCategory = (productId: string): string => {
  const product = PRODUCTS[productId];
  if (!product) return 'Other';
  
  switch (product.family.toLowerCase()) {
    case 'trade':
      return 'Trade Finance';
    case 'cash management':
      return 'Cash Management';
    case 'loans':
      return 'Lending';
    case 'global markets':
      return 'Global Markets';
    case 'insurance':
      return 'Insurance';
    case 'investments':
      return 'Investments';
    default:
      return product.family || 'Other';
  }
};

export const getProductFamily = (productId: string): string => {
  const product = PRODUCTS[productId];
  if (!product) return 'other';
  
  switch (product.family.toLowerCase()) {
    case 'trade':
      return 'trade_finance';
    case 'cash management':
      return 'cash_management';
    case 'loans':
      return 'loans';
    case 'global markets':
      return 'global_markets';
    case 'insurance':
      return 'insurance';
    case 'investments':
      return 'investments';
    default:
      return 'other';
  }
};
`;
};

// Main execution
const main = () => {
  const productsDir = path.join(__dirname, '..', 'products');
  const outputFile = path.join(__dirname, '..', 'src', 'products.ts');
  
  console.log('Reading markdown files from:', productsDir);
  
  try {
    const files = fs.readdirSync(productsDir).filter(file => file.endsWith('.md'));
    let allProducts = [];
    
    files.forEach(filename => {
      const filePath = path.join(productsDir, filename);
      const content = fs.readFileSync(filePath, 'utf8');
      
      console.log(`Processing ${filename}...`);
      const products = parseProductMarkdown(content, filename);
      allProducts = allProducts.concat(products);
      
      console.log(`Found ${products.length} products in ${filename}`);
    });
    
    console.log(`Total products found: ${allProducts.length}`);
    
    const typescriptContent = generateTypeScriptContent(allProducts);
    fs.writeFileSync(outputFile, typescriptContent);
    
    console.log(`Generated ${outputFile} with ${allProducts.length} products`);
    
    // Log some sample products for verification
    console.log('\nSample products:');
    allProducts.slice(0, 3).forEach(product => {
      console.log(`- ${product.id}: ${product.name}`);
    });
    
  } catch (error) {
    console.error('Error:', error.message);
    process.exit(1);
  }
};

main(); 
