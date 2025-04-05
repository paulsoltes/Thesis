document.getElementById('loginForm').addEventListener('submit', function(event) {
  event.preventDefault();
  
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  // Default Dean account
  const deanAccount = { username: 'dean', password: 'admin123' };

  if (username === deanAccount.username && password === deanAccount.password) {
      localStorage.setItem('userRole', 'dean');
      window.location.href = 'dashboard.html'; // Redirect to admin schedule page
  } else if (username && password) {
      localStorage.setItem('userRole', 'user');
      window.location.href = 'dashboard.html'; // Regular users go to standard timetable
  } else {
      alert('Please enter both username and password.');
  }
});
