define(function(require, exports, module) {
  "use strict";

  var app = require("app");

  var Model = Backbone.Model.extend({

    defaults: {
      id: '',
      name: '',
      image_url: '',
      models: [],
      styles: [],
      parts: []
    }

  });

  module.exports = Model;
});
