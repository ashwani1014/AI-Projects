export default function Header() {
  return (
    <header className="fixed top-0 left-72 right-0 h-16 bg-[#faf8ff]/80 backdrop-blur-xl z-40 shadow-[0_1px_8px_rgba(0,0,0,0.04)]">
      <div className="w-full h-16 px-6 flex items-center justify-between gap-4">
        <div className="flex items-center gap-2 min-w-0">
          <span className="font-semibold text-sm text-[#131b2e] truncate">Python Tutor AI</span>
          <span className="text-[#7b7487] text-xs">·</span>
          <span className="text-xs text-[#4a4455] truncate">Model: Python-Specialist-4o</span>
          <span className="text-[#7b7487] text-xs">·</span>
          <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-[#630ed4]/10 text-[#630ed4]">
            <span className="w-1.5 h-1.5 rounded-full bg-[#630ed4]"></span>
            <span className="text-xs font-medium">Python Programming Only</span>
          </div>
        </div>
        <div className="flex items-center gap-2 flex-shrink-0">
          <button className="inline-flex items-center gap-1.5 px-3 py-1 rounded-lg bg-[#eaedff] hover:bg-[#e2e7ff] text-[#4a4455] hover:text-[#131b2e] text-sm transition-colors">
            📤 Share Chat
          </button>
          <button className="inline-flex items-center gap-1.5 px-3 py-1 rounded-lg bg-[#630ed4] text-white hover:bg-[#7c3aed] font-semibold text-sm transition-colors">
            ⭐ Upgrade to Pro
          </button>
        </div>
      </div>
    </header>
  );
}
