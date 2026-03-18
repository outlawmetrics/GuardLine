from src.scanners.secrets.scanner import SecretsScanner


def test_finds_secrets_in_fake_config():
    scanner = SecretsScanner()
    findings = scanner.scan(['tests/fixtures/secrets/fake_config.py'], {})
    assert len(findings) == 5

def test_finds_scanner_name():
    scanner = SecretsScanner()
    findings = scanner.scan(['tests/fixtures/secrets/fake_config.py'], {})
    assert findings[0].scanner == "secrets"