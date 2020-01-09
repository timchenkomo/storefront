<template>
  <div class="flex flex-col items-center">
    <h1 class="w-64 mb-4 text-xl text-center">
      Вход
    </h1>

    <login-form @signin="onSignInClicked" class="w-64" />
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'nuxt-property-decorator'
import { SignInForm } from '@/lib/forms.ts'
import { msgStore, userStore } from '@/store/index'

@Component
class LoginPage extends Vue {
  private async onSignInClicked(form: SignInForm) {
    const authenticated = await userStore.signIn(form)

    if (authenticated) {
      msgStore.add({ msg: 'Вы вошли' })
      this.$router.push('/books')
    } else {
      msgStore.add({ msg: 'Неверный логин/пароль' })
    }
  }
}

export default LoginPage
</script>
