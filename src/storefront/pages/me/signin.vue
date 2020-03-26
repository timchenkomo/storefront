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
import { msgStore } from '@/store/index'

@Component
class SignInPage extends Vue {
  private async onSignInClicked(form: SignInForm) {
    const credentials = new FormData()
    credentials.set('username', form.login)
    credentials.set('password', form.password)

    try {
      await this.$auth.loginWith('local', { data: credentials })

      if (this.$auth.loggedIn) {
        msgStore.add({ msg: 'Вы вошли', color: 'green' })
        const returnBackUrl = (this.$route.query.r as string) || '/books'
        this.$router.push(returnBackUrl)
      }
    } catch {
      msgStore.add({ msg: 'Неверный логин/пароль' })
    }
  }
}

export default SignInPage
</script>
