<template>
  <span class="relative">
    <!-- Main button -->
    <button @click="onClicked" class="py-2 px-4 bg-blue-500 text-white rounded">
      <span>
        Мои книги

        <!-- Main button badge -->
        <span v-if="count > 0" class="px-2 bg-red-600 rounded-lg">
          {{ count }}
        </span>
      </span>
    </button>

    <!-- Overlay -->
    <button
      v-if="open"
      @click="onCloseClicked"
      tabindex="-1"
      class="fixed inset-0 w-full h-full cursor-default"
    />

    <!-- Menu items -->
    <div v-if="open" class="absolute right-0 flex flex-col bg-white rounded py-2 mt-2 w-48 shadow-md border-gray-300">
      <a href="#" class="px-4 py-2 hover:bg-blue-500 hover:text-white">Корзина</a>
      <a href="#" class="px-4 py-2 hover:bg-blue-500 hover:text-white">Мои книги</a>
      <a href="#" class="px-4 py-2 hover:bg-blue-500 hover:text-white">Отложенные</a>
    </div>
  </span>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'

@Component
class AccountButton extends Vue {
  @Prop({ default: false }) readonly active!: boolean;
  @Prop({ default: false }) readonly open!: boolean;
  @Prop({ default: 0 }) readonly count!: number;

  private onClicked() {
    this.$emit('click')
  }

  private onCloseClicked() {
    this.$emit('close')
  }
}

export default AccountButton
</script>
