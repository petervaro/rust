## INFO ########################################################################
##                                                                            ##
##                          Rust Syntax Highlighter                           ##
##                          =======================                           ##
##                                                                            ##
##                       Version: 0.1.00.114 (20141111)                       ##
##                             File: src/rust.py                              ##
##                                                                            ##
##            For more information about the project, please visit            ##
##                    <https://github.com/petervaro/rust>.                    ##
##                       Copyright (C) 2014 Peter Varo                        ##
##                                                                            ##
##  This program is free software: you can redistribute it and/or modify it   ##
##   under the terms of the GNU General Public License as published by the    ##
##       Free Software Foundation, either version 3 of the License, or        ##
##                    (at your option) any later version.                     ##
##                                                                            ##
##    This program is distributed in the hope that it will be useful, but     ##
##         WITHOUT ANY WARRANTY; without even the implied warranty of         ##
##            MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.            ##
##            See the GNU General Public License for more details.            ##
##                                                                            ##
##     You should have received a copy of the GNU General Public License      ##
##     along with this program, most likely a file in the root directory,     ##
##        called 'LICENSE'. If not, see <http://www.gnu.org/licenses>.        ##
##                                                                            ##
######################################################################## INFO ##

#-- CHEATSHEET ----------------------------------------------------------------#
# HOWTO: http://sublimetext.info/docs/en/reference/syntaxdefs.html
# REGEX: http://manual.macromates.com/en/regular_expressions
# SCOPE: http://manual.macromates.com/en/language_grammars

# escape | line-feed   | return     | tab        |
# null   | hexadecimal | unicode 16 | unicode 32 |
ESCAPED_CHARS = r'\\|n|r|t|0|x\h{2}|u\h{4}|U\h{8}'

