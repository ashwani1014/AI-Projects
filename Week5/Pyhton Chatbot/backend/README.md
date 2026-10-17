# Chatbot Backend

Node.js/Express backend for the Python Chatbot application.

## Installation

```bash
npm install
```

## Configuration

Create a `.env` file in the root directory:

```
PORT=5000
```

## Running the Server

Development mode (with auto-reload):
```bash
npm run dev
```

Production mode:
```bash
npm start
```

## API Endpoints

### POST /api/chat
Send a message to the chatbot.

Request body:
```json
{
  "message": "Your message here"
}
```

Response:
```json
{
  "response": "Bot response here"
}
```

### GET /api/health
Health check endpoint.

Response:
```json
{
  "status": "ok",
  "message": "Backend is running"
}
```
