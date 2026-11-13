# checks/cs.databases.py: recomputes every table, count and dependency the chapter states.
# The tables are rebuilt in Python (and in sqlite3, for the joins and the referential-integrity examples) and
# compared with the Markdown tables printed in the chapter.
import math
import pathlib
import re
import sqlite3

CHAPTER_ID = "cs.databases"
CHAPTER = pathlib.Path(__file__).resolve().parent.parent / "chapters" / f"{CHAPTER_ID}.md"
TEXT = CHAPTER.read_text(encoding="utf-8")
FENCES = list(re.finditer(r"^```(\w+)\n(.*?)^```", TEXT, re.S | re.M))
assert not [f for f in FENCES if f.group(1) in ("python", "pseudocode")], "this chapter has no code blocks"


def table_after(marker, nth=0):
    """Header and rows of the first Markdown table after the text marker (bold markers stripped)."""
    start = -1
    for _ in range(nth + 1):
        start = TEXT.index(marker, start + 1)
    rows = []
    for line in TEXT[start:].split("\n"):
        if line.startswith("|"):
            cells = [re.sub(r"^\*\*(.*)\*\*$", r"\1", c.strip()) for c in line.strip().strip("|").split("|")]
            if not all(set(c) <= set("-: ") for c in cells):
                rows.append(cells)
        elif rows:
            break
    return rows[0], rows[1:]


def as_dicts(header, rows):
    return [dict(zip(header, r)) for r in rows]


def fd_holds(rows, lhs, rhs):
    """True when every value of the lhs fields determines exactly one value of the rhs fields."""
    seen = {}
    for r in rows:
        k = tuple(r[f] for f in lhs)
        v = tuple(r[f] for f in rhs)
        if seen.setdefault(k, v) != v:
            return False
    return True


def unique(rows, fields):
    keys = [tuple(r[f] for f in fields) for r in rows]
    return len(keys) == len(set(keys))


# ---------------------------------------------------------------------------------------------
# Warm-up
# ---------------------------------------------------------------------------------------------
assert 2000 * 256 == 512000 and 512000 / 1024 == 500

# ---------------------------------------------------------------------------------------------
# The flat file and its anomalies
# ---------------------------------------------------------------------------------------------
fh, fr = table_after("| StudentID | StudentName | Form | FormTutor |")
flat = as_dicts(fh, fr)
assert len(flat) == 10 and fh == ["StudentID", "StudentName", "Form", "FormTutor", "ClubName", "ClubDay", "ClubLeader"]
assert sum(1 for r in flat if r["ClubName"] == "Chess") == 4            # "stored four times"
assert sum(1 for r in flat if r["FormTutor"] == "Mr Adeyemi") == 3       # "stored three times"
assert sum(1 for r in flat if r["ClubName"] == "Swimming") == 1          # the deletion anomaly
assert sum(1 for r in flat if r["Form"] == "11B") == 1                   # 11B and Mr Okafor appear only in Grace's row
assert {r["StudentID"] for r in flat if r["ClubName"] == "Swimming"} == {"107"}
assert fd_holds(flat, ["ClubName"], ["ClubDay", "ClubLeader"]) and fd_holds(flat, ["Form"], ["FormTutor"])
assert fd_holds(flat, ["StudentID"], ["StudentName", "Form"])
assert not unique(flat, ["StudentID"])                                   # a student is in several rows

# ---------------------------------------------------------------------------------------------
# The relational design: four tables rebuilt from the flat file, and the join gives the flat file back
# ---------------------------------------------------------------------------------------------
club_ids = {"Chess": "C1", "Robotics": "C2", "Drama": "C3", "Swimming": "C4"}
student = sorted({(r["StudentID"], r["StudentName"], r["Form"]) for r in flat})
form = sorted({(r["Form"], r["FormTutor"]) for r in flat})
club = sorted({(club_ids[r["ClubName"]], r["ClubName"], r["ClubDay"], r["ClubLeader"]) for r in flat})
membership = [(r["StudentID"], club_ids[r["ClubName"]]) for r in flat]


def chapter_rows(marker):
    h, r = table_after(marker)
    return h, [tuple(x) for x in r]


