'use client';

import { useState, useRef } from 'react';

interface ChatInputProps {
  onSubmit: (message: string) => void;
}

export default function ChatInput({ onSubmit }: ChatInputProps) {
  const [message, setMessage] = useState('');
  const [charCount, setCharCount] = useState(0);
  const [snippetMode, setSnippetMode] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  const handleInputChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    const value = e.target.value;
    setMessage(value);
    setCharCount(value.length);

    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
      textareaRef.current.style.height = `${Math.min(textareaRef.current.scrollHeight, 200)}px`;
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  const insertTracebackTemplate = () => {
    const template = "Traceback (most recent call last):\n  File \"main.py\", line 42, in <module>\n    result = process_data()\nTypeError: 'NoneType' object is not subscriptable\n\nExplain why this occurred and how to resolve it safely:";
    setMessage(template);
    setCharCount(template.length);
    if (textareaRef.current) {
      textareaRef.current.focus();
    }
  };

  const toggleSnippetMode = () => {
    setSnippetMode(!snippetMode);
    if (!snippetMode && !message.includes('python')) {
      setMessage("python\n# Write or paste Python code snippet here\n\n\n" + message);
    }
    if (textareaRef.current) {
      textareaRef.current.focus();
    }
  };

  const clearPrompt = () => {
    setMessage('');
    setCharCount(0);
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
      textareaRef.current.focus();
    }
  };

  const handleSubmit = async () => {
    const prompt = message.trim();
    if (!prompt) return;

    setIsSubmitting(true);
    await onSubmit(prompt);
    setIsSubmitting(false);
    clearPrompt();
  };

  return (
    <div className="sticky bottom-0 z-30 w-full bg-gradient-to-t from-[#faf8ff] via-[#faf8ff]/95 to-transparent pt-6 pb-4">
      <div className="max-w-4xl mx-auto px-6 flex flex-col items-center">
        <div className="w-full bg-white rounded-xl shadow-xl p-4 flex flex-col gap-2 relative">
          <div className="flex items-center justify-between gap-2 pb-1">
            <div className="flex items-center gap-1.5 overflow-x-auto py-0.5">
              <button
                onClick={insertTracebackTemplate}
                className="inline-flex items-center gap-1 px-2.5 py-1 rounded-md bg-[#f2f3ff] hover:bg-[#eaedff] text-[#131b2e] text-xs transition-colors"
              >
                📊 Attach Traceback
              </button>
              <button
                onClick={toggleSnippetMode}
                className={`inline-flex items-center gap-1 px-2.5 py-1 rounded-md text-xs transition-colors ${
                  snippetMode ? 'bg-[#d2bbff] text-[#25005a]' : 'bg-[#f2f3ff] hover:bg-[#eaedff] text-[#131b2e]'
                }`}
              >
                💻 Snippet Mode
              </button>
              <div className="inline-flex items-center gap-1 px-2.5 py-1 rounded-md bg-[#eaedff] text-[#131b2e] text-xs">
                🖥️ Python 3.12
              </div>
            </div>
            <div className="flex items-center gap-2">
              <span className="text-xs text-[#7b7487]">{charCount} / 2000</span>
            </div>
          </div>

          <div className="relative w-full">
            <textarea
              ref={textareaRef}
              value={message}
              onChange={handleInputChange}
              onKeyDown={handleKeyDown}
              placeholder="Ask anything about Python... (e.g., How do generators work?)"
              className="w-full bg-transparent resize-none text-[#131b2e] placeholder:text-[#7b7487] focus:outline-none leading-relaxed"
              rows={3}
              maxLength={2000}
            />
          </div>

          <div className="flex items-center justify-between pt-1">
            <div className="flex items-center gap-2 text-[#7b7487]">
              <span className="text-xs hidden sm:inline">
                <kbd className="px-1.5 py-0.5 rounded bg-[#eaedff] text-xs text-[#131b2e]">Shift + Enter</kbd> newline · <kbd className="px-1.5 py-0.5 rounded bg-[#eaedff] text-xs text-[#131b2e]">Enter</kbd> to send
              </span>
            </div>
            <div className="flex items-center gap-2">
              <button
                onClick={clearPrompt}
                className="p-1.5 rounded-lg hover:bg-[#eaedff] text-[#7b7487] hover:text-[#131b2e] transition-colors"
                title="Clear prompt"
              >
                🗑️
              </button>
              <button
                onClick={handleSubmit}
                disabled={!message.trim() || isSubmitting}
                className="inline-flex items-center justify-center gap-1 px-4 py-2 rounded-lg bg-[#630ed4] text-white hover:bg-[#7c3aed] disabled:opacity-40 transition-colors shadow-sm font-semibold cursor-pointer"
              >
                {isSubmitting ? (
                  <>
                    <span className="animate-spin">⏳</span>
                    <span>Running...</span>
                  </>
                ) : (
                  <>
                    <span>Send</span>
                    <span>↑</span>
                  </>
                )}
              </button>
            </div>
          </div>
        </div>

        <div className="text-center mt-2.5">
          <p className="text-xs text-[#7b7487]">
            Python questions only · AI-generated answers may require verification. Connected to POST /api/chat.
          </p>
        </div>
      </div>
    </div>
  );
}
