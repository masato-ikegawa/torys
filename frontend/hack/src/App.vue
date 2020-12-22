<template>
  <div class="container">
    <h1>ニコニコおみくじ</h1>
    <Button class="btn" label="おみくじを回す" @click="tappedBtn"></Button>
    <Loading class="loading"></Loading>
    <Footer />
  </div>
</template>

<script lang="ts">
import Button from "./components/Button.vue";
import Loading from "./components/Loading.vue";
import Footer from "./components/Footer.vue";

function omikuji() {
  var random = Math.floor(Math.random() * 16);
  return random;
}

export default {
  name: "App",
  components: {
    Button,
    Loading,
    Footer,
  },
  methods: {
    tappedBtn() {
      this.$el.children[0].textContent = "Now Loading...";
      this.$el.children[1].classList.add("nodisp");
      this.$el.children[2].classList.add("disp");

      var result = omikuji();

      setTimeout(() => {
        if (result < 1) {
          this.$el.children[0].textContent = "大凶…";
        } else if (result < 3) {
          this.$el.children[0].textContent = "凶…";
        } else if (result < 6) {
          this.$el.children[0].textContent = "末吉";
        } else if (result < 10) {
          this.$el.children[0].textContent = "小吉";
        } else if (result < 13) {
          this.$el.children[0].textContent = "中吉";
        } else if (result < 15) {
          this.$el.children[0].textContent = "吉！";
        } else {
          this.$el.children[0].textContent = "大吉！";
        }
        this.$el.children[2].classList.add("nodisp");
      }, 1000);
    },
  },
};
</script>

<style>
body {
  margin: 0;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.container {
  width: 100%;
  min-height: 100vh;
  padding-bottom: 70px;
  position: relative;
  box-sizing: border-box;
}

h1 {
  font-size: 18px;
  margin-top: 0;
  padding-top: 60px;
}

.btn {
  margin-top: 80px;
}

.loading {
  display: none;
}

.disp {
  display: block;
}

.nodisp {
  display: none;
}

@media screen and (min-width: 600px) {
  button {
    width: 280px;
    height: 40px;
    font-size: 13px;
  }

  h1 {
    font-size: 18px;
  }
}

@media screen and (min-width: 900px) {
  button {
    width: 350px;
    height: 40px;
    font-size: 15px;
  }

  h1 {
    font-size: 21px;
  }
}

@media screen and (min-width: 1200px) {
  button {
    width: 400px;
    height: 50px;
    font-size: 17px;
  }

  h1 {
    font-size: 24px;
  }
}
</style>
