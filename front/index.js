const user_list = document.querySelector('.user_list');
const loading = document.querySelector('.loading');
const token = `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg4OTMyNzczLCJpYXQiOjE2ODg4NDYzNzMsImp0aSI6IjM4ZTYzNDliOTEyODRkYzY5YzAwYWQxM2FjYTMzZDA4IiwidXNlcl9pZCI6MX0.uFsTbaA3tZ9VW2rTxz0JjzrKsuC995X8_086qPGNCOs`

const getUsers = async () => {
  let headers = new Headers();
  headers.set('Content-Type', 'application/json');
  // headers.set('Authorization', 'Basic ' + btoa("admin" + ":" + "admin"));
  headers.set('Authorization', 'Bearer ' + token);
  const response = await fetch(
    'http://localhost:8000/api/users/', {
    method: 'GET',
    headers
  }

  );
  const users = await response.json();
  console.log(users);
  return users;
}

const list_users = async () => {
  const users = await getUsers()
  loading.style.display = 'block';
  users.forEach(user => {
    const li = document.createElement('li');
    const email = user.email != "" && user.email != null ? user.email : 'Sem e-mail'
    li.innerHTML += user.username + ' - ' + email
    user_list.appendChild(li)
  });
  loading.style.display = 'none';
}

window.onload = () => { list_users() }