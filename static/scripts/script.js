function setAudioDevice(deviceNumber) {
    if(deviceNumber !== 1 && deviceNumber !== 2) {
        return;
    }
        
    var http = new XMLHttpRequest();
    http.open("POST", '/audio_device', true);
    http.setRequestHeader("Content-Type", "application/json")
    http.onload = function(e) {
        getAudioDevice();
    }
    var data = JSON.stringify({
        "deviceNumber": deviceNumber
    })
    http.send(data)
}

function getAudioDevice() {
    var http = new XMLHttpRequest();
    http.open("GET", '/audio_device', true);
    http.onload = function(e) {
        var currentDevice = document.getElementById('currentDevice');
        currentDevice.innerText = http.response;
    };

    http.send();
}
