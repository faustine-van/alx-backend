// Node Redis client subscriber
import { createClient, print} from 'redis';


let sub = createClient();
sub.on('connect', () => {console.log('Redis client connected to the server')});
sub.on('error', (error) => {console.error(`Redis client not connected to the server: ${error}`)});

sub.subscribe('holberton school channel')

sub.on('message', (channel, message) => {
    console.log(message)
    if (message === 'KILL_SERVER') {
        sub.unsubscribe();
        sub.quit()
    } 
})