h, rows = chapter_rows("**STUDENT**")
assert h == ["StudentID", "StudentName", "FormID"] and rows == student
h, rows = chapter_rows("**FORM**")
assert h == ["FormID", "FormTutor"] and rows == form
h, rows = chapter_rows("**CLUB**")
assert h == ["ClubID", "ClubName", "ClubDay", "ClubLeader"] and rows == club
h, rows = chapter_rows("**MEMBERSHIP**")
assert h == ["StudentID", "ClubID"] and sorted(rows) == sorted(membership) and rows == membership
assert sum(1 for m in membership if m[0] == "103") == 3 and sum(1 for m in membership if m[1] == "C1") == 4
assert len(set(membership)) == len(membership)                           # the composite key is unique

con = sqlite3.connect(":memory:")
con.execute("PRAGMA foreign_keys = ON")
con.executescript("""
CREATE TABLE Form (FormID CHARACTER(3), FormTutor VARCHAR(20), PRIMARY KEY (FormID));
CREATE TABLE Club (ClubID CHARACTER(2), ClubName VARCHAR(20), ClubDay VARCHAR(10), ClubLeader VARCHAR(20), PRIMARY KEY (ClubID));
CREATE TABLE Student (StudentID INTEGER, StudentName VARCHAR(30), FormID CHARACTER(3), PRIMARY KEY (StudentID),
  FOREIGN KEY (FormID) REFERENCES Form (FormID));
CREATE TABLE Membership (StudentID INTEGER, ClubID CHARACTER(2), PRIMARY KEY (StudentID, ClubID),
  FOREIGN KEY (StudentID) REFERENCES Student (StudentID), FOREIGN KEY (ClubID) REFERENCES Club (ClubID));
""")
con.executemany("INSERT INTO Form VALUES (?, ?)", form)
con.executemany("INSERT INTO Club VALUES (?, ?, ?, ?)", club)
con.executemany("INSERT INTO Student VALUES (?, ?, ?)", [(int(a), b, c) for a, b, c in student])
con.executemany("INSERT INTO Membership VALUES (?, ?)", [(int(a), b) for a, b in membership])
joined = con.execute("""SELECT Student.StudentID, StudentName, Form.FormID, FormTutor, ClubName, ClubDay, ClubLeader
  FROM Membership INNER JOIN Student ON Membership.StudentID = Student.StudentID
  INNER JOIN Form ON Student.FormID = Form.FormID INNER JOIN Club ON Membership.ClubID = Club.ClubID""").fetchall()
assert sorted(joined) == sorted((int(r["StudentID"]), r["StudentName"], r["Form"], r["FormTutor"], r["ClubName"],
                                 r["ClubDay"], r["ClubLeader"]) for r in flat)


def refused(sql):
    try:
        con.execute(sql)
    except sqlite3.IntegrityError:
        return True
    return False


assert refused("INSERT INTO Membership VALUES (108, 'C1')")             # no student 108
assert refused("INSERT INTO Membership VALUES (101, 'C9')")             # no club C9
assert refused("DELETE FROM Student WHERE StudentID = 103")             # still has memberships
assert refused("UPDATE Club SET ClubID = 'C7' WHERE ClubID = 'C1'")    # members still point at C1
assert not refused("DELETE FROM Membership WHERE StudentID = 107")      # membership first ...
assert not refused("DELETE FROM Student WHERE StudentID = 107")         # ... then the student, and Swimming survives
assert con.execute("SELECT COUNT(*) FROM Club WHERE ClubName = 'Swimming'").fetchone()[0] == 1

# ---------------------------------------------------------------------------------------------
# Keys: the employee table
# ---------------------------------------------------------------------------------------------
eh, er = table_after("| EmployeeID | NationalIDNumber | Email |")
emp = as_dicts(eh, er)
assert [f for f in eh if unique(emp, [f])] == ["EmployeeID", "NationalIDNumber", "Email", "Name"]
assert not unique(emp, ["DepartmentCode"])    # shared by several employees (and Name is only unique by luck of the rows)

# ---------------------------------------------------------------------------------------------
# Index: the sorted index and the "about 20 comparisons" claim
# ---------------------------------------------------------------------------------------------
ih, ir = table_after("| StudentName (sorted) | Record number |")
names = [r[1] for r in table_after("**STUDENT**")[1]]
assert [r[0] for r in ir] == sorted(names) and [int(r[1]) for r in ir] == [names.index(r[0]) + 1 for r in ir]
assert 2 ** 20 == 1048576 and math.ceil(math.log2(1_000_000)) == 20

