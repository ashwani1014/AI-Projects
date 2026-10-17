# Python Chatbot - Frontend

Next.js frontend for the Python Chatbot application.

## Architecture

This project is split into:
- **Frontend** (this folder): Next.js with React and Tailwind CSS
- **Backend** (../backend): Node.js/Express API server

## Getting Started

### 1. Start the Backend

Navigate to the backend folder and install dependencies:

```bash
cd ../backend
npm install
npm run dev
```

The backend will run on http://localhost:5000

### 2. Start the Frontend

Navigate back to this folder and run the development server:

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## Configuration

Create a `.env.local` file in the root directory:

```
NEXT_PUBLIC_API_URL=http://localhost:5000
```

## Project Structure

```
src/
├── app/
│   ├── component/       # React components
│   │   ├── Sidebar.tsx
│   │   ├── Header.tsx
│   │   ├── HeroSection.tsx
│   │   ├── SuggestionCards.tsx
│   │   ├── ChatInput.tsx
│   │   └── ChatbotInterface.tsx
│   ├── config/          # Configuration files
│   │   └── api.ts
│   ├── page.tsx         # Main page
│   └── layout.tsx
```

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
