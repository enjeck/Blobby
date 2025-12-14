'use client';

import { useState, useEffect, useRef, useCallback } from 'react';
import { generateCharacter } from '@/lib/character';

export default function Home() {
  const [svgContent, setSvgContent] = useState('');
  const [generatedCharacters, setGeneratedCharacters] = useState<string[]>([]);
  const [showScrollTop, setShowScrollTop] = useState(false);
  const observerRef = useRef<IntersectionObserver | null>(null);
  const loadMoreRef = useRef<HTMLDivElement | null>(null);

  const generateNew = () => {
    setSvgContent(generateCharacter());
  };

  // Generate initial characters
  useEffect(() => {
    generateNew();
    const initial = Array.from({ length: 8 }, () => generateCharacter());
    setGeneratedCharacters(initial);
  }, []);

  // Load more characters when scrolling
  const loadMoreCharacters = useCallback(() => {
    const newCharacters = Array.from({ length: 4 }, () => generateCharacter());
    setGeneratedCharacters(prev => [...prev, ...newCharacters]);
  }, []);

  // Track scroll position for scroll-to-top button
  useEffect(() => {
    const handleScroll = () => {
      setShowScrollTop(window.scrollY > 800);
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  // Set up intersection observer for infinite scroll
  useEffect(() => {
    observerRef.current = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting) {
          loadMoreCharacters();
        }
      },
      { threshold: 0.1 }
    );

    if (loadMoreRef.current) {
      observerRef.current.observe(loadMoreRef.current);
    }

    return () => {
      if (observerRef.current) {
        observerRef.current.disconnect();
      }
    };
  }, [loadMoreCharacters]);

  const downloadSVG = () => {
    const blob = new Blob([svgContent], { type: 'image/svg+xml' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'blobby.svg';
    a.click();
    URL.revokeObjectURL(url);
  };

  const downloadPNG = () => {
    // Convert SVG to PNG using canvas
    const canvas = document.createElement('canvas');
    canvas.width = 400;
    canvas.height = 400;
    const ctx = canvas.getContext('2d');
    
    const img = new Image();
    const svgBlob = new Blob([svgContent], { type: 'image/svg+xml;charset=utf-8' });
    const url = URL.createObjectURL(svgBlob);
    
    img.onload = () => {
      ctx?.drawImage(img, 0, 0);
      canvas.toBlob((blob) => {
        if (blob) {
          const pngUrl = URL.createObjectURL(blob);
          const a = document.createElement('a');
          a.href = pngUrl;
          a.download = 'blobby.png';
          a.click();
          URL.revokeObjectURL(pngUrl);
        }
      });
      URL.revokeObjectURL(url);
    };
    
    img.src = url;
  };

  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <main className="min-h-screen p-8">
      <div className="max-w-8xl mx-auto">
        <div className="grid md:grid-cols-2 gap-8 mb-12 mt-12 items-center">
          <div className="intro">
            <h1 className="text-7xl font-bold mb-4 blobby-title">Blobby</h1>
            <h2 className="text-4xl mb-4">Random blob characters</h2>
            <p className="mb-4 text-lg">
              No characters are the same! Each Blobby character has a different
              body shape. The shape is always unique, and the colors and eyes are
              randomly applied to each shape.
            </p>
            <p className="mb-6 text-lg">
              Feel free to download the images and use any Blobby character wherever
              you wish. Ideally, the characters can be used as avatars.
            </p>
            <div className="flex gap-4 flex-wrap">
              <button
                onClick={generateNew}
                className="px-6 py-3 bg-[#B5EAEA] border-3 border-[#B5EAEA] rounded-md text-base font-normal cursor-pointer transition-all hover:bg-[hsl(180,56%,62%)] focus:outline-none focus:ring-4 focus:ring-[#B5EAEA] focus:ring-opacity-50"
                aria-label="Generate new character"
              >
                New character
              </button>
              <button
                onClick={downloadSVG}
                className="px-6 py-3 bg-transparent border-[3px] border-[#B5EAEA] rounded-md text-base font-normal cursor-pointer transition-all hover:bg-[hsl(180,56%,62%)] focus:outline-none focus:ring-4 focus:ring-[#B5EAEA] focus:ring-opacity-50"
                aria-label="Download character as SVG file"
              >
                Download SVG
              </button>
              <button
                onClick={downloadPNG}
                className="px-6 py-3 bg-transparent border-[3px] border-[#B5EAEA] rounded-md text-base font-normal cursor-pointer transition-all hover:bg-[hsl(180,56%,62%)] focus:outline-none focus:ring-4 focus:ring-[#B5EAEA] focus:ring-opacity-50"
                aria-label="Download character as PNG file"
              >
                Download PNG
              </button>
            </div>
          </div>
          <div className="character flex justify-center items-center">
            <div
              dangerouslySetInnerHTML={{ __html: svgContent }}
              className="w-full max-w-md"
              role="img"
              aria-label="Current blob character"
            />
          </div>
        </div>

        {/* Examples section */}
        <div className="mt-32">
          <h2 className="text-center text-3xl font-semibold mb-6">Some creations</h2>
          <div className="examples grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-4 gap-4 justify-center mx-auto" role="region" aria-label="Generated blob characters gallery">
            {generatedCharacters.map((char, i) => (
              <div
                key={i}
                dangerouslySetInnerHTML={{ __html: char }}
                className="w-full aspect-square"
                role="img"
                aria-label={`Generated blob character ${i + 1}`}
              />
            ))}
          </div>
          {/* Invisible element to trigger loading more */}
          <div ref={loadMoreRef} className="h-20 flex items-center justify-center">
            <p className="text-gray-400">Loading more...</p>
          </div>
        </div>
      </div>

      {/* Scroll to top button */}
      {showScrollTop && (
        <button
          onClick={scrollToTop}
          className="fixed bottom-8 right-8 p-4 bg-[#B5EAEA] rounded-full shadow-lg hover:bg-[hsl(180,56%,62%)] transition-all z-50 focus:outline-none focus:ring-4 focus:ring-[#B5EAEA] focus:ring-opacity-50"
          aria-label="Scroll to top of page"
          title="Back to top"
        >
          <svg
            className="w-6 h-6"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M5 10l7-7m0 0l7 7m-7-7v18"
            />
          </svg>
        </button>
      )}
    </main>
  );
}
