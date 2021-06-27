<html>

<head>
 <title>reSTWiki - {{data['title']}}</title>
 <meta http-equiv="content-type" content="text/html; charset=UTF-8">
 <link type="text/css" rel="stylesheet" href="css/style.css">
 <script type="text/javascript" src="js/jquery.js"></script>
 <script type="text/javascript" src="js/jquery.blockUI.js"></script>
 <script type="text/javascript" src="js/reSTwiki.js"></script>
 <script>
<!--
function resize() {
	if ($("#content span").height() > $("#content").height()) {
		$("#main").css("height", $("#content span").height() + $("#top-menu").height() + 15);
		$("#right").css("height", $("#content span").height() + $("#top-menu").height() + 15);
		$("#content").css("height", $("#content span").height());
	}
}

$(document).ready(function() {
	$('#loginpoint').click(function() {
		$.blockUI({ message: $('#logindialog') });
	});

	$('#submit4login').click(function() {
		$.blockUI({ message: "<h1>Please wait...</h1>" });

		$.post(
			'/acts/auth',
			{ login: $('#userLogin').attr('value'), password: $('#userPassword').attr('value') },
			function(data) {
				/*
				$.blockUI({ message: data });
				alert(data);
				if (!data) {
					alert('Failed, ' + data); 
				} else {
					alert('Success, ' + data); 
				}
				*/

				$.unblockUI();
				return false;
			}
		);
	});

	$('#cancel4login').click(function() {
		$.unblockUI();
		return false;
	});
});

window.onload = function() {
	resize();
}
//-->
 </script>
</head>

<body>

<center>

%include header

<div id="main">
 <div id="left-pannel">
  %include pannel data = data
 </div>

 <div id="right">
  <div id="top-menu">
   <ul>
    <li><a id="editpage" href="/acts/edit/{{data['title']}}">Edit</a></li>
   </ul>
  </div>
  <div id="content"><span>{{!data['content']}}</span></div>
 </div>
</div>

%include footer

</center>

</body>

</html>
