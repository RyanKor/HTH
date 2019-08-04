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
            <b-breadcrumb v-if="isLogin">{{email}}</b-breadcrumb>
            <b-breadcrumb @click="logout">logout</b-breadcrumb>
          </b-navbar-nav>
        </b-collapse>
      </div>
    </b-navbar>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  data() {
    return {
      email: null
    };
  },
  computed: {
    ...mapState(["isLogin", "isLoginError"])
  },
  created() {
    axios
      .get("http://127.0.0.1:8000/api/user/")
      .then(({ data }) => (this.user = data.user));
  }
};
</script>


<style>
.bg-info {
  background-color: cadetblue;
}
</style>