import Vue from 'vue';
import FieldInput from '../../../src/FieldInput';

describe('FieldInput.vue', () => {
  it(`should render a text field input`, () => {

    const Constructor = Vue.extend(FieldInput);

    const component = new Constructor({
      propsData: {
        field:  { id: 1,
                 name: 'Test Text Field',
                 description: 'Test Text Field Description',
                 type: 'text'
               }
      }
    }).$mount();

    var expectedHtml = minify('<div>\
                                 <label>Test Text Field</label>\
                                 <textarea name="Test Text Field" placeholder="Test Text Field Description" rows="3">\
                                 </textarea>\
                               </div>');

    var fieldInput = removeClass(removeAllData(component.$el));

    expect(minify(fieldInput.html())).to.equal(expectedHtml);
  });

  it(`should render a numeric field input`, () => {

    const Constructor = Vue.extend(FieldInput);

    const component = new Constructor({
      propsData: {
        field:  { id: 1,
                 name: 'Test Numeric Field',
                 description: 'Test Numeric Field Description',
                 type: 'number'
               }
      }
    }).$mount();

    var expectedHtml = minify('<div>\
                                 <label>Test Numeric Field</label>\
                                 <input type="number" name="Test Numeric Field">\
                               </div>');

    var fieldInput = removeClass(removeAllData(component.$el));

    expect(minify(fieldInput.html())).to.equal(expectedHtml);
  });

  it(`should render a date field input`, () => {

    const Constructor = Vue.extend(FieldInput);

    const component = new Constructor({
      propsData: {
        field:  { id: 1,
                 name: 'Test Date Field',
                 description: 'Test Date Field Description',
                 type: 'date'
               }
      }
    }).$mount();

    var expectedHtml = minify('<div>\
                                 <label>Test Date Field</label>\
                                 <input type="date" name="Test Date Field">\
                               </div>');

    var fieldInput = removeClass(removeAllData(component.$el));

    expect(minify(fieldInput.html())).to.equal(expectedHtml);
  });

  it(`should render a enum field input`, () => {

    const Constructor = Vue.extend(FieldInput);

    const component = new Constructor({
      propsData: {
        field:  { id: 1,
                 name: 'Test Enum Field',
                 description: 'Test Enum Field Description',
                 type: 'enum',
                 choices: ['Test Choice 1', 'Test Choice 2']
               }
      }
    }).$mount();

    var expectedHtml = minify('<div>\
                                 <label>Test Enum Field</label>\
                                 <select>\
                                   <option>Test Choice 1</option>\
                                   <option>Test Choice 2</option>\
                                 </select>\
                               </div>');

    var fieldInput = removeClass(removeAllData(component.$el));

    expect(minify(fieldInput.html())).to.equal(expectedHtml);
  });
});