<template>
  <div class="flex flex-col items-center">
    <h1 class="w-64 mb-4 text-xl text-center">
      Регистрация
    </h1>

    <signup-form @signup="onSignUpClicked" class="w-64" />
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'nuxt-property-decorator'
import axios from 'axios'

@Component
class SignUpPage extends Vue {
  private async onSignUpClicked({ login, password, promocode }) {
    await axios.post('http://localhost:8000/me/signup', { login, password, promocode })
  }
}

export default SignUpPage
</script>
