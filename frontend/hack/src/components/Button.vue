<template>
  <button v-if="active" class="act">{{ label }}</button>
  <button v-else class="anact">{{ label }}</button>
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

.act {
  cursor: pointer;
  border: solid 4px rgb(255, 16, 18);
  background: white;
  color: rgb(255, 16, 18);
}

.act:hover {
  opacity: 0.8;
}

.anact {
  background: #ddd;
  border: solid 4px #999;
  color: #000;
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
