const net = require('net');

// Create a server
const server = net.createServer((socket) => {
  console.log('Client connected');

  // Event for receiving data from the client
  socket.on('data', (data) => {
    console.log(`Received from client: ${data.toString()}`);
    
    // Respond with "pong" if the client sends "ping"
    if (data.toString().trim().toLowerCase() === 'ping') {
      socket.write('pong');
    }
  });

  // Event for client disconnect
  socket.on('end', () => {
    console.log('Client disconnected');
  });
});

// Start the server on localhost:65432
server.listen(65432, '127.0.0.1', () => {
  console.log('Server is listening on 127.0.0.1:65432');
});
