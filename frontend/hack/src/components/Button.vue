<template>
  <button>{{ label }}</button>
</template>

<script>
export default {
  name: "Button",
  props: {
    label: String,
  },
};
</script>

<style scoped>
button {
  user-select: none;
  width: 280px;
  height: 40px;
  font-size: 13px;
  cursor: pointer;
  border: solid 1px #000;
  border-radius: 10px;
  background: rgb(249, 142, 18);
  font-weight: bold;
  color: #fff;
}

button:hover {
  opacity: 0.8;
}

button:focus {
  outline: 0;
}

@media screen and (min-width: 600px) {
  button {
    width: 280px;
    height: 40px;
    font-size: 13px;
  }
}

@media screen and (min-width: 900px) {
  button {
    width: 350px;
    height: 40px;
    font-size: 15px;
  }
}

@media screen and (min-width: 1200px) {
  button {
    width: 400px;
    height: 50px;
    font-size: 17px;
  }
}
</style>
