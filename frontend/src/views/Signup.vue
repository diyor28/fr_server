<template>
    <signup permanent show redirect-url="/login"></signup>
</template>

<script>
    import SignupForm from '../components/Signup.vue'

    export default {
        name: "Signup",
        components: {signup: SignupForm}
    }
</script>

<style scoped>

</style>