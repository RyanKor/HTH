<template>
<div>
  <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand>
      <router-link 
        :to="{ name: 'home' }">
        Here To Hear
      </router-link>
    </b-navbar-brand>

  <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>


      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <!-- Using 'button-content' slot -->
        <!-- <b-nav-item-dropdown right>
          <template slot="button-content"><em>Menu</em></template>
          <b-dropdown-item >
            <router-link 
              :to="{ name: 'home' }">
              Login
            </router-link>
            </b-dropdown-item>
          <b-dropdown-item >
            <router-link 
              :to="{ name: 'home' }">
              Signup
            </router-link>
          </b-dropdown-item>
          <b-dropdown-item>
            <router-link 
              :to="{ name: 'about' }">
              About Us
            </router-link>
          </b-dropdown-item>
        </b-nav-item-dropdown> -->
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
            text: 'Login',
            href: 'http://127.0.0.1:8080'
          },
          {
            text: 'Signup',
            href: 'http://127.0.0.1:8080'
          },
          {
            text: 'About Us',
            href : 'http://127.0.0.1:8080/about'
          }
        ]
      }
    }
}
</script>


<style>
.b-navbar{
  background-color: #88f;
}
</style>