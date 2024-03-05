import { createClient, print} from 'redis';


let client = createClient();
client.on('error', (error) => {console.error(`Redis client not connected to the server: ${error}`)});

console.log('Redis client connected to the server');

// Store and retrieve a map data.
client.hset('HolbertonSchools', 'Portland', 50, print);
client.hset('HolbertonSchools', 'Seattle', 80, print);
client.hset('HolbertonSchools', 'New York', 20, print);
client.hset('HolbertonSchools', 'Bogota', 20, print);
client.hset('HolbertonSchools', 'Cali', 40, print);
client.hset('HolbertonSchools', 'Paris', 2, print);

client.hgetall('HolbertonSchools', (err, val)  => {
    if (err) {
        console.log(err);
        return;
    }
    console.log(val);
});

