define(function(require, exports, module) {
  "use strict";

  var app = require("app");

  var bikeModel = require("./model");

  var Collection = Backbone.Collection.extend({

    // model: bikeModel,

    url: function() {
      return app.api + "bikes";
    },
    parse: function(data) {
      return data.results;
    }
  });

  module.exports = Collection;
});
