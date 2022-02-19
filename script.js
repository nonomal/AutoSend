var preview_codeblock = document.getElementById('preview_codeblock')
var example_json = {
    "AutoRoutine_1": {
        "AutoSend_1": {
            "ChannelID": "908973055605366784",
            "Sleep": "5",
            "RandomOffset": "0",
            "Send": {
                "Send_1": "hello",
                "Send_2": "how r you doing",
                "Send_3": "dayum chat is dead"
            }
        },
        "AutoSend_2": {
            "ChannelID": "908973055605366784",
            "Sleep": "5",
            "RandomOffset": "0",
            "Send": "seccond"
        },
        "AutoSend_3": {
            "ChannelID": "908973055605366784",
            "Sleep": "5",
            "RandomOffset": "0",
            "Send": "third"
        }
    },
    "AutoRoutine_2": {
        "AutoSend_1": {
            "ChannelID": "908973055605366784",
            "Sleep": "5",
            "RandomOffset": "0",
            "Send": "first2"
        },
        "AutoSend_2": {
            "ChannelID": "908973055605366784",
            "Sleep": "5",
            "RandomOffset": "0",
            "Send": "seccond2"
        },
        "AutoSend_3": {
            "ChannelID": "908973055605366784",
            "Sleep": "5",
            "RandomOffset": "0",
            "Send": "third2"
        },
        "AutoSend_4": {
            "ChannelID": "908973055605366784",
            "Sleep": "5",
            "RandomOffset": "0",
            "Send": "four2"
        }
    },
    "AutoCount": {
        "AutoSend_1": {
            "ChannelID": "908973055605366784",
            "Sleep": "5",
            "RandomOffset": "5",
            "Starting_Int": "0",
            "Interval": "1"
        },
        "AutoSend_2": {
            "ChannelID": "908973055605366784",
            "Sleep": "5",
            "RandomOffset": "5",
            "Starting_Int": "5",
            "Interval": "-2"
        }
    }
};

preview_codeblock.innerHTML = prettyPrint(example_json);
document.querySelectorAll("pre").forEach((codeblockDiv) => createCopyButton(codeblockDiv));
fix_dimensions()

////// EventListeners //////
var timeOutFunctionId;
window.addEventListener("resize", function() {
    clearTimeout(timeOutFunctionId);
    timeOutFunctionId = setTimeout(fix_dimensions, 500);
});
$("#config1").on("click", ".dropdown", function(){
    $(this).attr('tabindex', 1).focus();
    $(this).toggleClass('active');
    $(this).find('.dropdown-menu').slideToggle();
});
$("#config1").on("focusout", ".dropdown", function(){
    $(this).removeClass('active');
    $(this).find('.dropdown-menu').slideUp(300);
});
$("#config1").on("click", ".dropdown .dropdown-menu li", function(){
    $(this).parents('.dropdown').find('span').text($(this).text());
    $(this).parents('.dropdown').find('input').attr('value', $(this).text());
    preview_codeblock.innerHTML = prettyPrint(get_values())
    fix_dimensions()
})

$("#config1").on("click", "#btn_additem1", function(){
    new_item = '<div>' + createDropdown('Select Type', 'none', ['AutoRoutine', 'AutoCount', 'AutoResponse']) + '</div>'
    $(new_item).insertBefore('#btn_additem1');
});

////// Functions //////
function createDropdown(name, value, items) {
    innerhtml = '<div class="dropdown"><div class="select"><i class="fa fa-chevron-left">'
    innerhtml += '</i><span>' + name + '</span>' 
    innerhtml += '</div><input type="hidden" value="' + value + '">'
    innerhtml += '<ul class="dropdown-menu">'
    for (var i = 0; i < items.length; i++) {
        innerhtml += '<li>' + items[i] + '</li>'
    }
    innerhtml += '</ul></div>'
    return innerhtml
}
function get_values() {
    output = {}
    $(".dropdown input").each(function(i) {
        output[$(this).val()] = $(this).val()
    });
    return output
}
function prettyPrint(code){
    var jsonLine = /^( *)("[\w]+": )?("[^"]*"|[\w.+-]*)?([,[{])?$/mg;
    var replacer = function(match, pIndent, pKey, pVal, pEnd) {
        var key = '<span class="json-key" style="color: #7EE787">',
            val = '<span class="json-value" style="color: #79C0FF">',
            str = '<span class="json-string" style="color: #A5D6FF">',
            r = pIndent || '';
        if (pKey)
            r = r + key + `"${pKey.replace(/[": ]/g, '')}"` + '</span>: ';
        if (pVal)
            r = r + (pVal[0] == '"' ? str : val) + pVal + '</span>';
        return r + (pEnd || '');
    };
    return JSON.stringify(code, null, 3)
               .replace(/&/g, '&amp;').replace(/\\"/g, '&quot;')
               .replace(/</g, '&lt;').replace(/>/g, '&gt;')
               .replace(jsonLine, replacer);
}
function fix_dimensions() {
    $('#config').height("auto");
    $('#preview').height("auto");
    // if the 2 divs are sibe by side, make them the same height
    if ($('#config').width() + 100 < window.innerWidth) {
        if ($('#preview').height() > $('#config').height()){
            $('#config').height($('#preview').height());
        } else {
            $('#preview').height($('#config').height());
        }
        // if the 2 divs don't reach the bottom of the window, make them do so
        if (($('#preview').height() + $('#heading').height()) < window.innerHeight){
            new_height = window.innerHeight - $('#heading').height() - 90
            $('#preview').height(new_height)
            $('#config').height(new_height)
        }
    }
}

// CopyButton
function createCopyButton(codeblockDiv) {
    copybutton = document.createElement("copybutton");
    copybutton.className = "copy-button";
    copybutton.innerHTML = `<i class="fa-regular fa-clone"></i>`;
    copybutton.addEventListener("click", () => copyCodeToClipboard(copybutton, codeblockDiv));
    // addCopyButtonToDom
    codeblockDiv.insertBefore(copybutton, codeblockDiv.firstChild);
}
async function copyCodeToClipboard(copybutton, codeblockDiv) {
    codeToCopy = codeblockDiv.innerText;
    try {
      result = await navigator.permissions.query({ name: "clipboard-write" });
      if (result.state == "granted" || result.state == "prompt") {
        await navigator.clipboard.writeText(codeToCopy);
      } else {
        copyCodeBlockExecCommand(codeToCopy, codeblockDiv);
      }
    } catch (_) {
      copyCodeBlockExecCommand(codeToCopy, codeblockDiv);
    } finally {
        copybutton.innerHTML = `<i class="fa-solid fa-check" style="color: #3BA64C;"></i>`;
        copybutton.style.border = "1.5px solid #226337";
        setTimeout(function () {
            copybutton.innerHTML = `<i class="fa-regular fa-clone"></i>`;
            copybutton.style.border = "1.5px solid #363B42";
        }, 2000);;
    }
}
function copyCodeBlockExecCommand(codeToCopy, codeblockDiv) {
    textArea = document.createElement("textArea");
    textArea.contentEditable = "true";
    textArea.readOnly = "false";
    textArea.className = "copyable-text-area";
    textArea.value = codeToCopy;
    codeblockDiv.insertBefore(textArea, codeblockDiv.firstChild);
    const range = document.createRange();
    range.selectNodeContents(textArea);
    const sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);
    textArea.setSelectionRange(0, 999999);
    document.execCommand("copy");
    codeblockDiv.removeChild(textArea);
}
