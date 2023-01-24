/* eslint-disable */
import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'

Vue.use(Vuex);

export const API_URL = 'http://127.0.0.1:8000/api';
export const URL = 'http://127.0.0.1:8000';
export const SOCKET_URL = 'ws:127.0.0.1:8000/ws/products/';


export default new Vuex.Store({
  state: {
    all_products: [],
    product_types: [],
    cartProducts: [],
    currentProduct: {},
    showModal: false,
    showPopupCart: false
  },

  getters: {
    getProducts: state => state.all_products,
    getProductsInCart: state => state.cartProducts,
    getCurrentProduct: state => state.currentProduct,
    getShowModal: state => state.showModal,
    getPopupCart: state => state.showPopupCart,
    getProductTypes: state => state.product_types
  },

  mutations: {
    ADD_PRODUCT: (state, product) => {
      state.cartProducts.push(product);
    },
    ADD_UPDATE_PRODUCT_STATE: (state, product) => {
      product.image = URL + product.image
      console.log(product)
      if (state.all_products.filter((e) => e.id === product.id).length > 0) {
        state.all_products.filter((e, index) => { 
          if(e.id === product.id){
            state.all_products.splice(index, 1);
            state.all_products.splice(index, 0, product)
          }
        })
      }else{
        state.all_products.push(product);
      }
    },
    DELETE_PRODUCT_STATE: (state, id) => {
      state.all_products.filter((e, index) => {    
        if(e.id === id){
          state.all_products.splice(index, 1);
        }
      })
    },
    REMOVE_PRODUCT: (state, index) => {
      state.cartProducts.splice(index, 1);
    },
    CURRENT_PRODUCT: (state, product) => {
      state.currentProduct = product;
    },
    CLEAR_CART: (state) => {
      state.cartProducts = []
    },
    SHOW_MODAL: (state) => {
      state.showModal = !state.showModal;
    },
    SHOW_POPUP_CART: (state) => {
      state.showPopupCart = !state.showPopupCart;
    },
    GET_PRODUCTS: (state, payload) => {
      if("type_name" in payload){
        axios.get(`${API_URL}/products/?type=${payload.type_name}`)
        .then(response => {
          state.all_products = response.data;
        })
        .catch(e => {
          console.log(e);
        })
      }else{
        axios.get(`${API_URL}/products`)
        .then(response => {
          state.all_products = response.data;
        })
        .catch(e => {
          console.log(e);
        })
      }
    },
    GET_TYPES: (state) => {
      axios.get(`${API_URL}/product_types`)
      .then(response => {
        state.product_types = response.data;
      })
      .catch(e => {
        console.log(e);
      })
    }
  },

  actions: {
    addProduct: (context, product) => {
      context.commit('ADD_PRODUCT', product);
    },
    addUpdateProductState: (context, product) => {
      context.commit('ADD_UPDATE_PRODUCT_STATE', product);
    },
    deleteProductState: (context, id) => {
      context.commit('DELETE_PRODUCT_STATE', id);
    },
    removeProduct: (context, index) => {
      context.commit('REMOVE_PRODUCT', index);
    },
    currentProduct: (context, product) => {
      context.commit('CURRENT_PRODUCT', product);
    },
    showOrHiddenModal: (context) => {
      context.commit('SHOW_MODAL');
    },
    showOrHiddenPopupCart: (context) => {
      context.commit('SHOW_POPUP_CART');
    },
    getProducts: (context, payload) => {
      if(payload){
        context.commit('GET_PRODUCTS', payload);
      }else{
        context.commit('GET_PRODUCTS', {});
      }
    },
    getTypes: (context) => {
      context.commit('GET_TYPES');
    },
    addClient: (context, client) => {
      axios.post(API_URL + '/clients', client).then(response => {
        if(response.status == 201){
          context.commit('CLEAR_CART');
        }
      });
    }
  },
});
