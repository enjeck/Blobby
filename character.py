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
    slices = divide(edgesNum)
    destPoints = []

    for item in slices:
        p = randPoint(random.uniform(0.1, 1.1), innerRad, outerRad)
        end = point(center, p, item)
        destPoints.append(end)

    return destPoints

# Create SVG path from points


def createSvgPath(points):
    svgPath = ""
    mid = [(points[0][0] + points[1][0]) / 2,
           (points[0][1] + points[1][1]) / 2, ]
    svgPath += "M" + str(mid[0]) + "," + str(mid[1])

    for i in range(len(points)):
        p1 = points[(i + 1) % len(points)]
        p2 = points[(i + 2) % len(points)]
        mid = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]
        svgPath += "Q" + str(p1[0]) + "," + str(p1[1]) + \
            "," + str(mid[0]) + "," + str(mid[1])
    svgPath += "Z"
    return svgPath


# List of colors, from which random color will be picked

# preferable to randomly generating colors
colors = ['#CEE5D0', '#ff8080', '#79B4B7', '#6B7AA1',
          '#DEBA9D', '#F6AE99', '#FFBCBC', '#B5EAEA', '#CEE5D0',
          '#c0dba9', '#b8e0b6', '#9A8194', '#d8db76', '#E8E9A1',
          '#ECB390', '#CFDAC8', '#f0c0c0', '#E5EDB7', '#F6DEF6', '#F7C9C9', '#94A7D1',
          '#FED97A', '#93E5AC', '#FC8AA9', '#8CA4F7', '#BF9DFB']

bgColors = ['#FAF4EF', '#EFFAEF', '#EFF4FA', '#FAEFFA', '#EFF4FA', '#F4EFFA', '#FAFAEF',
            '#FAEFF4', '#EFFAFA', '#EFF7EB', '#DBDBDB', '#EDF1F7', '#EFF7EB', '#F7F7E9', '#EFEFEF']

# Eyes


