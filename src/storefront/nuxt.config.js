export default {
  mode: 'universal',
  env: {
    baseUrl: process.env.BASE_URL || 'http://localhost:3000',
    baseUrlApi: process.env.BASE_URL_API || 'http://localhost:8000',
    baseUrlApiBrowser: process.env.BASE_URL_API_BROWSER || 'http://localhost:8000'
  },
  /*
   ** Headers of the page
   */
  head: {
    title: 'BBT Online',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: process.env.npm_package_description || ''
      }
    ],
    link: [{ rel: 'icon', href: '/favicon.png' }]
  },
  /*
   ** Customize the progress-bar color
   */
  loading: { color: '#fff' },
  /*
   ** Global CSS
   */
  css: [],
  /*
   ** Plugins to load before mounting the App
   */
  plugins: [
    '~/plugins/icons',
    '~/plugins/ui-kit',
    '~/plugins/axios-accessor',
    { src: '~/plugins/local-storage.js', ssr: false },
    { src: '~/plugins/vue-lazyimage', ssr: false }
  ],
  /*
   ** Nuxt.js dev-modules
   */
  buildModules: [
    // Doc: https://github.com/nuxt-community/eslint-module
    '@nuxt/typescript-build'
  ],
  /*
   ** Nuxt.js modules
   */
  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/auth',
    '@nuxtjs/tailwindcss',
    'nuxt-webfontloader',
    'nuxt-svg-loader',
    'nuxt-purgecss'
  ],
  /*
   ** Axios module configuration
   ** See https://axios.nuxtjs.org/options
   */
  axios: {
    credentials: true,
    baseURL: (process.env.BASE_URL_API || 'http://localhost:8000') + '/api',
    browserBaseURL: (process.env.BASE_URL || 'http://localhost:8000') + '/api'
  },
  /*
   ** Build configuration
   */
  build: {
    /*
     ** You can extend webpack config here
     */
    // extend(config, ctx) {}
    postcss: {
      plugins: {
        tailwindcss: 'tailwind.config.js'
      }
    }
  },
  purgeCSS: {
    mode: 'postcss'
  },
  auth: {
    strategies: {
      local: {
        endpoints: {
          login: { url: '/me/signin', method: 'post', propertyName: 'access_token' },
          logout: { url: '/me/signout', method: 'post' },
          user: { url: '/me/', method: 'get', propertyName: false }
        }
      }
    },
    redirect: {
      login: '/me/signin',
      logout: '/',
      home: false,
      callback: '/me'
    },
    rewriteRedirects: false
  },
  webfontloader: {
    google: {
      families: ['Montserrat', 'Prata']
    }
  }
}
