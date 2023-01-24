<template>
  <div class="product-box">
    <div class="product-image">
      <img :src="currentProduct.image" :alt="currentProduct.name" width="250">
    </div>
    <div class="product-info">
      <h2 class="product-title">{{ currentProduct.name }}</h2>
      <span class="product-price">{{ currentProduct.price }} {{ currentProduct.currency }}</span>
      <p><strong>Type:</strong> {{ currentProduct.type_product.name }}</p>
      <p><strong>Code:</strong> {{ currentProduct.code }}</p>
      <p><strong>Manufacturer:</strong> {{ currentProduct.manufacturer }}</p>
      <p><strong>Updated:</strong> {{ currentProduct.date_update }}</p>
      <div v-if="currentProduct.in_stock > 0">
        <p><strong>In stock:</strong> {{ currentProduct.in_stock }}</p>
        <btn btnColor="btn btn-large btn-sucess" :cartIcon="true"
      @click.native="addProductToCart(currentProduct)">
        Buy Now
      </btn>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import { mapGetters, mapActions } from 'vuex';
import btn from './Btn';

export default {
  components: {
    btn
  },

  computed: {
    ...mapGetters({
      currentProduct: 'getCurrentProduct',
    }),
  },

  methods: {
    ...mapActions([
      'addProduct',
    ]),
    addProductToCart(product) {
      this.addProduct(product);
    },
    rated(rate) {
      return `${rate * 20}%`;
    }
  },

};
</script>

<style scoped>
  .product-box {
    width: 800px;
    height: 400px;
    margin: 50px auto;
    box-sizing: border-box;
    padding: 1.5em;
    background-color: #fff;
    border-radius: 7px;
    display: flex;
    justify-content: space-around;
    align-items: center;
  }

  .product-image {
    width: 300px;
  }

  .product-info {
    width: 400px;
    align-self: flex-start;
  }

  .product-title {
    font-weight: normal;
  }

  .product-price {
    font-size: 2em;
    font-weight: bolder;
  }

  .product-box button {
    width: 300px;
    margin: .3em 0;
  }
</style>
