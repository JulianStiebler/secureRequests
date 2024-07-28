# TLS, Certificates, and You

The `secureRequests.py` module is designed to enhance the security of HTTP requests made in Python applications by using TLS (Transport Layer Security) adapters and certificates. This markdown will provide a short dive into the security aspects of using TLS adapters, the role of certificates, and the importance of using secure communication protocols.

1. [Introduction](#introduction)
2. [What is TLS? (Transport Layer Security)](#what-is-tls-transport-layer-security)
    - [Role of TLS Adapters](#role-of-tls-adapters)
    - [Benefits of TLS Adapters](#benefits-of-tls-adapters)
3. [Certificates](#certificates)
    - [What are Certificates?](#what-are-certificates)
    - [Use of Certificates in `secureRequests.py`](#use-of-certificates-in-securerequestspy)
    - [Fetching and Verifying Certificates](#fetching-and-verifying-certificates)
4. [Why Use TLS and Certificates?](#why-use-tls-and-certificates)
    - [Protecting Sensitive Data](#protecting-sensitive-data)
    - [Compliance](#compliance)
    - [Trust and Integrity](#trust-and-integrity)
5. [How `secureRequests` Trys to Use Above Information](#how-securerequests-trys-to-use-above-information)
    - [Fetching Certificates](#fetching-certificates)
    - [Verifying Certificates](#verifying-certificates)
    - [Logging](#logging)
6. [Best Practices](#best-practices)

## Introduction

In today's digital world, secure communication is crucial. Ensuring that data transmitted over the internet is encrypted and authenticated is essential to protect against various cyber threats. The `secureRequests.py` module addresses these concerns by implementing TLS adapters and handling certificates effectively.

## What is TLS? (Transport Layer Security)

TLS is a cryptographic protocol designed to provide secure communication over a computer network. It ensures that data sent between a client and a server is encrypted, preventing eavesdropping and tampering.

- [Wikipedia: Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security)
- [RFC 5246: The Transport Layer Security (TLS) Protocol Version 1.2](https://tools.ietf.org/html/rfc5246)
- [CVE-2014-0160: Heartbleed](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0160)

### Role of TLS Adapters

In the `secureRequests.py` module, TLS adapters are used to enforce secure communication for HTTP requests. By default, Python's `requests` library uses TLS, but the module enhances this by allowing custom configurations and enforcing stricter security policies.

### Benefits of TLS Adapters

- **Encryption**: Ensures that the data transmitted is encrypted, making it unreadable to unauthorized parties.
- **Integrity**: Protects the data from being altered during transmission.
- **Authentication**: Verifies the identity of the communicating parties, ensuring that the data is sent to the intended recipient.

## Certificates

### What are Certificates?

Certificates are digital documents that bind a public key with an entity's identity, verified by a trusted third party known as a Certificate Authority (CA). They play a crucial role in establishing trust in secure communications.

- [Wikipedia: Public Key Certificate](https://en.wikipedia.org/wiki/Public_key_certificate)
- [RFC 5280: Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile](https://tools.ietf.org/html/rfc5280)

### Use of Certificates in `secureRequests.py`

The `secureRequests.py` module uses certificates to:
- **Verify Server Identity**: Ensure that the server you are communicating with is genuine and not an imposter.
- **Enable Mutual Authentication**: In some cases, both the client and server can authenticate each other using certificates.

### Fetching and Verifying Certificates

The module includes functionality to fetch certificates from a specified URL and verify their integrity using checksums. This ensures that the certificates used are valid and have not been tampered with.

## Why Use TLS and Certificates?

### Protecting Sensitive Data

When transmitting sensitive information such as personal data, financial information, or authentication credentials, encryption is vital to prevent data breaches.

- [GDPR Article 32: Security of Processing](https://gdpr-info.eu/art-32-gdpr/)

### Compliance

Many regulatory standards and legal requirements mandate the use of encryption and secure communication protocols to protect user data.

- [HIPAA Security Rule](https://www.hhs.gov/hipaa/for-professionals/security/index.html)
- [PCI DSS Requirement 4: Encrypt transmission of cardholder data across open, public networks](https://www.pcisecuritystandards.org/documents/PCI_DSS_v3-2-1.pdf)

### Trust and Integrity

Using TLS and certificates ensures that the data is transmitted securely and the identities of the communicating parties are verified, establishing trust between the client and server.

## How `secureRequests` trys to use above information

### Fetching Certificates

The `_certificateFetch` method fetches a certificate from a specified URL and saves it locally. It can force fetch a certificate even if it already exists and can verify the certificate's checksum to ensure its integrity.

### Verifying Certificates

The module verifies the fetched certificate's checksum against an expected value, ensuring that the certificate has not been altered during transmission.

### Logging

The module includes extensive logging to provide transparency and traceability in the certificate fetching and verification process.

## Best Practices

- Ensure that certificates are regularly updated and renewed before they expire to maintain secure communication.
- Use certificates from trusted Certificate Authorities (CAs) to ensure the authenticity of the certificates.
  - The default used CURL-certificate is regularly updated and trusted.
- Configure TLS adapters to enforce strong security policies, such as using the latest TLS versions and ciphers.
- For further information on implementing secure requests and configuring TLS adapters and certificates, refer to the official documentation of the requests library and TLS protocols.
  - [Requests Library Documentation](https://requests.readthedocs.io/en/latest/)
  - [TLS 1.3 Specification](https://tools.ietf.org/html/rfc8446)
