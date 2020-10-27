// Your web app's Firebase configuration
var firebaseConfig = {
  apiKey: "AIzaSyA47T1dM4C7nZaczOEkt_O1KcazxIZsAaw",
  authDomain: "legit-goods.firebaseapp.com",
  databaseURL: "https://legit-goods.firebaseio.com",
  projectId: "legit-goods",
  storageBucket: "legit-goods.appspot.com",
  messagingSenderId: "948613007995",
  appId: "1:948613007995:web:fd801774c6eff66e71f0de",
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.auth().onAuthStateChanged((firebaseUser) => {
  if (firebaseUser) {
    console.log("user : ", firebaseUser.uid);
  } else {
    console.log("not logged in");
    window.location = "./accounts/login/";
  }
});

const uid = firebaseUser.uid;


function getCSRFToken() {
  var cookieValue = null;
  if (document.cookie && document.cookie != "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      if (cookie.substring(0, 10) == "csrftoken" + "=") {
        cookieValue = decodeURIComponent(cookie.substring(10));
        break;
      }
    }
  }
  return cookieValue;
}
var data = {
  csrfmiddlewaretoken: getCSRFToken()
}
$.ajax({
  type: "POST",
  url: window.location.origin+"/api/allquestions/",
  data: data,
  success: function (value) {
    console.log(value);
    location.reload();
  },
});