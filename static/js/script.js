function checkFollowers() {
    fetch('/check_followers')
        .then(response => response.json())
        .then(data => {
            const resultsDiv = document.getElementById('results');
            if (data.no_change) {
                resultsDiv.textContent = 'No changes in mutual followers.';
            } else {
                resultsDiv.innerHTML = '<h2>Unfollowed You:</h2><ul>' +
                    data.unfollowed.map(user => '<li class="unfollowed">${user}</li>').join('') +
                    '</ul>';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('results').textContent = 'Error fetching data.';
        });
}