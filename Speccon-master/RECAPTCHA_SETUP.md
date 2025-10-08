# Google reCAPTCHA Setup Guide

This guide explains how to set up Google reCAPTCHA v2 for the SpecCon Holdings website to protect all enquiry forms from bots.

## Overview

reCAPTCHA has been integrated into:
1. **Contact Modal** - General contact form (all pages)
2. **Enquire Modal** - Quick enquiry form (SETA/qualification pages)
3. **Book Training Modal** - Training booking form (short course pages)
4. **Learnership Application Form** - Full learnership application

## Setup Steps

### 1. Get reCAPTCHA Keys

1. Go to [Google reCAPTCHA Admin Console](https://www.google.com/recaptcha/admin)
2. Sign in with your Google account
3. Click **"+ Create"** to register a new site
4. Fill in the form:
   - **Label**: SpecCon Holdings Website
   - **reCAPTCHA type**: Select **"reCAPTCHA v2"** → **"I'm not a robot" Checkbox**
   - **Domains**: Add your domains:
     - `speccon.co.za`
     - `www.speccon.co.za`
     - `localhost` (for testing)
   - Accept the reCAPTCHA Terms of Service
5. Click **"Submit"**
6. You'll receive two keys:
   - **Site Key** (public key)
   - **Secret Key** (private key - keep this secure!)

### 2. Update Site Key in Code

Replace `6LfYourSiteKeyHere` with your actual Site Key in these files:

#### File 1: `js/centralized-modals.js`
Update on **3 occurrences**:
```javascript
// Line ~102 (Contact Modal)
<div class="g-recaptcha" data-sitekey="YOUR_SITE_KEY_HERE"></div>

// Line ~194 (Enquire Modal)
<div class="g-recaptcha" data-sitekey="YOUR_SITE_KEY_HERE"></div>

// Line ~342 (Book Training Modal)
<div class="g-recaptcha" data-sitekey="YOUR_SITE_KEY_HERE"></div>
```

#### File 2: `learnership-application.html`
Update on **1 occurrence** (around line 913):
```html
<div class="g-recaptcha" data-sitekey="YOUR_SITE_KEY_HERE"></div>
```

### 3. Configure Server-Side Verification (Backend)

The frontend validation is in place, but you **must** also verify the reCAPTCHA response on your server to prevent bypass.

When the form is submitted, the reCAPTCHA response token is included. On your server:

```php
// PHP Example
$recaptcha_secret = 'YOUR_SECRET_KEY_HERE';
$recaptcha_response = $_POST['g-recaptcha-response'];
$remote_ip = $_SERVER['REMOTE_ADDR'];

$verify_url = 'https://www.google.com/recaptcha/api/siteverify';
$response = file_get_contents($verify_url . '?secret=' . $recaptcha_secret .
                              '&response=' . $recaptcha_response .
                              '&remoteip=' . $remote_ip);
$response_data = json_decode($response);

if ($response_data->success) {
    // reCAPTCHA verification successful
    // Process the form
} else {
    // reCAPTCHA verification failed
    // Reject the submission
}
```

```javascript
// Node.js Example
const axios = require('axios');

const verifyRecaptcha = async (token) => {
    const secretKey = 'YOUR_SECRET_KEY_HERE';
    const url = `https://www.google.com/recaptcha/api/siteverify?secret=${secretKey}&response=${token}`;

    try {
        const response = await axios.post(url);
        return response.data.success;
    } catch (error) {
        console.error('reCAPTCHA verification error:', error);
        return false;
    }
};

// In your form handler
app.post('/submit-form', async (req, res) => {
    const recaptchaToken = req.body['g-recaptcha-response'];

    const isHuman = await verifyRecaptcha(recaptchaToken);
    if (!isHuman) {
        return res.status(400).json({ error: 'reCAPTCHA verification failed' });
    }

    // Process the form...
});
```

### 4. Testing

1. **Local Testing**: reCAPTCHA works on localhost without any special configuration
2. **Test all forms**:
   - Contact modal (click "Contact Us" on any page)
   - Enquire modal (click "Enquiry now" on SETA/qualification pages)
   - Book Training modal (click "Book Training" on short course pages)
   - Learnership application form (complete all assessments and submit)
3. Try submitting without completing reCAPTCHA - should show error message
4. Complete reCAPTCHA and submit - should process successfully

## Files Modified

### JavaScript Files
- `js/centralized-modals.js` - Added reCAPTCHA to all 3 modal forms with validation

### HTML Files
- `index.html` - Added reCAPTCHA script tag
- `learnership-application.html` - Added reCAPTCHA script tag and form integration

## How It Works

1. **Display**: Each form now displays a reCAPTCHA checkbox before the submit button
2. **Client Validation**: JavaScript checks if reCAPTCHA is completed before allowing submission
3. **User Feedback**: If not completed, user sees alert: "Please complete the reCAPTCHA verification"
4. **Multiple Modals**: Each modal has its own reCAPTCHA instance (using widget IDs 0, 1, 2)
5. **Reset**: reCAPTCHA is reset when modal closes or after successful submission

## Security Notes

⚠️ **IMPORTANT**:
- Never expose your **Secret Key** in client-side code
- Always verify reCAPTCHA on the server-side
- The client-side check is only for UX - bots can bypass it
- Server-side verification is mandatory for security

## Troubleshooting

### reCAPTCHA not showing
- Check browser console for errors
- Verify Site Key is correct
- Ensure reCAPTCHA script is loaded: `<script src="https://www.google.com/recaptcha/api.js" async defer></script>`

### "Invalid site key" error
- Double-check the Site Key in your code
- Verify domain is registered in reCAPTCHA admin console

### reCAPTCHA shows but form still submits
- Check that `grecaptcha.getResponse()` is being called
- Verify the form submission handler has reCAPTCHA validation

### Multiple reCAPTCHAs on same page not working
- Ensure each widget has a unique ID (0, 1, 2 in our case)
- Use `grecaptcha.getResponse(widgetId)` and `grecaptcha.reset(widgetId)`

## Additional Resources

- [Google reCAPTCHA Documentation](https://developers.google.com/recaptcha/docs/display)
- [reCAPTCHA Admin Console](https://www.google.com/recaptcha/admin)
- [Server-Side Verification Guide](https://developers.google.com/recaptcha/docs/verify)

## Support

For issues or questions, contact the SpecCon development team.
