# Common Vulnerabilities

These are common web application vulnerabilities that attackers exploit to gain unauthorized access or manipulate systems.

- **CSRF (Cross-Site Request Forgery):**  
	- Tricks a user’s browser into making unintended requests (like form submissions) using their existing session cookies.  
	- Mitigation: Use CSRF tokens and same-site cookies.
- **XSS (Cross-Site Scripting):**  
	- Injects malicious JavaScript into web pages viewed by other users.  
	- Mitigation: Sanitize and escape user input; use Content Security Policy (CSP).
- **SSRF (Server-Side Request Forgery):**  
	- Exploits a server to make unauthorized requests to internal or external systems.  
	- Mitigation: Validate and restrict URLs servers can access.
- **SQLi (SQL Injection):**  
	- Injects malicious SQL statements through unsanitized inputs to access or modify databases.  
	- Mitigation: Use prepared statements and ORM frameworks.
    

These vulnerabilities all stem from improper validation or trust in user-supplied data.

---
Relates to: [web-security](web-security.md)