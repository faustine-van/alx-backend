import { createClient } from 'redis';


let client = createClient();
client.on('error', (error) => {console.error(`Redis client not connected to the server: ${error}`)});

console.log('Redis client connected to the server');
