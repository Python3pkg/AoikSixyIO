# coding: utf-8
"""
File ID: 2ePeUHV
"""

from aoiksixyio import SixyIO
from aoiksixyio import SixyIOObj
import os.path
import subprocess
import sys

#/
def make_arg_parser(cls, tt=None):
    #/
    tt = tt or (lambda x: x)

    #/ 3grGCaw
    parser = cls(prog='aoiksixyioexp', add_help=False)

    mutex_grp1 = parser.add_mutually_exclusive_group()

    mutex_grp2 = parser.add_mutually_exclusive_group()

    parser.add_argument(
       '-h',
       dest='help_on',
       action='store_true',
       help=tt('IfBWe0d'),
    )

    parser.add_argument(
        '--debug',
        dest='debug_on',
        action='store_true',
        help=tt('EOTuiRi'),
    )

    parser.add_argument(
        '--ei',
        dest='show_encoding_info',
        action='store_true',
        help=tt('BUv9hsz'),
    )

    parser.add_argument(
        '--stdioe',
        dest='stdioe',
        default=None,
        help=tt('Ay0if1H'),
    )

    parser.add_argument(
        '--stdie',
        dest='stdie',
        default=None,
        help=tt('AQTcrPq'),
    )

    parser.add_argument(
        '--stdoe',
        dest='stdoe',
        default=None,
        help=tt('HTstQFo'),
    )

    parser.add_argument(
        '--stdee',
        dest='stdee',
        default=None,
        help=tt('DO2cvC9'),
    )

    mutex_grp1.add_argument(
        '--ia',
        dest='input_arg_val',
        metavar='INPUT_ARG',
        help=tt('Ido2f1l'),
    )

    parser.add_argument(
        '--cae',
        dest='cae',
        default=None,
        help=tt('Az6N4l7'),
    )

    parser.add_argument(
        '--fse',
        dest='fse',
        default=None,
        help=tt('FVgnCju'),
    )

    mutex_grp1.add_argument(
        '--if',
        dest='input_file_path',
        metavar='INPUT_FILE',
        help=tt('C3Q0xhN'),
    )

    parser.add_argument(
        '--ife',
        dest='ife',
        default=None,
        help=tt('HdnJ115'),
    )

    parser.add_argument(
        '--of',
        dest='output_file_path',
        metavar='OUTPUT_FILE',
        help=tt('EqJvFJ7'),
    )

    parser.add_argument(
        '--ofe',
        dest='ofe',
        default=None,
        help=tt('EQq5Nla'),
    )

    mutex_grp2.add_argument(
        '--ofnte',
        dest='esc_to_empty',
        action='store_true',
        help=tt('EXSjWRS'),
    )

    mutex_grp2.add_argument(
        '--ofnts',
        dest='esc_to_space',
        action='store_true',
        help=tt('AcLZD2I'),
    )

    mutex_grp2.add_argument(
        '--ofntn',
        dest='esc_to_notation',
        action='store_true',
        help=tt('GeFIZQT'),
    )

    parser.add_argument(
        '--sp',
        dest='subproc_cmd',
        default=None,
        metavar='CMD',
        help=tt('C5DLRzH'),
    )
    
    parser.add_argument(
        '--spsep',
        dest='subproc_cmd_arg_sep',
        default=None,
        metavar='SEP',
        help=tt('CcmEKpl'),
    )

    parser.add_argument(
        '--spce',
        dest='spce',
        default=None,
        help=tt('BViterk'),
    )

    parser.add_argument(
        '--spie',
        dest='spie',
        default=None,
        help=tt('Ch8MLx8'),
    )

    parser.add_argument(
        '--spoe',
        dest='spoe',
        default=None,
        help=tt('Gn5NkKf'),
    )

    parser.add_argument(
        '--spee',
        dest='spee',
        default=None,
        help=tt('HxVZaBY'),
    )

    return parser

