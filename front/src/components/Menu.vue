<template>
  <header class="header">
    <nav class="nav">
      <ul class="nav-links">
        <li class="link" v-for="(product_type, index) in product_types" :key="index">
          <router-link :to="'/types/'+product_type.name">{{ product_type.name }}</router-link>
        </li>
      </ul>
    </nav>
    <slot></slot>
  </header>
</template>

<script>
/* eslint-disable */
import { mapActions, mapGetters } from 'vuex';

export default {
  data() {
    return {
      product_types: []
    }
  },
  computed: {
    ...mapActions([
      'getTypes'
    ]),
    ...mapGetters([
      'getProductTypes'
    ]),
  },
  mounted(){
    this.getTypes
    setTimeout(() => {
      this.product_types = this.$store.getters['getProductTypes']
    }, 1000)
  },
  methods: {

  }
};
</script>

<style scoped>
  .header {
    width: 100%;
    height: 70px;
    background-color: #333333;
    box-sizing: border-box;
    padding: .5em;
    display: flex;
    align-items: center;
  }

  .nav-links {
    width: 100%;
    display: flex;
    justify-content: flex-start;
  }

  .link {
    list-style: none;
    padding: 0 2em;
  }

  .link a {
    color: #fff;
    text-decoration: none;
  }
</style>
