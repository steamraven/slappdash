<template>
    <Button 
        :label="apps[appKey]['title']"
        class="button "
    ></Button>
</template>

<script lang="py">
    exports['default'] = {
        "props": {
            "appKey": String,
            "apps": Object,
        },
        "setup": lambda props: {

        }
    }
</script>

<style scoped lang="scss">
    @import 'node_modules/primeflex/primeflex.scss';
    .button {
        
        @extend .m-2;
        @extend .p-2;
        /*@extend .opacity-20;*/
        background-color: #FFFFFF30 !important;
    }
</style>
