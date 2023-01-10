const formul = document.querySelector("#sign_up")

formul.addEventListener("click", function(e)
{
    e.preventDefault();

    // variáveis recebem os dados inseridos no form do html

    const name = document.querySelector("#your_full_name").value;
    const username = document.querySelector("#your_username").value;
    const email = document.querySelector("#your_email").value;
    const password = document.querySelector("#your_password").value;
    const confirm = document.querySelector("#confirm_your_password").value;

    var cadastro = {

        name: name,
        username: username,
        email:email,
        password:password,
        confirm:confirm,

        get name(){
            return name;
        },

        get username(){
            return username;
        },

        get email(){
            return email;
        },

        get password(){
            return password;
        },

        get confirm(){
            return confirm;
        }
    }

console.log(cadastro.name);
console.log(cadastro.username);
console.log(cadastro.email),
console.log(cadastro.password),
console.log(console.confirm);
});