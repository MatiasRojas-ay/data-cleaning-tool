export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts}"],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#f0f8ff',  // Celeste muy suave
          100: '#e0f7fa', // Azul muy claro
          200: '#b2ebf2', // Azul pastel
          300: '#80deea', // Azul cielo
          400: '#4dd0e1', // Celeste medio
          500: '#26c6da', // Celeste fuerte
          600: '#00bcd4', // Azul turquesa
          700: '#0097a7', // Azul oscuro
          800: '#007b82', // Azul marino
          900: '#004d56', // Azul marino muy oscuro
        },
        secondary: {
          50: '#e1f5fe',  // Celeste muy suave
          100: '#b3e5fc', // Azul muy claro
          200: '#81d4fa', // Azul pastel
          300: '#4fc3f7', // Azul cielo
          400: '#29b6f6', // Celeste medio
          500: '#03a9f4', // Azul fuerte
          600: '#0288d1', // Azul oscuro
          700: '#0277bd', // Azul marino
          800: '#01579b', // Azul marino muy oscuro
          900: '#003c69', // Azul noche
        },
      },
      fontFamily: {
        sans: ['Poppins', 'ui-sans-serif', 'system-ui'],
      },
    },
  },
  plugins: [],
}