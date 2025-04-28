const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

// In-memory product database for simplicity
const products = {
  1: { id: 1, name: "Laptop", price: 999.99 },
  2: { id: 2, name: "Smartphone", price: 499.99 }
};

app.get('/products', (req, res) => {
  res.json(Object.values(products));
});

app.get('/products/:id', (req, res) => {
  const product = products[req.params.id];
  if (product) {
    res.json(product);
  } else {
    res.status(404).json({ error: "Product not found" });
  }
});

app.post('/products', (req, res) => {
  const productId = Object.keys(products).length > 0 ? 
    Math.max(...Object.keys(products).map(Number)) + 1 : 1;
    
  const product = {
    id: productId,
    name: req.body.name,
    price: req.body.price
  };
  
  products[productId] = product;
  res.status(201).json(product);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Product service running on port ${PORT}`);
});
