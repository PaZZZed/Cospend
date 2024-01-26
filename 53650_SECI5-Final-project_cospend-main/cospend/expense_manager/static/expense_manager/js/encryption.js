// const openpgp = require('openpgp');
async function generateUserKeys(username) {
    const pairKey = await openpgp.generateKey({
        userIDs: [{ name: username }],
        curve: 'ed25519', // ECC curve name
    });

    // console.log(pairKey.publicKey); // Add this line to log the output

    localStorage.setItem('privateKey', pairKey.privateKey); // Store private key in local storage
    return pairKey.publicKey; // Return public key to send to server
}
// generateUserKeys("daniel");

document.getElementById('registrationForm').addEventListener('submit', async function (e) {
    console.log("Form submission triggered");
    e.preventDefault();
    const username = document.querySelector('[name="username"]').value; // Adjust if your username field has a different name
    const PublicKeys = await generateUserKeys(username);
    document.getElementById('publicKey').value = PublicKeys;
    this.submit();
});

