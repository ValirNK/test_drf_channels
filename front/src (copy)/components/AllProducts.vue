<template>
 <listOfProducts :products="getProducts"/>
</template>

<script>
/* eslint-disable */ 
import { mapGetters } from 'vuex';
import listOfProducts from './ListOfProducts';
import {SOCKET_URL} from './../store.js'

export default {
  components: {
    listOfProducts,
  },
  data() {
    return {
        chatSocket: '',
        dialogs: []
    }
  },
  computed: {
    ...mapGetters([
      'getProducts'
    ]),
  },
  created(){
    if(Object.keys(this.$route.params).length != 0){
      if("type_name" in this.$route.params){
        this.$store.dispatch('getProducts', this.$route.params);
      }
    }else{
      this.$store.dispatch('getProducts');
    }
    
    this.connect()
    this.$watch(
      () => this.$route.params,
      (toParams, previousParams) => {
        this.$store.dispatch('getProducts', toParams);
      }
    )
  },
  methods: {
    connect(){
      this.chatSocket = new WebSocket(
      SOCKET_URL);
      this.chatSocket.onopen = () => {
          this.dialogs.push({event: "connected_products"})
          this.chatSocket.onmessage = ({data}) => {
              if(parseInt(data)){
                this.$store.dispatch('deleteProductState', parseInt(data));
              }else{
                this.$store.dispatch('addUpdateProductState', JSON.parse(data));
              }
              
          };
      };
    }
  }
};
</script>

<style scoped>
  .listOfProducts {
    width: 100%;
    max-width: 1000px;
    margin: 0 auto;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    padding: 0;
  }

  .product {
    width: 300px;
    background-color: #fff;
    list-style: none;
    box-sizing: border-box;
    padding: 1em;
    margin: 1em 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    border-radius: 7px;
  }

  .product-name {
    font-size: 1.2em;
    font-weight: normal;
  }

  .product-price {
    width: 100%;
    align-self: flex-start;
    display: flex;
    justify-content: space-between;
    margin-bottom: .5em;
  }

</style>

