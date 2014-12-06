define(function(require, exports, module) {
  "use strict";

  var app = require("app");
  var lightbox = require("lightbox");
  var Item = require("../item/view");

  var Layout = Backbone.Layout.extend({
    template: require("ldsh!./template"),

    serialize: function() {
      return { parts: this.collection };
    },

    beforeRender: function() {
      var self = this;
      this.collection.models.forEach(function(obj){
        self.insertView(".bikes-list", new Item({
            part: obj
          }));
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
