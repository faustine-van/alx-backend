import { createClient } from 'redis';
import express from 'express';
import { promisify } from 'util';

// Create an express server listening on the port 1245
const app = express();
// Create a client to connect to the Redis server
const client = createClient();
client.on('error', (error) => {console.error(`Redis client not connected to the server: ${error}`)});

// An array listProducts containing the list of the following products
const listProducts = [
    {Id: 1, name: 'Suitcase 250', price: 50, stock: 4},
    {Id: 2, name: 'Suitcase 450', price: 100, stock: 10},
    {Id: 3, name: 'Suitcase 650', price: 350, stock: 2},
    {Id: 4, name: 'Suitcase 1050', price: 550, stock: 5}
];
// Data access function: Get item by ID
function getItemById(id) {
    return listProducts.find(item => item.Id === id);
}

// route GET /list_products that will return the list of every available product
app.get('/list_products', (req, res) => {
    res.json(listProducts.map(product => ({
        itemId: product.Id,
        itemName: product.name,
        price: product.price,
        initialAvailableQuantity: product.stock
    })));
});


function reserveStockById(itemId, stock){
    client.set(`item.${itemId}`, stock);
}

const getCurrent = promisify(client.get).bind(client);
async function getCurrentReservedStockById(itemId) {
    try {
        const item = await getCurrent(`item.${itemId}`);
        return item ? parseInt(item) : 0;
    } catch (err) {
        throw new Error('Failed to get current reserved stock');
    }
}

// Product detail
app.get('/list_products/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId, 10);
    const item = getItemById(itemId);
    const currentStock = await getCurrentReservedStockById(itemId);
    if (!item) {
        res.status(404).json({"status":"Product not found"});
    } else{
    res.json({
        itemId: item.Id,
        itemName: item.name,
        price: item.price,
        initialAvailableQuantity: item.stock,
        currentQuantity: currentStock
    
    });
}
});



// Reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId, 10);
    const item = getItemById(itemId);
    if (!item) {
        res.status(404).json({"status":"Product not found"})
    } else {
        const currentStock = await getCurrentReservedStockById(itemId);
        if (currentStock >= item.stock) {
            res.json({"status":"Not enough stock available","itemId":itemId});
        } else {
            reserveStockById(itemId, currentStock + 1);
            res.json({"status":"Reservation confirmed","itemId":itemId});
        }
    }

});

app.listen(1245, () => {
    console.log(`Server is listening on port 1245`);
});
