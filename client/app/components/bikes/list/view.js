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
      var self = this;
      console.log('beforeRender');
      console.log('this.collection');
      console.log(this.collection);
      this.collection.each(function(bike) {
        bike.get("bikes").forEach(function(b){
          self.insertView(".bikes-list", new Item({
            bike: b
          }));
        });
      });
    },

    afterRender: function() {

    },

    initialize: function() {
      console.log('init...');
      console.log(this.collection);
      // Whenever the collection resets, re-render.
      this.listenTo(this.collection, "reset sync request", this.render);
    },

    events: {

    },
  });

  module.exports = Layout;
});