const list = document.getElementById("list");

document.getElementById("add").addEventListener("click", () => {
    const newItem = document.createElement("div");
    newItem.classList.add("list-item");

    const newContent = document.createElement("div");
    newContent.classList.add("content");
    newItem.style.opacity = 0;
    newItem.appendChild(newContent);

    list.prepend(newItem);

    const height = newItem.getBoundingClientRect().height;

    const listanimation = list.animate(
        [{
                transform: `translateY(-${height}px)`
            },
            {
                transform: "translateY(0px)"
            }
        ], {
            duration: 200,
        easing: "ease-in-out"
        }
    );

    listanimation.onfinish = () => {
        newItem.animate([{
            opacity: 0
        }, {
            opacity: 1
        }], {
            duration: 300,
            fill: "forwards",
            easing: "ease-in-out"
        });
    };
});

list.addEventListener("click", ev => {
	const item = ev.target.closest(".list-item");

	const itemFadeOut = item.animate([{
		opacity: 1
	}, {
		opacity: 0
	}], {
		duration: 300,
		fill: "forwards",
		easing: "ease-in-out"
	});

	itemFadeOut.onfinish = () => {
		const siblings = [];
		let el = item.nextElementSibling;

		if (el) {
			while (el) {
				siblings.push(el);
				el = el.nextElementSibling;
			}

			const height = item.getBoundingClientRect().height;

			let animation;
			siblings.forEach(sibling => {
				animation = sibling.animate(
					[{
							transform: "translateY(0)"
						},
						{
							transform: `translateY(${-height}px)`
						}
					], {
						duration: 500,
						easing: "ease-in-out"
					}
				);
			});

			animation.onfinish = () => list.removeChild(item);
		} else {
			list.removeChild(item);
		}
	};
});

Object.prototype.prettyPrint = function(){
    var jsonLine = /^( *)("[\w]+": )?("[^"]*"|[\w.+-]*)?([,[{])?$/mg;
    var replacer = function(match, pIndent, pKey, pVal, pEnd) {
        var key = '<span class="json-key" style="color: #7EE787">',
            val = '<span class="json-value" style="color: #79C0FF">',
            str = '<span class="json-string" style="color: #A5D6FF">',
            r = pIndent || '';
        if (pKey)
            r = r + key + pKey.replace(/[": ]/g, '') + '</span>: ';
        if (pVal)
            r = r + (pVal[0] == '"' ? str : val) + pVal + '</span>';
        return r + (pEnd || '');
    };

    return JSON.stringify(this, null, 3)
               .replace(/&/g, '&amp;').replace(/\\"/g, '&quot;')
               .replace(/</g, '&lt;').replace(/>/g, '&gt;')
               .replace(jsonLine, replacer);
}


var settings_json = {
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

document.getElementById('codeblock').innerHTML = settings_json.prettyPrint();
