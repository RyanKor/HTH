<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <div class="container">
        <b-navbar-brand>
          <router-link :to="{ name: 'home' }">60 dB</router-link>
          <router-link :to="{ name: 'ex' }">연습페이지</router-link>
        </b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-breadcrumb :items="items"></b-breadcrumb>
          </b-navbar-nav>
        </b-collapse>
      </div>
    </b-navbar>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [
        {
          text: "Login",
          router: "http://127.0.0.1:8080/login"
        },
        {
          text: "Signup",
          href: "http://127.0.0.1:8080"
        },
        {
          text: "About Us",
          href: "http://127.0.0.1:8080/about"
        }
      ]
    };
  }
};
</script>


<style>
.bg-info {
  background-color: cadetblue;
}
</style>