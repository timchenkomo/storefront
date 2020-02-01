<template>
  <span class="relative">
    <button
      @click="toggle(true)"
      class="hidden sm:block px-4 py-2 whitespace-no-wrap"
    >
      <slot name="activator">{{ title }}</slot>
    </button>

    <nuxt-link
      :to="link"
      class="sm:hidden"
    >
      {{ title }}
    </nuxt-link>

    <!-- Overlay -->
    <button
      v-if="open"
      @click="toggle(false)"
      tabindex="-1"
      class="fixed inset-0 w-full h-full cursor-default"
      style="z-index: 98"
    />

    <!-- Dropdown content -->
    <div
      v-if="open"
      class="absolute right-0 bg-white rounded py-2 mt-2 shadow-md"
      style="z-index: 99"
    >
      <slot />
    </div>
  </span>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'

@Component
class NavMenu extends Vue {
  @Prop({ default: '' }) readonly title!: string
  @Prop({ default: '' }) readonly link!: string
  private open: bool = false

  private toggle(value: bool) {
    this.open = value
  }
}

export default NavMenu
</script>
