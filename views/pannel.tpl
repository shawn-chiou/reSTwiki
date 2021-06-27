<div id="mainmenu">
 <ul>
  <li>\\
%if 'user_name' in data and data['user_name'] != None:
  {{data['user_name']}}, <a href="#">Logout</a>\\
%else:
  <a id="loginpoint" href="#">Login</a>\\
%end
  </li>
  <li><a href="/">Home</a></li>
  <!--
  <li><a href="/pref">Preference</a></li>
  -->
  <li><a href="/help">Help</a></li>
 </ul>
</div>
<div id="logindialog" style="display: none; cursor: default; text-align: left;">
 <h2>Please login!</h2>
 <center>
 <form name="loginForm" action="/acts/auth" method="POST">
  <table border="0" cellspacing="0" cellpadding="1">
   <tr>
    <td>Login</td>
    <td><input type="text" id="userLogin" name="login" width="30"></td>
   </tr>
   <tr>
    <td>Password</td>
    <td><input type="password" id="userPassword" name="password" width="30"></td>
   </tr>
   <tr>
    <td align="center" colspan="2">
     <input type="button" id="submit4login" value="Submit">
     <input type="button" id="cancel4login" value="Cancel">
    </td>
   </tr>
  </table>
 </form>
 </center>
</div>
