define(function(require, exports, module) {
  "use strict";

  var app = require("app");

  var Bikes = require("components/bikes/index");
  var Parts = require("components/parts/index");

  // require("collectionCache");
  require("bootstrap");

  // Defining the application router, you can attach sub routers here.
  var Router = Backbone.Router.extend({
    appLayout: null,
    initialize: function() {

      this.bikes = new Bikes.Collection();
      // Use main layout and set Views.
      var Layout = Backbone.Layout.extend({
        el: "main",

        template: require("ldsh!./templates/main"),

        views: {
          // ".filters": new User.Views.List({ collection: this.users }),
          // ".main-content": new Bikes.Views.List({ collection: this.bikes }),
        }
      });

      // Render to the page.
      this.appLayout = new Layout().render();
    },

    routes: {
      "": "index",
      "bikes/:id" : "getBikeById",
      "parts/:id" : "getPartsById",
      "models/:id": "getModelsById",
      "styles/:id": "getStylesById",
    },

    index: function() {
      // Reset the state and render.
      this.reset();
      this.appLayout.setView(".main-content", new Bikes.Views.List({ collection: this.bikes }));
      this.bikes.fetch();
    },

    getBikeById: function(id) {
      this.appLayout.setView(".main-content", new Bikes.Views.Single({ collection: this.bikes, bike_id: id }));
    },

    //Get Part by id - Show list of all Parts with same id
    getPartsById: function (id) {
      console.log(id);
      this.appLayout.setView(".main-content", new Bikes.Views.Single({ collection: this.bikes, bike_id: id }));
    },

    getModelsById: function (id) {
      console.log(id);
    },

    getStylesById: function (id) {
      console.log(id);
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
