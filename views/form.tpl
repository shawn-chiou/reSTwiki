<html>

<head>
 <title>reSTWiki - {{data['action']}} - {{data['title']}}</title>
 <meta http-equiv="content-type" content="text/html; charset=UTF-8">
 <script type="text/javascript" src="/js/jquery.js"></script>
 <script type="text/javascript" src="js/jquery.blockUI.js"></script>
 <script type="text/javascript" src="/js/reSTwiki.js"></script>
 <link type="text/css" rel="stylesheet" href="/css/style.css">
 <script>
<!--
function resize() {
	$("#editarea").css("height", $("#content").height() - 60);
	$("#editarea").css("width", $("#content").width());
}

window.onload = function() {
	resize();
}
//-->>
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
   <!--
   <ul>
    <li><a href="/acts/edit/{{data['title']}}">Edit</a></li>
   </ul>
   -->
  </div>
  <div id="content">
   <span id="form-title">{{data['action']}}ing {{data['title']}}</span>
   <form name="contentForm" action="/acts/save/{{data['title']}}" method="post">
    <textarea id="editarea" name="content">{{data['content']}}</textarea>
   </form>
   <ul id="form-acts">
    <li><a href="#" onClick="document.contentForm.submit()">Submit</a></li>
    <li><a href="{{data['back_url']}}">Cancel</a></li>
   </ul>
  </div>
 </div>
</div>

%include footer

</center>

</body>

</html>
