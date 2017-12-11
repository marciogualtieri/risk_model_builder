<template>
    <div class="risk-detail">
        <router-link to="/risks">Back to all risks</router-link>
        <field-form :fields="risk.fields" :title="risk.name" :key="risk.id"></field-form>
    </div>
</template>

<script>
    import FieldForm from './FieldForm.vue';
    import {API_BASE_URL} from './config.js';

    export default {
        name: 'risk-detail',
        data() {
            return {
                risk: {}
            }
        },
        components: {
            'field-form': FieldForm
        },
        created() {
            let id = this.$route.params.id;
            $.getJSON(API_BASE_URL + `/risks/${id}/`)
                .done(data => {this.risk = data;})
        }
    };
</script>

<style scoped>
.risk-detail {
    margin: 25px;
}
</style>