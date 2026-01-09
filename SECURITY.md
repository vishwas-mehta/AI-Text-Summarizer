# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please report it responsibly:

1. **Do not** open a public issue
2. Send details to the project maintainers
3. Include steps to reproduce the vulnerability
4. Allow time for the issue to be addressed

## Security Best Practices

### API Key Safety

- **Never** commit your `.env` file to version control
- Use environment variables for sensitive data
- Rotate API keys regularly
- Use read-only tokens when possible

### Input Validation

- All user input is validated before processing
- Text length limits are enforced
- Malicious content is sanitized

### Dependencies

- Dependencies are pinned to specific versions
- Regular security updates are applied
- Use `pip audit` to check for vulnerabilities

## Acknowledgments

We appreciate responsible disclosure of security vulnerabilities.
