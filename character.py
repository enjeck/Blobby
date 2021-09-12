import random 
import math

# Some helper functions
def divide(count):
  deg = 360 / count
  arr = ['0'] * count
  for i in range(len(arr)):
    arr[i] = int(i * deg)
  return arr

def shuf(listForShuffle):
  shuffledList = listForShuffle
  random.shuffle(shuffledList)
  return shuffledList
  
def randPoint(val, minv, maxv):
  radius = minv + val * (maxv - minv)
  if radius > maxv:
    radius = radius - minv
  elif radius < minv:
    radius = radius + minv
  return radius
 
def point(origin, radius, degree):
  x = origin + radius * math.cos(math.radians(degree))
  y = origin + radius * math.sin(math.radians(degree))
  return [round(x), round(y)]

# Create points from random points
def createPoints(size, minGrowth, edgesNum):
  outerRad = size/2
  innerRad = minGrowth * (outerRad / 10)
  center = size/2
  slices = divide(edgesNum);
  destPoints = []
  
  for item in slices:
    p = randPoint(random.uniform(0.1, 1.1), innerRad, outerRad)
    end = point(center, p, item)
    destPoints.append(end)
  
  return destPoints
  
# Create SVG path from points
def createSvgPath(points):
  svgPath = ""
  mid = [(points[0][0] + points[1][0]) / 2, (points[0][1] + points[1][1]) / 2,]
  svgPath += "M" + str(mid[0]) + "," + str(mid[1]);
  
  for i in range(len(points)):
    p1 = points[(i + 1) % len(points)]
    p2 = points[(i + 2) % len(points)]
    mid = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
    svgPath += "Q" + str(p1[0]) + "," + str(p1[1]) + "," + str(mid[0]) + "," + str(mid[1])
  svgPath += "Z"
  return svgPath

# List of colors, from which random color will be picked
# preferable to randomly generating colors
colors = ['#CEE5D0', '#ff8080', '#79B4B7', '#6B7AA1', 
'#DEBA9D', '#F6AE99','#FFBCBC','#B5EAEA','#CEE5D0',
'#c0dba9','#b8e0b6','#9A8194','#d8db76','#E8E9A1',
'#ECB390','#CFDAC8', '#f0c0c0', '#E5EDB7', '#F6DEF6']

bgColors = ['#FAF4EF', '#EFFAEF', '#EFF4FA', '#FAEFFA', '#EFF4FA', '#F4EFFA', '#FAFAEF', '#FAEFF4', '#EFFAFA', '#EFF7EB', '#DBDBDB', '#EDF1F7', '#EFF7EB', '#F7F7E9', '#EFEFEF']

# Create eyes
def createEyes(size):
  randNum = math.floor(random.random() * 10)
  randPositionX = random.uniform(-2, 2)
  randPositionY = random.uniform(-2, 2)
  # Give one or two eyes based on random number
  if randNum < 5:
    return f'<g id="eye" transform = "translate(50, 50)"><circle id="iris" cx="0" cy="0" r="{size}" stroke="#000" stroke-width="2" fill="#fff"></circle><circle id="pupil" cx="{randPositionX}" cy="{randPositionY}" r="{size/2}" fill="#000"></circle></g>'
  else:
    return f'<g><g transform = "translate(38, 50)"><circle cx="0" cy="0" r="{size}" stroke="#000" stroke-width="2" fill="#fff"></circle><circle cx="{randPositionX}" cy="{randPositionY}" r="{round(random.uniform(3, size/3))}" fill="#000"></circle></g><g transform = "translate(58, 50)"><circle cx="0" cy="0" r="{size}" stroke="#000" stroke-width="2" fill="#fff"></circle><circle cx="{randPositionX}" cy="{randPositionY}" r="{round(random.uniform(3, size/3))}" fill="#000"></circle></g></g>' 


# Create svg data
def generateCharacter():
  # Create blob and eyes with random values
  blobPoints = createPoints(round(random.uniform(95, 105)), round(random.uniform(4, 7)), round(random.uniform(6, 8)))
  blob = createSvgPath(blobPoints)   
  eyes = createEyes(round(random.uniform(6, 10)))
  
  # Random indices for the blob and background color
  randColorIndex = math.floor(random.random() * len(colors))
  randBgIndex = math.floor(random.random() * len(bgColors))
  
  # Compiling various parts
  header = f'<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" width="400" height="400">\n'
  footer = f'</svg>'
  background = f'<rect x="0" y="0" width="100" height="100" fill="{bgColors[randBgIndex]}"/>'
  body = f'<path stroke="transparent" stroke-width="0" fill = "{colors[randColorIndex]}" d="{blob}" />'
  stroke = f'<path transform="translate(-3, -3)" stroke="#000" stroke-width="2" fill = "none" d="{blob}" />'
  blush = '<g><circle  transform = "translate(70, 65)" cx="0" cy="0" r="6" fill="rgba(255,255,255,0.4)" ></circle><circle  transform = "translate(30, 65)" cx="0" cy="0" r="6" fill="rgba(255,255,255,0.4)"></circle></g>'
  
  # Join parts together
  fullCharacter = header + background + body + blush + stroke + eyes + footer
  return fullCharacter

#print (generateCharacter())




  
