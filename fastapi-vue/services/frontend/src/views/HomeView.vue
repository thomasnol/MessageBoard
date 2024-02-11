<template>
  <section>
    <p>
      <span><a href="https://www.nolasque.com/">Personal Website</a></span>
      <br/>
      <span><a href="https://github.com/thomasnol/MessageBoard">Github Repository</a></span>
      <br/>
      <span><a href="https://linkedin.com/in/thomas-nolasque/">LinkedIn</a></span>
    </p>
    <p v-if="!isLoggedIn">
      <span><a href="/register">Register</a></span>
      <span> or </span>
      <span><a href="/login">Log In</a></span>
    </p>
  </section>
</template>
<script>

import { defineComponent } from 'vue';

export default defineComponent({
  name: 'HomeView',
  computed : {
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    }
  },
});
</script>