def createEyes(size, colorDark, style):
    randNum = math.floor(random.random() * 10)
    randPositionX = random.uniform(-2, 2)
    randPositionY = random.uniform(-2, 2)

    randEllipse = random.uniform(size/2, size)
    randPupil = random.uniform(1, size/4)
    randPupil1 = random.uniform(2, size/1.5)
    randDot = random.uniform(1, size/6)

    randPositionX1 = random.uniform(-3, 3)
    randPositionY1 = random.uniform(-3, 3)

    randEllipse1 = random.uniform(size/2, size)
    randPupil1 = random.uniform(1, size/4)

    randRy = random.uniform(size/3, size/2)
    size1 = random.uniform(size/2, size)

    randPupil1 = random.uniform(2, size/1.5)

    options = {
        'cyclops_white_iris_small_pupil': f'<g transform = "translate(50, 40)"><ellipse style="filter:blur(1px)" fill="{colorDark}" id="iris" cx="0" cy="0" rx="{randEllipse*1.3}" ry="{random.uniform(size, size*1.5)}" /> <ellipse fill="#fff" id="iris" cx="0" cy="0" rx="{randEllipse}" ry="{random.uniform(size/1.5, size)}" /><circle cx="{randPositionX}" cy="{randPositionY}" r="{randPupil}" fill="#333"></circle></g>',
        'cyclops_googley': f'<g id="eye" transform = "translate(50, 45)"><circle id="iris" cx="0" cy="0" r="{size}" stroke="#333" stroke-width="2" fill="#fff"></circle><circle id="pupil" cx="{randPositionX}" cy="{randPositionY}" r="{size/2}" fill="#333"></circle></g>',
        'cyclops_thin_stroke_pupil': f'<g id="eye" transform = "translate(50, 45)"><circle cx="0" cy="0" r="{size}" stroke="#333" stroke-width="1" fill="#fff"></circle><circle cx="{randPositionX}" cy="{randPositionY}" r="{randPupil1}" fill="#333"></circle></g>',
        'cyclops_small_white_iris': f'<g transform = "translate(50, 45)"><circle stroke-width="1px" stroke="#fff" fill="#fff" id="iris" cx="0" cy="0" r="{size/2}"></circle> <circle fill="#fff" id="iris" cx="0" cy="0" r="{size/2}"></circle><circle cx="{randPositionX}" cy="{randPositionY}" r="{round(random.uniform(1, size/4))}" fill="#333"></circle></g>',
        'cyclops_thin_border': f'<g id="eye" transform = "translate(50, 45)"><circle id="iris" cx="0" cy="0" r="{size}" stroke="#333" stroke-width="1" fill="#fff"></circle><circle id="pupil" cx="{randPositionX}" cy="{randPositionY}" r="{size/2}" fill="#333"></circle></g>',
        'cyclops_half_closed_full': f'<g id="eye" transform = "translate(50, 44)"><circle cx="0" cy="0" r="{size}" stroke="#333" stroke-width="1" fill="#fff"></circle><circle cx="0" cy="0" r="3" fill="#333"></circle> <path d="M0,{size*2} a1,1 0 0,0 {size*2},0z" transform="translate({size}, {size*2}) rotate(180,0,0)" fill="#fff" stroke="#333" stroke-width="1"/></g>',
        'cyclops_half_closed_cut': f'<g id="eye" transform = "translate(50, 45)"><rect transform = "translate({-size*1.5}, {-size/2 - 0.5})" rx="1" ry="{-size/2}" x="0" y="0" width="{size*3}" height="1" fill="#333"/> <path d="M0,0 a1,1 0 0,0 {size*2},0z" transform="translate({-size}, {-size/2})" fill="#fff" stroke="#333" stroke-width="1"/> <circle cx="0" cy="0" r="1" fill="#333"></circle></g>',
        'cyclops_black_iris_white_pupil': f'<g transform = "translate(50, 45)" ><circle fill="#333" id="iris" cx="0" cy="0" r="{size/2}"></circle><circle cx="{randPositionX}" cy="{randPositionY}" r="{randDot}" fill="#fff"></circle></g>',
        'cyclops_black_reflective': f'<g transform = "translate(50, 45)"> <circle fill="#fff" stroke-width="1" stroke="#333" cx="0" cy="0" r="{size/1.2}"></circle><circle fill="#333" id="iris" cx="0" cy="0" r="{size/1.7}"></circle><circle cx="{randPositionX1}" cy="{randPositionY1}" r="{randDot}" fill="#fff"></circle></g>',
        'black_iris_white_pupil': f'<g><g transform = "translate(38, 45)"><circle fill="#333" id="iris" cx="0" cy="0" r="{size/2}"></circle><circle cx="{randPositionX}" cy="{randPositionY}" r="{randDot}" fill="#fff"></circle></g> <g transform = "translate(60, 45)"><circle fill="#333" id="iris" cx="0" cy="0" r="{size/2}"></circle><circle cx="{randPositionX}" cy="{randPositionY}" r="{randDot}" fill="#fff"></circle></g></g>',
        'black_reflective': f'<g><g transform = "translate(38, 45)"><circle fill="#fff" stroke-width="1" stroke="#333" cx="0" cy="0" r="{size/1.5}"></circle><circle fill="#333" id="iris" cx="0" cy="0" r="{size/2}"></circle><circle cx="{randPositionX}" cy="{randPositionY}" r="{randDot}" fill="#fff"></circle></g> <g transform = "translate(60, 45)"><circle fill="#fff" stroke-width="1" stroke="#333" cx="0" cy="0" r="{size/1.5}"></circle><circle fill="#333" id="iris" cx="0" cy="0" r="{size/2}"></circle><circle cx="{randPositionX}" cy="{randPositionY}" r="{randDot}" fill="#fff"></circle></g></g>',
        'white_iris_small_pupil': f'<g><g transform = "translate(38, 40)"><ellipse style="filter:blur(2px)" fill="{colorDark}" cx="0" cy="0" rx="{randEllipse1*1.1}" ry="{random.uniform(size, size*1.1)}" /> <ellipse fill="#fff" id="iris" cx="0" cy="0" rx="{randEllipse1}" ry="{random.uniform(size/1.5, size)}" /><circle cx="{randPositionX}" cy="{randPositionY}" r="{randPupil1}" fill="#333"></circle></g><g transform = "translate(58, 40)"><ellipse style="filter:blur(1px)" fill="{colorDark}" id="iris" cx="0" cy="0" rx="{randEllipse1*1.3}" ry="{random.uniform(size, size*1.5)}" /><ellipse fill="#fff" id="iris" cx="0" cy="0" rx="{randEllipse1}" ry="{random.uniform(size/1.5, size)}" /><circle cx="{randPositionX}" cy="{randPositionY}" r="{randPupil1}" fill="#333"></circle></g></g>',
        'small_white_iris': f'<g><g transform = "translate(38, 45)"><circle fill="#fff" id="iris" cx="0" cy="0" r="{size/2}"></circle><circle cx="{randPositionX}" cy="{randPositionY}" r="{round(random.uniform(2, size/4))}" fill="#333"></circle></g> <g transform = "translate(60, 45)"><circle fill="#fff" id="iris" cx="0" cy="0" r="{size/2}"></circle><circle cx="{randPositionX}" cy="{randPositionY}" r="{round(random.uniform(2, size/4))}" fill="#333"></circle></g></g>',
        'cross': f'<g fill="#333"><g transform = "translate(32, 43)"><rect transform = "rotate(-45 7 0)" rx="1" ry="1" x="0" y="0" width="10" height="1.5"/> <rect transform = "rotate(35 3 2)" rx="1" ry="1" x="0" y="0" width="10" height="1.5"/></g> <g transform = "translate(54, 43)"><rect transform = "rotate(-45 7 0)" rx="1" ry="1" x="0" y="0" width="10" height="1.5"/> <rect transform = "rotate(35 3 4)" rx="1" ry="1" x="0" y="0" width="10" height="1.5" /></g></g>',
        'slant_down': f'<g fill="#333" transform = "translate(36, 45)"><rect transform = "rotate(-35 7 0)" rx="1" ry="1" x="0" y="0" width="8" height="1.5"/>  <rect transform = "rotate(35 1 0) translate(15, -10)" rx="1" ry="1" x="0" y="0" width="8" height="1.5" /></g>',
        'small_iris_border': f'<g><g transform = "translate(38, 46)"><circle cx="0" cy="0" r="{size/3}" stroke="#000" stroke-width="1" fill="#fff"></circle><circle cx="{randPositionX}" cy="{randPositionY}" r="2" fill="#000"></circle></g><g transform = "translate(58, 46)"><circle cx="0" cy="0" r="{size/3}" stroke="#000" stroke-width="1" fill="#fff"></circle><circle cx="{randPositionX}" cy="{randPositionY}" r="2" fill="#000"></circle></g></g>',
        'small_black': f'<g><g transform = "translate(38, 46)"><ellipse cx="0" cy="0" rx="{size/3}" ry="{randRy}" fill="#000"/> <circle cx="{randPositionX}" cy="{randPositionY}" r="1" fill="#fff"> </circle></g><g transform = "translate(58, 46)"><ellipse cx="0" cy="0" rx="{size/3}" ry="{randRy}" fill="#000" /> <circle cx="{randPositionX}" cy="{randPositionY}" r="1" fill="#fff"></circle></g></g>',
        'slant_up': f'<g fill="#333" transform = "translate(36, 45)"><rect transform = "rotate(20 0 0)" rx="1" ry="1" x="0" y="0" width="8" height="1.5"/>  <rect transform = "rotate(-25 1 0) translate(15, 10)" rx="1" ry="1" x="0" y="0" width="8" height="1.5" /></g>',
        'squeezed': f'<g fill="#333"><g transform = "translate(35, 45)"><rect transform = "rotate(-45 7 0)" rx="1" ry="1" x="0" y="0" width="5" height="1.5"/> <rect transform = "rotate(35 2 3)" rx="1" ry="1" x="0" y="0" width="5" height="1.5"/></g> <g transform = "translate(54, 46)"><rect transform = "rotate(45 0 0)" rx="1" ry="1" x="0" y="0" width="5" height="1.5"/> <rect transform = "rotate(-35 1 2)" rx="1" ry="1" x="0" y="0" width="5" height="1.5"/></g></g>',
        'wink': f'<g fill="#333"><g transform = "translate(37, 44)"><rect transform = "rotate(-45 7 0)" rx="1" ry="1" x="0" y="0" width="5" height="2"/> <rect transform = "rotate(35 2 4)" rx="1" ry="1" x="0" y="0" width="5" height="2"/></g> <g transform = "translate(54, 47)"><circle cx="0" cy="0" r="3" ></circle></g></g>',
        'small_dark': f'<g fill="#000"><g transform = "translate(40, 45)"><circle cx="0" cy="0" r="{size/4}"></circle></g><g transform = "translate(55, 45)"><circle cx="0" cy="0" r="{size/4}"></circle></g></g>',
        'down_curve': f'<g><g transform = "translate(38, 40)">  <path d="M0,{size} a1,1 0 0,0 {size*1.5},0" transform="translate({size}, {size*2}) rotate(180,0,0)" fill="transparent" stroke="#333" stroke-width="2"/>  </g><g transform = "translate(58, 40)"> <path d="M0,{size} a1,1 0 0,0 {size*1.5},0" transform="translate({size}, {size*2}) rotate(180,0,0)" fill="transparent" stroke="#333" stroke-width="2"/>  </g></g>',
        'up_curve': f'<g><g transform = "translate(35, 30)">  <path d="M0,{size} a1,1 0 0,0 {size*1.5},0"  fill="transparent" stroke="#333" stroke-width="2"/>  </g><g transform = "translate(55, 30)"> <path d="M0,{size} a1,1 0 0,0 {size*1.5},0" fill="transparent" stroke="#333" stroke-width="2"/>  </g></g>',
        'half_closed_full': f'<g><g transform = "translate(40, 40)"> <circle cx="0" cy="0" r="{size}" stroke="#333" stroke-width="1" fill="#fff"></circle><circle cx="0" cy="0" r="3" fill="#333"></circle> <path d="M0,{size*2} a1,1 0 0,0 {size*2},0z" transform="translate({size}, {size*2}) rotate(180,0,0)" fill="#fff" stroke="#333" stroke-width="1"/>  </g><g transform = "translate(58, 40)"> <circle cx="0" cy="0" r="{size}" stroke="#333" stroke-width="1" fill="#fff"></circle><circle cx="0" cy="0" r="3" fill="#333"></circle> <path d="M0,{size*2} a1,1 0 0,0 {size*2},0z" transform="translate({size}, {size*2}) rotate(180,0,0)" fill="#fff" stroke="#333" stroke-width="1"/>  </g></g>',

        'half_closed_cut': f'<g><g transform = "translate(38, 50)"><rect transform = "translate({-size1*1.5}, {-size1/2 - 0.5})" rx="1" ry="{-size1/2}" x="0" y="0" width="{size1*3}" height="1" fill="#333"/> <path d="M0,0 a1,1 0 0,0 {size1*2},0z" transform="translate({-size1}, {-size1/2})" fill="#fff" stroke="#333" stroke-width="1"/> <circle cx="0" cy="0" r="1" fill="#333"></circle> </g><g transform = "translate(58, 50)"><rect transform = "translate({-size1*1.5}, {-size1/2 - 0.5})" rx="1" ry="{-size1/2}" x="0" y="0" width="{size1*3}" height="1" fill="#333"/> <path d="M0,0 a1,1 0 0,0 {size1*2},0z" transform="translate({-size1}, {-size1/2})" fill="#fff" stroke="#333" stroke-width="1"/> <circle cx="0" cy="0" r="1" fill="#333"></circle> </g></g>',

        'straight_lines': f'<g fill="#333"><rect transform = "translate(35, 50)" rx="1" ry="1" x="0" y="0" width="6" height="1.5" /><rect transform = "translate(58, 50)" rx="1" ry="1" x="0" y="0" width="6" height="1.5"/></g>',
        'eye_roll': f'<g fill="#333"><g transform = "translate(35, 44)"><rect rx="1" ry="1" x="0" y="0" width="8" height="1.5"/><circle cx="7.5" cy="2" r="2" ></circle></g> <g transform = "translate(50, 44)"><rect rx="1" ry="1" x="0" y="0" width="8" height="1.5" /><circle cx="7.5" cy="2" r="2"></circle></g></g>',
        'googley': f'<g><g transform = "translate(38, 45)"><circle cx="0" cy="0" r="{size}" stroke="#333" stroke-width="2" fill="#fff"></circle><circle cx="{randPositionX}" cy="{randPositionY}" r="{round(random.uniform(3, size/3))}" fill="#333"></circle></g><g transform = "translate(58, 45)"><circle cx="0" cy="0" r="{size}" stroke="#333" stroke-width="2" fill="#fff"></circle><circle cx="{randPositionX}" cy="{randPositionY}" r="{round(random.uniform(3, size/3))}" fill="#333"></circle></g></g>',
        'thin_border': f'<g><g transform = "translate(38, 45)"><circle cx="0" cy="0" r="{size}" stroke="#333" stroke-width="1" fill="#fff"></circle><circle cx="{randPositionX}" cy="{randPositionY}" r="{randPupil1}" fill="#333"></circle></g><g transform = "translate(58, 45)"><circle cx="0" cy="0" r="{size}" stroke="#333" stroke-width="1" fill="#fff"></circle><circle cx="{randPositionX}" cy="{randPositionY}" r="{randPupil1}" fill="#333"></circle></g></g>'

    }

    # Eye design options based on style
    soft = ['cyclops_white_iris_small_pupil', 'cyclops_googley', 'cyclops_thin_stroke_pupil', 'cyclops_small_white_iris', 'cyclops_thin_border', 'cyclops_half_closed_full', 'cyclops_half_closed_cut', 'cyclops_black_iris_white_pupil', 'cyclops_black_reflective',
            'black_iris_white_pupil', 'black_reflective', 'white_iris_small_pupil', 'small_white_iris', 'cross', 'small_iris_border', 'small_black', 'small_dark', 'down_curve', 'up_curve', 'half_closed_full', 'half_closed_cut',  'straight_lines', 'eye_roll', ]
    border = ['cyclops_white_iris_small_pupil', 'cyclops_googley', 'cyclops_thin_stroke_pupil', 'cyclops_small_white_iris', 'cyclops_thin_border', 'cyclops_half_closed_full', 'cyclops_half_closed_cut', 'cyclops_black_iris_white_pupil', 'cyclops_black_reflective', 'black_iris_white_pupil',
              'black_reflective', 'white_iris_small_pupil', 'small_white_iris', 'cross', 'slant_down', 'small_iris_border', 'small_black', 'slant_up', 'squeezed', 'wink', 'small_dark', 'down_curve', 'up_curve', 'half_closed_full', 'half_closed_cut',  'straight_lines', 'eye_roll', ]
    thin = ['cyclops_white_iris_small_pupil', 'cyclops_googley', 'cyclops_thin_stroke_pupil', 'cyclops_small_white_iris', 'cyclops_thin_border', 'cyclops_half_closed_full', 'cyclops_half_closed_cut', 'cyclops_black_iris_white_pupil', 'cyclops_black_reflective', 'black_iris_white_pupil',
            'black_reflective', 'white_iris_small_pupil', 'small_white_iris', 'cross', 'slant_down', 'small_iris_border', 'small_black', 'slant_up', 'squeezed', 'wink', 'small_dark',  'down_curve', 'up_curve', 'half_closed_full', 'half_closed_cut',  'straight_lines', 'eye_roll', ]
    classic = ['cyclops_googley', 'googley']

    # Randomly select eye design based on style
    if style == 'border':
        randEyeIndex = math.floor(random.random() * len(border))
        eye = border[randEyeIndex]
        return options[eye]
    elif style == 'thin':
        randEyeIndex = math.floor(random.random() * len(thin))
        eye = thin[randEyeIndex]
        return options[eye]
    elif style == 'soft':
        randEyeIndex = math.floor(random.random() * len(soft))
        eye = soft[randEyeIndex]
        return options[eye]
    else:
        randEyeIndex = math.floor(random.random() * len(classic))
        eye = classic[randEyeIndex]
        return options[eye]


