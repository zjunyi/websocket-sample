/**
 * @author komasshu
 */

var MyWebSocket = {
	ws : null,
	heartbeat : null,
	__HEARTBEAT__ : 'heartbeat',
	yourname : '',
	init: function(){
		var that = this;
		document.getElementsByName('connect')[0].addEventListener('click', function(e){
			var resource = document.getElementsByName('resource')[0].value;
			that.yourname = document.getElementsByName('yourname')[0].value;
			
			if(resource == '' || that.yourname == '') {
				alert('Resource nor Yourname specified...');
				return;
			}
			
			that.connect(resource);
		}, false);
	},
	
	connect : function(resource) {
		if(this.ws)
			this.ws.close();
		this.ws = new WebSocket("ws://"+location.host+"/"+resource);
		
		var that = this;
		
		this.ws.onopen = function(e) {
			
			document.getElementById('board').innerHTML = '<b>connect succeed : '+resource+'</b><br/>';
			document.getElementsByName('send')[0].disabled = false;
			document.getElementsByName('message')[0].disabled = false;
			document.getElementsByName('disconnect')[0].disabled = false;
			document.getElementsByName('yourname')[0].disabled = true;
			document.getElementsByName('resource')[0].disabled = true;
			document.getElementsByName('connect')[0].disabled = true;
			that.heartbeat = setInterval(function(){
				that.send(that.__HEARTBEAT__);
			}, 60000);
		};
		
		this.ws.onmessage = function(e) {
			if(!e.data.match(/heartbeat/)) {
				var nd = document.createElement('div');
				nd.setAttribute('class', 'messbody');
				nd.innerHTML = decodeURIComponent(e.data);
				document.getElementById('board').insertBefore(nd, document.getElementById('board').firstChild);
			}
		};
		this.ws.onclose = function(e) {
			if(that.heartbeat != null) {
				clearInterval(that.heartbeat);
				that.heartbeat = null;
			}
			var nd = document.createElement('div');
			nd.innerHTML = 'closed';
			document.getElementById('board').insertBefore(nd, document.getElementById('board').firstChild);
			document.getElementsByName('send')[0].disabled = true;
			document.getElementsByName('message')[0].disabled = true;
			document.getElementsByName('disconnect')[0].disabled = true;
			document.getElementsByName('resource')[0].disabled = false;
			document.getElementsByName('connect')[0].disabled = false;
			document.getElementsByName('yourname')[0].disabled = false;
		};
		document.getElementsByName('send')[0].onclick = function(e){
			message = document.getElementsByName('message')[0].value;
			message = message.replace(/</g, "&lt;");
			message = message.replace(/>/g, "&gt;");
			message = message.replace(/(https?|ftp)(:\/\/[-_.!~*\'()a-zA-Z0-9;\/?:\@&=+\$,%#]+)$/mg, "<a href='$&' target='_blank'>$&</a>");
			message = message.replace(/\n|\r\n|\r/g, "<br/>");
			that.send(message);
		};
		document.getElementsByName('disconnect')[0].onclick = function(e){
			if(that.ws) {
				that.ws.close();
			}
		};
		
	},
	
	send: function(message){
		if(typeof(message) == 'undefined' || message =='') {
			alert('not found Message...');
			return;
		}
		this.ws.send(encodeURIComponent(this.yourname+" : "+message));
		document.getElementsByName('message')[0].value = '';
	},

	close: function(){
		if(this.ws) ws.close();
	}
};

window.addEventListener('load', function(e){
	MyWebSocket.init();
}, false);

window.addEventListener('unload', function(e){
	MyWebSocket.close();
}, false); 
