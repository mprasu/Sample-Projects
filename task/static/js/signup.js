function nameValidation(inputTxt){
		var regex=/^[a-zA-z]+$/;
		var textField=document.getElementById('textField')
		if(inputTxt.value!="" ){
			if(inputTxt.value.length>=5 && inputTxt.value.length<=20){
				if(inputTxt.value.match(regex)){
					textField.textContent="its valid";
					textField.style.color='green';
				}else{
					textField.textContent="invalid input: only letters and white space";
					textField.style.color='red';
				}
			}else{
				textField.textContent="your input should be greater than 5 characters and lesser than 20";
				textField.style.color='red';
			}
		}else{
			textField.textContent="empty input";
			textField.style.color='red';
		}
	}
function ageValidation(inputTxt){
	var regex=/^[0-9]+$/;
		var textField=document.getElementById('ageField')
		if(inputTxt.value!="" ){
			if(inputTxt.value <=120){
				if(inputTxt.value.match(regex)){
					ageField.textContent="its valid";
					ageField.style.color='green';
				}else{
					ageField.textContent="invalid input: only numbers";
					ageField.style.color='red';
				}
			}else{
				ageField.textContent="invalid input";
				ageField.style.color='red';
			}
		}else{
			ageField.textContent="empty input";
			ageField.style.color='red';
		}
	}
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

function validatePassword() {
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
function phonenumberValidate(){
	var Phonenumber=document.getElementById('Phonenumber').value;
	var PhonenumberId=document.getElementById('PhonenumberId')
	if(Phonenumber.length==8 || Phonenumber.length==10){
		PhonenumberId.textContent="valid"
		PhonenumberId.style.color="green"
	}else{
		PhonenumberId.textContent="Invalid number"
		PhonenumberId.style.color="red"
	}
}
function locationValidate(inputTxt){
	var alphaRegex=/^[a-zA-Z]+$/
	var LocationId=document.getElementById('LocationId')
	if(inputTxt.value.match(alphaRegex)){
		LocationId.textContent="valid"
		LocationId.style.color="green"
	}else{
		LocationId.textContent="only alphabits  are allowed"
		LocationId.style.color="red"

	}
}
function stateValidate(inputTxt){
	var alphaRegex=/^[a-zA-Z]+$/
	var stateId=document.getElementById('stateId')
	if(inputTxt.value.match(alphaRegex)){
		stateId.textContent="valid"
		stateId.style.color="green"
	}else{
		stateId.textContent="only alphabits  are allowed"
		stateId.style.color="red"

	}
}
function countryValidate(inputTxt){
	var alphaRegex=/^[a-zA-Z]+$/
	var countryId=document.getElementById('countryId')
	if(inputTxt.value.match(alphaRegex)){
		countryId.textContent="valid"
		countryId.style.color="green"
	}else{
		countryId.textContent="only alphabits  are allowed"
		countryId.style.color="red"

	}
}

function addressValidate(inputTxt){
	var alphaRegex=/^[a-zA-Z0-9, -]+$/
	var addressId=document.getElementById('addressId')
	if(inputTxt.value.match(alphaRegex)){
		addressId.textContent="valid"
		addressId.style.color="green"
	}else{
		addressId.textContent="special characters are not allowed"
		addressId.style.color="red"

	}
}
