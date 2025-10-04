document.getElementById("loginForm").addEventListener("submit", function(e) {
  e.preventDefault(); // Ngăn submit thật

  const username = document.getElementById("username").value.trim();
  const password = document.getElementById("password").value.trim();

  if (username === "" || password === "") {
    alert("Vui lòng nhập Username và Password!");
    return;
  }

  if (password.length < 6) {
    alert("Password phải có ít nhất 6 ký tự!");
    return;
  }

  alert("Đăng nhập thành công!\nUsername: " + username);
});

document.getElementById("cancelBtn").addEventListener("click", function() {
  document.getElementById("username").value = "";
  document.getElementById("password").value = "";
  document.getElementById("remember").checked = false;
});