MAIN_RET_V_OK = 0
MAIN_RET_V_SHOW_HELP = 0
MAIN_RET_V_PYTHON_VER_NOT_SUPPORTED = 1
MAIN_RET_V_INIT_EASYIO_ERR = 2
MAIN_RET_V_DECODE_INPUT_FILE_PATH_ERR = 3
MAIN_RET_V_OPEN_INPUT_FILE_ERR = 4
MAIN_RET_V_READ_INPUT_FILE_ERR = 5
MAIN_RET_V_READ_STDIN_ERR = 6
MAIN_RET_V_DECODE_SUBPROC_CMD_ERR = 7
MAIN_RET_V_ENCODE_SUBPROC_CMD_ERR = 8
MAIN_RET_V_ENCODE_SUBPROC_INPUT_ERR = 9
MAIN_RET_V_RUN_SUBPROC_ERR = 10
MAIN_RET_V_DECODE_SUBPROC_STDERR_ERR = 11
MAIN_RET_V_WRITE_SUBPROC_STDERR_TO_STDERR_ERR = 12
MAIN_RET_V_DECODE_SUBPROC_STDOUT_ERR = 13
MAIN_RET_V_DECODE_OUTPUT_FILE_PATH_ERR = 14
MAIN_RET_V_WRITE_STDOUT_ERR = 15

TT_D = {
    'BlY3BYu': """Error: Unsupported Python version.
Make sure your Python 2 version is >=2.7 or Python 3 version is >=3.2""",
    'A1sZVil': '#/ Native encoding settings',
    '5tOBLf3': '#/ SixyIO encoding settings',
    'ClrVxdw': """Error: Failed decoding input data from cmd arg.
Encoding is |{}|.
Please use cmd arg |--cae| to specify a correct encoding.""",
    'IkN5JGx': 'Try if |--cae {}| works.',
    'Ed6AdJ9': """Failed decoding input file path.
Encoding is |{}|.
Please use cmd arg |--cae| to specify a correct encoding.""",
    'Ei1tnrR': 'Try if |--cae {}| works.',
    'B6Lk4XI': """Error: Failed opening input file.
Path is |{}|.""",
    'AqphK0K': """Error: Failed decoding input file data.
Encoding is |{}|.
Path is |{}|.
Please use cmd arg |--ife| to specify a correct encoding.""",
    'B37msq7': """Error: Failed reading input file.
Path is |{}|.""",
    'IXybCAa': """Error: Failed decoding input data from stdin.
Encoding is |{}|.
Please use cmd arg |--stdie| to specify a correct encoding.""",
    'AtkIgBP': 'Error: Failed reading input data from stdin.',
    'CWhvSZG': """Error: Failed decoding subproc command.
Encoding is |{}|.
Please use cmd arg |--cae| to specify a correct encoding.""",
    'FdgFTmj': 'Try if |--cae {}| works.',
    'Dm3mIS3': """Error: Failed encoding subproc command.
Encoding is |{}|.
Please use cmd arg |--spce| to specify a correct encoding.""",
    'BItk9r9': 'Try if |--spce {}| works.',
    'BdLRCnr': """Error: Failed encoding data to subproc stdin.
Encoding is |{}|.
Please use cmd arg |--spie| to specify a correct encoding.""",
    'BCK6oxA': 'Try if |--spie {}| works.',
    'FsfEwqB': 'Error: Failed running subproc command.',
    'DKm86F3': """Error: Failed decoding data from subproc stderr.
Encoding is |{}|.
Please use cmd arg |--spee| to specify a correct encoding.""",
    'CnoJPoC': 'Try if |--spee {}| works.',
    'E2z7epN': 'Error: Failed writing data from subproc stderr to stderr.',
    'GRzLy3z': """Error: Failed decoding data from subproc stdout.
Encoding is |{}|.
Please use cmd arg |--spoe| to specify a correct encoding.""",
    'Dl5ML6g': 'Try if |--spoe {}| works.',
    'CmfwiAq': """Error: Failed decoding output file path.
Encoding is |{}|.
Please use cmd arg |--cae| to specify a correct encoding.""",
    'GuCfy1d': 'Try if |--cae {}| works.',
    'IRQoaLq': """Error: Failed opening output file.
Path is |{}|.""",
    'HshHpp0': """Error: Failed encoding output data to file.
Encoding is |{}|.
Path is |{}|.
Please use cmd arg |--ofe| to specify a correct encoding.""",
    'AGCSyfb': """Error: Failed writing to output file.
Path is |{}|.""",
    'ARUsbv8': """Error: Failed encoding output data to stdout.
Encoding is |{}|.
Please use cmd arg |--stdoe| to specify a correct encoding.""",
    'DhY9aWc': 'Error: Failed writing to stdout',
    'BUv9hsz': 'Show encoding info.',
    'EOTuiRi': 'Show debugging info.',
    'IfBWe0d': 'Show help info.',
    'C3Q0xhN': 'Input file path.',
    'Ido2f1l': 'Input cmd arg value.',
    'EqJvFJ7': 'Output file path.',
    'EXSjWRS': 'Convert invalid characters in output file name to empty.',
    'AcLZD2I': 'Convert invalid characters in output file name to spaces.',
    'GeFIZQT': 'Convert invalid characters in output file name to %% notation.',
    'Ay0if1H': 'Stdin, stdout, and stderr encoding. Override env var |PYTHONIOENCODING|.',
    'AQTcrPq': """Stdin encoding.
Override env var |PYTHONIOENCODING| and cmd arg |--stdioe|.""",
    'HTstQFo': """Stdout encoding.
Override env var |PYTHONIOENCODING| and cmd arg |--stdioe|.""",
    'DO2cvC9': """Stderr encoding.
Override env var |PYTHONIOENCODING| and cmd arg |--stdioe|.""",
    'Az6N4l7': 'Cmd arg encoding. By default selected automatically.',
    'FVgnCju': 'File system encoding. By default selected automatically.',
    'HdnJ115': 'Input file encoding. By default utf-8.',
    'EQq5Nla': 'Output file encoding. By default utf-8.',
    'C5DLRzH': 'Subproc command.',
    'CcmEKpl': 'Subproc command argument separator.',
    'BViterk': 'Subproc command encoding. By default utf-8.',
    'Ch8MLx8': 'Subproc stdin encoding. By default utf-8.',
    'Gn5NkKf': 'Subproc stdout encoding. By default utf-8.',
    'HxVZaBY': 'Subproc stderr encoding. By default utf-8.',
}

