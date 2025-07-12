#!/usr/bin/env python3
"""
PDF to Text Converter

This script extracts text from PDF files using pypdf.
Usage: python pdf2txt.py <input_pdf> [output_txt]
"""

import sys
import argparse
from pathlib import Path
from pypdf import PdfReader


def extract_text_from_pdf(pdf_path: str, output_path: str | None = None) -> str:
    """
    Extract text from a PDF file.

    Args:
        pdf_path (str): Path to the input PDF file
        output_path (str, optional): Path to save the extracted text

    Returns:
        str: Extracted text from the PDF
    """
    try:
        # Create a PDF reader object
        reader = PdfReader(pdf_path)

        # Extract text from all pages
        text = ""
        for page_num, page in enumerate(reader.pages, 1):
            page_text = page.extract_text()
            text += f"--- Page {page_num} ---\n"
            text += page_text + "\n\n"

        # Save to file if output path is provided
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Text extracted and saved to: {output_path}")

        return text

    except Exception as e:
        print(f"Error processing PDF: {e}")
        return ""


def main():
    parser = argparse.ArgumentParser(description="Extract text from PDF files")
    parser.add_argument("input_pdf", help="Path to the input PDF file")
    parser.add_argument("output_txt", nargs='?', help="Path to save the extracted text (optional)")

    args = parser.parse_args()

    # Check if input file exists
    if not Path(args.input_pdf).exists():
        print(f"Error: File '{args.input_pdf}' not found.")
        sys.exit(1)

    # Generate output filename if not provided
    output_path = args.output_txt
    if not output_path:
        input_path = Path(args.input_pdf)
        output_path = str(input_path.with_suffix('.txt'))

    # Extract text
    text = extract_text_from_pdf(args.input_pdf, output_path)

    # Print text to console if no output file specified
    if not args.output_txt:
        print("Extracted text:")
        print("-" * 50)
        print(text)


if __name__ == "__main__":
    main()