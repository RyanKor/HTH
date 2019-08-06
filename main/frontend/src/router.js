import Vue from "vue";
import Router from "vue-router";
// import Home from "./views/Home.vue";
import Home from "./views/Home.vue";

Vue.use(Router);

// const requireAuth = () => (from, to, next) => {
//   const isAuthenticated = false;
//   if (isAuthenticated) return next();
//   next("/login?returnPath=home");
// };

export default new Router({
  hashbang: false,
  mode: "history",
  routes: [
    {
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
      component: () =>
        import(/* webpackChunkName: "about" */ "./views/About.vue")
    },
    {
      path: "/survey",
      name: "survey",
      // beforeEnter: requireAuth(),
      component: () => import("./views/Survey.vue")
    },
    {
      path: "/result",
      name: "result",
      // beforeEnter: requireAuth(),
      component: () => import("./views/Result.vue")
    },
    {
      path: "/login",
      name: "login",
      component: () => import("./views/Login.vue")
    },
    {
      path: "/signup",
      name: "signup",
      component: () => import("./views/Signup.vue")
    },
    {
      path: "/profileupdate",
      name: "profileupdate",
      // beforeEnter: requireAuth,
      component: () => import("./views/ProfileUpdate.vue")
    },
    {
      path: "/profiles",
      name: "profiles",
      // beforeEnter: requireAuth,
      component: () => import("./views/Profiles.vue")
    }
  ]
});
