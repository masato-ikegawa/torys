<template>
  <button v-if="active" id="act-btn">{{ label }}</button>
  <button v-else id="anact-btn">{{ label }}</button>
</template>

<script>
export default {
  name: "Button",
  props: {
    label: String,
    active: { type: Boolean, default: false },
  },
};
</script>

<style>
#act-btn {
  cursor: pointer;
  border: solid 4px rgb(255, 16, 18);
  background: white;
  color: rgb(255, 16, 18);
}

#act-btn:hover {
  opacity: 0.8;
}

#anact-btn {
  background: #ddd;
  border: solid 4px #999;
  color: #000;
}
</style>

<style scoped>
button {
  align-items: center;
  display: block;
  user-select: none;
  font-size: 15px;
  width: 250px;
  height: 40px;
  border-radius: 10px;
  font-weight: bold;
}

button:focus {
  outline: 0;
}

@media screen and (min-width: 900px) {
  button {
    width: 300px;
    height: 45px;
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
