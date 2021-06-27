<div id="login">
 <form name="loginForm" action="/acts/auth" method="POST">
  <table border="0" cellspacing="1" cellpadding="1">
   <tr>
    <td>Login</td>
    <td><input type="text" name="login" width="20"></td>
   </tr>
   <tr>
    <td>Password</td>
    <td><input type="password" name="password" width="20"></td>
   </tr>
  </table>
  <span>
   <a href="#" onClick="document.loginForm.submit();">Submit</a>&nbsp;&nbsp;
   <a href="{{data['back_url']}}">Cancel</a>
  </span>
 </form>
</div>
