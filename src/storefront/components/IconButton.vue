<template>
  <div
    :class="{ 'text-blue-500': active }"
    @click="onClicked"
  >
    <!-- Icon -->
    <slot name="icon" />

    <!-- Title -->
    <span class="text-sm font-light">
      <slot />
    </span>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'

@Component
class IconButton extends Vue {
  @Prop({ default: false }) readonly active!: boolean;

  private onClicked() {
    this.$emit('click')
  }
}

export default IconButton
</script>
