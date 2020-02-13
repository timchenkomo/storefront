<template>
  <span class="relative">
    <button
      @click="toggle(true)"
      :class="{'bg-blue-500 hover:bg-blue-600 rounded text-white': fill}"
      class="hidden sm:block whitespace-no-wrap px-4 py-2"
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
  @Prop({ default: false }) readonly fill!: boolean
  private open: boolean = false

  public toggle(value: boolean) {
    this.open = value
  }
}

export default NavMenu
</script>
