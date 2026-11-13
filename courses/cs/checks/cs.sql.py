# checks/cs.sql.py: runs every SQL statement of the chapter on Python's sqlite3 and compares each result
# table the chapter prints with the rows the database returns.
#   * every ```text fence that starts with SELECT, INSERT, UPDATE, DELETE, ALTER or CREATE is executed;
#   * a SELECT followed by a Markdown table (before the next fence, heading, ::: line or Q:) is compared with it;
#   * state is kept inside one example: it starts again from the printed data at every heading, ::: line and Q:;
#   * a fence whose first line is "-- rejected ..." must be refused by the DBMS (referential integrity).
import pathlib
import re
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "data"))
import cs_sql_data as D  # noqa: E402

CHAPTER = ROOT / "chapters" / "cs.sql.md"
TEXT = CHAPTER.read_text(encoding="utf-8")
LINES = TEXT.split("\n")


def md_table(lines, i):
    """Parse the Markdown table starting at line i; returns (header, rows, next index) or None."""
    if not (i < len(lines) and lines[i].startswith("|")):
        return None
    rows = []
    while i < len(lines) and lines[i].startswith("|"):
        cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        if not all(set(c) <= set("-: ") for c in cells):
            rows.append(cells)
        i += 1
    return rows[0], rows[1:], i


def same(cell, value):
    if value is None:
        return cell in ("", "NULL")
    try:
        return abs(float(cell) - float(value)) < 1e-9
    except (TypeError, ValueError):
        return cell == str(value)


def table_after_text(marker):
    start = TEXT.index(marker)
    lines = TEXT[start:].split("\n")
    for k, ln in enumerate(lines):
        if ln.startswith("|"):
            h, r, _ = md_table(lines, k)
            return h, r
    raise AssertionError(marker)


# ---------------------------------------------------------------------------------------------
# 1. the printed data tables equal the data sets in data/cs_sql_data.py
# ---------------------------------------------------------------------------------------------
for dsname, ds in D.DATASETS.items():
    for t, spec in ds.items():
        h, rows = table_after_text(f"**{t}**\n\n|")
        assert h == [f for f, _ in spec["fields"]], (t, h)
        assert len(rows) == len(spec["rows"]), (t, len(rows))
        for got, want in zip(rows, spec["rows"]):
            assert all(same(c, v) for c, v in zip(got, want)), (t, got, want)

# ---------------------------------------------------------------------------------------------
# 2. run every statement of the chapter
# ---------------------------------------------------------------------------------------------
state = {}


def reset():
    state.clear()


def db_for(name):
    if name not in state:
        state[name] = D.build(name, foreign_keys=True)
    return state[name]


stats = dict(select_table=0, select_plain=0, create=0, alter=0, insert=0, update=0, delete=0, rejected=0, tie_checked=0)
created = {}
KEYWORDS = ("SELECT", "INSERT", "UPDATE", "DELETE", "ALTER", "CREATE")


def order_keys(sql):
    m = re.search(r"ORDER BY (.*?);?\s*$", sql, re.S)
    if not m:
        return []
    keys = []
    for part in m.group(1).split(","):
        part = re.sub(r"\s+(ASC|DESC)\s*$", "", part.strip())
        keys.append(part)
    return keys


def check_select(sql, header_lines_after):
    name = D.dataset_for(sql)
    assert name, sql
    cur = db_for(name).execute(sql)
    cols = [d[0] for d in cur.description]
    rows = cur.fetchall()
    return cols, rows


