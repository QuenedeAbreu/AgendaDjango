const user_list = document.querySelector('.user_list');
const loading = document.querySelector('.loading');

const getUsers = async () => {
  let headers = new Headers();
  headers.set('Content-Type', 'application/json');
  headers.set('Authorization', 'Basic ' + btoa("admin" + ":" + "admin"));
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