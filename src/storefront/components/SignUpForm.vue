<template>
  <form>
    <!-- User info -->
    <div class="mb-4">
      <input v-model="name" class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" type="text" placeholder="Ваше имя">
    </div>

    <div class="mb-4">
      <input v-model="login" class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" type="email" placeholder="EMail">
    </div>

    <div class="mb-4">
      <input v-model="password" class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" type="password" placeholder="Пароль">
    </div>

    <div class="mb-4">
      <div class="relative">
        <input v-model="promocode" class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" placeholder="Промо-код">
        <div class="inline absolute bg-green-500 rounded rounded-full x-0 y-0 px-4 py-4 center-y w-24 h-24 mx-2 text-white text-center text-sm leading-none">
          <div class="flex flex-col justify-center h-full">
            <div>Скидка</div>
            <div class="font-bold text-lg">
              20%
            </div>
            <div class="text-xs">
              на все книги
            </div>
          </div>
        </div>
      </div>

      <div class="my-1 text-xs text-gray-300 leading-tight">
        Если у вас сейчас нет промокода, то вы можете ввести его после регистрации в разделе "Профиль".
      </div>
    </div>

    <!-- Submit button -->
    <button
      @click="onSignUpClicked"
      :class="{ 'opacity-50': !isFormValid, 'cursor-not-allowed': !isFormValid }"
      class="bg-blue-500 hover:bg-blue-700 text-white font-bold my-1 py-2 px-4 w-full rounded focus:outline-none focus:shadow-outline"
      type="button"
    >
      Регистрация
    </button>

    <nuxt-link
      class="block text-blue-500 text-center font-bold my-1 py-2 px-4 w-full rounded focus:outline-none"
      :to="returnBackUrl ? '/me/signin?r=' + returnBackUrl : '/me/signin'"
      type="button"
    >
      Войти
    </nuxt-link>
  </form>
</template>

<script lang="ts">
import { Vue, Component } from 'nuxt-property-decorator'

@Component
class SignInForm extends Vue {
  private name: string = '';
  private login: string = '';
  private password: string = '';
  private promocode: string = '';

  private onSignUpClicked() {
    if (!this.isFormValid) { return }
    this.$emit('signup', {
      name: this.name,
      login: this.login,
      password: this.password,
      promocode: this.promocode
    })
  }

  private get isFormValid(): boolean {
    if (this.name.trim().length === 0) { return false }
    if (this.login.trim().length === 0) { return false }
    if (!this.login.includes('@')) { return false }
    if (this.password.length < 3) { return false }
    return true
  }

  private get returnBackUrl(): string {
    return this.$route.query.r
  }
}

export default SignInForm
</script>

<style>
.center-y {
  transform:translateY(-25%);
}
</style>