i = 0
pending_rejected = False
while i < len(LINES):
    ln = LINES[i]
    if re.match(r"^(#{1,6} |:::|Q:)", ln):
        reset()
    if ln.startswith("```text"):
        j = i + 1
        body = []
        while not LINES[j].startswith("```"):
            body.append(LINES[j])
            j += 1
        end = j
        code = [b for b in body]
        comment = [b for b in code if b.startswith("--")]
        sql = "\n".join(b for b in code if not b.startswith("--")).strip()
        first = re.sub(r"^\d+\s+", "", sql.split(None, 1)[0]) if sql else ""
        if sql and sql.split(None, 1)[0].isdigit():
            i = end + 1      # a numbered student answer: shown, not run
            continue
        word = sql.split(None, 1)[0].upper() if sql else ""
        if word not in KEYWORDS or sql.upper().startswith("CREATE DATABASE") or "fields or aggregate" in sql \
                or "TableName" in sql:     # the two template boxes (clause order, CREATE TABLE) are not runnable
            i = end + 1
            continue
        stmts = [s.strip() for s in sql.split(";") if s.strip()]
        for st in stmts:
            kind = st.split(None, 1)[0].upper()
            if comment and comment[0].startswith("-- rejected"):
                name = D.dataset_for(st)
                try:
                    db_for(name).execute(st)
                except sqlite3.IntegrityError:
                    stats["rejected"] += 1
                    continue
                raise AssertionError("statement should have been rejected: " + st)
            if kind == "CREATE":
                con = sqlite3.connect(":memory:")
                con.execute("CREATE TABLE Patient (PatientID INTEGER, PRIMARY KEY (PatientID))")
                con.execute("PRAGMA foreign_keys = ON")
                con.execute(st)
                tname = re.match(r"CREATE TABLE (\w+)", st).group(1)
                created[tname] = st
                stats["create"] += 1
            elif kind == "ALTER":
                name = D.dataset_for(st)
                db_for(name).execute(st)
                stats["alter"] += 1
                if "ADD Email" in st:
                    assert db_for(name).execute("SELECT COUNT(Email), COUNT(*) FROM Student").fetchone() == (0, 12)
            elif kind in ("INSERT", "UPDATE", "DELETE"):
                name = D.dataset_for(st)
                db_for(name).execute(st)
                stats[kind.lower()] += 1
            elif kind == "SELECT":
                cols, rows = check_select(st, None)
                # look for a result table after the fence
                k = end + 1
                table = None
                while k < len(LINES):
                    t = LINES[k]
                    if t.startswith("```") or re.match(r"^(#{1,6} |:::|Q:)", t):
                        break
                    if t.startswith("|"):
                        table = md_table(LINES, k)
                        break
                    k += 1
                if table is None:
                    stats["select_plain"] += 1
                    continue
                header, trows, _ = table
                assert header == cols, f"header {header} != {cols} for\n{st}"
                assert len(trows) == len(rows), f"{len(trows)} rows in the chapter, {len(rows)} computed for\n{st}"
                for a, b in zip(trows, rows):
                    assert len(a) == len(b) and all(same(x, y) for x, y in zip(a, b)), f"row {a} != {b} for\n{st}"
                stats["select_table"] += 1
                # an ORDER BY must not leave ties, or the order shown would not be guaranteed
                keys = order_keys(st)
                if keys:
                    idx = []
                    for kname in keys:
                        short = kname.split(".")[-1] if "(" not in kname else kname
                        if short in cols:
                            idx.append(cols.index(short))
                        elif kname in cols:
                            idx.append(cols.index(kname))
                    if len(idx) == len(keys):
                        seen = [tuple(r[x] for x in idx) for r in rows]
                        assert len(seen) == len(set(seen)), f"ties in ORDER BY would make the order undefined:\n{st}"
                        stats["tie_checked"] += 1
        i = end + 1
        continue
    i += 1

print(stats)
assert stats == dict(select_table=42, select_plain=1, create=5, alter=2, insert=5, update=5, delete=9, rejected=2,
                     tie_checked=11), stats

# ---------------------------------------------------------------------------------------------
# 3. the CREATE TABLE statements of the chapter build the data set
# ---------------------------------------------------------------------------------------------
con = sqlite3.connect(":memory:")
con.execute("PRAGMA foreign_keys = ON")
con.execute(created["Club"])
con.execute(created["Student"])
con.executemany("INSERT INTO Club VALUES (?, ?, ?, ?, ?)", D.SCHOOL["Club"]["rows"])
con.executemany("INSERT INTO Student VALUES (?, ?, ?, ?, ?, ?)", D.SCHOOL["Student"]["rows"])
assert con.execute("SELECT COUNT(*) FROM Student").fetchone()[0] == 12
try:
    con.execute("INSERT INTO Student VALUES (999, 'X', '10A', '2011-01-01', 0, 'NOPE')")
    raise AssertionError("the foreign key declared in CREATE TABLE must be enforced")
