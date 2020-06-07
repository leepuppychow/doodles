<template>
  <div id="app">
    <h1>Welcome to Shared Canvas</h1>
    <canvas></canvas>
  </div>
</template>

<script>
export default {
  name: 'App',
  created() {
    console.log("Hello")
  }
}
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

canvas {
  width: 500px;
  height: 500px;
  border: solid black 1px;
}
</style>
