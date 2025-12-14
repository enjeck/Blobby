import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Blobby - Random Blob Character Generator | Unique Avatar Creator",
  description: "Generate unique blob characters with random shapes, colors, and expressions. Perfect for avatars, profile pictures, and creative projects. Download as SVG or PNG.",
  keywords: ["blob generator", "avatar generator", "character creator", "random avatar", "svg generator", "profile picture"],
  authors: [{ name: "Blobby" }],
  openGraph: {
    title: "Blobby - Random Blob Character Generator",
    description: "Generate unique blob characters for avatars and creative projects",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
