function checkPasswords(){
  var pass1 = document.getElementById("pass1").value;
  var pass2 = document.getElementById("pass2").value;
  if(pass1 != pass2){
    document.getElementById('pass1').style.borderColor = "#34234";
    document.getElementById('pass2').style.borderColor = "#34234";
    ok = false;
  }
  else {
    alert("Passwords match");
  }
  return ok;
}
