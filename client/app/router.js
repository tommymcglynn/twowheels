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
      "org/:name": "org",
      "org/:org/user/:name": "user",
      "org/:org/user/:user/repo/:name": "repo"
    },

    index: function() {
      // Reset the state and render.
      this.reset();
      this.bikes.fetch();

    },

    org: function(name) {
      // Reset the state and render.
      this.reset();

      // Set the organization.
      this.users.org = name;

      // Fetch the data.
      this.users.fetch();
    },

    user: function(org, name) {
      // Reset the state and render.
      this.reset();

      // Set the organization.
      this.users.org = org;
      // Set the user name.
      this.repos.user = name;

      // Fetch the data.
      this.users.fetch();
      this.repos.fetch();
    },

    repo: function(org, user, name) {
      // Reset the state and render.
      this.reset();

      // Set the organization.
      this.users.org = org;
      // Set the user name.
      this.repos.user = user;
      // Set the repo name.
      this.commits.user = user;
      this.commits.repo = name;

      // Fetch the data.
      this.users.fetch();
      this.repos.fetch();
      this.commits.fetch();
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
