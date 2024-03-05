# 0x03. Queuing System in JS
`Back-end` `JavaScript` `ES6` `Redis` `NodeJS` `ExpressJS` `Kue`

### Required Files for the Project
- package.json
```
{
    "name": "queuing_system_in_js",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
      "lint": "./node_modules/.bin/eslint",
      "check-lint": "lint [0-9]*.js",
      "test": "./node_modules/.bin/mocha --require @babel/register --exit",
      "dev": "nodemon --exec babel-node --presets @babel/preset-env"
    },
    "author": "",
    "license": "ISC",
    "dependencies": {
      "chai-http": "^4.3.0",
      "express": "^4.17.1",
      "kue": "^0.11.6",
      "redis": "^2.8.0"
    },
    "devDependencies": {
      "@babel/cli": "^7.8.0",
      "@babel/core": "^7.8.0",
      "@babel/node": "^7.8.0",
      "@babel/preset-env": "^7.8.2",
      "@babel/register": "^7.8.0",
      "eslint": "^6.4.0",
      "eslint-config-airbnb-base": "^14.0.0",
      "eslint-plugin-import": "^2.18.2",
      "eslint-plugin-jest": "^22.17.0",
      "nodemon": "^2.0.2",
      "chai": "^4.2.0",
      "mocha": "^6.2.2",
      "request": "^2.88.0",
      "sinon": "^7.5.0"
    }
  }

```
- .babelrc
```
{
  "presets": [
    "@babel/preset-env"
  ]
}
```
### Setup and run projects
Download, extract, and compile the latest stable Redis version (higher than 5.0.7 - https://redis.io/download/):
```
# setup
$ npm install #  when package.json exists
$ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
$ tar xzf redis-6.0.10.tar.gz
$ cd redis-6.0.10
$ make
Start Redis in the background with src/redis-server
$ src/redis-server &
```
------------------
```
# Run
$ ./src/redis-server > /dev/null 2>&1 &
$ npm run dev 0-redis_client.js
```
### Reference
1. [Redis quick start](https://redis.io/docs/install/install-redis/)
2. [Redis client interface](https://redis.io/docs/connect/cli/)
3. [Redis client for Node JS](https://redis.io/docs/connect/clients/nodejs/)
3. [Kue](https://github.com/Automattic/kue)deprecated but still use in the industry

4. [redis@2.8.0](https://www.npmjs.com/package/redis/v/2.8.0)
5. [util.promisify(original)](https://nodejs.org/dist/latest-v8.x/docs/api/util.html#util_util_promisify_original)
6. [https://stackoverflow.com/questions/29595315/testing-node-js-application-that-uses-kue](https://stackoverflow.com/questions/29595315/testing-node-js-application-that-uses-kue)
