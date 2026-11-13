"""CLI for agent-api-fuzz-test-synthesizer."""
import sys
import argparse
from .fuzzer import APIFuzzSynthesizer

def main():
    parser = argparse.ArgumentParser(description="Agent API Fuzz Test Synthesizer CLI")
    parser.add_argument("--demo", action="store_true", help="Run API fuzz payload synthesis demo")
    args = parser.parse_args()

    if args.demo:
        payloads = APIFuzzSynthesizer.generate_fuzz_values_for_type("user_age", "int")
        print(f"[+] Generated {len(payloads)} fuzz payloads for 'user_age' (int):")
        for p in payloads:
            print(f"    - {p.category}: {p.value}")
    else:
        parser.print_help()
    sys.exit(0)

if __name__ == "__main__":
    main()
