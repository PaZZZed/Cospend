const selectedUserIds = [/* array of selected user IDs */];

fetch('/api/users/public-keys/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ user_ids: selectedUserIds }),
})
.then(response => response.json())
.then(data => {
    // data contains the public keys of the selected users
    console.log(data);
});
