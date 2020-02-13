<template>
  <form>
    <div class="mb-4">
      <input
        v-model="password"
        class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        type="text"
        placeholder="Новый пароль"
      >
    </div>

    <button
      @click="onSaveClicked"
      :class="{
        'bg-blue-400 cursor-not-allowed': !isPasswordValid,
        'hover:bg-blue-700 bg-blue-500 cursor-pointer': isPasswordValid}"
      class="text-white font-bold py-2 px-4 w-full rounded focus:outline-none focus:shadow-outline"
      type="button"
    >
      Изменить пароль
    </button>
  </form>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'

@Component
class ChangePasswordForm extends Vue {
  private password: string = ''
  private onSaveClicked() {
    if (this.isPasswordValid) {
      this.$emit('save', this.password)
    }
  }
  private get isPasswordValid(): boolean {
    return this.password.length > 3
  }
}

export default ChangePasswordForm
</script>
