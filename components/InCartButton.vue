<template>
  <div @click="onClicked" class="rounded text-blue-500 py-2 border border-solid border-blue-500 text-sm font-semibold text-center inline-block px-4 cursor-pointer hover:border-blue-600 hover:text-blue-600">
    В корзину

    <!-- <div class="py-2 px-4">
        <svg
          class="h-6 inline-block"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 21 19"
        >
          <defs>
            <style>
              .def { fill: #ffffff; }
            </style>
          </defs>
          <g>
            <path
              class="def"
              d="M9,15a2,2,0,1,0,2,2A2,2,0,0,0,9,15Zm0,3a1,1,0,1,1,1-1A1,1,0,0,1,9,18Zm8-3a2,2,0,1,0,2,2A2,2,0,0,0,17,15Zm0,3a1,1,0,1,1,1-1A1,1,0,0,1,17,18ZM20.52,5.88A2.27,2.27,0,0,0,18.72,5H5.55L4.87,2A2.62,2.62,0,0,0,2.31,0H.5A.5.5,0,0,0,0,.5.5.5,0,0,0,.5,1H2.31A1.62,1.62,0,0,1,3.89,2.26L6.07,11.7A3,3,0,0,0,9,14h8.1A3,3,0,0,0,20,11.75l1-3.92A2.27,2.27,0,0,0,20.52,5.88ZM18.72,6A1.27,1.27,0,0,1,20,7.59L19.61,9H6.47L5.78,6ZM19,11.51A2,2,0,0,1,17.07,13H9a2,2,0,0,1-1.92-1.53L6.71,10H19.36Z"
            />
          </g>
        </svg>
      </div> -->
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'

@Component
class InCartButton extends Vue {
  private onClicked() {
    this.$emit('click')
  }
}

export default InCartButton
</script>
