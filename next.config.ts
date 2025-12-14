import type { NextConfig } from "next";

const isProd = process.env.NODE_ENV === 'production';

const nextConfig: NextConfig = {
  /* config options here */
  images: {
    unoptimized: true,
  },
  basePath: isProd ? '/Blobby' : '',
  assetPrefix: isProd ? '/Blobby/' : '',
  output: "export",
};

export default nextConfig;
