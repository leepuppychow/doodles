<template>
  <div id="app">
    <h1>Welcome to Shared Canvas</h1>
    <canvas
      ref="canvas"
      :width="canvasWidth"
      :height="canvasHeight"
      @mousedown="isDrawing = true"
      @mouseup="isDrawing = false"
      @mousemove="draw"
    ></canvas>
  </div>
</template>

<script>
const CANVAS_WIDTH_PERCENT = 0.7;
const CANVAS_HEIGHT_PERCENT = 0.6;

export default {
  name: 'App',
  data() {
    return {
      isDrawing: false,
      cursorX: 0,
      cursorY: 0,
      canvasWidth: 0,
      canvasHeight: 0,
    }
  },
  created() {
    window.addEventListener('resize', this.resizeCanvas);
    this.resizeCanvas();
  },
  methods: {
    resizeCanvas() {
      this.canvasWidth = window.innerWidth * CANVAS_WIDTH_PERCENT;
      this.canvasHeight = window.innerHeight * CANVAS_HEIGHT_PERCENT;
    },
    draw(event) {
      if (!this.isDrawing) return;

      const { canvas } = this.$refs;
      const context = canvas.getContext('2d');
      const canvasPosition = canvas.getBoundingClientRect();

      context.beginPath();
      context.lineWidth = 5;
      context.lineCap = 'round';
      context.strokeStyle = 'green';

      this.cursorX = event.clientX - canvasPosition.left;
      this.cursorY = event.clientY - canvasPosition.top;

      context.lineTo(this.cursorX, this.cursorY);
      context.stroke();
    }
  },
}
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

canvas {
  border: solid black 1px;
}
</style>
