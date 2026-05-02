#!/usr/bin/env bash
# Download Bluetooth Core Specification PDFs from bluetooth.com
#
# Usage:
#   ./scripts/download_specs.sh               # Download all versions
#   ./scripts/download_specs.sh 6.0           # Download specific version
#   ./scripts/download_specs.sh 5.2 5.3 5.4   # Download multiple versions
#
# Requirements:
#   - curl or wget
#   - A bluetooth.com account is NOT required for these downloads
#   - You must accept bluetooth.com's terms of use before downloading
#
# Output:
#   PDF files saved to sources/specs/core-spec-X.Y.pdf

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
OUTPUT_DIR="$REPO_ROOT/sources/specs"

mkdir -p "$OUTPUT_DIR"

# Bluetooth Core Spec download doc IDs (from bluetooth.com)
# These are the direct download URLs via the bluetooth.com docman handler
# Each URL requires accepting the Terms of Use on bluetooth.com first.
# If a direct download fails, visit the spec page and accept terms manually.
declare -A SPEC_URLS=(
  ["5.0"]="https://www.bluetooth.com/specifications/specs/core-specification-5-0/"
  ["5.1"]="https://www.bluetooth.com/specifications/specs/core-specification-5-1/"
  ["5.2"]="https://www.bluetooth.com/specifications/specs/core-specification-5-2/"
  ["5.3"]="https://www.bluetooth.com/specifications/specs/core-specification-5-3/"
  ["5.4"]="https://www.bluetooth.com/specifications/specs/core-specification-5-4/"
  ["6.0"]="https://www.bluetooth.com/specifications/specs/core-specification-6-0/"
)

# Direct download links (PDF) - may require manual acceptance of terms on bluetooth.com first
# Visit the spec page, accept terms, then the direct PDF link will work
declare -A DIRECT_PDF_URLS=(
  ["5.0"]="https://www.bluetooth.org/docman/handlers/downloaddoc.ashx?doc_id=421043"
  ["5.1"]="https://www.bluetooth.org/docman/handlers/downloaddoc.ashx?doc_id=457080"
  ["5.2"]="https://www.bluetooth.org/docman/handlers/downloaddoc.ashx?doc_id=478726"
  ["5.3"]="https://www.bluetooth.org/docman/handlers/downloaddoc.ashx?doc_id=521059"
  ["5.4"]="https://www.bluetooth.org/docman/handlers/downloaddoc.ashx?doc_id=545963"
  ["6.0"]="https://www.bluetooth.org/docman/handlers/downloaddoc.ashx?doc_id=556599"
)

# Versions to download
if [[ $# -eq 0 ]]; then
  VERSIONS=("5.0" "5.1" "5.2" "5.3" "5.4" "6.0")
else
  VERSIONS=("$@")
fi

download_spec() {
  local version="$1"
  local output_file="$OUTPUT_DIR/core-spec-${version}.pdf"

  if [[ -f "$output_file" ]]; then
    echo "  [SKIP] core-spec-${version}.pdf already exists"
    return 0
  fi

  if [[ -z "${DIRECT_PDF_URLS[$version]+x}" ]]; then
    echo "  [ERROR] Unknown version: $version"
    echo "  Available: ${!DIRECT_PDF_URLS[*]}"
    return 1
  fi

  local url="${DIRECT_PDF_URLS[$version]}"
  local spec_page="${SPEC_URLS[$version]}"

  echo "  Downloading Core Spec ${version}..."
  echo "  Spec page (accept terms here if download fails): $spec_page"

  if command -v curl &>/dev/null; then
    if curl -L --fail --progress-bar \
         -H "User-Agent: Mozilla/5.0" \
         -H "Referer: https://www.bluetooth.com/" \
         -o "$output_file" "$url"; then
      echo "  [OK] Saved to: $output_file"
    else
      echo "  [WARN] Direct download failed. Please visit:"
      echo "         $spec_page"
      echo "         Accept the terms, download the PDF, and save it as:"
      echo "         $output_file"
      rm -f "$output_file"
      return 1
    fi
  elif command -v wget &>/dev/null; then
    if wget -q --show-progress \
         --user-agent="Mozilla/5.0" \
         --referer="https://www.bluetooth.com/" \
         -O "$output_file" "$url"; then
      echo "  [OK] Saved to: $output_file"
    else
      echo "  [WARN] Direct download failed. See above."
      rm -f "$output_file"
      return 1
    fi
  else
    echo "  [ERROR] Neither curl nor wget found. Install one and retry."
    return 1
  fi
}

echo "=== Bluetooth Core Spec Downloader ==="
echo "Output directory: $OUTPUT_DIR"
echo ""

failed=()
for version in "${VERSIONS[@]}"; do
  echo "--- Version ${version} ---"
  if ! download_spec "$version"; then
    failed+=("$version")
  fi
  echo ""
done

echo "=== Summary ==="
if [[ ${#failed[@]} -eq 0 ]]; then
  echo "All downloads completed successfully."
else
  echo "Failed versions: ${failed[*]}"
  echo ""
  echo "For failed versions, download manually from bluetooth.com:"
  for v in "${failed[@]}"; do
    echo "  Version $v: ${SPEC_URLS[$v]}"
  done
fi

echo ""
echo "Next step: run ./scripts/convert_to_md.py to convert PDFs to Markdown"
