define(function(require, exports, module) {
  "use strict";

  var app = require("app");
  var Item = require("../item/view");

  var Layout = Backbone.Layout.extend({
    template: require("ldsh!./template"),

    serialize: function() {
      return { bikes: this.collection };
    },

    beforeRender: function() {
      this.collection.each(function(bike) {
        this.insertView(".bikes-list", new Item({
          model: bike
        }));
      }, this);
    },

    afterRender: function() {

    },

    initialize: function() {
      // Whenever the collection resets, re-render.
      this.listenTo(this.collection, "reset sync request", this.render);
    },

    events: {

    },
  });

  module.exports = Layout;
});
