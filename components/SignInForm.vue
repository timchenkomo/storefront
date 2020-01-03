<template>
  <form>
    <!-- Email and password -->
    <div class="mb-4">
      <input v-model="login" class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" type="text" placeholder="EMail">
    </div>
    <div class="mb-6">
      <input v-model="password" class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" type="password" placeholder="Пароль">
    </div>

    <!-- Sign In -->
    <button
      @click="onSignInClicked"
      class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 w-full rounded focus:outline-none focus:shadow-outline"
      type="button"
    >
      Войти
    </button>

    <nuxt-link
      to="/me/signup"
      class="block text-blue-500 text-center font-bold my-1 py-2 px-4 w-full rounded focus:outline-none"
      type="button"
    >
      Регистрация
    </nuxt-link>
    <!-- Restore password -->
    <!--
         <a
         class="inline-block align-baseline font-bold text-sm text-blue-500 hover:text-blue-800"
         href="#"
         >
         Забыли пароль?
         </a>
    -->
  </form>
</template>

<script lang="ts">
import { Vue, Component } from 'nuxt-property-decorator'

@Component
class SignInForm extends Vue {
  private login: string = '';
  private password: string = '';

  private onSignInClicked() {
    this.$emit('signin', { login: this.login, password: this.password })
  }
}

export default SignInForm
</script>
