const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  theme: {
    extend: {
      fontFamily: {
        sans: [
          'Montserrat',
          ...defaultTheme.fontFamily.sans
        ],
        montserrat: [
          'Montserrat',
          ...defaultTheme.fontFamily.sans
        ],
        prata: [
          'Prata',
          ...defaultTheme.fontFamily.serif
        ]
      }
    }
  },
  variants: {},
  plugins: []
}
