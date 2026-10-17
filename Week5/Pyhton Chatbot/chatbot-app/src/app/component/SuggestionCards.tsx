interface SuggestionCardsProps {
  onPromptSelect: (prompt: string) => void;
}

export default function SuggestionCards({ onPromptSelect }: SuggestionCardsProps) {
  const cards = [
    {
      icon: '🔧',
      title: 'Explain Python decorators',
      description: 'Understand @wraps, closures, and inner functions',
      prompt: 'Explain Python decorators with real-world examples: @wraps, closures, and inner functions.',
    },
    {
      icon: '🐛',
      title: 'Debug my Python code',
      description: 'Paste a traceback or syntax error to diagnose',
      prompt: 'Help me debug this Python traceback and optimize the faulty logic:',
    },
    {
      icon: '📝',
      title: 'Teach me list comprehensions',
      description: 'From basic loops to nested filtering patterns',
      prompt: 'Teach me Python list comprehensions: from simple iterators to nested dictionary comprehensions and walrus operator filters.',
    },
    {
      icon: '🚀',
      title: 'Build a Python project with me',
      description: 'Scaffold CLI tools, FastAPI backends, or scripts',
      prompt: 'I want to build a Python project with you. Guide me step-by-step from project structure to deployment:',
    },
  ];

  return (
    <div className="w-full grid grid-cols-1 md:grid-cols-2 gap-4">
      {cards.map((card, index) => (
        <button
          key={index}
          onClick={() => onPromptSelect(card.prompt)}
          className="group text-left p-4 rounded-xl bg-white hover:bg-[#f2f3ff] transition-all duration-200 shadow-sm hover:shadow-md flex items-start gap-4"
        >
          <div className="w-10 h-10 rounded-lg bg-[#eaedff] flex items-center justify-center text-[#630ed4] group-hover:bg-[#630ed4] group-hover:text-white transition-colors flex-shrink-0">
            {card.icon}
          </div>
          <div className="flex-1 min-w-0">
            <div className="flex items-center justify-between gap-2 mb-1">
              <h2 className="font-semibold text-sm text-[#131b2e] group-hover:text-[#630ed4] transition-colors truncate">
                {card.title}
              </h2>
              <span className="text-sm text-[#7b7487] opacity-0 group-hover:opacity-100 transition-opacity">→</span>
            </div>
            <p className="text-sm text-[#4a4455] leading-relaxed">
              {card.description}
            </p>
          </div>
        </button>
      ))}
    </div>
  );
}
