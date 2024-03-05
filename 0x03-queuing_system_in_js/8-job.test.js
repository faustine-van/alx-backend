import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';
import { createQueue } from 'kue';

describe('createPushNotificationsJobs', () => {
    let queue;

    before(() => {
        queue = createQueue();
        queue.testMode.enter();
    });

    after(() => {
        queue.testMode.clear();
        queue.testMode.exit();
    });

    it('displays an error message if jobs is not an array', () => {
        const notArray = {}; // This should be a non-array argument
        expect(() => createPushNotificationsJobs(notArray, queue)).to.throw(Error, 'Jobs is not an array');
    });
    it('create two new jobs to the queue', () => {
        const dataArray = [{
            phoneNumber: '4153788783',
            message: '6-job_creator.js'
            },
            {
            phoneNumber: '4153518780',
            message: '6-job_creator.js',
        }];
        createPushNotificationsJobs(dataArray, queue)
        expect(queue.testMode.jobs.length).to.equal(2);
        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
        expect(queue.testMode.jobs[1].data).to.eql({
            phoneNumber: '4153518780',
            message: '6-job_creator.js',
        });
        expect(queue.testMode.jobs[0].data).to.eql({
            phoneNumber: '4153788783',
            message: '6-job_creator.js'
        });
        
    });


});
