var lastchat =  "new-client-200";
const searchParams = new URLSearchParams(window.location.search);
var user_name = searchParams.get('user')
const chatContainer = document.getElementById('msgs-box-main');


function update_chat_room() {
    const apiUrl = 'http://localhost:5000/api/room-updates?id='+lastchat;

    fetch(apiUrl)
      .then(response => {

        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        return response.json();
      })
      .then(data => {

        console.log(data);
        lastchat = data["messages"][data['messages'].length - 1 ]['id']
        // console.log(lastchat)
        element = `<div class="msg-box">? <span id="msg-user" class="msg-user">`+ "" +`</span> > ` + "" + ` </div>`
         


        data['messages'].forEach(function (item, index) {
            console.log(item, index);

            let name_ele = document.createElement("span")
            name_ele.appendChild(document.createTextNode(item.user))
            
            name_ele.className = "msg-user"
            let msg_ele = document.createElement("div")
            msg_ele.appendChild(document.createTextNode("? "))
            msg_ele.appendChild(name_ele)
            msg_ele.appendChild(document.createTextNode(" > "))
            msg_ele.appendChild(document.createTextNode(item.msg))
            msg_ele.className = "msg-box"
        
            document.getElementById("msgs-box-main").appendChild(msg_ele)

            scrollToBottom();
          });

      })
      .catch(error => {

        console.error('Error:', error);
      });
}




function scrollToBottom() {
  chatContainer.scrollTop = chatContainer.scrollHeight;
}


function message_send(text,user) {
  console.log(text,user);

  const apiUrl = "http://localhost:5000/api/send-msg";

  const postData = {
    "user":user,
    "msg":text
  };

  const requestOptions = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(postData),
  };
  fetch(apiUrl, requestOptions)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      console.log(data);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

let chat_form = document.getElementById("msg-form")
chat_form.addEventListener("submit", (e) => {
    e.preventDefault();
  
    let input_Msg = document.getElementById("input-msg");
    console.log(input_Msg.value)

    message_send(input_Msg.value, user_name)

    input_Msg.value = ""
  
    
  });

setInterval(update_chat_room, 600);

