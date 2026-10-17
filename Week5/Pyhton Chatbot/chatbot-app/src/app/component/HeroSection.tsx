export default function HeroSection() {
  return (
    <div className="flex flex-col items-center text-center space-y-4 mb-6">
      <div className="relative group cursor-pointer transition-transform duration-300 hover:scale-105">
        <div className="absolute -inset-2 bg-gradient-to-r from-[#7c3aed] to-[#712edd] rounded-2xl blur-lg opacity-25 group-hover:opacity-45 transition duration-500"></div>
        <div className="relative w-16 h-16 rounded-xl bg-white shadow-md flex items-center justify-center p-2.5">
          <div className="w-full h-full bg-[#7c3aed] rounded-lg flex items-center justify-center text-white font-bold text-xl">PT</div>
        </div>
      </div>

      <div className="relative group inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#f2f3ff] shadow-sm">
        <span className="relative flex h-2 w-2">
          <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#630ed4] opacity-75"></span>
          <span className="relative inline-flex rounded-full h-2 w-2 bg-[#630ed4]"></span>
        </span>
        <span className="text-xs text-[#131b2e] font-semibold tracking-wide uppercase">Python Programming Only</span>
        <span className="text-xs text-[#7b7487]">v3.12 active</span>
      </div>

      <div className="space-y-1.5 max-w-xl">
        <h1 className="text-3xl font-bold text-[#131b2e] tracking-tight">
          Your Personal Python Mentor
        </h1>
        <p className="text-lg text-[#4a4455]">
          Learn Python, debug code, and build real-world projects.
        </p>
      </div>

      <div className="flex flex-wrap items-center justify-center gap-2 pt-1">
        <span className="text-xs px-2.5 py-1 rounded-md bg-[#eaedff] text-[#4a4455]">CPython 3.12.3</span>
        <span className="text-xs px-2.5 py-1 rounded-md bg-[#eaedff] text-[#4a4455]">mypy --strict</span>
        <span className="text-xs px-2.5 py-1 rounded-md bg-[#eaedff] text-[#4a4455]">ruff linter</span>
        <span className="text-xs px-2.5 py-1 rounded-md bg-[#d2bbff] text-[#25005a] font-medium">Interactive REPL</span>
      </div>
    </div>
  );
}
