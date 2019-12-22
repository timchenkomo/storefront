<template functional>
  <div
    :ref="data.ref"
    :style="[data.style, data.staticStyle]"
    :class="[data.class, data.staticClass]"
    v-bind="data.attrs"
    v-on="listeners"
    class="overflow-hidden mb-3"
  >
    <div class="flex relative justify-center items-center">
      <img :src="props.cover" class="rounded w-full">
      <slot name="cover" />
    </div>

    <div class="text-center my-2">
      <div class="font-bold text-sm leading-tight my-1">
        {{ props.title }}
      </div>
      <p class="text-gray-500 text-xs leading-none">
        {{ props.author }}
      </p>
    </div>
  </div>
</template>
