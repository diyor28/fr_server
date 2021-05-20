<template>
    <v-dialog v-model="showForm" width="440">
        <v-card class="text-center px-4 pb-4">
            <v-row justify="end">
                <v-btn v-show="!permanent" @click="hide" icon>
                    <v-icon>close</v-icon>
                </v-btn>
            </v-row>
            <v-card-text class="subtitle-1 font-weight-bold">
                Are you sure you want to log out?
            </v-card-text>
            <v-btn @click="logout" color="error">
                LogOut
            </v-btn>
        </v-card>
    </v-dialog>
</template>

<script>
    export default {
        name: "Logout",
        props: {
            show: Boolean,
            permanent: Boolean,
            redirectUrl: String
        },
        model: {
            prop: "show",
            event: "change"
        },
        data() {
            return {}
        },
        methods: {
            hide() {
                this.$emit('change', false);
            },

            logout() {
                this.hide();
                localStorage.removeItem('user');
                this.$router.push(this.redirectUrl);
            }
        },
        computed: {
            showForm: {
                get() {
                    return this.show
                },
                set(value) {
                    if (this.permanent) {
                        value = true
                    }
                    this.$emit('change', value);
                }
            }
        }
    }
</script>

<style scoped>

</style>