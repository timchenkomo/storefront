<template>
  <div class="font-montserrat">
    <nuxt />
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'

@Component
class PlainLayout extends Vue {
}

export default PlainLayout
</script>
