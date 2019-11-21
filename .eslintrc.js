module.exports = {
  root: true,
  env: {
    browser: true,
    node: true
  },
  parserOptions: {
    parser: "babel-eslint"
  },
  extends: [
    "@nuxtjs",
    "@nuxtjs/eslint-config-typescript",
    "plugin:nuxt/recommended"
  ],
  rules: {
    "space-before-function-paren": 0
  }
};
