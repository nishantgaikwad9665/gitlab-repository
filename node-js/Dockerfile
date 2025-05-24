# Base image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy dependency definitions
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy app source
COPY . .

# Expose port
EXPOSE 3000

# Start the application
CMD ["node", "app.js"]
