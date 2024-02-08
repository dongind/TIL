// import drawBall from "./test1.ts";
import drawingRect from "./drawingRec.ts";

document.querySelector<HTMLDivElement>("#app")!.innerHTML = `
<div>
  <canvas id="canvas" width="300" height="300">
  </canvas>
</div>
`;

var canvas = document.getElementById("canvas") as HTMLCanvasElement;
drawingRect(canvas);

canvas.addEventListener("click", (e) => {
  console.log(e.clientX, e.clientY);
});
// const ball = drawBall(canvas);

// ball.draw();
