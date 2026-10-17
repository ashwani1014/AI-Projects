'use client';

import { useState } from 'react';
import Sidebar from './Sidebar';
import Header from './Header';
import HeroSection from './HeroSection';
import SuggestionCards from './SuggestionCards';
import ChatInput from './ChatInput';
import { API_BASE_URL } from '../../config/api';

interface Message {
  role: 'user' | 'assistant';
  content: string;
}

export default function ChatbotInterface() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [showHero, setShowHero] = useState(true);

  const handlePromptSelect = (prompt: string) => {
    setShowHero(false);
    handleSubmitInternal(prompt);
  };

  const handleSubmitInternal = async (message: string) => {
    const userMessage: Message = { role: 'user', content: message };
    setMessages((prev) => [...prev, userMessage]);

    try {
      const response = await fetch(`${API_BASE_URL}/api/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message }),
      });

      const data = await response.json();
      const botMessage: Message = { role: 'assistant', content: data.response };
      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      console.error('Error:', error);
      const errorMessage: Message = { role: 'assistant', content: 'Sorry, something went wrong. Please try again.' };
      setMessages((prev) => [...prev, errorMessage]);
    }
  };

  const handleSubmit = async (message: string) => {
    setShowHero(false);
    await handleSubmitInternal(message);
  };

  return (
    <div className="min-h-screen bg-[#faf8ff] font-sans text-[#131b2e]">
      <Sidebar />

      <div className="pl-72">
        <Header />

        <main className="relative pt-16 bg-[#faf8ff] w-full min-h-screen">
          <div className="flex flex-col w-full relative min-h-[calc(100vh-4rem)] justify-between overflow-x-hidden">
            <div className="absolute top-12 left-1/2 -translate-x-1/2 w-[720px] h-[340px] bg-gradient-to-b from-[#eaddff]/40 via-[#eaedff]/20 to-transparent blur-3xl pointer-events-none -z-10"></div>

            <div className="w-full max-w-4xl mx-auto px-6 pt-6 pb-36 flex flex-col items-center">
              {showHero ? (
                <>
                  <HeroSection />
                  <SuggestionCards onPromptSelect={handlePromptSelect} />
                </>
              ) : (
                <div className="w-full space-y-4">
                  {messages.map((msg, index) => (
                    <div
                      key={index}
                      className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}
                    >
                      <div
                        className={`max-w-[80%] p-4 rounded-xl ${
                          msg.role === 'user'
                            ? 'bg-[#630ed4] text-white'
                            : 'bg-white text-[#131b2e] shadow-sm'
                        }`}
                      >
                        <p className="whitespace-pre-wrap">{msg.content}</p>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>

            <ChatInput onSubmit={handleSubmit} />
          </div>
        </main>
      </div>
    </div>
  );
}
