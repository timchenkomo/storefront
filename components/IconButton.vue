<template>
  <div class="inline-block mr-6">
    <img :src="iconUrl" class="h-5 mr-4 inline-block fill-current">
    <span class="text-sm font-light">
      <slot />
    </span>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'

@Component
class IconButton extends Vue {
  @Prop() readonly iconUrl!: string
}

export default IconButton
</script>
