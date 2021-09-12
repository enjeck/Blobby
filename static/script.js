
// New Character on page load
getCharacter() 

 // Click buttons to generate new characters or download
document.getElementById("new").addEventListener("click", function() {
  getCharacter();
})
document.querySelector(".download-svg").addEventListener("click", function() {
  download('svg');
})
document.querySelector(".download-png").addEventListener("click", function() {
  download('png');
})


function getCharacter() {
 async function postChar(url = '', data = {}) {
  const response = await fetch(url, {
    method: 'POST',
    mode: 'cors',
    cache: 'no-cache', 
    credentials: 'same-origin', 
    headers: {
      'Content-Type': 'application/json'
    },
    redirect: 'follow',
    referrerPolicy: 'no-referrer', 
  });
  let svg = response.json();
  return svg
}

postChar('/character')
  .then(data => {
    let svgData = data.svg
    let svgContainer = document.getElementById("svg-box");
    svgContainer.innerHTML = svgData;
  });
}

function download(type) {
let svgContainer = document.getElementById("svg-box");
let svgToConvert = {
  svgCode: svgContainer.innerHTML,
  type: type
}
 async function postPNG(url = '', data = {}) {
  const response = await fetch(url, {
    method: 'POST',
    mode: 'cors',
    cache: 'no-cache', 
    credentials: 'same-origin', 
    headers: {
      'Content-Type': 'application/json'
    },
    redirect: 'follow',
    referrerPolicy: 'no-referrer', 
    body: JSON.stringify(data)
  });
  let pngData = response;
  return pngData
}

postPNG('/download', svgToConvert)
     .then(response => response.blob())
        .then(blob => {
            var url = window.URL.createObjectURL(blob);
            var a = document.getElementById("download-text");
            a.href = url;
            a.download = `blobby.${type}`; 
            a.click()   
        });
}



