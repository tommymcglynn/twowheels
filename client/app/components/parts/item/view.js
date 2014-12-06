define(function(require, exports, module) {
  "use strict";

  var app = require("app");

  var Layout = Backbone.Layout.extend({
    template: require("ldsh!./template"),

    tagName: 'div class="col-xs-3 bike-item"',

    serialize: function() {
      return { part: this.part };
    },

    events: {

    },

    initialize: function() {
      // this.listenTo(this.model, "change", this.render);
    }
  });

  module.exports = Layout;
});
