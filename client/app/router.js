define(function(require, exports, module) {
  "use strict";

  var app = require("app");

  var Bikes = require("components/bikes/index");
  // var Filters = require("components/bikes/index");

  // require("collectionCache");
  require("bootstrap");

  // Defining the application router, you can attach sub routers here.
  var Router = Backbone.Router.extend({
    initialize: function() {

      this.bikes = new Bikes.Collection();

      // Use main layout and set Views.
      var Layout = Backbone.Layout.extend({
        el: "main",

        template: require("ldsh!./templates/main"),

        views: {
          // ".filters": new User.Views.List({ collection: this.users }),
          ".main-content": new Bikes.Views.List({ collection: this.bikes }),
        }
      });

      // Render to the page.
      new Layout().render();
    },

    routes: {
      "": "index",
      "bikes/:id": "getBikeById",
    },

    index: function() {
      // Reset the state and render.
      this.reset();
      this.bikes.fetch();

    },

    getBikeById: function(id) {
      console.log('get bike by id: ' + id);
    },

    // Shortcut for building a url.
    go: function() {
      return this.navigate(_.toArray(arguments).join("/"), true);
    },

    reset: function() {
      // Reset collections to initial state.
      if (this.bikes.length) {
        this.bikes.reset();
      }

      // Reset active model.
      app.active = false;
    }
  });

  module.exports = Router;
});
