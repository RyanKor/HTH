import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";

Vue.use(Router);

export default new Router({
  hashbang: false,
  mode : "history",
  routes: [{

      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import( /* webpackChunkName: "about" */ "./views/About.vue")
    },
    {
      path: "/ex",
      name: "ex",
      component: () => import("./views/ex.vue")
    },
    {
      path: "/survey",
      name: "survey",
      component: () => import("./views/Survey.vue")
    },
    {
      path: "/result",
      name: "result",
      component: () => import("./views/Result.vue")
    },
    {
      path: "/login",
      name: "login",
      component: () => import("./views/Login.vue")
    }
  ]
});