import { createClient } from "redis";
import { createQueue } from "kue";
import express, { json } from 'express';
import { promisify } from 'util';
import { error } from "console";


const client = createClient();
client.on('error', (error) => {console.error(`Redis client not connected to the server: ${error}`)});
const queue = createQueue();
const app = express();
// set key
function reserveSeat (number) {
    client.set('available_seats', number);
}

async function getCurrentAvailableSeats () {
    const getSeat = promisify(client.get).bind(client);
    try {
        const availableSeats = await getSeat('available_seats');
        return availableSeats
    } catch (error) {
        throw new Error('unavailable seats');
    }
}
reserveSeat(50);
let reservationEnabled = true;

// get available seats
app.get('/available_seats', async (req, res) => {
    const availableSeats = await getCurrentAvailableSeats();
    res.json({
        numberOfAvailableSeats: availableSeats
    });
});
// reserve seats
app.get('/reserve_seat', async (req, res) => {
    if (!reservationEnabled){
        res.json({ "status": "Reservation are blocked" });
        return; // important
    }
    // create jobs
    const job = queue.create('reserve_seat').save((error) => {
        if (error) {
            res.json({ "status": "Reservation failed" });
        } else {
            res.json({ "status": "Reservation in process" });

        }
    });
    job.on('complete', (result) => {
        console.log(`Seat reservation job ${job.id} completed`)
    });
    job.on('failed', (errorMessage) => {
        console.error(`Seat reservation job ${job.id} failed: ${errorMessage}`)
    });
});
// reserve seats
app.get('/process', (req, res) => {
    queue.process('reserve_seat', async (job, done) => {
        job.remove();
        let currentSeats = await getCurrentAvailableSeats();
        currentSeats -= 1;
        if (currentSeats >= 0) {
            reserveSeat(currentSeats);
            if (currentSeats === 0) {
                reservationEnabled = false;
            }
            done();
        } else {
            return done(new Error('Not enough seats available'));
        }
    });
    res.json({ "status": "Queue processing" });
});

app.listen(1245, () => {
    console.log(`Server is listening on port 1245`);
});