# ---------------------------------------------------------------------------------------------
# Worked normalisation: the order book
# ---------------------------------------------------------------------------------------------
uh, ur = table_after("**Unnormalised data**")
unf = as_dicts(uh, ur)
rows1 = []
for r in unf:
    for item in r["Items ordered"].split(";"):
        m = re.match(r"\s*(P\d+) (.+?) (\d+\.\d\d) × (\d+)\s*$", item)
        assert m, item
        pid, pname, price, qty = m.groups()
        rows1.append({"OrderID": r["OrderID"], "ProductID": pid, "OrderDate": r["OrderDate"],
                      "CustomerID": r["CustomerID"], "CustomerName": r["CustomerName"], "City": r["City"],
                      "ProductName": pname, "UnitPrice": price, "Quantity": qty})
h1, r1 = table_after("**First normal form.**")
assert len(rows1) == 7 and as_dicts(h1, r1) == rows1
assert unique(rows1, ["OrderID", "ProductID"])
assert not unique(rows1, ["OrderID"]) and not unique(rows1, ["ProductID"])
# the dependencies the chapter states
assert fd_holds(rows1, ["OrderID"], ["OrderDate", "CustomerID"])
assert fd_holds(rows1, ["CustomerID"], ["CustomerName", "City"])
assert fd_holds(rows1, ["ProductID"], ["ProductName", "UnitPrice"])
assert fd_holds(rows1, ["OrderID", "ProductID"], ["Quantity"])
assert not fd_holds(rows1, ["OrderID"], ["Quantity"]) and not fd_holds(rows1, ["ProductID"], ["Quantity"])
# redundancy remarks: Mercy five times, the stapler three times (the stapler appears twice: P20 twice)
assert sum(1 for r in rows1 if r["CustomerName"] == "Mercy Banda") == 5
assert sum(1 for r in rows1 if r["ProductName"] == "Pencil box") == 3 and sum(1 for r in rows1 if r["ProductName"] == "Stapler") == 2
customer = sorted({(r["CustomerID"], r["CustomerName"], r["City"]) for r in rows1})
orders = sorted({(r["OrderID"], r["OrderDate"], r["CustomerID"]) for r in rows1})
product = sorted({(r["ProductID"], r["ProductName"], r["UnitPrice"]) for r in rows1})
orderline = [(r["OrderID"], r["ProductID"], r["Quantity"]) for r in rows1]
for marker, want in (("**CUSTOMER**", customer), ("**ORDERS**", orders), ("**PRODUCT**", product),
                     ("**ORDERLINE**", orderline)):
    h, rows = chapter_rows(marker)
    assert rows == want, (marker, rows, want)
# the join of the four tables rebuilds the 1NF rows
con2 = sqlite3.connect(":memory:")
con2.executescript("""CREATE TABLE Customer (CustomerID, CustomerName, City); CREATE TABLE Orders (OrderID, OrderDate, CustomerID);
CREATE TABLE Product (ProductID, ProductName, UnitPrice); CREATE TABLE OrderLine (OrderID, ProductID, Quantity);""")
con2.executemany("INSERT INTO Customer VALUES (?,?,?)", customer)
con2.executemany("INSERT INTO Orders VALUES (?,?,?)", orders)
con2.executemany("INSERT INTO Product VALUES (?,?,?)", product)
con2.executemany("INSERT INTO OrderLine VALUES (?,?,?)", orderline)
rebuilt = con2.execute("""SELECT Orders.OrderID, Product.ProductID, OrderDate, Customer.CustomerID, CustomerName, City,
  ProductName, UnitPrice, Quantity FROM OrderLine INNER JOIN Orders ON OrderLine.OrderID = Orders.OrderID
  INNER JOIN Customer ON Orders.CustomerID = Customer.CustomerID
  INNER JOIN Product ON OrderLine.ProductID = Product.ProductID""").fetchall()
assert sorted(rebuilt) == sorted(tuple(r[k] for k in ("OrderID", "ProductID", "OrderDate", "CustomerID", "CustomerName",
                                                       "City", "ProductName", "UnitPrice", "Quantity")) for r in rows1)