# Mouth

def createMouth(widthRandom, colorDark, colorDarker, style):

    options = {
        'no_mouth': '',
        'forced_smile_colored': f'<g><rect transform = "translate({(-widthRandom)/10+44}, 60)" rx="2" ry="2" x="0" y="0" width="{widthRandom}" height="5" stroke="{colorDarker}" fill="#fff" stroke-width="1"/><rect transform = "translate({(-widthRandom)/10+44}, 62)" rx="1" ry="1" x="0" y="0" width="{widthRandom/1.7}" height="1" fill="{colorDarker}"/> <rect transform = "translate({(-widthRandom)/2.5+44+widthRandom}, 62)" rx="1" ry="1" x="0" y="0" width="{widthRandom/5}" height="1" fill="{colorDarker}"/> </g>',
        'forced_smile_black': f'<g><rect transform = "translate({(-widthRandom)/10+44}, 60)" rx="2" ry="2" x="0" y="0" width="{widthRandom}" height="5" stroke="#333" fill="#fff" stroke-width="1"/><rect transform = "translate({(-widthRandom)/10+44}, 62)" rx="1" ry="1" x="0" y="0" width="{widthRandom/1.7}" height="1" fill="#333"/> <rect transform = "translate({(-widthRandom)/2.5+44+widthRandom}, 62)" rx="1" ry="1" x="0" y="0" width="{widthRandom/5}" height="1" fill="#333"/> </g>',
        'straight_line_colored': f'<g> <rect transform = "translate({(-widthRandom)/3+45}, 58)" rx="0.5" ry="0.5" x="0" y="0" width="{widthRandom}" height="2" fill="{colorDarker}" /></g>',
        'straight_line_black': f'<g> <rect transform = "translate({(-widthRandom)/3+45}, 58)" rx="0.5" ry="0.5" x="0" y="0" width="{widthRandom}" height="2" fill="#333" /></g>',
        'full_pink_lips': f'<g><rect transform = "translate({(-widthRandom)/4+45}, 60)" rx="4" ry="4" x="0" y="0" width="{widthRandom}" height="4" fill="#FFB7C4" stroke-width="1" stroke="#F68393" /><rect transform = "translate({(-widthRandom/1.7)/6+45}, 61.5)" rx="0.5" ry="0.5" x="0" y="0" width="{widthRandom/1.7}" height="1" fill="#F68393" /></g>',
        'straight_line_shadow': f'<g><rect transform = "translate({(-widthRandom)/3+45}, 60)" rx="0.5" ry="0.5" x="0" y="0" width="{widthRandom}" height="2" fill="#fff" stroke-width="5" stroke ="{colorDarker}" /> <rect transform = "translate({(-widthRandom)/3+45}, 60)" rx="2" ry="1" x="0" y="0" width="{widthRandom}" height="2" fill="#333"/></g>',
        'straight_line_cheeks': f'<g><rect transform = "translate({(-widthRandom)/3+47}, 60)" rx="0" ry="0" x="0" y="0" width="{widthRandom}" height="1.5" fill="#333"/><rect transform = "translate({(-widthRandom)/3+47}, 57.5) rotate(90,0,0)" rx="1" ry="1" x="0" y="0" width="6" height="1.5" fill="#333"/> <rect transform = "translate({(widthRandom)/1.45+47}, 57.5) rotate(90,0,0)" rx="1" ry="1" x="0" y="0" width="6" height="1.5" fill="#333"/> </g>',
        'round_stroke': f'<g transform = "translate(50, 64)"><ellipse stroke="{colorDarker}" stroke-width="2" fill="rgba(255,255,255,0.4)" cx="0" cy="0" rx="{random.uniform(3, 5)}" ry="{random.uniform(3, 5)}" /></g>',
        'curved_sad_open': f'<g transform = "translate({50+(widthRandom/2)}, 65)"><path d="M0,0 a1,1 0 0,0 {widthRandom},0" transform=" rotate(180,0,0)" fill="transparent" stroke="{colorDarker}" stroke-width="2"/></g>',
        'curved_happy_open': f'<g transform = "translate({50-(widthRandom/2)}, 60)"><path d="M0,0 a1,1 0 0,0 {widthRandom},0" fill="transparent" stroke="{colorDarker}" stroke-width="2"/></g>',
        'curved_happy_closed_filled': f'<g transform = "translate({50-(widthRandom/2)}, 60)"><path d="M0,0 a1,1 0 0,0 {widthRandom},0z" fill="{colorDarker}" stroke="{colorDarker}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></g>',
        'curved_happy_closed_stroke': f'<g transform = "translate({50-(widthRandom/2)}, 60)"><path d="M0,0 a1,1 0 0,0 {widthRandom},0z" fill="transparent" stroke="{colorDarker}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></g>',
        'curved_sad_closed_stroke': f'<g transform = "translate({50+(widthRandom/2)}, 63)"><path d="M0,0 a1,1 0 0,0 {widthRandom},0z" transform=" rotate(180,0,0)" fill="transparent" stroke="{colorDarker}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></g>',
        'curved_sad_closed_filled': f'<g transform = "translate({50+(widthRandom/2)}, 68)"><path d="M0,0 a1,1 0 0,0 {widthRandom},0z" transform=" rotate(180,0,0)" fill="{colorDarker}" stroke="{colorDarker}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></g>',
        'round_filled': f'<g transform = "translate(50, 61)"><ellipse cx="0" cy="0" rx="{random.uniform(3, 6)}" ry="{random.uniform(1.2, 6)}" fill="{colorDarker}"/></g>'

    }

    soft = ['forced_smile', ]
    border = ['forced_smile_black', 'no_mouth', 'straight_line_colored', 'straight_line_black', 'full_pink_lips', 'straight_line_shadow', 'straight_line_cheeks', 'round_stroke', 'curved_sad_open',
              'curved_happy_open', 'curved_happy_closed_filled', 'forced_smile_colored', 'curved_happy_closed_stroke', 'curved_happy_closed_stroke', 'curved_sad_closed_filled', 'round_filled']
    thin = ['forced_smile_black', 'no_mouth', 'straight_line_colored', 'straight_line_black', 'full_pink_lips', 'straight_line_shadow', 'straight_line_cheeks', 'round_stroke', 'curved_sad_open',
            'curved_happy_open', 'curved_happy_closed_filled', 'forced_smile_colored', 'curved_happy_closed_stroke', 'curved_happy_closed_stroke', 'curved_sad_closed_filled', 'round_filled']
    soft = ['forced_smile_black', 'no_mouth', 'straight_line_colored', 'straight_line_black', 'full_pink_lips', 'straight_line_shadow', 'straight_line_cheeks', 'round_stroke', 'curved_sad_open',
            'curved_happy_open', 'curved_happy_closed_filled', 'forced_smile_colored', 'curved_happy_closed_stroke', 'curved_happy_closed_stroke', 'curved_sad_closed_filled', 'round_filled']

    if style == 'border':
        randMouthIndex = math.floor(random.random() * len(border))
        mouth = border[randMouthIndex]
        return options[mouth]
    elif style == 'thin':
        randMouthIndex = math.floor(random.random() * len(thin))
        mouth = thin[randMouthIndex]
        return options[mouth]
    elif style == 'soft':
        randMouthIndex = math.floor(random.random() * len(soft))
        mouth = soft[randMouthIndex]
        return options[mouth]
    else:
        return ''

