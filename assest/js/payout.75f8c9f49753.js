var error = document.getElementById("error");
error.style.visibility = "hidden";
var payout_limit = 0;
// TODO set user id in form

var firebaseConfig = {
  apiKey: "AIzaSyA47T1dM4C7nZaczOEkt_O1KcazxIZsAaw",
  authDomain: "legit-goods.firebaseapp.com",
  databaseURL: "https://legit-goods.firebaseio.com",
  projectId: "legit-goods",
  storageBucket: "legit-goods.appspot.com",
  messagingSenderId: "948613007995",
  appId: "1:948613007995:web:fd801774c6eff66e71f0de",
};
var uid = "";
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.auth().onAuthStateChanged((firebaseUser) => {
  if (firebaseUser) {
    console.log("user : ", firebaseUser.uid);
    uid = firebaseUser.uid;
    var data = {
      uid: uid,
    };
    $.ajax({
      type: "Get",
      url: window.location.origin + "/api/getPayoutAmount/",
      data: data,
      success: function (value) {
        payout_limit = value.amount;
        document.getElementById('available_amount').innerText = "₹"+payout_limit;
      },
    });
  } else {
    console.log("not logged in");
    const uid = null;
  }
});

function applypayout() {
  var amount = document.getElementById("amount").value;
  if (amount >= payout_limit) {
    error.style.visibility = "visible";
  } else {
    error.style.visibility = "hidden";
    var data = {
        'uid' : uid,
        "amount" : amount
      };
    $.ajax({
        type: "Get",
        url: window.location.origin + "/api/requestpayout/",
        data: data,
        success: function (value) {
          console.log(value);  
          form = document.getElementById('form');
          form.innerHTML = `<h3 class="text-center mt-5 pt-5">Request has been successfully submitted!</h3>
          <button class="d-block mx-auto btn btn-primary py-2 mt-5" onclick="gotohome()">Go To Home</button>`
        },
      });
  }
}

function gotohome() {
    window.location = "../../";
}