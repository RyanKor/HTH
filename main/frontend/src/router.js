import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";

Vue.use(Router);

export default new Router({
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
      component: () => import("./views/Survey.vue")
    },
    {
      path: "/result",
      name: "result",
      component: () => import("./views/Result.vue")
    },
    {
      path: "/checkup",
      name: "checkup",
      component: () => import("./comfort/Checkup.vue")
    },
    {
      path: "/cs",
      name: "cs",
      component: () => import("./comfort/Cs.vue")
    },
    {
      path: "/doctor",
      name: "doctor",
      component: () => import("./comfort/Doctor.vue")
    },
    {
      path: "/prescription",
      name: "prescription",
      component: () => import("./comfort/Prescription.vue")
    },
    {
      path: "/sick",
      name: "sick",
      component: () => import("./comfort/Sick.vue")
    },
    {
      path: "/stomach",
      name: "stomach",
      component: () => import("./comfort/Stomach.vue")
    }
  ]
});
