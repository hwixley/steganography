from models.XMode import XMode
from models.XOutput import XOutput
from argparse import ArgumentParser
from pathlib import Path

class Default:
    output_type = XOutput.FILE
    input_text = "If you're reading this it means you did not input any custom text, or maybe you wanted to see this message instead, well if so it worked! WOOP Your image is now secretly encoded with this message."
    input_file = None
    input_image = "sample.png"
    export_path = "encoded.png"

    @staticmethod
    def arg_parser() -> ArgumentParser:
        arg_parser = ArgumentParser()
        arg_parser.add_argument(
            "--mode",
            "-m",
            type=XMode
        )
        arg_parser.add_argument(
            "--output-type",
            "-o", type=XOutput,
            default=Default.output_type
        )
        arg_parser.add_argument(
            "--text",
            "-t", 
            type=str
        )
        arg_parser.add_argument(
            "--file",
            "-f",
            type=Path
        )
        arg_parser.add_argument(
            "--input-image",
            "-i",
            type=Path,
            required=True
        )
        arg_parser.add_argument(
            "--export-path",
            "-e",
            type=Path
        )
        arg_parser.add_argument(
            "--key",
            "-k",
            type=str
        )
        return arg_parser