# Syntax Definition
syntax = {
    'name': '{NAME}',
    'comment': ('\n\t\tCopyright (C) 2014 Peter Varo'
                '\n\t\t<http://github.com/petervaro/rust>'
                '\n'
                '\n\t\tThis program is free software: you can redistribute it'
                '\n\t\tand/or modify it under the terms of the GNU General'
                '\n\t\tPublic License as published by the Free Software'
                '\n\t\tFoundation, either version 3 of the License, or (at your'
                '\n\t\toption) any later version.'
                '\n'
                '\n\t\tThis program is distributed in the hope that it will be'
                '\n\t\tuseful, but WITHOUT ANY WARRANTY; without even the'
                '\n\t\timplied warranty of MERCHANTABILITY or FITNESS FOR A'
                '\n\t\tPARTICULAR PURPOSE. See the GNU General Public License'
                '\n\t\tfor more details.'
                '\n'
                '\n\t\tYou should have received a copy of the GNU General Public'
                '\n\t\tLicense along with this program, most likely a file in'
                '\n\t\tthe root directory, called "LICENSE". If not, see'
                '\n\t\t<http://www.gnu.org/licenses>.'
                '\n\t'),
    'scopeName': 'source.{SCOPE}',
    # Patterns
    'patterns':
    [
#-- COMMENT -------------------------------------------------------------------#
        {
            'include': '#line_comments'
        },
        {
            'include': '#block_comments'
        },

#-- NUMBERS -------------------------------------------------------------------#
        {
            'name' : 'constant.numeric.integer.binary.{SCOPE}',
            'match': r'\b0b[01_]+((i|u)(8|16|32|64)?)?'
        },
        {
            'name' : 'constant.numeric.integer.octal.{SCOPE}',
            'match': r'\b0o[0-7_]+((i|u)(8|16|32|64)?)?'
        },
        {
            'name' : 'constant.numeric.integer.hexadecimal.{SCOPE}',
            'match': r'\b0x[\h_]+((i|u)(8|16|32|64)?)?'
        },
        {
            'name' : 'constant.numeric.float.decimal.{SCOPE}',
            'match': r'\b\d[\d_]*(\.\d[\d_]*)?([eE][+-]?\d[\d_]*)?(f(32|64))?(?=\W|$)'
        },
        {
            'name' : 'constant.numeric.integer.decimal.{SCOPE}',
            'match': r'\b(?<!\.)\d[\d_]*((i|u)(8|16|32|64)?)?'
        },

#-- CONSTANTS -----------------------------------------------------------------#
        {
            'include': '#strong_constants'
        },
        {
            'include': '#weak_constants'
        },

#-- KEYWORDS ------------------------------------------------------------------#
        {
            # FROM C
            'name' : 'keyword.storage.class_specifiers.{SCOPE}',
            'match': r'\b(typedef|extern|static|_Thread_local|auto|register)\b'
        },
        {
            'name' : 'keyword.type.type_qualifiers.{SCOPE}',
            'match': r'\b(const|static)\b'
        },
        {
            'name' : 'keyword.other.declaration.{SCOPE}',
            'match': r'\b(let|move|pub|type)\b'
        },
        {
            'name' : 'keyword.other.access.{SCOPE}',
            'match': r'\b(extern|use|where)\b'
        },
        {
            'name' : 'keyword.type.pointer.cast.{SCOPE}',
            'match': r'\b(box|mut)\b'
        },
        {
            'name' : 'keyword.type.cast.{SCOPE}',
            'match': r'\b(as)\b'
        },
        {
            'name' : 'keyword.type.borrow.{SCOPE}',
            'match': r'\b(ref)\b'
        },
        {
            'name' : 'keyword.storage.{SCOPE}',
            'match': r'\b(crate|fn|impl|mod|proc|unsafe)\b'
        },
        {
            'name' : 'keyword.other.{SCOPE}',
            'match': r'\b(once)\b'
        },
        {
            'name' : 'keyword.control.flow_control.{SCOPE}',
            'match': r'\b(break|continue|return)\b'
        },
        {
            'name' : 'keyword.control.iteration_statements.{SCOPE}',
            'match': r'\b(for|in|loop|while)\b'
        },
        {
            'name' : 'keyword.control.branching.{SCOPE}',
            'match': r'\b(if|else|match)\b'
        },
        {
            'name' : 'invalid.illegal.reserved_keyword.{SCOPE}',
            'match': r'\b('
                     r'abstract|be|do|final|override|priv|pure|unsized|virtual|'
                     r'yield|(align|offset|size|type)of'
                     r')\b'
        },

#-- OPERATORS -----------------------------------------------------------------#
        {
            'name' : 'keyword.operator.assignment.augmented.{SCOPE}',
            'match': r'(\+|-|\*|/|%|&|\^|\||<<|>>)='
        },
        {
            'name' : 'keyword.operator.comparison.{SCOPE}',
            'match': r'(<|>)=?|(=|!)='
        },
        {
            'name' : 'keyword.operator.bool.logical.{SCOPE}',
            'match': r'&&|\|\||!'
        },
        {
            'name' : 'keyword.operator.arithmetic.{SCOPE}',
            'match': r'\+|-|\*|/|%|&|\^|\||~|<<|>>|'
        },
        {
            'name' : 'keyword.operator.value_and_annotation_assignment.{SCOPE}',
            'match': r'=|\.|::?|(-|=)>'
        },

#-- BUILTINS ------------------------------------------------------------------#
        {
            'include': '#builtin_functions'
        },
        {
            'include': '#builtin_macros'
        },
        {
            'include': '#builtin_types'
        },

#-- MAGIC STUFFS --------------------------------------------------------------#
        {
            'include': '#language_variables'
        },

#-- ACCESS --------------------------------------------------------------------#
        {
            'name' : 'meta.function_call.{SCOPE}',
            'begin': r'([a-zA-Z_]\w*)\s*(<.+>)?\s*\(',
            'beginCaptures':
            {
                1: {'name': 'support.function.name.{SCOPE}'}
            },
            'patterns':
            [
                {'include': '$self'}
            ],
            'end':r'\)'
        },
        {
            'name' : 'meta.macro_invocation.{SCOPE}',
            'begin': r'(macro_rules)',
            'beginCaptures':
            {
                1: {'name': 'entity.name.section.macro.{SCOPE}'},
            },
            'patterns':
            [
                {
                    'name': 'meta.macro_invocation.{SCOPE}',
                    'begin': r'(!)',
                    'beginCaptures':
                    {
                        1: {'name': 'entity.name.section.macro.{SCOPE}'},
                    },
                    'patterns':
                    [
                        {
                            'name': 'meta.macro_invocation.{SCOPE}',
                            'begin': r'\(',
                            'patterns':
                            [
                                {
                                    'name' : 'variable.parameter.macro.{SCOPE}',
                                    'match': r'(\$)[a-zA-Z_]\w*\s*(:)\s*(item|block|stmt|pat|expr|'
                                             r'ty|ident|path|matchers|tt)',
                                    'captures':
                                    {
                                        1: {'name': 'keyword.operator.variable.macro.{SCOPE}'},
                                        2: {'name': 'keyword.operator.specifier.macro.{SCOPE}'},
                                        3: {'name': 'support.type.macro.{SCOPE}'},
                                    },
                                },
                                {
                                    'name' : 'variable.parameter.macro.{SCOPE}',
                                    'match': r'(\$)[a-zA-Z_]\w*',
                                    'captures':
                                    {
                                        1: {'name': 'keyword.operator.variable.macro.{SCOPE}'},
                                    },
                                },
                                {'include': '$self'},
                            ],
                            'end': r'\)',
                        },
                        {
                            'name': 'keyword.operator.arrow.macro.{SCOPE}',
                            'begin': r'=>',
                        },
                    ],
                    'end': r';'
                }
            ],
            'end': r'\)',
        },
        # {
        #     'name' : 'meta.macro_invocation.{SCOPE}',
        #     'begin': r'(macro_rules[\s\n]*!)[\s\n]*([a-zA-Z_]\w*)\s*\(',
        #     'beginCaptures':
        #     {
        #         1: {'name': 'entity.name.section.macro.{SCOPE}'},
        #         2: {'name': 'support.function.name.{SCOPE}'},
        #     },
        #     'patterns':
        #     [
        #         {
        #             'name' : 'variable.parameter.macro.{SCOPE}',
        #             'match': r'(\$)[a-zA-Z_]\w*\s*(:)\s*(item|block|stmt|pat|expr|'
        #                      r'ty|ident|path|matchers|tt)',
        #             'captures':
        #             {
        #                 1: {'name': 'keyword.operator.variable.macro.{SCOPE}'},
        #                 2: {'name': 'keyword.operator.specifier.macro.{SCOPE}'},
        #                 3: {'name': 'support.type.macro.{SCOPE}'},
        #             },
        #         },
        #         {
        #             'name' : 'variable.parameter.macro.{SCOPE}',
        #             'match': r'(\$)[a-zA-Z_]\w*',
        #             'captures':
        #             {
        #                 1: {'name': 'keyword.operator.variable.macro.{SCOPE}'},
        #             },
        #         },
        #         {'include': '$self'},
        #     ],
        #     'end':r';\s*\)'
        # },

#-- STRING --------------------------------------------------------------------#
        {
            'include': '#string_quoted'
        },
    ],

#-- REPOSITORY ----------------------------------------------------------------#
    'repository':
    {
#-- COMMENTS ------------------------------------------------------------------#
        'line_comments':
        {
            # One-liner
            # /// ... => doc comment
            # //! ... => parent comment
            'name' : 'comment.line.double_slash.{SCOPE}',
            'match': r'//.*$\n?',
        },
        'block_comments':
        {
            # Multi-liner
            # /** ... */ => doc comment
            'name' : 'comment.block.slash_star.{SCOPE}',
            'begin': r'/\*',
            'patterns':
            [
                # Nested block comments
                {'include': '#block_comments'}
            ],
            'end': r'\*/'
        },

#-- CONSTANTS -----------------------------------------------------------------#
        'strong_constants':
        {
            'patterns':
            [
                {
                    'name' : 'constant.language.unit.{SCOPE}',
                    'match': r'(?<!\w|!|>)\(\)'
                },
                {
                    'name' : 'constant.language.word_like.{SCOPE}',
                    'match': r'\b(false|true)\b'
                },
            ]
        },
        'weak_constants':
        {
            'patterns':
            [
                {
                    'name' : 'constant.other.enum_values.{SCOPE}',
                    'match': r'\b('
                             r'Some|None|Ok|Err|Less|Equal|Greater'
                             r')\b'
                }
            ]
        },

#-- BUILTINS ------------------------------------------------------------------#
        # http://doc.rust-lang.org/std/prelude/index.html
        'builtin_functions':
        {
            'name' : 'support.function.builtin.{SCOPE}',
            'match': r'\b(from_str|drop|range|repeat|(sync_)?channel|spawn)\b'
        },

        'builtin_macros':
        {
            'name' : 'support.macro.builtin.{SCOPE}',
            'match': r'\b('
                     r'assert|assert_eq|bitflags|bytes|cfg|col|concat|'
                     r'concat_idents|debug_assert|debug_assert_eq|env|file|'
                     r'format|format_args|include_bin|include_str|line|'
                     r'local_data_key|module_path|option_env|panic|print|'
                     r'println|select|stringify|try|unimplemented|unreachable|'
                     r'vec|write|writeln'
                     r')!',
        },

        'builtin_types':
        {
            'patterns':
            [
                {
                    'name' : 'support.type.{SCOPE}',
                    'match': r'\b('
                             r'bool|(u|i)(8|16|32|64)|f(32|64)|u?int|'
                             r'((char|str)(?!::))'
                             r')\b'
                },
                {
                    'name' : 'support.type.member.{SCOPE}',
                    'match': r'\b(enum|struct|trait)\b'
                },
                # Structs
                {
                    'name' : 'support.class.structs.{SCOPE}',
                    'match': r'\b('
                             r'Ascii|Box|(Posix|Windows)?Path|String|Vec|'
                             r'(Sync)?Sender|Receiver'
                             r')\b'
                },
                # Enums
                {
                    'name' : 'entity.name.type.enums.{SCOPE}',
                    'match': r'\b('
                             r'Ordering|Option|Result'
                             r')\b'
                },
                # Traits
                {
                    'name' : 'storage.modifier.traits.{SCOPE}',
                    'match': r'\b('
                             r'Copy|Send|Sized|Sync|Add|Sub|Mul|Div|Rem|Neg|'
                             r'Not|Bit(And|Or|Xor)|Drop|Deref(Mut)?|Shl|'
                             r'Shr|Index(Mut)?|Slice(Mut)?|Fn(Mut|Once)?|'
                             r'(Owned)?AsciiCast|AsciiStr|'
                             r'Into(Bytes|Str)|ToCStr|(Unicode)?Char|Clone|'
                             r'Partial(Eq|Ord)|Ord(ering)?|Eq(uiv)?|Extend|'
                             r'ExactSize|(From|RandomAccess|Cloneable|Ord|'
                             r'(Mutable)?DoubleEnded)?Iterator|Num(Cast)?|'
                             r'Checked(Add|Sub|Mul|Div)|'
                             r'(Uns|S)igned|Int|Float(Math)?|'
                             r'(To|From)?Primitive|GenericPath|'
                             r'Raw(Mut)?Ptr|(Buff|Writ|Read)er|Seek|'
                             r'Str(Vector|Prelude|Allocating)?|IntoMaybeOwned|'
                             r'UnicodeStrPrelude|ToString|'
                             r'Tuple(1(0|1|2)?|2|3|4|5|6|7|8|9)|'
                             r'AsSlice|(Clone)?SlicePrelude|'
                             r'VectorVector|PartialEqSlicePrelude|'
                             r'CloneSliceAllocPrelude|'
                             r'OrdSlice(Alloc)?Prelude|SliceAllocPrelude'
                             r')\b'
                },
            ]
        },

#-- ENTITY --------------------------------------------------------------------#
        'entity_name_class':
        {
            'patterns':
            [
                {'include': '#illegal_names'},
                {'include': '#generic_names'}
            ]
        },
        'generic_names':
        {
            'match': r'[a-zA-Z_]\w*'
        },
        'illegal_names':
        {
            'name' : 'invalid.illegal_names.name.{SCOPE}',
            'match': r'\b('
                     r'abstract|as|be|box|break|const|continue|crate|do|else|'
                     r'enum|extern|false|final|fn|for|if|impl|in|let|loop|'
                     r'match|mod|move|mut|once|override|priv|proc|pub|pure|ref|'
                     r'return|static|self|struct|super|true|trait|type|unsafe|'
                     r'unsized|use|virtual|where|while|yield|'
                     r'(align|offset|size|type)of'
                     r')\b'
        },

#-- MAGIC STUFFS --------------------------------------------------------------#
        'language_variables':
        {
            'name' : 'variable.language.{SCOPE}',
            'match': r'(?<!\.)\b(self|super)\b'
        },

#-- COMPILER MAGIC ------------------------------------------------------------#
        'compiler_magic':
        {
            'name' : '.{SCOPE}',
            'match': r'#\[(doc|path)\s*=\s*\]',
        },

#-- STRING --------------------------------------------------------------------#
        'string_quoted':
        {
            'patterns':
            [
                # Single Quoted Byte Literal
                {
                    'name' : 'string.quoted.single.bytes.escaped.{SCOPE}',
                    'match': r"(b)'(\\('|" + ESCAPED_CHARS + r"))'",
                    'captures':
                    {
                        1: {'name': 'storage.type.bytes.prefix.{SCOPE}'},
                        2: {'name': 'constant.character.escaped.special.{SCOPE}'},
                    }
                },
                {
                    'name' : 'string.quoted.single.bytes.illegal.{SCOPE}',
                    'match': r"(b)'(\\|'|\p{^ASCII}|\n)'",
                    'captures':
                    {
                        1: {'name': 'storage.type.bytes.prefix.{SCOPE}'},
                        2: {'name': 'invalid.illegal.bytes.quoted.single.{SCOPE}'},
                    }
                },
                {
                    'name' : 'string.quoted.single.bytes.regular.{SCOPE}',
                    'match': r"(b)'\p{ASCII}(.*?)'",
                    'captures':
                    {
                        1: {'name': 'storage.type.string.prefix.{SCOPE}'},
                        2: {'name': 'invalid.illegal.bytes.quoted.single.{SCOPE}'},
                    },
                },

                # Single Quoted Char Literal
                {
                    'name' : 'string.quoted.single.escaped.{SCOPE}',
                    'match': r"(?<!\w)'(\\('|" + ESCAPED_CHARS + r"))'",
                    'captures':
                    {
                        1: {'name': 'constant.character.escaped.special.{SCOPE}'}
                    }
                },
                {
                    'name' : 'string.quoted.single.illegal.{SCOPE}',
                    'match': r"(?<!\w)'(\\|'|\n)'",
                    'captures':
                    {
                        1: {'name': 'invalid.illegal.string.quoted.single.{SCOPE}'}
                    }
                },
                {
                    'name' : 'string.quoted.single.regular.{SCOPE}',
                    'match': r"(?<!\w)'.(.*?)'",
                    'captures':
                    {
                        1: {'name': 'invalid.illegal.string.quoted.more.{SCOPE}'}
                    }
                },

                # Double Quoted String Literal
                {
                    'name' : 'string.quoted.double.raw.{SCOPE}',
                    'begin': r'(r(#*))"',
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.string.prefix.{SCOPE}'},
                    },
                    # TODO: catch # escapes (also do this br#"..."#)
                    #'patterns':
                    #[
                    #    {
                    #        'name' : 'constant.character.escaped.special.{SCOPE}',
                    #        'match': r'(#)+.\1',
                    #    },
                    #],
                    'end'  : r'"(\2)',
                    'endCaptures':
                    {
                        1: {'name': 'storage.type.string.suffix.{SCOPE}'},
                    },
                },
                {
                    'name' : 'string.quoted.double.regular.{SCOPE}',
                    'begin': r'"',
                    'patterns':
                    [
                        {
                            'name' : 'constant.character.escaped.special.{SCOPE}',
                            'match': r'\\("|\n|' + ESCAPED_CHARS + r')',
                        },
                    ],
                    'end': r'"',
                },

                # Double Quoted Byte Literal
                {
                    'name' : 'string.quoted.double.bytes.raw.{SCOPE}',
                    'begin': r'(br(#*))"',
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.bytes.prefix.{SCOPE}'},
                    },
                    'patterns':
                    [
                        {
                            'name' : 'invalid.illegal.bytes.quoted.{SCOPE}',
                            'match': r'\p{^ASCII}',
                        }
                    ],
                    'end'  : r'"(\2)',
                    'endCaptures':
                    {
                        1: {'name': 'storage.type.bytes.suffix.{SCOPE}'}
                    },
                },
                {
                    'name' : 'string.quoted.double.bytes.regular.{SCOPE}',
                    'begin': r'(b)"',
                    'beginCaptures':
                    {
                        1: {'name': 'storage.type.bytes.prefix.{SCOPE}'},
                    },
                    'patterns':
                    [
                        {
                            'name' : 'invalid.illegal.bytes.quoted.{SCOPE}',
                            'match': r'\p{^ASCII}',
                        },
                        {
                            'name' : 'constant.character.escaped.special.{SCOPE}',
                            'match': r'\\("|\n|' + ESCAPED_CHARS + r')',
                        },
                    ],
                    'end': r'"',
                },
            ]
        },
    },
    'uuid': '4DE8A258-3469-48CE-BDB8-52624D0FF2D1'
}
