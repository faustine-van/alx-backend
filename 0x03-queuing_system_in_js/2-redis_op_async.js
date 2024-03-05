import { createClient, print} from 'redis';
import { promisify } from 'util';

let client = createClient();
client.on('error', (error) => {console.error(`Redis client not connected to the server: ${error}`)});

console.log('Redis client connected to the server');

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
    const getValue = promisify(client.get).bind(client);
    try {
        const value = await getValue(schoolName);
        console.log(value);
    } catch {((error) => {
        console.error(error)
    })};
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');