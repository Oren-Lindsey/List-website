async function toggleItem(itemToToggle) {
  if (confirm(`Are you sure you want to change the status of this item?`)) {
    console.log(`user confirmed`);
    console.log(itemToToggle)
    var url = `https://list.s40.repl.co/api/toggle-item/${itemToToggle}`;

    var xhr = new XMLHttpRequest();
    xhr.open("POST", url);

    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4) {
       console.log(xhr.status);
        console.log(xhr.responseText);
      }};

    var data = `{
      "itemToToggle": ${itemToToggle}
    }`;

    xhr.send(data);
    console.log("Toggled")
    var label = document.getElementById(`${itemToToggle}-label`)
    var checkboxChecked = document.getElementById(`${itemToToggle}-checkbox`) .checked;
    console.log(checkboxChecked)
    if (checkboxChecked) {
      label.innerHTML = `Someone has bought this  (Uncheck this if you're sure no one has bought it)`
    } else {
    label.innerHTML = `No one has bought this (Check this box if you buy it)`
    }
    } else {
      var checkbox = document.getElementById(`${itemToToggle}-checkbox`)
      checkbox.checked = true;
    }
}