import { createQueue } from "kue";
const jobs = [
    {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    },
    {
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153518743',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153538781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153118782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4153718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4159518782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4158718781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4153818782',
      message: 'This is the code 4321 to verify your account'
    },
    {
      phoneNumber: '4154318781',
      message: 'This is the code 4562 to verify your account'
    },
    {
      phoneNumber: '4151218782',
      message: 'This is the code 4321 to verify your account'
    }
  ];

const pushNotificationQueue = createQueue();

jobs.forEach(jobObj => {
  // Create a new job for each job object
  const job = pushNotificationQueue.create('push_notification_code_2', jobObj);

  // Log when a job is created
  job.on('created', function(id) {
      console.log(`Notification job created: ${id}`);
  });

  // Log when a job is completed
  job.on('complete', function(result) {
      console.log(`Notification job ${job.id} completed`);
  });

  // Log when a job fails
  job.on('failed', function(err) {
      console.log(`Notification job ${job.id} failed: ${err}`);
  });

  // Log job progress
  job.on('progress', function(progress) {
      console.log(`Notification job ${job.id} ${progress}% complete`);
  });

  // Save the job to the queue
  job.save();
});