define(function(require, exports, module) {
  "use strict";

  var app = require("app");

  var Layout = Backbone.Layout.extend({
    template: require("ldsh!./template"),

    tagName: 'div class="col-xs-3 bike-item"',

    serialize: function() {
      return { bike: this.bikeModel };
    },

    events: {

    },

    initialize: function() {
      console.log('Item: this.bikeModel');
      console.log(this.bikeModel);
      this.render();
      // this.listenTo(this.model, "change", this.render);
    }
  });

  module.exports = Layout;
});
