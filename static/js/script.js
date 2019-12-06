function restGet(url){
    var request = new XMLHttpRequest();
    // Open a new connection, using the GET request on the URL endpoint
    request.open('GET', url, true)

    request.onload = function () {
    // Begin accessing JSON data here
    }

    // Send request
    request.send()
}

function update(jscolor) {
    // 'jscolor' instance can be used as a string
    console.log(jscolor)
    // document.getElementById('rect').style.backgroundColor = '#' + jscolor
    restGet('/x/hyperion_sendcolor?color='+jscolor)
}

document.getElementById("rpi_reboot").onclick = function(){ restGet('/x/reboot_rpi' )}
document.getElementById("rpi_poweroff").onclick = function(){ restGet('/x/poweroff_rpi' )}
document.getElementById("hyperion_start").onclick = function(){ restGet('/x/start_hyperion' )}
document.getElementById("hyperion_restart").onclick = function(){ restGet('/x/restart_hyperion' )}
document.getElementById("hyperion_stop").onclick = function(){ restGet('/x/stop_hyperion' )}
document.getElementById("hyperion_interactive").onclick = function(){ restGet('/x/hyperion_interactive' )}
document.getElementById("kodi_start").onclick = function(){ restGet('/x/start_kodi' )}
document.getElementById("kodi_restart").onclick = function(){ restGet('/x/restart_kodi' )}
document.getElementById("kodi_stop").onclick = function(){ restGet('/x/stop_kodi' )}