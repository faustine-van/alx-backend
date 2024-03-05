// Writing the job creation function
function createPushNotificationsJobs(jobs, queue){
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }
    jobs.forEach(jobObj => {
        // Create a new job for each job object
        const job = queue.create('push_notification_code_3', jobObj);
      
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
}
export default createPushNotificationsJobs;