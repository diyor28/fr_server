// define a mixin object
export default {
    data() {
        return {}
    },
    methods: {
        openDialog({ id, data }) {
            this.$root.$emit('show-dialog', id, (data || {}))
        },

        hide(id) {
            this.$root.$emit('close-dialog', id)
        }
    }
}
