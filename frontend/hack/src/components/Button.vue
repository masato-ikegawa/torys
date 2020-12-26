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
  font-size: 15px;
  cursor: pointer;
  width: 250px;
  height: 40px;
  border: solid 4px rgb(255, 16, 18);
  border-radius: 10px;
  background: white;
  font-weight: bold;
  color: rgb(255, 16, 18);
}

button:hover {
  opacity: 0.8;
}

button:focus {
  outline: 0;
}

@media screen and (min-width: 600px) {
  button {
    width: 250px;
    height: 40px;
    font-size: 13px;
  }
}

@media screen and (min-width: 900px) {
  button {
    width: 300px;
    height: 45px;
    font-size: 15px;
  }
}

@media screen and (min-width: 1200px) {
  button {
    width: 450px;
    height: 50px;
    font-size: 17px;
  }
}
</style>
