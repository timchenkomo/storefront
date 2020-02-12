<template>
  <div class="flex flex-col items-center">
    <h1 class="w-64 mb-4 text-xl text-center">
      Восстановление пароля
    </h1>

    <restore-password-form @restore="onRestoreClicked" class="w-64" />
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import { msgStore } from '@/store/index'
import RestorePasswordForm from '@/components/RestorePasswordForm.vue'

@Component({ components: { RestorePasswordForm } })
class RestorePage extends Vue {
  async private onRestoreClicked({ login }) {
    try {
      await this.$axios.post('/me/password/restore', { email: login })
      msgStore.add({ msg: 'Инструкция по восстановлению пароля выслана', color: 'green' })
    } catch (ex) {
      msgStore.add({ msg: 'Ошибка при восстановлении пароля' })
    }
  }
}

export default RestorePage
</script>
