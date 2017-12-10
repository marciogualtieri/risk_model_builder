<template>
    <div class="field-form">
        <form>
          <fieldset>
            <h2><strong>{{title}} Application Form</strong></h2>
            <field-input v-for="field in fields" :field="field" :key="field.id"></field-input>
          </fieldset>
          <input type="submit" value="Submit">
        </form>
    </div>
</template>

<script>
    import FieldInput from './FieldInput.vue';

    export default {
        name: 'field-form',
        props: ['fields', 'title'],
        components: {
            'field-input': FieldInput
        },
    };
</script>

<style scoped>
fieldset {
  border: 1px solid #781351;
  width: 500px;
  background-color: #229922;
}

h2 {
  text-align: center;
  border: 1px solid black;
  margin: 0px;
  background-color: #FEEBB2;
  padding: 10px;
  color: #D85146 !important;
  text-shadow: -1px -1px 0 #000,
                1px -1px 0 #000,
               -1px 1px 0 #000,
                1px 1px 0 #000;
}

input[type="submit"] {
    background-color: #FC634D;
    border: 1px solid black;
    font-weight: bold;
    padding: 10px;
    margin-top: 10px;
}
</style>