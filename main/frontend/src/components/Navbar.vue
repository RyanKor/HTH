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

        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
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
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
</template>

<script>
</script>

<style>
.b-navbar{
  background-color: #88f;
}
</style>