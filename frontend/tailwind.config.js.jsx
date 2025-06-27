/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],

    theme: {
        extend: {
            maskImage: {
                'fade-right': 'linear-gradient(to right, black 80%, transparent 100%)',
            },
        },
    },
    plugins: [],
}