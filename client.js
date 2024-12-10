const net = require('net');

// Create a connection to the server
const client = net.createConnection({ host: '127.0.0.1', port: 65432 }, () => {
  console.log('Connected to the server');

  // Send "ping" to the server
  client.write('ping');
});

// Event for receiving data from the server
client.on('data', (data) => {
  console.log(`Received from server: ${data.toString()}`);
  client.end(); // Close the connection after receiving the response
});

// Event for client disconnect
client.on('end', () => {
  console.log('Disconnected from the server');
});
