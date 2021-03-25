console.log('Sanity check!')

// Get stripe publishable keys
fetch('/config')
.then((result) => {return result.json();})
.then((data) => {
    // Initialize stripe.js
    const stripe = Stripe(data.publicKey);
});