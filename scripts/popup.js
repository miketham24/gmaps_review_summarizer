document.getElementById('summarize').addEventListener('click', () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        chrome.scripting.executeScript({
            target: { tabId: tabs[0].id },
            function: scrapeAndSummarize
        });
    });
});

async function scrapeAndSummarize() {
    const reviews = [];
    const reviewElements = document.querySelectorAll('.jftiEf');

    for (const element of reviewElements) {
        try {
            const moreButton = element.querySelector('.w8nwRe');
            if (moreButton) {
                moreButton.click();
                await new Promise(r => setTimeout(r, 5000));
            }
        } catch (err) {
            console.error('Error clicking more button:', err);
        }

        const snippet = element.querySelector('.MyEned');
        if (snippet) {
            reviews.push(snippet.textContent.trim());
        }
    }

    const summary = await fetchSummary(reviews.join('\n'));
    document.getElementById('summary').innerText = summary;
}

async function fetchSummary(reviews) {
    try {
        //TODO: add flask backend api
        const response = await fetch('', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ reviews })
        });

        const data = await response.json();
        return data.summary;
    } catch (error) {
        console.error('Error fetching summary:', error);
        return 'Failed to fetch summary.';
    }
}
