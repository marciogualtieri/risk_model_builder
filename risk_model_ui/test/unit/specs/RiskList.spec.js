import Vue from 'vue';
import RiskList from '../../../src/RiskList';

describe('RiskList.vue', () => {
  it(`should render a risk list`, () => {
    const Constructor = Vue.extend(RiskList);

    const component = new Constructor({
      propsData: {
        risks:  [{ id: 1,
                   name: 'Test Risk Name 1',
                   description: 'Test Risk Description 1',
                   fields: [{ id: 2,
                              name: 'Test Field Name 1',
                              description: 'Test Field Description 1',
                              type: 'text'
                            }
                           ]
                 },
                 { id: 3,
                   name: 'Test Risk Name 2',
                   description: 'Test Risk Description 2',
                   fields: [{ id: 4,
                              name: 'Test Field Name 2',
                              description: 'Test Field Description 2',
                              type: 'text'
                            }
                           ]
                 }
                ],
        title: 'Test Title'
      }
    }).$mount();

    var expectedHtml = minify('<h2>Test Title</h2>\
                               <div>\
                                 <div>\
                                   <div>\
                                     <div>\
                                       <h2>\
                                         <strong>\
                                           <router-link to="/risks/1">Test Risk Name 1</router-link>\
                                         </strong>\
                                       </h2>\
                                       <p>Test Risk Description 1</p>\
                                     </div>\
                                   </div>\
                                   <div>\
                                     <div>\
                                       <h2>\
                                         <strong>\
                                           <router-link to="/risks/3">Test Risk Name 2</router-link>\
                                         </strong>\
                                       </h2>\
                                       <p>Test Risk Description 2</p>\
                                     </div>\
                                   </div>\
                                 </div>\
                               </div>');

    var riskList = removeClass(removeAllData(component.$el));

    expect(minify(riskList.html())).to.equal(expectedHtml);
  });
});