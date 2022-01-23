if (document.getElementById("qr-canvas")) {
  var _qrcode = window.qrcode;

  var video = document.createElement("video");
  var canvasElement = document.getElementById("qr-canvas");
  var canvas = canvasElement.getContext("2d");

  var qrResult = document.getElementById("qr-result");
  var outputData = document.getElementById("outputData");
  var btnScanQR = document.getElementById("btn-scan-qr");
  var btnScanClose = document.getElementById("btn-scan-close");
  var btnSubmitLog = document.getElementById("btn-log-data");

  var user_id = 0;
  var user_name = "";
  var user_address = "";
  var user_phone = "";

  var location_id = 0;
  var location_name = "";
  var location_address = "";
  var location_phone = "";

  var scanning = false;

  $(document).ready(function () {
    btnSubmitLog.hidden = true;
  });

  _qrcode.callback = (res) => {
    if (res) {
      /* Fetch User Data */

      var user_type = document.getElementById("user_type").value;

      $.get(
        "/trace/fetch/" + res + "/?auth_token=bUb0uCjBTk8RAyQMRvVNYOxB8AdxDVxh",
        function (data) {
          var userData = data["user"];

          // console.log(userData);

          if (user_type == "USER") {
            user_uuid = document.getElementById("user_uuid").value;
            user_name =
              document.getElementById("user_first_name").value +
              " " +
              document.getElementById("user_last_name").value[0] +
              ".";
            user_address = document.getElementById("user_address").value;
            user_phone = document.getElementById("user_phone").value;

            location_uuid = userData["uuid"];
            location_name =
              userData["first_name"] + " " + userData["last_name"];
            location_address = userData["address"];
            location_phone = userData["phone"];
          }

          if (user_type == "LOCATION") {
            location_uuid = document.getElementById("user_uuid").value;
            location_name =
              document.getElementById("user_first_name").value +
              " " +
              document.getElementById("user_last_name").value;
            location_address = document.getElementById("user_address").value;
            location_phone = document.getElementById("user_phone").value;

            user_uuid = userData["uuid"];
            user_name =
              userData["first_name"] + " " + userData["last_name"][0] + ".";
            user_address = userData["address"];
            user_phone = userData["phone"];
          }

          var user_html =
            "<hr/><strong>USER: " +
            user_name +
            "</strong><hr/><br/>Address: " +
            user_address +
            "<br/>Phone: " +
            user_phone;
          var location_html =
            "<br/><br/><hr/><strong>LOCATION: " +
            location_name +
            "</strong><hr/><br/>Address: " +
            location_address +
            "<br/>Phone: " +
            location_phone;

          outputData.innerHTML = user_html + location_html;
          scanning = false;

          video.srcObject.getTracks().forEach((track) => {
            track.stop();
          });

          qrResult.hidden = false;
          canvasElement.hidden = true;
          btnScanQR.hidden = true;
          btnSubmitLog.hidden = false;
        }
      );
    }
  };

  btnSubmitLog.onclick = () => {
    var temperature = document.getElementById("temperature").value;
    var csrfmiddlewaretoken = $("input[name=csrfmiddlewaretoken]").val();
    /* Save Custom Content  */
    console.log("Save");
    $.ajax({
      type: "POST",
      url: "/trace/log/" + user_uuid + "/",
      data: {
        auth_token: "bUb0uCjBTk8RAyQMRvVNYOxB8AdxDVxh",
        csrfmiddlewaretoken: csrfmiddlewaretoken,
        location_uuid: location_uuid,
        temperature: temperature,
      },
      success: function (data) {
        location.reload();

        if (data["error"]) {
          alert(data["error"]);
          location.reload();
        }
      },
    });
  };

  btnScanQR.onclick = () => {
    video.setAttribute("autoplay", "");
    video.setAttribute("muted", "");
    video.setAttribute("playsinline", "");
    var constraints = {
      audio: false,
      video: {
        facingMode: "environment",
      },
    };
    console.log("Start video");
    navigator.mediaDevices
      .getUserMedia(constraints)
      .then(function success(stream) {
        scanning = true;
        qrResult.hidden = true;
        btnScanQR.hidden = true;
        canvasElement.hidden = false;
        video.srcObject = stream;
        video.setAttribute("playsinline", true); // required to tell iOS safari we don't want fullscreen
        video.play();
        tick();
        scan();
      });
  };

  btnScanClose.onclick = () => {
    video.setAttribute("autoplay", "");
    video.setAttribute("muted", "");
    video.setAttribute("playsinline", "");
    var constraints = {
      audio: false,
      video: {
        facingMode: "environment",
      },
    };
    console.log("Stop video");
    navigator.mediaDevices.getUserMedia(constraints).then(function (stream) {
      scanning = false;
      qrResult.hidden = true;
      btnScanQR.hidden = false;
      canvasElement.hidden = true;
      stream.getTracks().forEach(function (track) {
        track.stop();
      });
    });
  };

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
