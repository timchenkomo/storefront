<template>
  <form>
    <div class="mb-4">
      <input
        v-model="login"
        class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        type="text"
        placeholder="EMail"
      >
    </div>

    <!-- Restore password -->
    <button
      @click="onRestoreClicked"
      :class="{
        'bg-blue-400 cursor-not-allowed': !isLoginValid,
        'hover:bg-blue-700 bg-blue-500 cursor-pointer': isLoginValid}"
      class="text-white font-bold py-2 px-4 w-full rounded focus:outline-none focus:shadow-outline"
      type="button"
    >
      Восстановить пароль
    </button>
  </form>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'

@Component
class RestorePasswordForm extends Vue {
  private login: string = ''
  private onRestoreClicked() {
    if (this.isLoginValid) {
      this.$emit('restore', { login: this.login })
    }
  }
  private get isLoginValid(): bool {
    return this.login.length > 0
  }
}

export default RestorePasswordForm
</script>
