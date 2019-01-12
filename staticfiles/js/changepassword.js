

function emailValidation(){
	var emailTextBox=document.getElementById('emailField');
	var email=emailTextBox.value;
	var emailId=document.getElementById('emailId')
	var emailRegEx=/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	

	if (emailRegEx.test(email)){
		emailId.textContent="valid"
		emailId.style.color="green";
	}
	else{
		emailId.textContent="not valid"
		emailId.style.color="red";
	}
}

function validatePassword(inputTxt) {
    var Password = document.getElementById('passwordField')
    var mypassword=Password.value;
    var regularExpression  = /^[a-zA-Z0-9!@#$%^&*]{6,16}$/;
    var passwordId=document.getElementById('passwordId')

    
    if(!regularExpression.test(mypassword)) {
        passwordId.textContent="password is not strong";
        passwordId.style.color="red"
    }
    else{
    	passwordId.textContent="password is valid";
        passwordId.style.color="green"


    }
}
function confirmPasswordValidate(inputTxt){
	var Password = document.getElementById('passwordField').value;
	var confirmPasswordField=document.getElementById('confirmPasswordField').value;
	var confirmPasswordId=document.getElementById('confirmPasswordId')
	if(Password!=confirmPasswordField ){
		confirmPasswordId.textContent="password dint matched"
		confirmPasswordId.style.color="red"
	}
	else{
		confirmPasswordId.textContent="password matched"
		confirmPasswordId.style.color="green"
	}

}
