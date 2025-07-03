
const urlTab = document.getElementById('urlTab');
const textTab = document.getElementById('textTab');
const urlInput = document.getElementById('urlInput');
const textInput = document.getElementById('textInput');

urlTab.addEventListener('click', () => {
  urlTab.classList.add('active');
  textTab.classList.remove('active');
  urlInput.style.display = '';
  textInput.style.display = 'none';
});

textTab.addEventListener('click', () => {
  textTab.classList.add('active');
  urlTab.classList.remove('active');
  urlInput.style.display = 'none';
  textInput.style.display = '';
});


document.getElementById('generateBtn').addEventListener('click', async () => {
  const summariesList = document.getElementById('summariesList');
  const isUrlMode = urlTab.classList.contains('active');
  const content = isUrlMode ? urlInput.value.trim() : textInput.value.trim();

  if (!content) {
    summariesList.innerHTML = `<div class="no-summaries">Please enter a ${isUrlMode ? 'URL' : 'text'} to summarize.</div>`;
    return;
  }

  try {
    summariesList.innerHTML = `<div class="summary-item">Generating summary...</div>`;

    const response = await fetch("/summarize", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        source_type: isUrlMode ? "url" : "text",
        content: content
      })
    });

    const result = await response.json();

    if (result.error) {
      summariesList.innerHTML = `<div class="no-summaries">${result.error}</div>`;
    } else {
      summariesList.innerHTML = `
        <div class="summary-item">
          <strong>Summary:</strong><br>${result.summary}
          ${result.question && result.answer ? `<br><br><strong>Q:</strong> ${result.question}<br><strong>A:</strong> ${result.answer}` : ''}
        </div>`;
    }

  } catch (err) {
    summariesList.innerHTML = `<div class="no-summaries">Error generating summary: ${err.message}</div>`;
  }
});
