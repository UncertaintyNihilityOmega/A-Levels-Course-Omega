# data/cs_sql_data.py: the data sets used by cs.sql, its checks and the cs-sql widget (single source).
#   py data/cs_sql_data.py --embed   rewrites the DATA block inside widgets/cs-sql.js
#   py data/cs_sql_data.py --cases   writes scratch/sql_cases.json (every widget query spec with sqlite's result)
import json
import pathlib
import re
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Each data set: tables -> {fields: [(name, type)], pk, fk: (field, table, field) or None, rows: [...]}
# types: int, real, text, date (the widget formats real with 2 decimals)
SCHOOL = {
    "Student": {
        "fields": [("StudentID", "int"), ("FirstName", "text"), ("Form", "text"), ("BirthDate", "date"),
                   ("Points", "int"), ("ClubCode", "text")],
        "pk": "StudentID", "fk": ("ClubCode", "Club", "ClubCode"),
        "rows": [
            (101, "Amina", "10A", "2011-03-14", 46, "CO01"),
            (102, "Bilal", "10A", "2011-07-02", 31, "FB01"),
            (103, "Chioma", "10B", "2010-11-23", 58, "CH01"),
            (104, "Dev", "10B", "2011-01-30", 24, "RB01"),
            (105, "Elena", "11A", "2010-05-19", 67, "DR01"),
            (106, "Farid", "11A", "2010-09-08", 39, "CO01"),
            (107, "Grace", "11B", "2010-12-01", 52, "FB01"),
            (108, "Hiro", "11B", "2011-02-17", 41, "CO01"),
            (109, "Ingrid", "10A", "2011-08-25", 29, "DR01"),
            (110, "Jamal", "10B", "2011-04-09", 35, "RB01"),
            (111, "Kofi", "11A", "2010-06-30", 63, "CH01"),
            (112, "Lucia", "11B", "2010-10-12", 55, "CO01"),
        ],
    },
    "Club": {
        "fields": [("ClubCode", "text"), ("ClubName", "text"), ("MeetingDay", "text"), ("Room", "text"),
                   ("Fee", "real")],
        "pk": "ClubCode", "fk": None,
        "rows": [
            ("CH01", "Chess", "Monday", "B12", 5.0),
            ("CO01", "Coding", "Tuesday", "L3", 12.5),
            ("DR01", "Drama", "Wednesday", "Hall", 8.0),
            ("FB01", "Football", "Thursday", "Field", 10.0),
            ("RB01", "Robotics", "Friday", "L3", 15.0),
            ("SW01", "Swimming", "Saturday", "Pool", 20.0),
        ],
    },
}

SHOP = {
    "Product": {
        "fields": [("ProductID", "int"), ("ProductName", "text"), ("Category", "text"), ("Price", "real"),
                   ("Stock", "int")],
        "pk": "ProductID", "fk": None,
        "rows": [
            (1, "Notebook", "Stationery", 2.5, 120),
            (2, "Pen", "Stationery", 0.8, 300),
            (3, "Backpack", "Bags", 24.0, 35),
            (4, "Calculator", "Electronics", 18.5, 40),
            (5, "Headphones", "Electronics", 32.0, 22),
            (6, "Water bottle", "Outdoor", 7.5, 60),
            (7, "Torch", "Outdoor", 11.0, 25),
            (8, "Ruler", "Stationery", 1.2, 150),
            (9, "Lunch box", "Kitchen", 9.0, 45),
        ],
    },
    "Sale": {
        "fields": [("SaleID", "int"), ("ProductID", "int"), ("Quantity", "int"), ("SaleDate", "date"),
                   ("Branch", "text")],
        "pk": "SaleID", "fk": ("ProductID", "Product", "ProductID"),
        "rows": [
            (1, 3, 2, "2026-10-01", "Accra"),
            (2, 1, 10, "2026-10-01", "Kumasi"),
            (3, 5, 1, "2026-10-02", "Accra"),
            (4, 2, 25, "2026-10-02", "Accra"),
            (5, 4, 3, "2026-10-03", "Kumasi"),
            (6, 6, 4, "2026-10-03", "Accra"),
            (7, 1, 6, "2026-10-04", "Accra"),
            (8, 9, 2, "2026-10-04", "Kumasi"),
            (9, 3, 1, "2026-10-05", "Kumasi"),
            (10, 7, 3, "2026-10-05", "Accra"),
            (11, 8, 12, "2026-10-06", "Kumasi"),
            (12, 5, 2, "2026-10-06", "Kumasi"),
            (13, 2, 15, "2026-10-07", "Kumasi"),
            (14, 4, 1, "2026-10-07", "Accra"),
            (15, 6, 3, "2026-10-08", "Kumasi"),
        ],
    },
}

