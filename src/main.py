from src.orchestrator import Orchestrator
from src.reporter import Reporter

orchestrator = Orchestrator()
reporter = Reporter()

test_files = ["tests/fixtures/secrets/fake_config.py", "tests/fixtures/vulnerable_deps/requirements.txt", "tests/fixtures/bad_configs/Dockerfile","tests/fixtures/dangerous_patterns/fake_code.py"]

report = orchestrator.run(test_files, {})

output = reporter.generate(report)

print(output)