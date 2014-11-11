{
    'name': "Rust",
    "scopeName": "source.rust",
    "fileTypes": ["rs", "rc"],
    "foldingStartMarker": "^.*\bfn\s*(\w+\s*)?\([^\)]*\)(\s*\{[^\}]*)?\s*$",
    "foldingStopMarker": "^\s*\}",
    "patterns":
    [
        {
            'name': "meta.function.source.rust",
            'match': r'\b(fn)\s+([a-zA-Z_][a-zA-Z0-9_]?[\w\:,+ \'<>?]*)\s*(?:\()',
            'captures':
            {
                1: {'name': "keyword.source.rust"},
                2: {'name': "entity.name.function.source.rust"}
            }
        },
        {
            # This matches the 'let x = val' style of variable intitialization
            'name': "meta.initialization.rust",
            'match': r'(let)\s+(mut\s+)?([[:alpha:]_][[:alnum:]_]*)\s*(:.+?)?(=)',
            'captures':
            {
                1: {'name': "keyword.source.rust"},
                2: {'name': "keyword.source.rust"},
                3: {'name': "variable.other.rust"},
                4: {'name': "storage.type.source.rust"},
                5: {'name': "keyword.operator.rust"}
            },
        },
        {
            'name': "meta.import.rust",
            'match': r'(extern\s+crate)\s+(\w+)',
            'captures':
            {
                1: {'name': "keyword.source.rust"},
                2: {'name': "support"}
            }
        },
        {
            'name': "keyword.source.rust",
            'match': r'\b('
                     r'as|box|break|claim|const|continue|copy|Copy|crate|do|'
                     r'drop|else|extern|for|if|impl|in|let|loop|match|mod|mut|'
                     r'Owned|priv|pub|pure|ref|return|unsafe|use|while|mod|'
                     r'Send|static|trait|struct|enum|type|where'
                     r')\b'
        },
        {
            'name': "storage.type.source.rust",
            'match': r'\b('
                     r'Self|m32|m64|m128|f80|f16|f128|int|uint|float|char|bool|'
                     r'u8|u16|u32|u64|f32|f64|i8|i16|i32|i64|str|Option|Either|'
                     r'c_float|c_double|c_void|FILE|fpos_t|DIR|dirent|c_char|'
                     r'c_schar|c_uchar|c_short|c_ushort|c_int|c_uint|c_long|'
                     r'c_ulong|size_t|ptrdiff_t|clock_t|time_t|c_longlong|'
                     r'c_ulonglong|intptr_t|uintptr_t|off_t|dev_t|ino_t|pid_t|'
                     r'mode_t|ssize_t'
                     r')\b'
        },
        {
            'name': "support.constant.source.rust",
            'match': r'\b('
                     r'EXIT_FAILURE|EXIT_SUCCESS|RAND_MAX|EOF|SEEK_SET|'
                     r'SEEK_CUR|SEEK_END|_IOFBF|_IONBF|_IOLBF|BUFSIZ|FOPEN_MAX|'
                     r'FILENAME_MAX|L_tmpnam|TMP_MAX|O_RDONLY|O_WRONLY|O_RDWR|'
                     r'O_APPEND|O_CREAT|O_EXCL|O_TRUNC|S_IFIFO|S_IFCHR|S_IFBLK|'
                     r'S_IFDIR|S_IFREG|S_IFMT|S_IEXEC|S_IWRITE|S_IREAD|S_IRWXU|'
                     r'S_IXUSR|S_IWUSR|S_IRUSR|F_OK|R_OK|W_OK|X_OK|'
                     r'STDIN_FILENO|STDOUT_FILENO|STDERR_FILENO'
                     r')\b'
        },
        {
            'name': "comment.block.attribute.rust",
            'begin': r'(#!?\[)',
            "patterns":
            [
                {
                    'name': "string.quoted.double",
                    'match': r'\".+?\"'
                }
            ]
            'end': r'(\])',
        },
        {
            'name': "comment.line.documentation.source.rust",
            'begin': r'(//[!/][^/\n].*)',
            'end': r'($\n)'
        },
        {
            'name': "keyword.operator.rust",
            'match': r'(=>)|(->)|[-:=*,!.+|%/&~@<>;]'
        },
        {
            'name': "support.function.rust",
            'match': r'\b_\b'
        },
        {
            'name': "support.function.rust",
            'match': r'\b(\w+)\b(?=\()'
        },
        {
            'name': "meta.namespace-block.rust",
            'match': r'\b(\w+)::'
        },
        {
            'name': "meta.macro.source.rust",
            'match': r'\b(\w+!)\s*[({\[]',
            'captures':
            {
                1: { 'name': "meta.preprocessor.rust" }
            }
        },
        {
            'match': r'(\[|\]|{|}|\(|\))',
            'name': "punctuation.definition.bracket.rust"
        },
    ],
    'repository':
    {
        "rust_comment_doc_block":
        {
            'name': "comment.block.documentation.source.rust",
            'begin': r'(/\*[!\*][^\*])',
            'end': r'(\*/)',
            "patterns":
            [
                {"include": "#rust_comment_doc_block"}
            ]
        },
        "rust_ref_lifetime":
        {
            'match': r'&(\'([a-zA-Z_][a-zA-Z0-9_]*))\b',
            'captures':
            {
                1: { 'name': "storage.modifier.lifetime.source.rust" },
                2: { 'name': "entity.name.lifetime.source.rust" }
            }
        },
        "rust_lifetime":
        {
            'name': "storage.modifier.lifetime.source.rust",
            'match': r'\'([a-zA-Z_][a-zA-Z0-9_]*)[^\']\b',
            'captures':
            {
                1: { 'name': "entity.name.lifetime.source.rust" }
            }
        },
    },
    'uuid': "4339386b-4d67-4f0e-9e78-09ecbcddf71d"
}
