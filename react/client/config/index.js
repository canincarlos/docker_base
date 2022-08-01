const dev = process.env.NODE_ENV !== 'production'

export const server = dev ? 'http://localhost:3000' : 'https://yourwebsite.com'
// export const api = "https://api.sampleapis.com/futurama/info"
export const api = "http://localhost:8000/api"