from apache_beam.options.pipeline_options import PipelineOptions

class CustomPipelineOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        parser.add_argument(
            '--input',
            dest='input',
            default='input.txt',
            help='Input file to process.'
        )
        parser.add_argument(
            '--output',
            dest='output',
            default='output',
            help='Output prefix for files.'
        )