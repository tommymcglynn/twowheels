define(function(require, exports, module) {
  "use strict";

  var app = require("app");

  var Layout = Backbone.Layout.extend({
    template: require("ldsh!./template"),

    serialize: function() {
      return { bike: this.bike };
    },

    beforeRender: function() {
      var self = this;

    },

    afterRender: function() {

    },

    initialize: function(options) {
      var self = this;
      this.collection.fetch({
        success: function(e, data){
          console.log('e');
          console.log(e);
          console.log('data');
          console.log(data);
          self.bike = e.find(function(model) { return model.get('id') == options.bike_id; });
          console.log(self.bike);
          self.render();
        }
      });

    },

    events: {

    },
  });

  module.exports = Layout;
});
