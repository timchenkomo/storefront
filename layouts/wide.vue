<template>
  <div class="font-montserrat">
    <nav-bar />
    <nuxt />
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'

@Component()
class WideLayout extends Vue {
}

export default WideLayout
</script>
