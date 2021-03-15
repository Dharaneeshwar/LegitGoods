userid_form = document.getElementById("id_userid")
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
  
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  firebase.auth().onAuthStateChanged((firebaseUser) => {
    if (firebaseUser) {
      console.log("user : ", firebaseUser.uid);
      const uid = firebaseUser.uid;
      userid_form.value = uid; 
    } else {
      console.log("not logged in");
      window.location = "../accounts/login/";
      const uid = null;
    }
  });
