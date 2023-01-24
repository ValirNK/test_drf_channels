<template>
<div>
  <div class="checkout-box" v-if="!created">
    <ul class="checkout-list">
      <transition-group name="fade">
      <li v-for="(product, index) in getProductsInCart" :key="index" class="checkout-product">
        <img :src="product.image" alt="" class="product-image">
        <h3 class="product-name">{{ product.name }}</h3>
        <span class="product-price">{{ product.price }}</span>
        <button class="product-remove" @click="remove(index)">X</button>
      </li>
      </transition-group>
    </ul>
    <div v-if="!hasProduct()" class="checkout-message">
      <h3>Нет товаров</h3>
      <router-link to="./">К списку товаров</router-link>
    </div>
    <div v-else>
      <div class="contact-info">
        <label for="client_name">Имя клиента</label>
        <input type="text" name="client_name" v-model="client_name">
        <label for="client_adress">Адрес доставки</label>
        <input type="text" name="client_adress" v-model="client_adress">
        <button id="pushOrder" @click="addClient">Заказать</button>
      </div>
    </div>
    <h3 class="total" v-if="hasProduct()">
      Итого: {{ totalPrice() }}
    </h3>
  </div>
</div>
</template>

<script>
/* eslint-disable */
import { mapGetters, mapActions } from 'vuex';

export default {
  data() {
    return {
      client_name: '',
      client_adress: '',
      created: false
    }
  },
  computed: {
    ...mapGetters([
      'getProductsInCart'
    ]),
  },
  methods: {
    ...mapActions([
      'removeProduct',
    ]),
    hasProduct() {
      return this.getProductsInCart.length > 0;
    },
    totalPrice() {
      return this.getProductsInCart.reduce((current, next) =>
        current + next.price, 0);
    },
    remove(index) {
      this.removeProduct(index);
    },
    addClient(){
      if(this.client_name != '' && this.client_adress != ''){
        let client = {
          name: this.client_name,
          adress: this.client_adress,
          cart:  this.getProductsInCart
        }
        this.$store.dispatch('addClient', client)
      }
    }
  },
};
</script>

<style scoped>
  .contact-info{
    text-align: center;
  }
  #pushOrder{
    padding: 4px 10px;
    color: #fff;
    background-color: green;
    border-radius: 5px;
    font-size: 16px;
    border: 0;
    cursor: pointer;
  }
  .contact-info input[type="text"]{
    border-radius: 4px;
    padding: 3px 8px;
    border: 1px solid #ccc;
  }
  .checkout-box {
    width: 100%;
    max-width: 900px;
    display: flex;
    flex-direction: column;
    margin: 50px auto;
    box-sizing: border-box;
    padding: 1em;
  }

  .checkout-list {
    padding: 0;
  }

  .checkout-product {
    display: grid;
    grid-template-columns: 1fr 3fr 2fr .5fr;
    background-color: #fff;
    box-shadow: 0px 0px 10px rgba(73, 74, 78, 0.1);
    border-radius: 5px;
    list-style: none;
    box-sizing: border-box;
    padding: .8em;
    margin: 1em 0;
  }

  .checkout-product * {
    place-self: center;
  }
  .product-image {
    grid-column: 1/2;
    width: 50%;
  }

  .product-name {
    box-sizing: border-box;
  }

  .product-price {
    font-size: 1.2em;
    font-weight: bold;
  }

  .product-remove {
    width: 25px;
    height: 25px;
    border-radius: 50%;
    border: 0;
    background-color: #E0E0E0;
    color: #fff;
    cursor: pointer;
  }

  .total {
    font-size: 2em;
    font-weight: bold;
    align-self: flex-end;
  }

  .checkout-message {
    font-size: 1.5em;
  }

  .fade-enter-active, .fade-leave-active {
    transition: all .5s;
  }

  .fade-enter, .fade-leave-to {
    transform: translateX(-40px);
    opacity: 0;
  }
</style>
