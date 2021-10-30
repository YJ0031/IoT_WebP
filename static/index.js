function onoff() {
    'use strict';
    var XHR = new XMLHttpRequest();
    XHR.onreadystatechange = function () {
        if (XHR.readyState === 4 && XHR.status === 200) {
            var response = JSON.parse(XHR.responseText);
	    document.getElementById('status').innerHTML = "Status : " + response.status;
            
        }
    };
    XHR.open('POST', '/led');
    XHR.send(null);
}
