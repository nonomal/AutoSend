/*
From: https://gist.github.com/Armster15/719a4849f6c028f66f46b5550d863e81
*/


// This creates the function
function getToken() {
    let popup;
    popup = window.open('', '', `top=0,left=${screen.width-800},width=850,height=${screen.height}`);
    if(!popup || !popup.document || !popup.document.write) return alert('Popup blocked! Please allow popups and after you do so, rerun the code');
    
    window.dispatchEvent(new Event('beforeunload'));
    token = popup.localStorage.token
    token = token.slice(1, -1); // Gets rid of the quotes

    popup.document.write(`
    <!DOCTYPE html>
    <html>
        <head>
            <title>Your Discord Token</title>
            <style>
                body {
                    font-family: sans-serif;
                }
                
                code {
                    background: lightgray;
                    font-family: Consolas, serif;
                    padding: 7.5px;
                    border-radius: 7.5px;
                    margin-right: 5px;
                }
    
                .warning {
                    background: yellow;
                    border: 5px solid red;
                    padding: 7.5px;
                    margin-top: 40px;
                }

                button {
                    padding: 6px;
                }

                .noselect {
                	-webkit-user-select: none;
					-khtml-user-select: none;
					-moz-user-select: none;
					-ms-user-select: none;
					-o-user-select: none;
					user-select: none;
                }
            </style>
        </head>
        <body>
            <h1>Your Discord Token</h1>
            <code id="token_p"></code>
            <button class="noselect" id="button_1">Show</button>
            <button class="noselect" id="copy">Copy</button>
            <h2 class="warning">DO NOT SHARE THIS WITH ANYONE, IF SOMEONE OBTAINS THIS THEY CAN ACCESS YOUR ENTIRE DISCORD</h2>
        </body>
    </html>
    `)

    function censor(string) {
        var censored = ""
        for(var i = 0; i < string.length; i++) {
            censored = censored + "*";
        }
        return censored
    }

    // SHOW/HIDE BUTTON CODE
    popup.document.getElementById('token_p').innerHTML = censor(token);
    var btn = popup.document.getElementById("button_1");
    btn.addEventListener('click', onBtnClick);

    function onBtnClick(){
        var token_p = popup.document.getElementById("token_p");
        if(btn.innerHTML.toLowerCase() == "hide") {
            btn.innerHTML = "Show";
            token_p.innerHTML = censor(token_p.innerHTML);
        }

        else if(btn.innerHTML.toLowerCase() == "show") {
            btn.innerHTML = "Hide";
            token_p.innerHTML = token;
        }
    }

    // COPY BUTTON CODE
    var copyButton = popup.document.getElementById("copy");
    copyButton.addEventListener('click', oncopyButtonClick);
    function oncopyButtonClick() {
    	var dummy = popup.document.createElement("textarea");
	    popup.document.body.appendChild(dummy);
	    dummy.value = token;
	    dummy.select();
	    popup.document.execCommand("copy");
	    popup.document.body.removeChild(dummy);

  	    popup.alert("Successfully copied your Discord token!")
    }

}		


// Now to actually run the function
getToken()
