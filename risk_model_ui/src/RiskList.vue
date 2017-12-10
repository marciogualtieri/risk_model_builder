<template>
    <div class="risk-list">
        <h2>{{title}}</h2>
        <div class="container">
            <div class="row">
                <risk-item v-for="risk in risks" :risk="risk" :key="risk.id"></risk-item>
            </div>
        </div>
    </div>
</template>

<script>
    import RiskItem from './RiskItem.vue';

    export default {
        name: 'risk-list',
        props: ['risks', 'title'],
        components: {
            'risk-item': RiskItem
        },
    };
</script>

<style scoped>
h2 {
    text-align: center
}
</style>