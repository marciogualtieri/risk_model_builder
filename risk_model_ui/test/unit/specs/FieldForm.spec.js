import Vue from 'vue';
import FieldForm from '../../../src/FieldForm';

describe('FieldForm.vue', () => {
  it(`should render a field form`, () => {
    const Constructor = Vue.extend(FieldForm);

    const component = new Constructor({
      propsData: {
        fields: [{ id: 1,
                   name: 'Test Text Field',
                   description: 'Test Text Field Description',
                   type: 'text'
                 },
                 { id: 1,
                   name: 'Test Date Field',
                   description: 'Test Date Field Description',
                   type: 'date'
                 }],
        title: 'Test'
      }
    }).$mount();

    var expectedHtml = minify('<form>\
                                 <fieldset>\
                                   <h2>\
                                     <strong>Test Application Form</strong>\
                                   </h2>\
                                   <div>\
                                     <div>\
                                       <label>Test Text Field</label>\
                                       <textarea name="Test Text Field" placeholder="Test Text Field Description" rows="3">\
                                       </textarea>\
                                     </div>\
                                   </div>\
                                   <div>\
                                     <div>\
                                       <label>Test Date Field</label>\
                                       <input type="date" name="Test Date Field">\
                                     </div>\
                                   </div>\
                                 </fieldset>\
                                 <input type="submit" value="Submit">\
                               </form>');

    var fieldForm = removeClass(removeAllData(component.$el));

    expect(minify(fieldForm.html())).to.equal(expectedHtml);
  });
});