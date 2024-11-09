import langchain
from langchain_openai import ChatOpenAI

from questions import MCQQuestion, MCQSet

from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini").with_structured_output(MCQSet)

example = """Our hello program begins life as a source program (or source file) that the
programmer creates with an editor and saves in a text file called hello.c. The
source program is a sequence of bits, each with a value of 0 or 1, organized
in 8-bit chunks called bytes. Each byte represents some text character in the
program.
Most modern systems represent text characters using the ASCII standard that
represents each character with a unique byte-sized integer value. For example,
Figure 1.2 shows the ASCII representation of the hello.c program.
The hello.c program is stored in a file as a sequence of bytes. Each byte has
an integer value that corresponds to some character. For example, the first byte
has the integer value 35, which corresponds to the character '#'. The second byte
has the integer value 105, which corresponds to the character 'i', and so on. Notice
that each text line is terminated by the invisible newline character '\\n', which is
represented by the integer value 10. Files such as hello.c that consist exclusively
of ASCII characters are known as text files. All other files are known as binary
files.
The representation of hello.c illustrates a fundamental idea: All information
in a system—including disk files, programs stored in memory, user data stored in
memory, and data transferred across a network—is represented as a bunch of bits.
The only thing that distinguishes different data objects is the context in which
we view them. For example, in different contexts, the same sequence of bytes
might represent an integer, floating-point number, character string, or machine
instruction.
As programmers, we need to understand machine representations of numbers
because they are not the same as integers and real numbers. They are finite
approximations that can behave in unexpected ways. This fundamental idea is
explored in detail in Chapter 2.
# i n c l u d e <sp> < s t d i o .
35 105 110 99 108 117 100 101 32 60 115 116 100 105 111 46
h > \\n \\n i n t <sp> m a i n ( ) \\n {
104 62 10 10 105 110 116 32 109 97 105 110 40 41 10 123
\\n <sp> <sp> <sp> <sp> p r i n t f ( " h e l
10 32 32 32 32 112 114 105 110 116 102 40 34 104 101 108
l o , <sp> w o r l d \\ n " ) ; \\n }
108 111 44 32 119 111 114 108 100 92 110 34 41 59 10 125
Figure 1.2 The ASCII text representation of hello.c.
4 Chapter 1 A Tour of Computer Systems
Aside Origins of the C programming language
C was developed from 1969 to 1973 by Dennis Ritchie of Bell Laboratories. The American National
Standards Institute (ANSI) ratified the ANSI C standard in 1989, and this standardization later became
the responsibility of the International Standards Organization (ISO). The standards define the C
language and a set of library functions known as the C standard library. Kernighan and Ritchie describe
ANSI C in their classic book, which is known affectionately as “K&R” [58]. In Ritchie's words [88], C
is “quirky, flawed, and an enormous success.” So why the success?
. C was closely tied with the Unix operating system. C was developed from the beginning as the
system programming language for Unix. Most of the Unix kernel, and all of its supporting tools
and libraries, were written in C. As Unix became popular in universities in the late 1970s and early
1980s, many people were exposed to C and found that they liked it. Since Unix was written almost
entirely in C, it could be easily ported to new machines, which created an even wider audience for
both C and Unix.
. C is a small, simple language.The design was controlled by a single person, rather than a committee,
and the result was a clean, consistent design with little baggage. The K&R book describes the
complete language and standard library, with numerous examples and exercises, in only 261 pages.
The simplicity of C made it relatively easy to learn and to port to different computers.
. C was designed for a practical purpose. C was designed to implement the Unix operating system.
Later, other people found that they could write the programs they wanted, without the language
getting in the way.
C is the language of choice for system-level programming, and there is a huge installed base of
application-level programs as well. However, it is not perfect for all programmers and all situations.
C pointers are a common source of confusion and programming errors. C also lacks explicit support
for useful abstractions such as classes, objects, and exceptions. Newer languages such as C++ and Java
address these issues for application-level programs.
"""

questions = llm.invoke("Please generate some MCQ questions from the following text:\n\n" + example)

for question in questions.questions:
    print(question.question)
    print(question.options)
    print(question.answer)
    print()
