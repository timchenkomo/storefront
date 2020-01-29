<template>
  <span class="relative">
    <slot name="activator">
      <button
        @click="onOpenCloseClicked(true)"
        class="text-white rounded bg-blue-500 px-4 py-2"
      >
        {{ title }}
      </button>
    </slot>

    <!-- Overlay -->
    <button
      v-if="open"
      @click="onOpenCloseClicked(false)"
      tabindex="-1"
      class="fixed inset-0 w-full h-full cursor-default"
    />

    <!-- Dropdown content -->
    <div
      v-if="open"
      class="absolute right-0 bg-white rounded py-2 mt-2 shadow-md"
    >
      <slot>
        Here is some stuff
      </slot>
    </div>

  </span>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'nuxt-property-decorator'

@Component
class Dropdown extends Vue {
  @Prop({ default: false }) readonly open: boolean
  @Prop() readonly title: string

  private onOpenCloseClicked(value: boolean) {
    this.$emit('open', value)
  }
}

export default Dropdown
</script>
