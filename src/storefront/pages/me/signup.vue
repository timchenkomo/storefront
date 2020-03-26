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
import { msgStore } from '@/store/index'
import { SignUpForm } from '@/lib/forms.ts'

@Component
class SignUpPage extends Vue {
  private async onSignUpClicked(form: SignUpForm) {
    const { data } = await this.$axios.post('/me/signup', form)
    if (data.success) {
      // login after registration
      const credentials = new FormData()
      credentials.set('username', form.login)
      credentials.set('password', form.password)
      await this.$auth.loginWith('local', { data: credentials })

      // go to the /books page
      msgStore.add({ msg: 'Вы были успешно зарегистрированы!', color: 'green' })
      const returnBackUrl = this.$route.query.r || '/books'
      this.$router.push(returnBackUrl)
    } else {
      const errorMsg = Object.prototype.hasOwnProperty.call(data, 'msg') && data.msg.length > 0 ? data.msg : ''
      msgStore.add({ msg: 'Ошибка во время регистрации. ' + errorMsg, color: 'red' })
    }
  }
}

export default SignUpPage
</script>
