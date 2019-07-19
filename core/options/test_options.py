from .base_options import BaseOptions


class TestOptions(BaseOptions):
    """This class includes test options.
    It also includes shared options defined in BaseOptions.
    """

    def initialize(self, parser):
        parser = BaseOptions.initialize(self, parser)  # define shared options
        parser.add_argument('--test_size', type=float, default=0.1,
            help='# of test examples.')
        parser.add_argument('--results_dir', type=str, default='./results/',
            help='saves results here.')
        parser.add_argument('--phase', type=str, default='test',
            help='train, val, test, etc')
        
        # Dropout and Batchnorm has different behavioir during training and test.
        parser.add_argument('--eval_mode', action='store_true',
            help='use eval mode during test time.')

        self.isTrain = False
        return parser