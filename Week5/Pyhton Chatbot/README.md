# Python Chatbot

A full-stack Python tutoring chatbot application with a modern UI.

## Architecture

This project is divided into two parts:

- **Frontend** (`chatbot-app/`): Next.js application with React and Tailwind CSS
- **Backend** (`backend/`): Node.js/Express API server

## Project Structure

```
Pyhton Chatbot/
├── chatbot-app/          # Next.js frontend
│   ├── src/
│   │   ├── app/
│   │   │   ├── component/    # React components
│   │   │   ├── config/       # API configuration
│   │   │   ├── page.tsx
│   │   │   └── layout.tsx
│   │   └── ...
│   ├── package.json
│   └── README.md
├── backend/              # Node.js/Express backend
│   ├── server.js
│   ├── package.json
│   ├── .env
│   └── README.md
└── README.md
```

## Getting Started

### Prerequisites

- Node.js (v18 or higher)
- npm or yarn

### 1. Install Backend Dependencies

```bash
cd backend
npm install
```

### 2. Configure Backend

The backend uses a `.env` file for configuration. The file is already created with:

```
PORT=5000
```

### 3. Start the Backend

```bash
npm run dev
```

The backend will run on http://localhost:5000

### 4. Install Frontend Dependencies

Open a new terminal:

```bash
cd chatbot-app
npm install
```

### 5. Configure Frontend

Create a `.env.local` file in the `chatbot-app` directory:

```
NEXT_PUBLIC_API_URL=http://localhost:5000
```

### 6. Start the Frontend

```bash
npm run dev
```

The frontend will run on http://localhost:3000

## API Endpoints

### POST /api/chat
Send a message to the chatbot.

Request:
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

## Features

- Modern, responsive UI with Tailwind CSS
- Modular component architecture
- Real-time chat interface
- Python-specific suggestions and prompts
- Separate frontend and backend for scalability

## Development

For detailed information about each part, see:
- [Frontend README](./chatbot-app/README.md)
- [Backend README](./backend/README.md)
