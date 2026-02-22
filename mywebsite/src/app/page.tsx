export default function Home() {
  return (
    <main className="min-h-screen bg-gray-100 flex flex-col items-center justify-center text-center p-8">
      <h1 className="text-5xl font-bold text-pink-500 mb-4">
        Vanessa Wang
      </h1>

      <p className="text-lg text-gray-700 max-w-xl mb-6">
        Hi! I'm a second year cybersecurity and fintech student at Northeastern University.
      </p>

      <div className="flex gap-6">
        <a
          href="https://github.com/vanessawangg"
          target="_blank"
          className="text-blue-500 hover:underline"
        >
          GitHub
        </a>

        <a
          href="https://linkedin.com/in/vanessawang7"
          target="_blank"
          className="text-blue-500 hover:underline"
        >
          LinkedIn
        </a>
      </div>
    </main>
  );
}