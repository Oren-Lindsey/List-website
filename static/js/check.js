function checkItems() {
  async function getApi(url) {
      // Storing response
      const response = await fetch(url);
    
      // Storing data in form of JSON
      var data = await response.json();
      console.log(data);
      if (response) {
          console.log(`the request worked`);
      }
      editHtml(data);
  }
  getApi(`https://list.s40.repl.co/api/get-status/`)
}
function editHtml(data) {
  const dataToParse = data;
  const count = Object.keys(dataToParse).length;
  const itemNames = Object.keys(dataToParse);
  const itemVals = Object.values(dataToParse);
  console.log(count);
  console.log(itemNames);
  console.log(itemVals);
  for (let i = 0; i < count; i++) {
    var currentItemName = itemNames[i];
    console.log(currentItemName);
    var currentItemVal = itemVals[i];
    console.log(currentItemVal);
    var label = document.getElementById(`${currentItemName}-label`);
    if (currentItemVal) {
      var checkbox = document.getElementById(`${currentItemName}-checkbox`);
      console.log(`Item "${currentItemName}" is true`);
      console.log(checkbox);
      checkbox.checked = !checkbox.checked;
      label.innerHTML = `Someone has bought this (Uncheck this if you're sure no one has bought it)`
    } else {
      label.innerHTML = `No one has bought this (Check this box if you buy it)`
    }
  }
}