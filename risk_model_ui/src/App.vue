<template>
  <router-view :risks="risks" title="Choose a Risk Type!"></router-view>
</template>

<script>
  import {API_BASE_URL} from './config.js';

  export default {
    name: 'app',
    data() {
      return {
        risks: []
      };
    },
    created: function() {
        $.getJSON(API_BASE_URL + '/risks/')
            .done(data => {this.risks = data;});
    }
  }
</script>
