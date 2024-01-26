// Function to decrypt data
async function decryptData(encryptedText) {
    // Retrieve the private key from local storage
    const privateKeyArmored = localStorage.getItem('privateKey');

    if (!privateKeyArmored) {
        console.error("No private key found in local storage.");
        return;
    }

    try {
        const privateKey = await openpgp.readPrivateKey({ armoredKey: privateKeyArmored });
        const message = await openpgp.readMessage({
            armoredMessage: encryptedText // parse armored message
        });

        const { data: decryptedText } = await openpgp.decrypt({
            message,
            decryptionKeys: privateKey
        });

        return decryptedText; // decrypted text
    } catch (error) {
        console.error("Decryption error:", error);
        return;
    }
}

// Example usage
// Assuming 'encryptedData' is a variable containing your encrypted text
const encryptedData = '...'; // Replace with your actual encrypted data
decryptData(encryptedData).then(decryptedText => {
    console.log("Decrypted Text:", decryptedText);
    // Handle the decrypted text as needed
});
