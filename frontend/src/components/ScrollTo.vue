<template>
    <span ref="component">
        <slot/>
    </span>
</template>

<script>
export default {
    name: 'scroll-to',
    props: {
        alignToTop: {
            required: false,
            default: null,
            type: Boolean,
        },
        options: {
            required: false,
            default: null,
            type: Object,
        },
    },
    methods: {
        scrollTo () {
            this.$refs.component.scrollIntoView(this.options !== null ? this.options : this.alignToTop);
        },
    },
};
</script>

<style scoped>

</style>