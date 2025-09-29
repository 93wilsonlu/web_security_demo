const express = require("express");
const crypto = require("crypto");

const app = express();
const PORT = process.env.PORT || 10010;

const secret = crypto.randomBytes(32).toString("hex");
const FLAG = process.env.FLAG || "NTHUTS{Just_JS_trick}";

app.use(express.json());

const validators = {
    "HMAC-SHA256": (data, secret) => {
        return crypto
            .createHmac("sha256", secret)
            .update(data)
            .digest("base64");
    },
    "HMAC-SHA512": (data, secret) => {
        return crypto
            .createHmac("sha512", secret)
            .update(data)
            .digest("base64");
    },
};

function validate(credential, secret) {
    const [method, content, signature] = credential.split(".");
    const validator = validators[method];
    if (!validator) return false;

    const expectedSignature = validator(content, secret);
    return encodeURIComponent(signature) === encodeURIComponent(expectedSignature);
}

app.get("/", (req, res) => {
    if (req.query.credential) {
        const isValid = validate(req.query.credential, secret);
        if (isValid) {
            res.json({ message: `Flag: ${FLAG}` });
        } else {
            res.status(401).json({ error: "Invalid credential" });
        }
    } else {
        // page to input credential
        res.status(200).send(`
            <html>
                <body>
                    <form method="GET" action="/">
                        <label for="credential">Credential:</label>
                        <input type="text" id="credential" name="credential" required />
                        <button type="submit">Submit</button>
                    </form>
                </body>
            </html>
        `);
    }
});

app.use("*", (req, res) => {
    res.status(404).json({
        error: "Resource not found",
        message: "The requested resource does not exist",
    });
});

app.listen(PORT, () => {});
