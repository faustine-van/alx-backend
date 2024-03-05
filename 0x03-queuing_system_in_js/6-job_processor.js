import { createQueue } from "kue";
// Create the Job processor

// create Queue
const sendNotificationQueue = createQueue();

function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

sendNotificationQueue.process('push_notification_code', (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message);
    done(); // when finish
});