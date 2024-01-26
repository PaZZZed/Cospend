// Function to fetch the public key for the current user
async function fetchPublicKey() {
    const csrftoken = getCookie('csrftoken');
    const response = await fetch('api/public_key/');
    return await response.json();
}

// Function to encrypt the group name
async function encryptGroupName(groupName, publicKeyArmored) {
    // Extract the public key string from the publicKeyArmored object
    const publicKeyString = publicKeyArmored.publicKey;

    console.log("publicKeyString: ", publicKeyString);  // Log the actual public key string

    if (typeof publicKeyString !== 'string' || publicKeyString.trim() === '') {
        console.error("Invalid publicKeyString:", publicKeyString);
        throw new Error("Invalid public key");
    }

    const publicKey = await openpgp.readKey({ armoredKey: publicKeyString });
    const encryptedGroupName = await openpgp.encrypt({
        message: await openpgp.createMessage({ text: groupName }),
        encryptionKeys: publicKey,
    });
    return encryptedGroupName;
}


// Function to handle form submission
async function encryptAndSubmitForm(form) {
    const groupName = document.querySelector('[name="name"]').value;
    const publicKey = await fetchPublicKey();

    let encryptedGroupName = '';
    if (publicKey) {
        encryptedGroupName = await encryptGroupName(groupName, publicKey);
    }

    const encryptedDataField = document.createElement('input');
    encryptedDataField.type = 'hidden';
    encryptedDataField.name = 'encrypted_group_name';
    encryptedDataField.value = encryptedGroupName;
    form.appendChild(encryptedDataField);

    form.submit();
}

document.getElementById('groupForm').addEventListener('submit', function (e) {
    e.preventDefault();
    encryptAndSubmitForm(this);
});

// Function to get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
