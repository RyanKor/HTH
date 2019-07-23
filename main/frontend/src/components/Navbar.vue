<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info">
      <b-navbar-brand>
        <router-link :to="{ name: 'home' }">Here To Hear</router-link>
        <router-link :to="{ name: 'ex' }">연습페이지</router-link>
      </b-navbar-brand>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-breadcrumb :items="items"></b-breadcrumb>
        </b-navbar-nav>
      </b-collapse>
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
          href: "http://127.0.0.1:8080"
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