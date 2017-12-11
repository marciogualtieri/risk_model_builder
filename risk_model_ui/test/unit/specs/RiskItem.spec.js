import Vue from 'vue';
import RiskItem from '../../../src/RiskItem';

describe('RiskItem.vue', () => {
  it(`should render a risk item`, () => {

    const Constructor = Vue.extend(RiskItem);

    const component = new Constructor({
      propsData: {
        risk:  { id: 1,
                 name: 'Test Risk Name',
                 description: 'Test Risk Description',
                 fields: [{ id: 2,
                            name: 'Test Field Name',
                            description: 'Test Field Description',
                            type: 'text'
                          }
                         ]
               }
      }
    }).$mount();

    var expectedHtml = minify('<div>\
                                 <h2>\
                                   <strong>\
                                     <router-link to="/risks/1">Test Risk Name</router-link>\
                                   </strong>\
                                 </h2>\
                                 <p>Test Risk Description</p>\
                               </div>');

    var riskItem = removeClass(removeAllData(component.$el));

    expect(minify(riskItem.html())).to.equal(expectedHtml);
  });
});