assert len(orders) == 4 and len(customer) == 3 and len(product) == 3 and len(orderline) == 7

# ---------------------------------------------------------------------------------------------
# Exam practice: the garage data (question and the model answer)
# ---------------------------------------------------------------------------------------------
gh, gr = table_after("| JobID | JobDate | Registration | VehicleType |")
garage = as_dicts(gh, gr)
g1 = []
for r in garage:
    for item in r["Work done (code, description, hours)"].split(";"):
        m = re.match(r"\s*(W\d) (.+?) (\d+\.\d+)\s*$", item)
        assert m, item
        g1.append(dict(JobID=r["JobID"], JobDate=r["JobDate"], Registration=r["Registration"], VehicleType=r["VehicleType"],
                       OwnerName=r["OwnerName"], WorkCode=m.group(1), WorkDescription=m.group(2), Hours=m.group(3)))
assert unique(g1, ["JobID", "WorkCode"]) and not unique(g1, ["JobID"]) and not unique(g1, ["WorkCode"])
assert fd_holds(g1, ["JobID"], ["JobDate", "Registration"])
assert fd_holds(g1, ["Registration"], ["VehicleType", "OwnerName"])
assert fd_holds(g1, ["WorkCode"], ["WorkDescription"])
assert fd_holds(g1, ["JobID", "WorkCode"], ["Hours"])
assert not fd_holds(g1, ["WorkCode"], ["Hours"]) and not fd_holds(g1, ["JobID"], ["Hours"])     # Hours needs the whole key
assert not fd_holds(g1, ["JobID"], ["WorkDescription"])
job = sorted({(r["JobID"], r["JobDate"], r["Registration"]) for r in g1})
vehicle = sorted({(r["Registration"], r["VehicleType"], r["OwnerName"]) for r in g1})
work = sorted({(r["WorkCode"], r["WorkDescription"]) for r in g1})
jobwork = [(r["JobID"], r["WorkCode"], r["Hours"]) for r in g1]
assert len(job) == 4 and len(vehicle) == 3 and len(work) == 3 and len(jobwork) == 6   # KDA214T has two jobs
con3 = sqlite3.connect(":memory:")
con3.executescript("CREATE TABLE Job (a,b,c); CREATE TABLE Vehicle (a,b,c); CREATE TABLE Work (a,b); CREATE TABLE JobWork (a,b,c);")
con3.executemany("INSERT INTO Job VALUES (?,?,?)", job)
con3.executemany("INSERT INTO Vehicle VALUES (?,?,?)", vehicle)
con3.executemany("INSERT INTO Work VALUES (?,?)", work)
con3.executemany("INSERT INTO JobWork VALUES (?,?,?)", jobwork)
back = con3.execute("""SELECT Job.a, Job.b, Job.c, Vehicle.b, Vehicle.c, Work.a, Work.b, JobWork.c FROM JobWork
  INNER JOIN Job ON JobWork.a = Job.a INNER JOIN Vehicle ON Job.c = Vehicle.a INNER JOIN Work ON JobWork.b = Work.a""").fetchall()
assert sorted(back) == sorted((r["JobID"], r["JobDate"], r["Registration"], r["VehicleType"], r["OwnerName"], r["WorkCode"],
                               r["WorkDescription"], r["Hours"]) for r in g1)

# ---------------------------------------------------------------------------------------------
# Other exam-style tables: dependencies stated in the questions hold in the 'obvious' data
# ---------------------------------------------------------------------------------------------
# RESULT table: Mark needs both key parts; SubjectTitle needs SubjectCode only
result = [dict(StudentID=s, SubjectCode=c, SubjectTitle={"MA": "Mathematics", "PH": "Physics"}[c], Mark=m)
          for s, c, m in [("1", "MA", "70"), ("1", "PH", "64"), ("2", "MA", "58"), ("2", "PH", "64")]]
assert fd_holds(result, ["StudentID", "SubjectCode"], ["Mark"]) and fd_holds(result, ["SubjectCode"], ["SubjectTitle"])
assert not fd_holds(result, ["SubjectCode"], ["Mark"]) and not fd_holds(result, ["StudentID"], ["Mark"])

print("ok")
