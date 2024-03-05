import { createClient, print} from 'redis';


let client = createClient();
client.on('error', (error) => {console.error(`Redis client not connected to the server: ${error}`)});

console.log('Redis client connected to the server');

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
}
function displaySchoolValue(schoolName) {
    client.get(schoolName, (error, value) => {
        if (error) {
            console.error(error)
            return;
        }
        console.log(value);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');