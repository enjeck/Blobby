// lib/character.ts

// Helper functions
function divide(count: number): number[] {
  const deg = 360 / count;
  const arr: number[] = [];
  for (let i = 0; i < count; i++) {
    arr.push(Math.floor(i * deg));
  }
  return arr;
}

function randPoint(val: number, minv: number, maxv: number): number {
  let radius = minv + val * (maxv - minv);
  if (radius > maxv) {
    radius = radius - minv;
  } else if (radius < minv) {
    radius = radius + minv;
  }
  return radius;
}

function point(origin: number, radius: number, degree: number): [number, number] {
  const x = origin + radius * Math.cos((degree * Math.PI) / 180);
  const y = origin + radius * Math.sin((degree * Math.PI) / 180);
  return [Math.round(x), Math.round(y)];
}

// Create points from random points
function createPoints(size: number, minGrowth: number, edgesNum: number): [number, number][] {
  const outerRad = size / 2;
  const innerRad = minGrowth * (outerRad / 10);
  const center = size / 2;
  const slices = divide(edgesNum);
  const destPoints: [number, number][] = [];

  for (const item of slices) {
    const p = randPoint(Math.random() * 1.0 + 0.1, innerRad, outerRad);
    const end = point(center, p, item);
    destPoints.push(end);
  }

  return destPoints;
}

// Create SVG path from points
function createSvgPath(points: [number, number][]): string {
  let svgPath = "";
  const mid: [number, number] = [
    (points[0][0] + points[1][0]) / 2,
    (points[0][1] + points[1][1]) / 2,
  ];
  svgPath += `M${mid[0]},${mid[1]}`;

  for (let i = 0; i < points.length; i++) {
    const p1 = points[(i + 1) % points.length];
    const p2 = points[(i + 2) % points.length];
    const midPoint: [number, number] = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2];
    svgPath += `Q${p1[0]},${p1[1]},${midPoint[0]},${midPoint[1]}`;
  }
  svgPath += "Z";
  return svgPath;
}

// Colors
const colors = [
  '#CEE5D0', '#ff8080', '#79B4B7', '#6B7AA1', 
  '#DEBA9D', '#F6AE99','#FFBCBC','#B5EAEA','#CEE5D0',
  '#c0dba9','#b8e0b6','#9A8194','#d8db76','#E8E9A1',
  '#ECB390','#CFDAC8', '#f0c0c0', '#E5EDB7', '#F6DEF6'
];

const bgColors = [
  '#FAF4EF', '#EFFAEF', '#EFF4FA', '#FAEFFA', '#EFF4FA', 
  '#F4EFFA', '#FAFAEF', '#FAEFF4', '#EFFAFA', '#EFF7EB', 
  '#DBDBDB', '#EDF1F7', '#EFF7EB', '#F7F7E9', '#EFEFEF'
];

// Create eyes
function createEyes(size: number): string {
  const randNum = Math.floor(Math.random() * 10);
  const randPositionX = Math.random() * 4 - 2;
  const randPositionY = Math.random() * 4 - 2;

  if (randNum < 5) {
    return `<g id="eye" transform="translate(50, 50)"><circle id="iris" cx="0" cy="0" r="${size}" stroke="#000" stroke-width="2" fill="#fff"></circle><circle id="pupil" cx="${randPositionX}" cy="${randPositionY}" r="${size/2}" fill="#000"></circle></g>`;
  } else {
    return `<g><g transform="translate(38, 50)"><circle cx="0" cy="0" r="${size}" stroke="#000" stroke-width="2" fill="#fff"></circle><circle cx="${randPositionX}" cy="${randPositionY}" r="${Math.round(Math.random() * (size/3 - 3) + 3)}" fill="#000"></circle></g><g transform="translate(58, 50)"><circle cx="0" cy="0" r="${size}" stroke="#000" stroke-width="2" fill="#fff"></circle><circle cx="${randPositionX}" cy="${randPositionY}" r="${Math.round(Math.random() * (size/3 - 3) + 3)}" fill="#000"></circle></g></g>`;
  }
}

// Main generation function
export function generateCharacter(): string {
  const blobPoints = createPoints(
    Math.round(Math.random() * 10 + 95),
    Math.round(Math.random() * 3 + 4),
    Math.round(Math.random() * 2 + 6)
  );
  const blob = createSvgPath(blobPoints);
  const eyes = createEyes(Math.round(Math.random() * 4 + 6));

  const randColorIndex = Math.floor(Math.random() * colors.length);
  const randBgIndex = Math.floor(Math.random() * bgColors.length);

  const header = '<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" width="400" height="400">\n';
  const footer = '</svg>';
  const body = `<path stroke="transparent" stroke-width="0" fill="${colors[randColorIndex]}" d="${blob}" />`;
  const stroke = `<path transform="translate(-3, -3)" stroke="#000" stroke-width="2" fill="none" d="${blob}" />`;
  const blush = '<g><circle transform="translate(70, 65)" cx="0" cy="0" r="6" fill="rgba(255,255,255,0.4)"></circle><circle transform="translate(30, 65)" cx="0" cy="0" r="6" fill="rgba(255,255,255,0.4)"></circle></g>';

  return header + body + blush + stroke + eyes + footer;
}
