function validation(){
	var xz=$('#Name').val();
			console.log(xz);
	var Name=document.getElementById('Name').value;
	var regex = /^[0-9a-zA-Z]+$/
		if( Name == "" || Name.length<3 || Name.length>20){
			document.getElementById('Name1').innerHTML="**Enter valid name";
			return false;
		}

		var Age=document.getElementById('Age').value;
		var numbers = /^[0-9]+$/;
		var comp=Age.match(numbers);
		if (comp===null || Age>=110){
			document.getElementById('Age1').innerHTML="**Age must be integer";
			return false;
		}
		 var Email_id=document.getElementById('Email_id').value;
		if(Email_id.indexOf('@')<=0 || (Email_id.charAt(Email_id.length-4))!='.' && (Email_id.charAt(Email_id.length-3)!='.')){
			document.getElementById('Email_id1').innerHTML="**enter valid mail"
		}
		var Password=document.getElementById('Password').value;
		if(Password.length <8 || Password.length >20){
			document.getElementById('Password1').innerHTML="**password length should be minimum 8 ";
			return false;
		}
		var ConfirmPassword=document.getElementById('ConfirmPassword').value;

		if(Password!=ConfirmPassword){
			document.getElementById('ConfirmPassword1').innerHTML="**password and confirm password dint match";
			return false;
		}

		var Phonenumber=document.getElementById('Phonenumber').value;
		var cmp=Phonenumber.match(numbers);
		if(cmp===null || Phonenumber.length != 10 || Phonenumber.length != 10){
			document.getElementById('Phonenumber1').innerHTML="**please check the number should not include character";
			return false;

		}
		else{
        // $('#exampleModalLong').modal({show: false});
        $('#exampleModalLong').modal('show');
    }


	}


