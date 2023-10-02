/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'public',
  experimental: {
    serverActions: true,
  },
}

module.exports = nextConfig