except sqlite3.IntegrityError:
    pass
shop = sqlite3.connect(":memory:")
shop.execute("PRAGMA foreign_keys = ON")
shop.execute(created["Product"])
shop.execute(created["Sale"])
shop.executemany("INSERT INTO Product VALUES (?, ?, ?, ?, ?)", D.SHOP["Product"]["rows"])
shop.executemany("INSERT INTO Sale VALUES (?, ?, ?, ?, ?)", D.SHOP["Sale"]["rows"])
for bad in ("INSERT INTO Sale VALUES (17, 12, 1, '2026-10-09', 'Accra')",):
    try:
        shop.execute(bad)
        raise AssertionError("product 12 does not exist")
    except sqlite3.IntegrityError:
        pass

# ---------------------------------------------------------------------------------------------
# 4. numbers quoted in the prose, the quiz and the hints
# ---------------------------------------------------------------------------------------------
school = D.build("school", foreign_keys=True)


def one(sql, db=school):
    return db.execute(sql).fetchall()


assert one("SELECT COUNT(*), SUM(Points) FROM Student") == [(12, 540)] and 540 / 12 == 45
assert one("SELECT COUNT(*) FROM Student WHERE Points > 50") == [(5,)]       # "the result has five rows"
assert one("SELECT AVG(Points) FROM Student WHERE Form = '10B'") == [(39.0,)] and (58 + 24 + 35) / 3 == 39
assert one("SELECT COUNT(*) FROM Student, Club") == [(72,)] and 12 * 6 == 72
assert sum(r[1] for r in one("SELECT Form, SUM(Points) FROM Student GROUP BY Form")) == 540
assert 2 * 5 + 4 * 12.5 + 2 * 8 + 2 * 10 + 2 * 15 == 126
assert one("SELECT SUM(Club.Fee) FROM Student INNER JOIN Club ON Student.ClubCode = Club.ClubCode") == [(126.0,)]
assert one("SELECT COUNT(*) FROM Student WHERE Form = '10A'") == [(3,)]      # quiz
assert 46 + 39 + 41 + 55 == 181 and 58 + 63 == 121                           # Coding and Chess sums
assert one("SELECT Points FROM Student WHERE ClubCode = 'RB01' ORDER BY StudentID") == [(24,), (35,)]   # before the update
assert one("SELECT COUNT(*) FROM Club WHERE ClubCode NOT IN (SELECT ClubCode FROM Student)") == [(1,)]  # Swimming only
# empty fields: COUNT(*) versus COUNT(Phone)
assert one("SELECT COUNT(*), COUNT(Phone) FROM Contact", D.build("contact")) == [(4, 2)]
# an aggregate in WHERE is refused by the DBMS (the stretch error list)
try:
    school.execute("SELECT Form, COUNT(*) FROM Student WHERE COUNT(*) > 1 GROUP BY Form")
    raise AssertionError("an aggregate in WHERE should be an error")
except sqlite3.Error:
    pass
shopdb = D.build("shop", foreign_keys=True)
assert one("SELECT SUM(Quantity) FROM Sale", shopdb) == [(90,)] and 42 + 48 == 90 and 68 + 7 + 2 + 10 + 3 == 90
assert one("SELECT COUNT(*) FROM Sale WHERE SaleDate < '2026-10-03'", shopdb) == [(4,)]
assert one("SELECT Stock FROM Product WHERE ProductID = 4", shopdb) == [(40,)]
assert (2.5 + 0.8 + 1.2) / 3 == 1.5
assert one("SELECT COUNT(*) FROM Sale WHERE ProductID = 8", shopdb) == [(1,)]       # the Ruler has one sale
assert 1 + 12 + 2 + 15 + 3 == 33 and 3 + 1 == 4 and 10 + 12 + 15 == 37
assert one("SELECT SUM(Quantity) FROM Sale WHERE ProductID = 1", shopdb) == [(16,)] and 10 + 6 == 16
# ambiguous field names must be qualified
try:
    school.execute("SELECT ClubCode FROM Student INNER JOIN Club ON Student.ClubCode = Club.ClubCode")
    raise AssertionError("ClubCode is ambiguous in the join")
except sqlite3.OperationalError:
    pass

print("ok")
