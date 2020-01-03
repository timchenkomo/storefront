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
import axios from 'axios'
import { SignInForm } from '@/lib/forms.ts'

@Component
class LoginPage extends Vue {
  private async onSignInClicked(form: SignInForm) {
    await axios.post('http://localhost:8000/me/signin', form)
  }
}

export default LoginPage
</script>
