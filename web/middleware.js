import { NextResponse } from 'next/server'

export function middleware(request) {
  const response = NextResponse.next()

  // X-Frame-Options (Allow all origins)
  response.headers.set('X-Frame-Options', 'ALLOWALL')

  // Content-Security-Policy (Allow all origins for iframe embedding)
  response.headers.set('Content-Security-Policy', 'frame-ancestors *;')

  return response
}
