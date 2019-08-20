<template>
  <div id="app">
      <button id="button" v-on:click="getdata"></button>
      {{info}}
  </div>
</template>

<script>
    import MyTree from "./components/MyTree";
    import axios from 'axios'

    export default {
        name: 'App',
        components: {
            MyTree
        },
        data() {
            return {
                info: null
            }
        },
        methods: {
            getdata: function () {
                var url = "http://127.0.0.1:8000/atf/testapi/";
                // 发送请求:将数据返回到一个回到函数中
                var that = this;
                // 并且响应成功以后会执行then方法中的回调函数
                axios.get(url).then(response => (that.info = response));
            }
        }
    }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
  #button{
    height: 100px;
    width: 100px;
  }
</style>
