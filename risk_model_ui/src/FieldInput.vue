<template>
    <div class="row">
        <div class="form-group">
            <label class="control-label requiredField">{{field.name}}</label>
            <select class="form-control" v-if="field.type == 'enum'">
                <option v-for="choice in field.choices">{{ choice }}</option>
            </select>
            <textarea v-else-if="field.type =='text'" :name="field.name" :placeholder="field.description" rows="3"></textarea>
            <input class="form-control" v-else :type="field.type" :name="field.name">
        </div>
    </div>
</template>

<script>
    export default {
        name: 'field-input',
        props: ['field'],
    };
</script>

<style scoped>
.form-group{
  margin-left: 50px;
}

input, label, select {
  display:block;
  max-width: 95%;
}

textarea {
  width: 95%;
}
</style>