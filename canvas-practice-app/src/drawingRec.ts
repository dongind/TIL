const drawingRect = (canvas: HTMLCanvasElement) => {
  const ctx = canvas.getContext("2d");

  if (!ctx) {
    return;
  }

  const drawingArc = (
    x: number,
    y: number,
    x1: number,
    x2: number,
    y1: number,
    y2: number,
    radius: number
  ) => {
    ctx.beginPath();
    ctx.fillStyle = "red";
    ctx.arc(x1, y1, 3, 0, 2 * Math.PI);
    ctx.arc(x2, y2, 3, 0, 2 * Math.PI);
    ctx.fill();

    ctx.beginPath();
    ctx.fillStyle = "blue";
    ctx.arc(x, y, 3, 0, 2 * Math.PI);
    ctx.fill();

    ctx.beginPath();
    ctx.fillStyle = "black";
    ctx.lineWidth = 5;
    ctx.moveTo(x, y);
    ctx.arcTo(x1, x2, y1, y2, radius);
    ctx.fill();
  };
  drawingArc(150, 150, 150, 130, 130, 130, 20);
};

export default drawingRect;
