// Tab switching logic
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

// Handle summary generation
document.getElementById('generateBtn').addEventListener('click', async () => {
  const summariesList = document.getElementById('summariesList');
  const isUrlMode = urlTab.classList.contains('active');
  const content = isUrlMode ? urlInput.value.trim() : textInput.value.trim();
  const question = document.getElementById('questionInput')?.value.trim() || "";

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
        content: content,
        question: question || null
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
      loadSavedSummaries(); // Refresh saved list
    }

  } catch (err) {
    summariesList.innerHTML = `<div class="no-summaries">Error generating summary: ${err.message}</div>`;
  }
});

// Load saved summaries from backend
async function loadSavedSummaries() {
  const history = document.querySelector('.summary-history');
  try {
    const res = await fetch("/summaries");
    const data = await res.json();

    if (data.length === 0) {
      history.innerHTML = "No saved summaries yet.";
      return;
    }

    history.innerHTML = "";
    data.forEach(item => {
      const block = document.createElement("div");
      block.classList.add("summary-item");
      block.innerHTML = `
        <strong>Summary:</strong><br>${item.summary}<br>
        <em>Source:</em> ${item.source_type} <br>
        ${item.question ? `<strong>Q:</strong> ${item.question}<br><strong>A:</strong> ${item.answer}<br>` : ""}
        <hr>
      `;
      history.appendChild(block);
    });
  } catch (err) {
    history.innerHTML = "Error loading summaries.";
  }
}

// Load saved summaries when page loads
window.onload = loadSavedSummaries;
