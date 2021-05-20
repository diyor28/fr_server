<template>
    <v-app>
        <login permanent show redirect-url="/"></login>
    </v-app>
</template>

<script>
    import {mapActions} from 'vuex'
    import LoginForm from '../components/Login.vue'

    export default {
        name: 'Login',
        components: {login: LoginForm},
        data() {
            return {
            }
        },
        mounted() {
        },
        methods: {
            ...mapActions({"login": "login"}),
        },
        computed: {}
    };
</script>

<style>
</style>