# Blush

def createBlush(color, style):

    ryRandom = random.uniform(3, 6)
    blush_options = {
        'many_dots': f'<g fill="{color}"><g transform = "translate(65, 60)"><circle  cx="0" cy="0" r="0.9" ></circle> <circle  cx="2" cy="2" r="1" ></circle> <circle  cx="-2" cy="2" r="0.6" ></circle> <circle  cx="1.5" cy="-1.8" r="1" ></circle><circle  cx="-2" cy="-2" r="0.8" ></circle><circle  cx="-4" cy="0" r="1.1" ></circle></g>   <g transform = "translate(35, 60)" ><circle  cx="0" cy="0" r="0.8" ></circle> <circle  cx="3" cy="3" r="1" ></circle> <circle  cx="-2" cy="2" r="0.7" ></circle> <circle  cx="3" cy="-3" r="1.1" ></circle><circle  cx="-2" cy="-2" r="0.8" ></circle></g></g>',
        'round_far': f'<g fill="rgba(255,255,255,0.3)"><ellipse transform = "translate(70, 65)" cx="0" cy="0" rx="6" ry="{ryRandom}" /> <ellipse transform = "translate(30, 65)" cx="0" cy="0" rx="6" ry="{ryRandom}"/></g>',
    }
    blushes = ['many_dots', 'round_far']

    if style == 'classic' or style == 'border' or style == 'thin':
        randBlushIndex = math.floor(random.random() * len(blushes))
        blush = blushes[randBlushIndex]
        return blush_options[blush]
    else:
        return ""

