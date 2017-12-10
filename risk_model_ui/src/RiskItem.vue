<template>
    <div class="col-lg-4 col-md-6 col-xs-12">
        <div class="item">
            <h2><strong><router-link :to="`/risks/${risk.id}`">{{risk.name}}</router-link></strong></h2>
            <p>{{risk.description}}</p>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'risk-item',
        props: ['risk'],
    };
</script>

<style scoped>
.item {
  background-color: #229922;
  border: 1px solid black;
  margin: 10px;
}

p {
  padding: 10px 10px 10px 10px;
  margin: 0px;
  clear: left;
}

h2 {
  float: left;
  text-align: center;
  border: 1px solid black;
  margin: 0px;
  background-color: #FEEBB2;
  padding: 10px;
}

a {
  color: #D85146 !important;
}

a:hover, a:visited, a:link, a:active {
  color: #D85146 !important;
  text-decoration: none;
  text-shadow: -1px -1px 0 #000,
                1px -1px 0 #000,
               -1px 1px 0 #000,
                1px 1px 0 #000;
}

</style> 
