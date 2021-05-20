<template>
    <v-app>
        <v-content>
            <v-container class="pa-0 pt-5">
                <v-overlay :value="loading.config" absolute>
                    <v-progress-circular indeterminate v-show="loading.config" size="100"></v-progress-circular>
                </v-overlay>
                <v-row align="center" justify="space-between">
                    <v-card width="420" height="700" class="pa-5">
                        <v-form class="px-5">
                            <br>
                            <h5>Pusher Config</h5>
                            <hr>
                            <br>

                            <v-text-field v-model="config.pusher.app_id" label="App ID"></v-text-field>
                            <v-text-field v-model="config.pusher.key" label="Public key"></v-text-field>
                            <v-text-field v-model="config.pusher.secret" label="Secret"></v-text-field>
                            <v-text-field v-model="config.pusher.cluster" label="Cluster"></v-text-field>
                            <v-text-field v-model="config.pusher.retry_time" label="Retry time"></v-text-field>
                            <v-switch v-model="config.pusher.retry" label="Retry"></v-switch>
                            <v-row align="end" justify="end">
                                <v-btn v-on:click="clearPusherConfig" class="mr-2">Clear</v-btn>
                                <v-btn v-on:click="saveConfigData">Save</v-btn>
                            </v-row>
                        </v-form>
                    </v-card>

                    <v-card width="420" height="700" class="pa-5">
                        <v-form class="px-5" height="100%">
                            <br>
                            <h5>Parameters</h5>
                            <hr>
                            <br>
                            <v-text-field v-model="config.params.recognition_threshold"
                                          label="Recognition threshold"></v-text-field>
                            <v-text-field v-model="config.params.detection_threshold"
                                          label="Detection threshold"></v-text-field>
                            <v-text-field v-model="config.params.tasks_per_worker"
                                          label="Tasks per worker"></v-text-field>
                            <v-text-field v-model="config.params.max_workers"
                                          label="Max number of workers"></v-text-field>
                            <v-row align="end" justify="end">
                                <v-btn v-on:click="clearParametersConfig" class="mr-2">Clear</v-btn>
                                <v-btn v-on:click="saveConfigData">Save</v-btn>
                            </v-row>
                        </v-form>
                    </v-card>

                    <v-card width="420" height="700" class="pa-5">
                        <v-form class="px-5">
                            <br>
                            <h5>Weights</h5>
                            <hr>
                            <br>
                            <v-text-field v-model="config.weights.facenet" label="Facenet weights"></v-text-field>
                            <v-text-field v-model="config.weights.detector" label="Detector weights"></v-text-field>
                            <v-text-field v-model="config.weights.detector_config"
                                          label="Detector config file"></v-text-field>
                            <v-text-field v-model="config.weights.generator" label="Generator weights"></v-text-field>
                            <v-text-field v-model="config.weights.gendernet" label="Gendernet weights"></v-text-field>
                            <v-row align="end" justify="end" height="200">
                                <v-btn v-on:click="clearWeightsConfig" class="mr-2">Clear</v-btn>
                                <v-btn v-on:click="saveConfigData">Save</v-btn>
                            </v-row>
                        </v-form>
                    </v-card>
                </v-row>

            </v-container>
        </v-content>
    </v-app>
</template>

<script>
    import {mapActions, mapGetters} from 'vuex'

    export default {
        name: "Settings",
        components: {},
        data() {
            return {}
        },
        mounted() {
            this.getConfig({buffer: true});
        },
        methods: {
            ...mapActions({
                "getConfig": "getConfig",
                "saveConfig": "saveConfig"
            }),

            saveConfigData() {
                this.saveConfig(this.conf)
            },

            clearPusherConfig() {
                Object.keys(this.hostConfig).forEach((key) => {
                    this.hostConfig[key] = null
                })
            },

            clearParametersConfig() {
                Object.keys(this.paramsConfig).forEach((key) => {
                    this.paramsConfig[key] = null
                })
            },

            clearWeightsConfig() {
                Object.keys(this.weightsConfig).forEach((key) => {
                    this.weightsConfig[key] = null
                })
            },
        },
        computed: {
            ...mapGetters({'conf': "config", "loading": "loading"}),
            config: {
                get() {
                    return this.conf
                },

                set(value) {
                    this.$store.commit('setConfig', value)
                }
            }
        }
    }
</script>

<style scoped>

</style>