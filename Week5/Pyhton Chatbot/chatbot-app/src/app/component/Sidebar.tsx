export default function Sidebar() {
  return (
    <aside className="fixed left-0 top-0 h-screen w-72 bg-[#f2f3ff] flex flex-col justify-between z-50 shadow-[0_1px_8px_rgba(0,0,0,0.04)]">
      <div className="flex flex-col flex-1 min-h-0">
        <div className="px-6 pt-6 pb-2 flex items-center justify-between gap-2">
          <div className="flex items-center gap-2 min-w-0">
            <div className="h-8 w-8 bg-[#7c3aed] rounded-lg flex items-center justify-center text-white font-bold">PT</div>
            <span className="font-semibold text-sm text-[#131b2e] truncate">Python Tutor AI</span>
          </div>
          <span className="text-xs px-2 py-0.5 rounded bg-[#f2f3ff] text-[#630ed4]">v2.4</span>
        </div>

        <div className="px-3 py-1 flex flex-col gap-1">
          <button className="w-full flex items-center justify-between px-3 py-2 rounded-lg bg-[#630ed4] text-white hover:bg-[#7c3aed] transition-colors">
            <div className="flex items-center gap-2">
              <span className="text-base">+</span>
              <span className="font-semibold text-sm">New Chat</span>
            </div>
            <span className="text-xs px-1.5 py-0.5 rounded bg-white/20">⌘N</span>
          </button>
          <button className="w-full flex items-center justify-between px-3 py-2 rounded-lg bg-[#eaedff] hover:bg-[#e2e7ff] text-[#4a4455] hover:text-[#131b2e] transition-colors">
            <div className="flex items-center gap-2">
              <span className="text-base">🔍</span>
              <span className="text-sm">Search chats...</span>
            </div>
            <span className="text-xs px-1.5 py-0.5 rounded bg-white text-[#4a4455]">⌘F</span>
          </button>
        </div>

        <div className="flex-1 overflow-y-auto px-3 py-2 flex flex-col gap-4">
          <nav className="flex flex-col gap-1">
            <div className="px-2 pb-1">
              <span className="text-xs uppercase tracking-wider text-[#7b7487]">Today</span>
            </div>
            <a className="flex items-center px-2 py-1 rounded-lg text-[#4a4455] hover:bg-[#eaedff] hover:text-[#131b2e] transition-colors cursor-pointer">
              <span className="mr-2">💬</span>
              <span className="text-sm truncate">Python Lists Explained</span>
            </a>
            <a className="flex items-center px-2 py-1 rounded-lg text-[#4a4455] hover:bg-[#eaedff] hover:text-[#131b2e] transition-colors cursor-pointer">
              <span className="mr-2">💬</span>
              <span className="text-sm truncate">Debugging a TypeError</span>
            </a>
            <a className="flex items-center px-2 py-1 rounded-lg text-[#4a4455] hover:bg-[#eaedff] hover:text-[#131b2e] transition-colors cursor-pointer">
              <span className="mr-2">💬</span>
              <span className="text-sm truncate">Understanding Decorators</span>
            </a>
          </nav>

          <div className="flex flex-col gap-1">
            <div className="px-2 pb-1">
              <span className="text-xs uppercase tracking-wider text-[#7b7487]">Python Topics</span>
            </div>
            <nav className="flex flex-col gap-1">
              <a className="flex items-center px-2 py-1 bg-[#7c3aed] text-white font-semibold rounded-lg cursor-pointer">
                <span className="mr-2">🖥️</span>
                <span className="text-sm truncate">Python Basics</span>
              </a>
              <a className="flex items-center px-2 py-1 rounded-lg text-[#4a4455] hover:bg-[#eaedff] hover:text-[#131b2e] transition-colors cursor-pointer">
                <span className="mr-2">📊</span>
                <span className="text-sm truncate">Data Structures</span>
              </a>
              <a className="flex items-center px-2 py-1 rounded-lg text-[#4a4455] hover:bg-[#eaedff] hover:text-[#131b2e] transition-colors cursor-pointer">
                <span className="mr-2">💻</span>
                <span className="text-sm truncate">Functions</span>
              </a>
            </nav>
          </div>
        </div>
      </div>

      <div className="p-3 bg-[#eaedff]/60 flex items-center justify-between gap-2">
        <div className="flex items-center gap-2 min-w-0">
          <div className="w-8 h-8 rounded-full bg-[#7c3aed] flex items-center justify-center text-white font-bold">AR</div>
          <div className="flex flex-col min-w-0">
            <span className="font-semibold text-sm text-[#131b2e] truncate">Alex Rivera</span>
            <span className="text-xs text-[#630ed4] truncate">Python Pro</span>
          </div>
        </div>
        <div className="flex items-center gap-1">
          <button className="w-7 h-7 flex items-center justify-center rounded text-[#4a4455] hover:bg-[#e2e7ff] transition-colors">🌙</button>
          <button className="w-7 h-7 flex items-center justify-center rounded text-[#4a4455] hover:bg-[#e2e7ff] transition-colors">⚙️</button>
        </div>
      </div>
    </aside>
  );
}