# A tiny table for the COUNT(*) versus COUNT(field) warning (an empty field is NULL)
CONTACT = {
    "Contact": {
        "fields": [("ContactID", "int"), ("Name", "text"), ("Phone", "text")],
        "pk": "ContactID", "fk": None,
        "rows": [(1, "Asha", "0712 000 111"), (2, "Bruno", None), (3, "Carla", "0733 222 444"), (4, "Dmitri", None)],
    }
}

DATASETS = {"school": SCHOOL, "shop": SHOP, "contact": CONTACT}
SQLTYPE = {"int": "INTEGER", "real": "REAL", "text": "VARCHAR(30)", "date": "DATE"}


def build(name, foreign_keys=False):
    """Return an in-memory sqlite database holding the named data set (parents are created first)."""
    con = sqlite3.connect(":memory:")
    if foreign_keys:
        con.execute("PRAGMA foreign_keys = ON")
    ds = DATASETS[name]
    order = sorted(ds, key=lambda t: 1 if ds[t]["fk"] else 0)
    for t in order:
        spec = ds[t]
        cols = ", ".join(f"{f} {SQLTYPE[k]}" for f, k in spec["fields"])
        extra = f", PRIMARY KEY ({spec['pk']})"
        if spec["fk"]:
            extra += f", FOREIGN KEY ({spec['fk'][0]}) REFERENCES {spec['fk'][1]}({spec['fk'][2]})"
        con.execute(f"CREATE TABLE {t} ({cols}{extra})")
        marks = ", ".join("?" for _ in spec["fields"])
        con.executemany(f"INSERT INTO {t} VALUES ({marks})", spec["rows"])
    con.commit()
    return con


def table_names(name):
    return list(DATASETS[name])


def dataset_for(sql):
    """Which data set a statement belongs to, from the table names it mentions."""
    words = set(re.findall(r"[A-Za-z_]+", sql))
    for name, ds in DATASETS.items():
        if words & set(ds):
            return name
    return None


# ---------------------------------------------------------------------------------------------
# widget query specs (the same model the widget builds) -> SQL text -> sqlite result
# ---------------------------------------------------------------------------------------------
def spec_to_sql(db, spec):
    """spec: {from: 'Student' | 'join', select: [field or [func, field]], where: [[field, op, value], ...] with
    'and'/'or' in spec['bool'], group: field or None, order: [key, 'ASC'|'DESC'] or None}"""
    ds = DATASETS[db]
    tables = list(ds)
    child = next(t for t in tables if ds[t]["fk"])
    parent = ds[child]["fk"][1]
    fk = ds[child]["fk"]
    joined = spec["from"] == "join"
    sel = []
    for s in spec["select"]:
        sel.append(f"{s[0]}({s[1]})" if isinstance(s, list) else s)
    lines = ["SELECT " + ", ".join(sel)]
    if joined:
        lines.append(f"FROM {child}")
        lines.append(f"INNER JOIN {parent} ON {child}.{fk[0]} = {parent}.{fk[2]}")
    else:
        lines.append(f"FROM {spec['from']}")
    if spec.get("where"):
        parts = []
        for f, op, v in spec["where"]:
            parts.append(f"{f} {op} {v}")
        lines.append("WHERE " + f" {spec.get('bool', 'AND')} ".join(parts))
    if spec.get("group"):
        lines.append("GROUP BY " + spec["group"])
    if spec.get("order"):
        lines.append(f"ORDER BY {spec['order'][0]} {spec['order'][1]}")
    return "\n".join(lines)


def run(db, sql):
    con = build(db)
    cur = con.execute(sql)
    return [d[0] for d in cur.description], cur.fetchall()


def qualified_fields(db, joined, table=None):
    ds = DATASETS[db]
    tables = list(ds)
    child = next(t for t in tables if ds[t]["fk"])
    parent = ds[child]["fk"][1]
    if joined:
        return [(f"{t}.{f}", k) for t in (child, parent) for f, k in ds[t]["fields"]]
    return [(f, k) for f, k in ds[table]["fields"]]


