<template>
  <router-view :risks="risks" title="Choose a Risk Type!"></router-view>
</template>

<script>

export default {
  name: 'app',
  data() {
    return {
      risks: []
    };
  },
  created: function() {
      $.getJSON('http://127.0.0.1:8000/risks/')
          .done(data => {this.risks = data;});
  }
}
</script>