def main():
    #/ 9w4YZfi
    SixyIO.reload_default_encoding('utf-8')

    #/ 4ik08Ok
    SixyIO.register_special_codecs()
    
    #/
    def tt(key):
        return TT_D[key]

    #/ 5ueXs6y
    if (sys.version_info[0] == 2 and sys.version_info < (2, 7))\
    or (sys.version_info[0] > 2 and sys.version_info < (3, 2)):
        #/ 2hF7IEj
        SixyIO.stderr_print_safe(tt('BlY3BYu'))

        #/ 6jGNubo
        return MAIN_RET_V_PYTHON_VER_NOT_SUPPORTED

    #/
    from argparse import ArgumentParser

    #/ 5qZ4gkT
    tmp_parser = make_arg_parser(cls=ArgumentParser, tt=tt)

    #/
    tmp_args = list(sys.argv[1:])

    #/ 7jgFMxP
    tmp_args_obj = tmp_parser.parse_known_args(args=tmp_args)[0]

    #/
    debug_on = tmp_args_obj.debug_on

    SixyIO.DEBUG_ON = debug_on

    #/ 8dLNrwl
    ##
    #/ 2wxliSS
    ## print msg inside |init| if has error.
    ##
    #/ 9rkDyfz
    ## exit inside |init| if has error.
    sio = SixyIOObj(
        stdioe=tmp_args_obj.stdioe,
        stdie=tmp_args_obj.stdie,
        stdoe=tmp_args_obj.stdoe,
        stdee=tmp_args_obj.stdee,
        cae=tmp_args_obj.cae,
        fse=tmp_args_obj.fse,
        ife=tmp_args_obj.ife,
        ofe=tmp_args_obj.ofe,
        spce=tmp_args_obj.spce,
        spie=tmp_args_obj.spie,
        spoe=tmp_args_obj.spoe,
        spee=tmp_args_obj.spee,
        exit_code=MAIN_RET_V_INIT_EASYIO_ERR,
        debug_on=debug_on,
    )

    #/
    args = sys.argv[1:]

    #/ 6pcwxTL
    parser = make_arg_parser(cls=ArgumentParser, tt=tt)

    #/ 2hgn08k
    ## Because of |add_help=False| at 3grGCaw, |-h| is no longer a special option.
    ## |parse_args| will print usage message if positional arguments are not enough,
    ##  even if |-h| is specified.
    ## We do not want this behavior. So handle it before calling |parse_args| at 2pePlsG.
    if tmp_args_obj.help_on:
        #/
        parser.print_help()

        #/
        return MAIN_RET_V_SHOW_HELP

    #/ 8ntpDyN
    if tmp_args_obj.show_encoding_info:
        #/
        sio.stderr_print_safe(tt('A1sZVil'))
        sio.stderr_print_safe(SixyIO.get_native_encodings_info())
        sio.stderr_print_safe('')

        #/
        sio.stderr_print_safe(tt('5tOBLf3'))
        sio.stderr_print_safe(sio.get_sixyio_encodings_info())
        sio.stderr_print_safe('')

    #/ 9qw2HGt
    args_obj = parser.parse_args(args)
    #/
    ## exit inside |parse_args| if has errors

    #/ 7mqi7PB
    input_utxt = None

    input_arg_val_stxt = args_obj.input_arg_val
    ## can be None
    ## |stxt| means bytes str on Py2, unicode str on Py3.

    input_file_path_stxt = args_obj.input_file_path
    ## can be None
    ## |stxt| means bytes str on Py2, unicode str on Py3.
    
    #/ 4vMmBo5
    if input_arg_val_stxt is not None:
        #/ 4vMmBo5
        try:
            input_utxt = sio.cae_to_u(input_arg_val_stxt)
        except Exception:
            #/ 4vMmBo5
            sio.stderr_print_fmt_safe(tt('ClrVxdw'), sio.cae_utxt)

            if sio.cae != SixyIO.STDIE:
                sio.stderr_print_fmt_safe(tt('IkN5JGx'), SixyIO.STDIE_UTXT)

            #/
            if debug_on:
                sio.stderr_write_tb_safe()

            #/ 4szO3LX
            return MAIN_RET_V_DECODE_INPUT_FILE_PATH_ERR

        assert input_utxt is not None
    
    #/ 2dvQxw3
    elif input_file_path_stxt is not None:
        #/ 9sLK0CP
        try:
            input_file_path = sio.cae_to_u(input_file_path_stxt)
        except Exception:
            #/ 3zN2DyO
            sio.stderr_print_fmt_safe(tt('Ed6AdJ9'), sio.cae_utxt)

            if sio.cae != SixyIO.STDIE:
                sio.stderr_print_fmt_safe(tt('Ei1tnrR'), SixyIO.STDIE_UTXT)

            #/
            if debug_on:
                sio.stderr_write_tb_safe()

            #/ 7oBeBvw
            return MAIN_RET_V_DECODE_INPUT_FILE_PATH_ERR

        #/ 5hxB9lf
        try:
            input_file = sio.open_in(input_file_path)
        except Exception:
            #/ 6gATkmv
            sio.stderr_print_fmt_safe(tt('B6Lk4XI'), input_file_path)

            #/
            if debug_on:
                sio.stderr_write_tb_safe()

            #/ 8oy1gRL
            return MAIN_RET_V_OPEN_INPUT_FILE_ERR

        #/ 9aLExHg
        try:
            input_utxt = input_file.read()
        except Exception as e:
            #/ 4hEv1El
            if isinstance(e, UnicodeDecodeError):
                sio.stderr_print_fmt_safe(tt('AqphK0K'), sio.ife_utxt, input_file_path)
            else:
                sio.stderr_print_fmt_safe(tt('B37msq7'), input_file_path)
                
            #/
            if debug_on:
                sio.stderr_write_tb_safe()

            #/ 8sDUvAY
            return MAIN_RET_V_READ_INPUT_FILE_ERR

    else:
        try:
            #/ 8e0bK1I
            stdin_reader = sio.stdin_make_reader()
            
            #/ 7i9CcnB
            input_utxt = stdin_reader.read()
        except Exception as e:
            #/ 2fRbg40
            if isinstance(e, UnicodeDecodeError):
                sio.stderr_print_fmt_safe(tt('IXybCAa'), sio.stdie_utxt)
            else:
                sio.stderr_print_fmt_safe(tt('AtkIgBP'))

            #/
            if debug_on:
                sio.stderr_write_tb_safe()

            #/ 6c3zIP6
            return MAIN_RET_V_READ_STDIN_ERR
        
    #/ 3cP3Fst
    assert SixyIO.is_u(input_utxt)
    
    output_utxt = input_utxt
    
    #/ 2eTGHcd
    subproc_cmd_stxt = args_obj.subproc_cmd
    
    if subproc_cmd_stxt is not None:
        #/ 5gmWFQl
        
        #/ 7kqdgx5
        try:
            subproc_cmd_utxt = sio.cae_to_u(subproc_cmd_stxt)
        except Exception:
            #/ 8v9cD4R
            sio.stderr_print_fmt_safe(tt('CWhvSZG'), sio.cae_utxt)
    
            if sio.cae != SixyIO.STDIE:
                sio.stderr_print_fmt_safe(tt('FdgFTmj'), SixyIO.STDIE_UTXT)
    
            #/
            if debug_on:
                sio.stderr_write_tb_safe()
    
            #/ 4b5BwuP
            return MAIN_RET_V_DECODE_SUBPROC_CMD_ERR
        
        #/ 9adD1em
        try:
            subproc_cmd_btxt = sio.spce_to_b(subproc_cmd_utxt)
        except Exception:
            #/ 7hs0meB
            sio.stderr_print_fmt_safe(tt('Dm3mIS3'), sio.spce_utxt)
    
            if sio.spce != SixyIO.STDIE:
                sio.stderr_print_fmt_safe(tt('BItk9r9'), SixyIO.STDIE_UTXT)
    
            #/
            if debug_on:
                sio.stderr_write_tb_safe()
    
            #/ 5ckdfD8
            return MAIN_RET_V_DECODE_SUBPROC_CMD_ERR
        
        #/ 6ahDu4o
        subproc_cmd_arg_sep_stxt = args_obj.subproc_cmd_arg_sep
        ## can be None. None means split by whitespaces. 
        
        #/
        if not subproc_cmd_arg_sep_stxt:
            subproc_cmd_btxt_part_s = subproc_cmd_btxt.split()
        else:
            subproc_cmd_arg_sep_btxt = SixyIO.to_b_safe(subproc_cmd_arg_sep_stxt, encoding='ascii')
            
            subproc_cmd_btxt_part_s = subproc_cmd_btxt.split(subproc_cmd_arg_sep_btxt)
        
        #/ 4mwJcw7
        try:
            subproc_stdin_btxt = sio.spie_to_b(output_utxt)
        except Exception:
            #/ 3sb9l3k
            sio.stderr_print_fmt_safe(tt('BdLRCnr'), sio.spie_utxt)
    
            if sio.spie != SixyIO.SPIE:
                sio.stderr_print_fmt_safe(tt('BCK6oxA'), SixyIO.SPIE_UTXT)
    
            #/
            if debug_on:
                sio.stderr_write_tb_safe()
    
            #/ 3fQOwsV
            return MAIN_RET_V_ENCODE_SUBPROC_INPUT_ERR
        
        #/ 6mWJVnP
        try:
            proc_obj = subprocess.Popen(subproc_cmd_btxt_part_s,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True,
            )
            
            stdout_stderr_tuple = proc_obj.communicate(subproc_stdin_btxt)
        except Exception:
            #/ 5wPPeO4
            sio.stderr_print_safe(tt('FsfEwqB'))
    
            #/
            if debug_on:
                sio.stderr_write_tb_safe()
    
            #/ 7wXi8nl
            return MAIN_RET_V_RUN_SUBPROC_ERR
        
        #/ 3hP3mlZ
        try:
            subproc_stderr_btxt = stdout_stderr_tuple[1]
            
            if not subproc_stderr_btxt:
                subproc_stderr_utxt = ''
            else:
                subproc_stderr_utxt = sio.spee_to_u(subproc_stderr_btxt)
        except Exception:
            #/ 6qzI4yL
            sio.stderr_print_fmt_safe(tt('DKm86F3'), sio.spee_utxt)
    
            if sio.spee != SixyIO.SPEE:
                sio.stderr_print_fmt_safe(tt('CnoJPoC'), SixyIO.SPEE_UTXT)
    
            #/
            if debug_on:
                sio.stderr_write_tb_safe()
    
            #/ 4zyralJ
            return MAIN_RET_V_DECODE_SUBPROC_STDERR_ERR
        
        #/
        if subproc_stderr_utxt:
            #/ 7qcEsZD
            try:
                sio.stderr_write_fmt_safe('#/ Subproc stderr\n---\n{}---\n', subproc_stderr_utxt)
            except Exception as e:
                #/ 8cijfJr
                sio.stderr_print_safe(tt('E2z7epN'))
        
                #/
                if debug_on:
                    sio.stderr_write_tb_safe()
        
                #/ 8kLQbwx
                return MAIN_RET_V_WRITE_SUBPROC_STDERR_TO_STDERR_ERR
        
        #/ 2nnZF4R
        try:
            subproc_stdout_btxt = stdout_stderr_tuple[0]
            
            if not subproc_stdout_btxt:
                subproc_stdout_utxt = ''
            else:
                subproc_stdout_utxt = sio.spoe_to_u(subproc_stdout_btxt)
                
        except Exception:
            #/ 5tAqT6m
            sio.stderr_print_fmt_safe(tt('GRzLy3z'), sio.spoe_utxt)
    
            if sio.spoe != SixyIO.SPOE:
                sio.stderr_print_fmt_safe(tt('Dl5ML6g'), SixyIO.SPOE_UTXT)
    
            #/
            if debug_on:
                sio.stderr_write_tb_safe()
    
            #/ 9csU4iB
            return MAIN_RET_V_DECODE_SUBPROC_STDOUT_ERR
        
        #/ 8k3qpHj
        output_utxt = subproc_stdout_utxt
        
    #/
    assert SixyIO.is_u(output_utxt)
        
    #/ 8fwlpZy

    #/
    output_file_path_stxt = args_obj.output_file_path
    ## can be None
    ## |stxt| means bytes str on Py2, unicode str on Py3.

    #/ 9dPh9hN
    if output_file_path_stxt is not None:
        #/ 3iHG4bD
        try:
            output_file_path = sio.cae_to_u(output_file_path_stxt)
        except Exception:
            #/ 5bCTyP9
            sio.stderr_print_fmt_safe(tt('CmfwiAq'), sio.cae_utxt)
    
            if sio.cae != SixyIO.STDIE:
                sio.stderr_print_fmt_safe(tt('GuCfy1d'), SixyIO.STDIE_UTXT)
    
            #/
            if debug_on:
                sio.stderr_write_tb_safe()
    
            #/ 5bCTyP9
            return MAIN_RET_V_DECODE_OUTPUT_FILE_PATH_ERR
    
        #/
        esc_to_space = args_obj.esc_to_space
    
        esc_to_empty = args_obj.esc_to_empty
    
        esc_to_notation = args_obj.esc_to_notation
    
        #/
        if esc_to_space or esc_to_empty or esc_to_notation:
            #/
            output_file_dir, output_file_name = os.path.split(output_file_path)
            
            #/
            if esc_to_space or esc_to_empty:
                #/
                esc_char = ' ' if esc_to_space else ''
        
                output_file_name = output_file_name\
                    .replace('\\', esc_char)\
                    .replace('/', esc_char)\
                    .replace('<', esc_char)\
                    .replace('>', esc_char)\
                    .replace(':', esc_char)\
                    .replace('*', esc_char)\
                    .replace('?', esc_char)\
                    .replace('"', esc_char)\
                    .replace('|', esc_char)
            elif esc_to_notation:
                output_file_name = output_file_name\
                    .replace('\\', '%5C')\
                    .replace('/', '%2F')\
                    .replace('<', '%3C')\
                    .replace('>', '%3E')\
                    .replace(':', '%3A')\
                    .replace('*', '%2A')\
                    .replace('?', '%3F')\
                    .replace('"', '%22')\
                    .replace('|', '%7C')
            else:
                assert False
                
            #/
            output_file_path = os.path.join(output_file_dir, output_file_name)
    
        #/ 8tKpz6C
        try:
            output_file = sio.open_out(output_file_path)
        except Exception:
            #/ 3qDTzam
            sio.stderr_print_fmt_safe(tt('IRQoaLq'), output_file_path)
    
            #/
            if debug_on:
                sio.stderr_write_tb_safe()
    
            #/ 3mQGvRY
            return
    
        #/ 2zli7tD
        try:
            with output_file:
                output_file.write(output_utxt)
        except Exception as e:
            #/ 4srhuSj
            if isinstance(e, UnicodeEncodeError):
                sio.stderr_print_fmt_safe(tt('HshHpp0'), sio.ofe_utxt, output_file_path)
            else:
                sio.stderr_print_fmt_safe(tt('AGCSyfb'), output_file_path)
    
            #/
            if debug_on:
                sio.stderr_write_tb_safe()
            
            #/ 8sXeIhg
            return
    #/
    else:
        #/ 4uXYGqG
        try:
            sio.stdout_write(output_utxt)
        except Exception as e:
            #/ 9sufbR0
            if isinstance(e, UnicodeEncodeError):
                sio.stderr_print_fmt_safe(tt('ARUsbv8'), sio.stdoe_utxt)
            else:
                sio.stderr_print_safe(tt('DhY9aWc'))
    
            #/
            if debug_on:
                sio.stderr_write_tb_safe()
    
            #/ 8da437J
            return MAIN_RET_V_WRITE_STDOUT_ERR
    
    #/ 3jB9xDg
    return MAIN_RET_V_OK

if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(0)
