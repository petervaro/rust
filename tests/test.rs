// Example of a single-line comment

/* Example of
   multi-line comment */

use /* this is the start of a comment
       which has another line here
       /* and this is the start of a nested comment
          which also has another line here
          /* and this one here,
             is a deeply nested comment */
          which is followed by some lines
          and this is the end of the first nest-level */
       and here comes the end of the original
       comment block */ std::fmt;

();
true; false;

012i;                              // type int
123i;                              // type int
123u;                              // type uint
123_u;                             // type uint
0________u;                        // type uint
0xff_u8;                           // type u8
0o70_i16;                          // type i16
0b1111_1111_1001_0000_i32;         // type i32

123.0f64;                          // type f64
0.1f64;                            // type f64
0.1f32;                            // type f32
12E+99_f64;                        // type f64

'a'; 'b'; 'c'; '1'; '2'; '3'; '£',
'\n'; '\t'; '\r'; '\0'; '\\'; '\'';
'\xf8'; '\uf6a9'; '\Uabcd0123';
'ab'; '''; '\';

b'~'; b'x';
b'\n'; b'\t'; b'\r'; b'\0'; b'\\'; b'\'';
b'\xf8'; b'\uf6a9'; b'\Uabcd0123';
b'£'; b'ab'; b'''; b'\';

"foo"; r"foo";                     // foo
"\"foo\""; r#""foo""#;             // "foo"

"foo #\"# bar";
r##"foo #"# bar"##;                // foo #"# bar

"\x52"; "R"; r"R";                 // R
"\\x52"; r"\x52";                  // \x52

""; r""; r#""#;
"abc"; r"abc"; r#"abc"#;
"\n\t\r\0\\"; r"\n\t\r\0\\"
"\xf8\xf8"; "\uf6a9\uf6a9"; "\Uabcd0123\Uabcd0123";
r"\xf8\xf8"; r"\uf6a9\uf6a9"; r"\Uabcd0123\Uabcd0123";

"\
hello\
world\
";
"
hello
world
";
r"\
hello\
world\
";
r#"\
hello\
world\
"#;

b"foo"; br"foo";                     // foo
b"\"foo\""; br#""foo""#;             // "foo"

b"foo #\"# bar";
br##"foo #"# bar"##;                 // foo #"# bar

b"\x52"; b"R"; br"R";                // R
b"\\x52"; br"\x52";                  // \x52

b""; br""; br#""#;
b"abc"; br"abc"; br#"abc"#;
b"\n\t\r\0\\"; br"\n\t\r\0\\"
b"\xf8\xf8"; b"\uf6a9\uf6a9"; b"\Uabcd0123\Uabcd0123";
br"\xf8\xf8"; br"\uf6a9\uf6a9"; br"\Uabcd0123\Uabcd0123";
b"pound: £"; br"pound: £"; br#"pound: £"#;

b"\
hello\
world\
";
b"
hello
world
";
br"\
hello\
world\
";
br#"\
hello\
world\
"#;

pub use kinds::{Copy, Send, Sized, Sync};
pub use ops::{Add, Sub, Mul, Div, Rem, Neg, Not};
pub use ops::{BitAnd, BitOr, BitXor};
pub use ops::{Drop, Deref, DerefMut};
pub use ops::{Shl, Shr};
pub use ops::{Index, IndexMut};
pub use ops::{Slice, SliceMut};
pub use ops::{Fn, FnMut, FnOnce};
pub use from_str::from_str;
pub use iter::{range, repeat};
pub use mem::drop;
pub use ascii::{Ascii, AsciiCast, OwnedAsciiCast, AsciiStr};
pub use ascii::IntoBytes;
pub use c_str::ToCStr;
pub use char::{Char, UnicodeChar};
pub use clone::Clone;
pub use cmp::{PartialEq, PartialOrd, Eq, Ord};
pub use cmp::{Ordering, Less, Equal, Greater, Equiv};
pub use iter::{FromIterator, Extend, ExactSize};
pub use iter::{Iterator, DoubleEndedIterator};
pub use iter::{RandomAccessIterator, CloneableIterator};
pub use iter::{OrdIterator, MutableDoubleEndedIterator};
pub use num::{Num, NumCast, CheckedAdd, CheckedSub, CheckedMul, CheckedDiv};
pub use num::{Signed, Unsigned, Primitive, Int, Float};
pub use num::{FloatMath, ToPrimitive, FromPrimitive};
pub use boxed::Box;
pub use option::{Option, Some, None};
pub use path::{GenericPath, Path, PosixPath, WindowsPath};
pub use ptr::{RawPtr, RawMutPtr};
pub use result::{Result, Ok, Err};
pub use io::{Buffer, Writer, Reader, Seek};
pub use str::{Str, StrVector, StrPrelude};
pub use str::{IntoMaybeOwned, StrAllocating, UnicodeStrPrelude};
pub use to_string::{ToString, IntoStr};
pub use tuple::{Tuple1, Tuple2, Tuple3, Tuple4};
pub use tuple::{Tuple5, Tuple6, Tuple7, Tuple8};
pub use tuple::{Tuple9, Tuple10, Tuple11, Tuple12};
pub use slice::{SlicePrelude, AsSlice, CloneSlicePrelude};
pub use slice::{VectorVector, PartialEqSlicePrelude, OrdSlicePrelude};
pub use slice::{CloneSliceAllocPrelude, OrdSliceAllocPrelude, SliceAllocPrelude};
pub use string::String;
pub use vec::Vec;
pub use comm::{sync_channel, channel};
pub use comm::{SyncSender, Sender, Receiver};
pub use task::spawn;
