# data/plan.py: writes the chapter plan, packages and papers into course.json (LEAD, 2026-11-13)
import json
C = [
 ("cs.overview","Computer Science: the course map","guide","Start here"),
 ("cs.f.basics","Programming from zero: Python and pseudocode","pre","Start here"),
 ("cs.data","Number systems and binary arithmetic","as","AS theory"),
 ("cs.media","Images, sound and compression","as","AS theory"),
 ("cs.networks","Networks: models, topologies and hardware","as","AS theory"),
 ("cs.internet","The internet: IP addresses, DNS and streaming","as","AS theory"),
 ("cs.hardware","Computers and their components","as","AS theory"),
 ("cs.logic","Logic gates and logic circuits","as","AS theory"),
 ("cs.processor","Processor fundamentals and the fetch-execute cycle","as","AS theory"),
 ("cs.assembly","Assembly language and bit manipulation","as","AS theory"),
 ("cs.software","System software: operating systems and translators","as","AS theory"),
 ("cs.security","Security, privacy and data integrity","as","AS theory"),
 ("cs.ethics","Ethics, ownership and the impact of AI","as","AS theory"),
 ("cs.databases","Databases: the relational model and normalisation","as","AS theory"),
 ("cs.sql","DBMS and SQL","as","AS theory"),
 ("cs.algorithms","Computational thinking and algorithms","as","AS programming"),
 ("cs.programming","Programming basics: variables, selection and loops","as","AS programming"),
 ("cs.datatypes","Data types, records and arrays","as","AS programming"),
 ("cs.procedures","Procedures, functions and parameters","as","AS programming"),
 ("cs.structures","Text files, stacks, queues and linked lists","as","AS programming"),
 ("cs.development","The development life cycle and program design","as","AS programming"),
 ("cs.testing","Testing, errors and maintenance","as","AS programming"),
 ("cs.usertypes","User-defined types, file organisation and hashing","a2","A Level theory"),
 ("cs.float","Floating-point numbers","a2","A Level theory"),
 ("cs.networks2","Protocols, TCP/IP and packet switching","a2","A Level theory"),
 ("cs.hardware2","Processors, parallel processing and virtual machines","a2","A Level theory"),
 ("cs.boolean","Boolean algebra, Karnaugh maps, adders and flip-flops","a2","A Level theory"),
 ("cs.os","Operating systems: processes, scheduling and memory","a2","A Level theory"),
 ("cs.translators","Compilers, BNF and Reverse Polish notation","a2","A Level theory"),
 ("cs.security2","Encryption, SSL/TLS and digital certificates","a2","A Level theory"),
 ("cs.ai","Graphs and pathfinding: Dijkstra and A*","a2","A Level theory"),
 ("cs.ml","Machine learning and neural networks","a2","A Level theory"),
 ("cs.algorithms2","Searching, sorting and Big O","a2","A Level programming"),
 ("cs.adts","Abstract data types: stacks, queues, lists, trees and graphs","a2","A Level programming"),
 ("cs.recursion","Recursion","a2","A Level programming"),
 ("cs.oop","Object-oriented programming","a2","A Level programming"),
 ("cs.paradigms","Programming paradigms: low-level, imperative and declarative","a2","A Level programming"),
 ("cs.fileproc","File processing and exception handling","a2","A Level programming"),
 ("cs.python","Python for Paper 4: the practical toolkit","a2","Skills"),
 ("cs.exam.p1","Paper 1 guide: Theory Fundamentals","guide","Exam readiness"),
 ("cs.exam.p2","Paper 2 guide: Problem-solving and Programming","guide","Exam readiness"),
 ("cs.mixed.as","Mixed practice: AS (Papers 1 and 2)","guide","Exam readiness"),
 ("cs.exam.p3","Paper 3 guide: Advanced Theory","guide","Exam readiness"),
 ("cs.exam.p4","Paper 4 guide: the Practical","guide","Exam readiness"),
 ("cs.mixed.a2","Mixed practice: A Level (Papers 3 and 4)","guide","Exam readiness"),
 ("cs.mock.p1","Mock Paper 1: Theory Fundamentals","mock","Exam readiness"),
 ("cs.mock.p2","Mock Paper 2: Problem-solving and Programming","mock","Exam readiness"),
 ("cs.mock.p3","Mock Paper 3: Advanced Theory","mock","Exam readiness"),
 ("cs.mock.p4","Mock Paper 4: Practical","mock","Exam readiness"),
]
P = [
 ("P1","Start here: course map and programming from zero",["cs.overview","cs.f.basics"],[]),
 ("P2","Number systems, images, sound and compression",["cs.data","cs.media"],["cs-binary"]),
 ("P3","Networks and the internet",["cs.networks","cs.internet"],["cs-ip"]),
 ("P4","Hardware and logic gates",["cs.hardware","cs.logic"],["cs-logic"]),
 ("P5","The processor and assembly language",["cs.processor","cs.assembly"],["cs-asm"]),
 ("P6","System software, security and ethics",["cs.software","cs.security","cs.ethics"],["cs-check"]),
 ("P7","Databases and SQL",["cs.databases","cs.sql"],["cs-sql"]),
 ("P8","Algorithms, pseudocode and the basic constructs",["cs.algorithms","cs.programming"],["cs-trace"]),
 ("P9","Arrays, procedures, files and first ADTs",["cs.datatypes","cs.procedures","cs.structures"],["cs-stack"]),
 ("P10","Software development and testing",["cs.development","cs.testing"],[]),
 ("P11","User-defined types, hashing and floating point",["cs.usertypes","cs.float"],["cs-float"]),
 ("P12","Protocols and processors (A Level)",["cs.networks2","cs.hardware2"],["cs-pipeline"]),
 ("P13","Boolean algebra and operating systems",["cs.boolean","cs.os"],["cs-kmap","cs-sched"]),
 ("P14","Translators and encryption",["cs.translators","cs.security2"],["cs-rpn"]),
 ("P15","Artificial intelligence",["cs.ai","cs.ml"],["cs-path"]),
 ("P16","Searching, sorting and ADTs (A Level)",["cs.algorithms2","cs.adts"],["cs-sort"]),
 ("P17","Recursion and object-oriented programming",["cs.recursion","cs.oop"],["cs-calls"]),
 ("P18","Paradigms, file processing and Python for Paper 4",["cs.paradigms","cs.fileproc","cs.python"],[]),
 ("P19","Exam readiness: AS guides and mixed practice",["cs.exam.p1","cs.exam.p2","cs.mixed.as"],[]),
 ("P20","Exam readiness: A Level guides and mixed practice",["cs.exam.p3","cs.exam.p4","cs.mixed.a2"],[]),
 ("P21","Mock Papers 1 and 2",["cs.mock.p1","cs.mock.p2"],[]),
 ("P22","Mock Papers 3 and 4",["cs.mock.p3","cs.mock.p4"],[]),
]
papers = [
 {"id": "P1", "title": "Paper 1: Theory Fundamentals", "chapters": ["cs.data", "cs.media", "cs.networks", "cs.internet", "cs.hardware", "cs.logic", "cs.processor", "cs.assembly", "cs.software", "cs.security", "cs.ethics", "cs.databases", "cs.sql"]},
 {"id": "P2", "title": "Paper 2: Fundamental Problem-solving and Programming Skills", "chapters": ["cs.algorithms", "cs.programming", "cs.datatypes", "cs.procedures", "cs.structures", "cs.development", "cs.testing"]},
 {"id": "P3", "title": "Paper 3: Advanced Theory", "chapters": ["cs.usertypes", "cs.float", "cs.networks2", "cs.hardware2", "cs.boolean", "cs.os", "cs.translators", "cs.security2", "cs.ai", "cs.ml", "cs.algorithms2", "cs.adts", "cs.recursion", "cs.oop", "cs.paradigms", "cs.fileproc"]},
 {"id": "P4", "title": "Paper 4: Practical", "chapters": ["cs.algorithms2", "cs.adts", "cs.recursion", "cs.oop", "cs.fileproc", "cs.python"]},
]
ids = [c[0] for c in C]
pk = [x for p in P for x in p[2]]
assert ids == pk, "packages must list every chapter once, in course order"
w = [x for p in P for x in p[3]]
assert len(w) == len(set(w)), "a widget belongs to one package"
with open("course.json", encoding="utf-8") as f:
    j = json.load(f)
j["chapters"] = [{"id": a, "title": b, "level": c, "group": d} for a, b, c, d in C]
j["aliases"] = {"cs.datarep2": "cs.usertypes", "cs.software2": "cs.os", "cs.exam.p13": "cs.exam.p1", "cs.exam.p24": "cs.exam.p2"}
j["packages"] = [{"id": a, "title": b, "chapters": c, "widgets": d} for a, b, c, d in P]
j["papers"] = papers
j["years"] = "2027–2029"
with open("course.json", "w", encoding="utf-8", newline="\n") as f:
    json.dump(j, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(len(C), "chapters,", len(P), "packages")
