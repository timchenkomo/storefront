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
      <div v-lazy-container="{ selector: 'img' }" class="rounded w-full">
        <img :data-src="props.cover" data-loading="/loading-book.jpg" class="rounded w-full">
      </div>
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
