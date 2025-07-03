
document.getElementById('summaryForm').addEventListener('submit', function(event) {
    event.preventDefault();
  
    const url = document.getElementById('articleUrl').value;
    const text = document.getElementById('articleText').value;
    const summary = `Summary from URL: ${url} | Text: ${text}`;
  
    const summaryList = document.getElementById('summaryList');
    const listItem = document.createElement('li');
    listItem.className = 'summary-item';
    listItem.textContent = summary;
    summaryList.appendChild(listItem);
  
    // Clear input fields
    document.getElementById('articleUrl').value = '';
    document.getElementById('articleText').value = '';
  });
  
  const darkModeToggle = document.getElementById("dark-mode-toggle");
  
  darkModeToggle.addEventListener("click", function() {
    document.body.classList.toggle("dark-mode");
  });

  