# Body

def createBody(blob, color, colorLight, colorLightest, colorDark, colorDarker, colorLightDark, style):
    blobPoints = createPoints(round(random.uniform(45, 65)), round(
        random.uniform(2, 4)), round(random.uniform(12, 17)))
    shadowBlob = createSvgPath(blobPoints)
    blobPoints1 = createPoints(round(random.uniform(65, 85)), round(
        random.uniform(2, 4)), round(random.uniform(12, 17)))
    shadowBlob1 = createSvgPath(blobPoints1)

    # Creating body patterns

    # Circles pattern
    nums = [0]*150
    r = list(map((lambda x: {'x': random.uniform(
        0, 100), 'y': random.uniform(0, 100)}), nums))
    circles = ''
    for val in r:
        circles += f'<rect width="1" height="{random.uniform(1,2)}" x="{val["x"]}" y="{val["x"]}" rx="0.5" ry="0.5" transform="matrix(0.75,0,0,0.75, {random.uniform(0,85)}, {random.uniform(0,85)})" />'

    # Lines pattern
    nums = [0]*50
    r = list(map((lambda x: {'x': random.uniform(
        0, 100), 'y': random.uniform(0, 100)}), nums))
    lines = ''
    for val in r:
        lines += f'<rect width="90" height="0.5" x="{val["x"]}" y="{val["x"]}" rx="0.5" ry="0.5" transform="matrix(0.75,0,0,0.75, {random.uniform(-40,45)}, {random.uniform(0,95)})" />'

    # Dash pattern
    nums = [0]*150
    r = list(map((lambda x: {'x': random.uniform(
        0, 100), 'y': random.uniform(0, 100)}), nums))
    dash = ''
    for val in r:
        dash += f'<rect width="3" height="0.5" x="{val["x"]}" y="{val["x"]}" rx="0.5" ry="0.5" transform="matrix(0.75,0,0,0.75, {random.uniform(-40,45)}, {random.uniform(0,95)})" />'

    offsetRandom = math.floor(random.uniform(-8, 8))
    if style == "soft":
        return f'<defs><clipPath id="cutbody" transform = "translate({offsetRandom}, 0)"><path d="{blob}" /></clipPath></defs> <path style="filter:blur(1px)" stroke="#fff" stroke-width="1" fill = "none" d="{blob}" /><path stroke="transparent" stroke-width="0" fill = "{color}" d="{blob}" /> <path transform = " translate({-offsetRandom}, 0) scale(1)" stroke="#fff" stroke-width="1" fill = "rgba(255,255,255,0.3)" clip-path="url(#cutbody)" d="{blob}" style="filter:blur(2px)"/> <path style="filter:blur(1px)" stroke="#fff" stroke-width="1" fill = "none" d="{blob}" />'
    elif style == "thin":
        offsetRandom = math.floor(random.uniform(-6, 6))
        return f'<defs> <pattern fill="{color}" id="pattern-lines" x="0" y="0" width="150%" height="150%" patternUnits="userSpaceOnUse" patternContentUnits="userSpaceOnUse"> {lines} </pattern> <pattern fill="{colorDarker}" id="pattern-dash" x="0" y="0" width="150%" height="150%" patternUnits="userSpaceOnUse" patternContentUnits="userSpaceOnUse"> {dash} </pattern> <clipPath id="cutbody" transform = "translate({offsetRandom}, 0)"><path d="{blob}" /></clipPath></defs> <path style="filter:blur(1px)" stroke="#fff" stroke-width="1" fill = "none" d="{blob}" /> <path stroke="transparent" stroke-width="0" fill="{colorLightDark}" d="{blob}" /> <path stroke="transparent" stroke-width="0" fill="url(#pattern-lines)" d="{blob}" /> <path transform = " translate({-offsetRandom}, 0)" stroke="none" stroke-width="1" fill = "{color}" clip-path="url(#cutbody)" d="{blob}"/> <path stroke="{colorDarker}" stroke-width="1" fill = "none" d="{blob}" /><path stroke="none" stroke-width="1" fill="url(#pattern-dash)" d="{blob}" /> <path transform="scale(0.8) translate({12-offsetRandom}, 12)" stroke="none" stroke-width="1" fill = "{colorLight}" d="{blob}" />'
    elif style == "classic":
        return f'<path stroke="transparent" stroke-width="0" fill = "{color}" d="{blob}" /> <path transform="translate(-3, -3)" stroke="#333" stroke-width="2" fill = "none" d="{blob}" />'
    elif style == "border":
        return f'<defs><clipPath id="cutshadow" transform = "translate(15, -20)"><path d="{blob}" /></clipPath> <clipPath id="cutshadow1" transform = "translate(-60, -10)"><path d="{blob}" /></clipPath> <pattern fill="#333" id="pattern-circles" x="0" y="0" width="150%" height="150%" patternUnits="userSpaceOnUse" patternContentUnits="userSpaceOnUse"> {circles} </pattern> </defs> <path stroke="#fff" stroke-width="1" fill = "{color}" d="{blob}" /> <path transform = " translate(-15, 20)" stroke="none" stroke-width="1" fill = "{colorLightest}" clip-path="url(#cutshadow)" d="{shadowBlob}" /><path transform = " translate(60, 10)" stroke="none" stroke-width="1" fill = "{colorLightest}" clip-path="url(#cutshadow1)" d="{shadowBlob1}" /><path stroke="transparent" stroke-width="0" fill = "url(#pattern-circles)"  d="{blob}" /><path stroke="#000" stroke-width="1" fill = "none" d="{blob}" />'


