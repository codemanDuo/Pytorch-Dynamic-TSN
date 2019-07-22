from .base_options import BaseOptions


class TrainOptions(BaseOptions):
    """This class includes training options.
    It also includes shared options defined in BaseOptions.
    """

    def initialize(self, parser):
        parser = super(TrainOptions, self).initialize(parser)

        # ========================= Runtime Configs ==========================
        parser.add_argument('--save_epoch_freq', type=int, default=5,
            help='Frequency of saving checkpoints at the end of epochs')
        parser.add_argument('--continue_last', action='store_true',
            help='Continue training: load the latest model')
        parser.add_argument('--phase', type=str, default='train',
            help='Phases, choices: train/val/test')
        
        # ========================= Learning Configs ==========================
        parser.add_argument('--momentum', type=float, default=0.5,
            help='Momentum terms for learning rate')
        parser.add_argument('--lr', type=float, default=0.002,
            help='Initial learning rate for adam')
        parser.add_argument('--lr_policy', type=str, default='linear',
            help='Learning rate policy. [linear | step | plateau | cosine]')
        parser.add_argument('--lr_decay_rate', type=float, default=0.1,
            help='Learning rate decay gamma/const')
        parser.add_argument('--lr_decay_iters', type=int, default=150,
            help='Multiply by a lr_decay_rate every <lr_decay_iters> iterations')
        
        # ========================= Monitor Configs ==========================
        parser.add_argument('--eval_epoch_freq', type=int, default=3,
            help='Frequency of eval validation in epoch')
        parser.add_argument('--print_freq', type=int, default=25,
            help='Frequency of printing loss and scores')

        self.isTrain = True
        return parser