def all_cases(db):
    """A broad sweep of valid widget specs (and, for the error rules, the invalid ones the widget must refuse)."""
    ds = DATASETS[db]
    tables = list(ds)
    child = next(t for t in tables if ds[t]["fk"])
    cases = []
    sources = [(t, False, t) for t in tables] + [("join", True, None)]
    for src, joined, tbl in sources:
        fields = qualified_fields(db, joined, tbl)
        names = [f for f, _ in fields]
        kinds = dict(fields)
        nums = [f for f, k in fields if k in ("int", "real")]
        # sample values per field for WHERE
        base = [f.split(".")[-1] for f in names]
        wheres = [None]
        for f, k in fields:
            short = f.split(".")[-1]
            tname = f.split(".")[0] if "." in f else tbl
            rows = ds[tname]["rows"]
            idx = [x for x, _ in ds[tname]["fields"]].index(short)
            vals = sorted({r[idx] for r in rows if r[idx] is not None}, key=lambda v: (str(type(v)), v))
            pick = [vals[0], vals[len(vals) // 2], vals[-1]]
            ops = ["=", "<>", "<", "<=", ">", ">="] if k != "text" else ["=", "<>", "<", ">"]
            for op in ops:
                for v in pick[:2]:
                    lit = f"'{v}'" if k in ("text", "date") else repr(v)
                    wheres.append([[f, op, lit]])
        # plain selects
        selects = [[n] for n in names] + [names[:2], names[1:4], names]
        groups = [None] + names
        for sel in selects:
            for w in wheres[::3] if len(wheres) > 40 else wheres:
                for o in [None, [sel[0], "ASC"], [sel[0], "DESC"]]:
                    cases.append({"db": db, "from": src, "select": sel, "where": w and [w[0]], "group": None, "order": o})
        # aggregates
        aggs = [["COUNT", "*"]] + [["COUNT", n] for n in names] + [[fn, n] for n in nums for fn in ("SUM", "AVG")]
        for a in aggs:
            for g in groups:
                sel = ([g] if g else []) + [a]
                for w in wheres[::2]:
                    for o in [None, [g, "ASC"] if g else None, [g, "DESC"] if g else None,
                              [f"{a[0]}({a[1]})", "DESC"]]:
                        cases.append({"db": db, "from": src, "select": sel, "where": w and [w[0]], "group": g, "order": o})
        # two conditions
        for w1 in wheres[1::5]:
            for w2 in wheres[2::7]:
                for b in ("AND", "OR"):
                    cases.append({"db": db, "from": src, "select": names[:2], "where": [w1[0], w2[0]], "bool": b,
                                  "group": None, "order": [names[0], "ASC"]})
    # remove duplicates
    seen, out = set(), []
    for c in cases:
        key = json.dumps(c, sort_keys=True)
        if key not in seen:
            seen.add(key)
            out.append(c)
    import random
    random.Random(7).shuffle(out)
    return out[:6000]      # a seeded sample of the sweep keeps the test fast


def embed():
    data = {}
    for name in ("school", "shop"):
        ds = DATASETS[name]
        data[name] = {"tables": [{"name": t, "fields": [{"n": f, "k": k} for f, k in ds[t]["fields"]],
                                  "pk": ds[t]["pk"], "fk": ds[t]["fk"], "rows": ds[t]["rows"]} for t in ds]}
    block = "// DATA-BEGIN (generated by data/cs_sql_data.py --embed; do not edit by hand)\n  const DATA = " + \
            json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n  // DATA-END"
    path = ROOT / "widgets" / "cs-sql.js"
    text = path.read_text(encoding="utf-8")
    new = re.sub(r"// DATA-BEGIN.*?// DATA-END", lambda m: block, text, flags=re.S)
    path.write_text(new, encoding="utf-8")
    print("embedded", len(block), "characters")


def cases():
    out = []
    for db in ("school", "shop"):
        for c in all_cases(db):
            sql = spec_to_sql(db, c)
            try:
                cols, rows = run(db, sql)
                c = dict(c, sql=sql, rows=rows, cols=cols)
            except sqlite3.Error as e:
                c = dict(c, sql=sql, error=str(e))
            out.append(c)
    (ROOT / "scratch").mkdir(exist_ok=True)
    (ROOT / "scratch" / "sql_cases.json").write_text(json.dumps(out), encoding="utf-8")
    print(len(out), "cases,", sum(1 for c in out if "error" in c), "sqlite errors")


if __name__ == "__main__":
    if "--embed" in sys.argv:
        embed()
    if "--cases" in sys.argv:
        cases()
