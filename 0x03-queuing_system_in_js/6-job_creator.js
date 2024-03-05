import { createQueue } from "kue";

// Create the Job creator
const pushNotificationQueue = createQueue();
const  JOB = pushNotificationQueue.create('push_notification_code', 
    {
        phoneNumber: '4153518780',
        message: '6-job_creator.js',
      }
).save(); // save() making it available for processing by the worker processes.

JOB.on('job enqueue', () => {
    console.log(`Notification job created: ${JOB.id}`);
}).on('complete', () => {
    console.log('Notification job completed');
}).on('failed', () => {
    console.error('Notification job failed');
});