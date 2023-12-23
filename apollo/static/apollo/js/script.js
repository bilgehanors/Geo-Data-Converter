function calculateNewTime() {
    var date = document.getElementById('dateInput').value;
    var second = document.getElementById('secondsInput').value;
    
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/new_time/", true);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.send(JSON.stringify({datum: date, sec: second }));

    xhr.onload = function () {
        if (xhr.status === 200) {
            var resultContainer = document.getElementById("resultOutput");
            resultContainer.innerHTML = xhr.responseText;
        } else {
            console.error("Error:", xhr.statusText);
        }
    };
}
function calculateNewCoordinates() {
    var xcord = document.getElementById('xInitial').value;
    var ycord = document.getElementById('yInitial').value;
    var zcord  = document.getElementById('zInitial').value;
    var x_rot = document.getElementById('xRotation').value;
    var y_rot = document.getElementById('yRotation').value;
    var z_rot = document.getElementById('zRotation').value;
    
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/new_coordinate/", true);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.send(JSON.stringify({x: xcord, y: ycord, z: zcord, rotx: x_rot, roty: y_rot, rotz: z_rot }));

    xhr.onload = function () {
        if (xhr.status === 200) {
            var resultContainer = document.getElementById("resultOutputc");
            resultContainer.innerHTML = xhr.responseText;
        } else {
            console.error("Error:", xhr.statusText);
        }
    };
}
function convertCoordinates() {
    var xcord = document.getElementById('x').value;
    var ycord = document.getElementById('y').value;
    var zcord  = document.getElementById('z').value;
    var precision = document.getElementById('precision').value;
    var ellipsoid = document.getElementById('ellipsoid').value;

    
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/ellipsoid/", true);
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.send(JSON.stringify({x: xcord, y: ycord, z: zcord, precision: precision, ellipsoid: ellipsoid}));

    xhr.onload = function () {
        if (xhr.status === 200) {
            var resultContainer = document.getElementById("resultOutpute");
            resultContainer.innerHTML = xhr.responseText;
        } else {
            console.error("Error:", xhr.statusText);
        }
    };
}


