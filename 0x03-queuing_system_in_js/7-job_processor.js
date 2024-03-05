import { createQueue } from "kue";

// Track progress and errors with Kue: Create the Job processor
const pushNotificationCode2 = createQueue();
// blacklistedPhoneNumbers
const blacklisted = ['4153518780', '4153518781'];


function sendNotification(phoneNumber, message, job, done) {
    // Track the progress of the job
    job.progress(0, 100);

    // Check if phone number is blacklisted
    if (blacklisted.includes(phoneNumber)) {
        // Fail the job
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }
    // Track progress to 50%
    job.progress(50, 100);
    // Log sending notification
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    // Mark job as completed
    done();
}

// Process jobs from the queue
pushNotificationCode2.process('push_notification_code_2', (job, done) => {
    // Extract job data
    const { phoneNumber, message } = job.data;

    // Call sendNotification function
    sendNotification(phoneNumber, message, job, done);
});