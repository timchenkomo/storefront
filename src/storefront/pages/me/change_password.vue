<template>
  <div class="flex flex-col items-center">
    <h1 class="w-64 mb-4 text-xl text-center">
      Новый пароль
    </h1>

    <change-password-form @save="onSaveClicked" class="w-64" />
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import { msgStore } from '@/store/index'
import ChangePasswordForm from '@/components/ChangePasswordForm.vue'

@Component({ components: { ChangePasswordForm } })
class ChangePasswordPage extends Vue {
  async private onSaveClicked({ password }) {
    try {
      const token = this.$route.query.token
      const { data } = await this.$axios.post('/me/password/change', { token, password })
      if (data.success) {
        msgStore.add({ msg: 'Пароль успешно изменён', color: 'green' })
        this.$router.push('/me/signin')
      } else {
        msgStore.add({ msg: data.msg || 'Ошибка', color: 'red' })
      }
    } catch (ex) {
      msgStore.add({ msg: 'Ошибка при смене пароля' })
    }
  }
}

export default ChangePasswordPage
</script>