def generateCharacter():

    # Create blob and eyes with random values
    blobPoints = createPoints(round(random.uniform(95, 105)), round(
        random.uniform(4, 7)), round(random.uniform(8, 10)))
    blob = createSvgPath(blobPoints)

    # Numbers corresponding to RGB values of various colors
    colors = [[252, 161, 178], [120, 193, 232], [225, 215, 193],
              [147, 67, 144], [150, 228, 151], [107, 122, 161]]

    # Numbers corresponding to HSL values of various colors
    #colors = [ [11,31,72], [41, 34, 82], [201, 71, 69], [349, 94, 81], [112, 30, 75], [121, 59, 74], [302, 37, 42]]

    # Random indices for the blob and background color
    randColorIndex = math.floor(random.random() * len(colors))
    randBgIndex = math.floor(random.random() * len(bgColors))
    col = colors[randColorIndex]
    color = f'rgb({col[0]},{col[1]},{col[2]})'
    colorLight = f'rgb({col[0]+6},{col[1]+6},{col[2]+6})'
    colorLightest = f'rgb({col[0]*1.1},{col[1]*1.1},{col[2]*1.1})'
    colorDark = f'rgb({col[0]-2},{col[1]-2},{col[2]-2})'
    colorDarker = f'rgb({col[0]-col[0]/6},{col[1]-col[1]/6},{col[2]-col[2]/6})'
    colorLightDark = f'rgb({col[0]-10},{col[1]-10},{col[2]-10})'

    # Select style
    style = 'classic'

    # Random mouth size
    widthRandom = random.uniform(8, 22)

    # Create body parts
    mouth = createMouth(widthRandom, colorDark, colorDarker, style)
    eyes = createEyes(round(random.uniform(6, 10)), colorDark, style)
    blush = createBlush(colorDarker, style)
    body = createBody(blob, color, colorLight, colorLightest,
                      colorDark, colorDarker, colorLightDark, style)
    header = f'<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" width="400" height="400">\n'
    footer = f'</svg>'
    background = f'<rect x="0" y="0" width="100" height="100" fill="{bgColors[randBgIndex]}"/>'

    # Join parts together
    #fullCharacter = header + background + body + blush + stroke + mouth + eyes + footer
    fullCharacter = header + body + blush + eyes + mouth + footer

    return fullCharacter
