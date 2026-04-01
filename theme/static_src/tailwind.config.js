/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../../templates/**/*.html",
  ],
  theme: {
    extend: {
      colors: {
        sky: {
          950: '#0a1628',
        },
        teal: {
          450: '#2dd4bf',
        },
        gold: {
          400: '#f5c842',
          500: '#e6b800',
        },
      },
      fontFamily: {
        display: ['"Playfair Display"', 'Georgia', 'serif'],
        body: ['"DM Sans"', 'system-ui', 'sans-serif'],
      },
      animation: {
        'fade-up': 'fadeUp 0.6s ease-out both',
        'fade-in': 'fadeIn 0.8s ease-out both',
      },
      keyframes: {
        fadeUp: {
          '0%': { opacity: '0', transform: 'translateY(24px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
      },
    },
  },
  plugins: [],
  safelist: [
    'animate-fade-up',
    'animate-fade-in',
  ],
}