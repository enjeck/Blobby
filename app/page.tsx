'use client';

import { useState, useEffect } from 'react';
import { generateCharacter } from '@/lib/character';

export default function Home() {
  const [svgContent, setSvgContent] = useState('');

  const generateNew = () => {
    setSvgContent(generateCharacter());
  };

  // Generate on mount
  useEffect(() => {
    generateNew();
  }, []);

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

  return (
    <main className="min-h-screen p-8">
      <div className="max-w-7xl mx-auto">
        <div className="grid md:grid-cols-2 gap-8 mb-12 mt-12 items-center">
          <div className="intro">
            <h1 className="text-7xl font-bold mb-4 blobby-title">Blobby</h1>
            <h3 className="text-4xl mb-4">Generative blob characters</h3>
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
                className="px-6 py-3 bg-[#B5EAEA] border-3 border-[#B5EAEA] rounded-md text-base font-normal cursor-pointer transition-all hover:bg-[hsl(180,56%,62%)]"
              >
                New character
              </button>
              <button
                onClick={downloadSVG}
                className="px-6 py-3 bg-transparent border-[3px] border-[#B5EAEA] rounded-md text-base font-normal cursor-pointer transition-all hover:bg-[hsl(180,56%,62%)]"
              >
                Download SVG
              </button>
              <button
                onClick={downloadPNG}
                className="px-6 py-3 bg-transparent border-[3px] border-[#B5EAEA] rounded-md text-base font-normal cursor-pointer transition-all hover:bg-[hsl(180,56%,62%)]"
              >
                Download PNG
              </button>
            </div>
          </div>
          <div className="character flex justify-center items-center">
            <div
              dangerouslySetInnerHTML={{ __html: svgContent }}
              className="w-full max-w-md"
            />
          </div>
        </div>

        {/* Examples section */}
        <div className="mt-32">
          <p className="text-center text-xl mb-6">Some creations</p>
          <div className="examples grid grid-cols-5 md:grid-cols-10 gap-1 justify-center">
            {[...Array(30)].map((_, i) => (
              <img
                key={i}
                src={`/examples/blobby${i + 1}.png`}
                alt={`Blobby ${i + 1}`}
                className="w-full"
              />
            ))}
          </div>
        </div>
      </div>
    </main>
  );
}
