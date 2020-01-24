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
      msgStore.add({ msg: 'Вы были успешно зарегистрированы!', color: 'green' })
      this.$router.push('/books')
    } else {
      msgStore.add({ msg: 'Ошибка во время регистрации', color: 'red' })
    }
  }
}

export default SignUpPage
</script>
