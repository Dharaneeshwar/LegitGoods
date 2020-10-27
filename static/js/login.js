window.onload = function () {
    document.getElementById("pin").style.visibility = "hidden";
    document.getElementById("signinbutton").style.visibility = "hidden";
    var firebaseConfig = {
        apiKey: "AIzaSyA47T1dM4C7nZaczOEkt_O1KcazxIZsAaw",
        authDomain: "legit-goods.firebaseapp.com",
        databaseURL: "https://legit-goods.firebaseio.com",
        projectId: "legit-goods",
        storageBucket: "legit-goods.appspot.com",
        messagingSenderId: "948613007995",
        appId: "1:948613007995:web:fd801774c6eff66e71f0de"
    };
    firebase.initializeApp(firebaseConfig);
    render();
  };
  function render() {
    window.recaptchaVerifier = new firebase.auth.RecaptchaVerifier(
      "recaptcha-container"
    );
    recaptchaVerifier.render();
  }
  
  function phoneAuth() {
    var phoneNumber = document.getElementById("phno").value;
    if (phoneNumber[0] !== "+") {
      phoneNumber = "+91" + phoneNumber;
    }
    console.log(phoneNumber);
    firebase
      .auth()
      .signInWithPhoneNumber(phoneNumber, window.recaptchaVerifier)
      .then(function (confirmationResult) {
        window.confirmationResult = confirmationResult;
        coderesult = confirmationResult;
        console.log(coderesult + "Message Sent");
        document.getElementById("pin").style.visibility = "visible";
        document.getElementById("signinbutton").style.visibility = "visible";
        document.getElementById("otp").style.display = "none";
        document.getElementById("recaptcha-container").style.visibility = "hidden";
      })
      .catch(function (error) {
        console.log(error.message);
      });
  }
  
  function codeVerify() {
    var code = document.getElementById("pin").value;
    coderesult
      .confirm(code)
      .then(function (result) {
        console.log("registered");
        var user = result.user;
        window.location = "../../";
      })
      .catch(function (error) {
        console.log(error.message);
      });
  }
  