// 0-redis_client

const redis = require('redis');
const client = redis.connect.createClient();

redis.connect.createClient = lib;

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error('Redis client not connected to the server: ERROR_MESSAGE:', err);
});
