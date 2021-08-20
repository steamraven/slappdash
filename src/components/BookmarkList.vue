<template>
  <draggable
    :modelValue="modelValue"
    @update:model-value="$emit('update:modelValue',$event)"
    group="bookmarked"
    item-key="name"
    class="list"
    animation=200
    :removeOnSpill="true"
    >
    <template #item="{element}">
      <div class="element">{{element.name}}</div>
    </template>
  </draggable>
</template>

<script lang="py">
  draggable = require("vuedraggable")
  exports['default'] = {
    "name": "BookmarkList",
    "components": {
      "draggable": draggable
    },
    "props": {
      "modelValue": Array

    },
    "emits": [
      "update:modelValue"
    ]
  }
</script>