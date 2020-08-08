  if(document.getElementById("qr-canvas")) {


    const _qrcode = window.qrcode;

    const video = document.createElement("video");
    const canvasElement = document.getElementById("qr-canvas");
    const canvas = canvasElement.getContext("2d");

    const qrResult = document.getElementById("qr-result");
    const outputData = document.getElementById("outputData");
    const btnScanQR = document.getElementById("btn-scan-qr");
    const btnScanClose = document.getElementById("btn-scan-close");
    const btnSubmitLog = document.getElementById("btn-log-data");

    var user_id = 0
    var user_name = '';
    var user_address = '';
    var user_phone = '';

    var location_id = 0;
    var location_name = '';
    var location_address = '';
    var location_phone = '';

    var temperature = '36.7';

    let scanning = false;

    _qrcode.callback = res => {
      if (res) {        
        /* Fetch User Data */

        var user_type = document.getElementById("user_type").value;

        $.get( "/trace/fetch/" + res + "/?auth_token=bUb0uCjBTk8RAyQMRvVNYOxB8AdxDVxh", function( data ) {
            var userData = JSON.parse(data['user']);

            // console.log(userData);            

            if(user_type == "USER") {
              user_id = document.getElementById("user_id").value;
              user_name = document.getElementById("user_first_name").value + " " + document.getElementById("user_last_name").value;
              user_address = document.getElementById("user_address").value;
              user_phone = document.getElementById("user_phone").value;

              location_id = userData[0]['pk'];
              location_name = userData[0]['fields']['first_name'] + " " + userData[0]['fields']['last_name'];
              location_address = userData[0]['fields']['address'];
              location_phone = userData[0]['fields']['phone'];
            }

            if(user_type == "LOCATION") {
              location_id = document.getElementById("user_id").value;
              location_name = document.getElementById("user_first_name").value + " " + document.getElementById("user_last_name").value;
              location_address = document.getElementById("user_address").value;
              location_phone = document.getElementById("user_phone").value;

              user_id = userData[0];
              user_name = userData[0]['fields']['first_name'] + " " + userData[0]['fields']['last_name'];
              user_address = userData[0]['fields']['address'];
              user_phone = userData[0]['fields']['phone'];
            }

            var user_html = "<hr/><strong>USER: " + user_name + "</strong><hr/>(" + temperature + " C&deg;)<br/>Address: " + user_address + "<br/>Phone: " + user_phone; 
            var location_html = "<br/><br/><hr/><strong>LOCATION: " + location_name + "</strong><hr/><br/>Address: " + location_address + "<br/>Phone: " + location_phone; 

            outputData.innerHTML = user_html + location_html;
            scanning = false;

            video.srcObject.getTracks().forEach(track => {
              track.stop();
            });

            qrResult.hidden = false;
            canvasElement.hidden = true;
            btnScanQR.hidden = false;
        });
      }
    };

    btnSubmitLog.onclick = () => {
      var csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
      /* Save Custom Content  */
      console.log('Save');
      $.ajax({
          type: "POST",
          url: "/trace/log/" + user_id + "/",
          data: {
              'auth_token': 'bUb0uCjBTk8RAyQMRvVNYOxB8AdxDVxh',
              'csrfmiddlewaretoken': csrfmiddlewaretoken,
              'location_id': location_id,
              'temperature': temperature
          },
          success: function(data){
              location.reload();
          }
      });

    }

    btnScanQR.onclick = () => {
      console.log('Start video');
      navigator.mediaDevices
        .getUserMedia({ video: { facingMode: "environment" } })
        .then(function(stream) {
          scanning = true;
          qrResult.hidden = true;
          btnScanQR.hidden = true;
          canvasElement.hidden = false;
          video.setAttribute("playsinline", true); // required to tell iOS safari we don't want fullscreen
          video.srcObject = stream;
          video.play();
          tick(); 
          scan();
        });
    };

    btnScanClose.onclick = () => {
      console.log('Stop video')
      navigator.mediaDevices
        .getUserMedia({ video: { facingMode: "environment" } })
        .then(function(stream) {
          scanning = false;
          qrResult.hidden = true;
          btnScanQR.hidden = false;
          canvasElement.hidden = true;
          stream.getTracks().forEach(function(track) {
            track.stop();
          })
        });
    }

    function tick() {
      canvasElement.height = video.videoHeight;
      canvasElement.width = video.videoWidth;
      canvas.drawImage(video, 0, 0, canvasElement.width, canvasElement.height);

      scanning && requestAnimationFrame(tick);
    }

    function scan() {
      try {
        _qrcode.decode();
      } catch (e) {
        setTimeout(scan, 300);
      }
    }
}