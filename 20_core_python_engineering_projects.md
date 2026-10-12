# 20 Core Python Engineering Projects
## A Progressive Project Roadmap for Mastering Core Python

**Purpose:** Build strong core Python skills through practical, testable command-line applications.

**Scope:** These projects use core Python and the Python standard library only. No web frameworks, third-party packages, external APIs, or database servers. Use built-in data structures, functions, modules, exceptions, file handling, JSON/CSV, `datetime`, `pathlib`, `argparse`, `collections`, `unittest`, and other standard-library tools when appropriate.

## How to use this roadmap

For every project:
1. Understand the problem before coding.
2. Write down your data model and function contracts.
3. Break the work into small features.
4. Implement one feature at a time.
5. Test normal cases, invalid inputs, and boundary cases with `unittest`.
6. Use Git branches, focused commits, and pull requests if collaborating.
7. Explain your implementation without relying on AI to do the reasoning for you.

Suggested quality standard for every project:
- Separate application logic from interactive input/output.
- Validate inputs and raise meaningful exceptions where appropriate.
- Avoid duplicated logic and unnecessary global state.
- Include a README with run instructions and known limitations.
- Include at least 8 meaningful automated tests; larger projects should have more.
- Handle expected errors without crashing or silently destroying data.
- Use type hints where they improve clarity, and docstrings for public functions.

---

# Project 1 — Number Toolkit CLI
**Level:** Beginner  
**Main concepts:** Variables, numeric types, operators, conditionals, loops, functions, input validation.

## 1. The problem
Beginners often write one-off calculations that cannot be reused or tested easily. Build a command-line toolkit for common number operations.

## 2. Your mission
Create a menu-driven program that accepts numbers and performs calculations while rejecting invalid input safely.

## 3. Requirements
- Accept integers and decimal numbers.
- Reject blank input and text that cannot be converted to a number.
- Handle division by zero.
- Keep the menu running until the user chooses Exit.
- Do not use `eval()` to calculate user input.

## 4. Features
- F1 — Addition, subtraction, multiplication, and division.
- F2 — Find the minimum and maximum of a set of numbers.
- F3 — Determine whether a number is even or odd.
- F4 — Determine whether a number is positive, negative, or zero.
- F5 — Generate a multiplication table.
- F6 — Calculate a number's power without relying on user-entered expressions.
- F7 — Display clear messages for invalid choices and values.

## 5. Suggested structure
```text
number_toolkit/
├── main.py
├── number_toolkit/
│   ├── __init__.py
│   └── calculations.py
├── tests/
│   └── test_calculations.py
└── README.md
```

## 6. Acceptance tests
- Correctly add positive, negative, integer, and decimal values.
- Division by zero is handled explicitly.
- Zero is not classified as positive or negative.
- Invalid menu options do not terminate the application.
- Multiplication tables have the correct number of rows.
- Calculation functions can be tested without interactive input.

## 7. Stretch goals
Add factorial and prime-number checks, with appropriate validation for negative or non-integer inputs.

---

# Project 2 — Personal Expense Tracker
**Level:** Beginner  
**Main concepts:** Lists, dictionaries, loops, functions, validation, aggregation.

## 1. The problem
People often lose track of small daily expenses and cannot easily tell which categories consume most of their money.

## 2. Your mission
Build a terminal application that records expenses and summarizes spending. Start with in-memory storage; add file persistence only after the basic logic works.

## 3. Data model
Each expense should contain:
- `id`
- `description`
- `amount`
- `category`
- `date`

## 4. Features
- F1 — Add an expense with a positive amount.
- F2 — List all expenses.
- F3 — Filter expenses by category or date.
- F4 — Calculate total spending.
- F5 — Calculate spending by category.
- F6 — Find the largest and smallest expense.
- F7 — Delete an expense by ID.
- F8 — Save and load expenses using JSON.

## 5. Suggested structure
```text
expense_tracker/
├── main.py
├── expense_tracker/
│   ├── __init__.py
│   ├── expenses.py
│   └── storage.py
├── tests/
│   ├── test_expenses.py
│   └── test_storage.py
└── README.md
```

## 6. Rules
- Amounts must be greater than zero.
- Descriptions and categories cannot be blank.
- IDs must remain unique after loading saved data.
- Missing data files should allow a fresh start.
- Malformed JSON must produce a useful error, not silently erase data.

## 7. Acceptance tests
Test adding, listing, deleting, category totals, empty reports, invalid amounts, missing files, and save/load round trips.

## 8. Stretch goals
Add monthly summaries and a budget limit per category.

---

# Project 3 — Quiz and Exam Engine
**Level:** Beginner  
**Main concepts:** Lists and dictionaries, loops, functions, strings, randomization, scoring.

## 1. The problem
A learner needs a reusable way to practise questions, receive immediate feedback, and review weak areas.

## 2. Your mission
Build a command-line quiz application that loads questions from a JSON file and records a quiz session's result.

## 3. Question model
Each question should contain an ID, prompt, answer choices, correct answer, and topic.

## 4. Features
- F1 — Load questions from JSON.
- F2 — Select a quiz by topic.
- F3 — Shuffle question order using `random`.
- F4 — Validate answers and give feedback.
- F5 — Calculate score and percentage.
- F6 — Show missed questions after the quiz.
- F7 — Save session results to a file.
- F8 — Handle an empty or invalid question bank.

## 5. Suggested structure
```text
quiz_engine/
├── main.py
├── quiz_engine/
│   ├── __init__.py
│   ├── questions.py
│   ├── session.py
│   └── storage.py
├── data/
│   └── questions.json
├── tests/
│   ├── test_questions.py
│   └── test_session.py
└── README.md
```

## 6. Acceptance tests
Test correct and incorrect answers, zero-question quizzes, invalid answer choices, score calculations, topic filtering, and malformed question data.

## 7. Stretch goals
Add a timed mode using `time` and a historical score report.

---

# Project 4 — Contact Book
**Level:** Beginner  
**Main concepts:** Strings, dictionaries, searching, sorting, validation, JSON persistence.

## 1. The problem
Contact information becomes difficult to manage when names are duplicated, details are inconsistent, or records cannot be found quickly.

## 2. Your mission
Create a contact manager that can add, find, update, list, and delete contacts.

## 3. Contact fields
- Unique contact ID
- Full name
- Phone number
- Email address (optional)
- Notes (optional)

## 4. Features
- F1 — Add and validate contacts.
- F2 — Search by full or partial name.
- F3 — Update selected fields.
- F4 — Delete by ID after confirming the target.
- F5 — List contacts alphabetically.
- F6 — Detect likely duplicate contacts.
- F7 — Save and load records as JSON.

## 5. Suggested structure
```text
contact_book/
├── main.py
├── contact_book/
│   ├── __init__.py
│   ├── contacts.py
│   └── storage.py
├── tests/
│   ├── test_contacts.py
│   └── test_storage.py
└── README.md
```

## 6. Rules and acceptance tests
- Names cannot be blank.
- Search is case-insensitive.
- Unknown IDs raise a clear error.
- Updating a contact preserves fields not being changed.
- Test duplicate detection, empty searches, sorting, deletion, and persistence.

## 7. Stretch goals
Import and export contacts as CSV using the `csv` module.

---

# Project 5 — Text File Analyzer
**Level:** Beginner to Intermediate  
**Main concepts:** File I/O, strings, dictionaries, `pathlib`, exceptions, text processing.

## 1. The problem
Reading a long text file manually makes it hard to find word counts, repeated terms, and basic document statistics.

## 2. Your mission
Build a command-line tool that analyzes a text file and produces a readable report.

## 3. Features
- F1 — Accept a file path from command-line arguments.
- F2 — Count lines, words, characters, and non-empty lines.
- F3 — Count word frequencies case-insensitively.
- F4 — Show the most frequent words.
- F5 — Ignore configurable common words.
- F6 — Find lines containing a search phrase.
- F7 — Save the report to a text file.
- F8 — Handle missing files, directories, and unreadable files.

## 4. Suggested structure
```text
text_analyzer/
├── main.py
├── text_analyzer/
│   ├── __init__.py
│   ├── analysis.py
│   └── reports.py
├── tests/
│   └── test_analysis.py
└── README.md
```

## 5. Acceptance tests
Test empty files, punctuation, mixed case, repeated words, blank lines, missing paths, and ties in word frequency.

## 6. Stretch goals
Add a comparison report for two files and a summary of words unique to each file.

---

# Project 6 — Password Policy Checker
**Level:** Beginner to Intermediate  
**Main concepts:** Boolean logic, strings, functions, sets, regular expressions, test cases.

## 1. The problem
Applications often need to check whether a proposed password meets a stated policy before accepting it.

## 2. Your mission
Create a local password policy checker. It must assess policy compliance, not claim that a password is impossible to crack.

## 3. Features
- F1 — Check minimum and maximum length.
- F2 — Check for uppercase and lowercase letters.
- F3 — Check for digits and allowed special characters.
- F4 — Detect whitespace if the policy disallows it.
- F5 — Return a list of all failed rules rather than only the first failure.
- F6 — Read a policy configuration from JSON.
- F7 — Offer a strength category based on transparent rules.

## 4. Suggested structure
```text
password_checker/
├── main.py
├── password_checker/
│   ├── __init__.py
│   ├── policy.py
│   └── evaluation.py
├── tests/
│   └── test_policy.py
└── README.md
```

## 5. Acceptance tests
Test minimum-length boundaries, missing character classes, multiple simultaneous failures, Unicode input, and invalid policy configuration.

## 6. Safety and scope
Do not store or log the entered password. Do not transmit it anywhere. This is a learning tool, not an authentication system.

## 7. Stretch goals
Compare the password against a small local denylist without saving the password.

---

# Project 7 — File Organizer
**Level:** Intermediate  
**Main concepts:** `pathlib`, file handling, dictionaries, sorting, exceptions, dry-run design.

## 1. The problem
A downloads folder can become cluttered with documents, images, archives, and miscellaneous files.

## 2. Your mission
Build a tool that groups files by extension and can preview its planned actions before moving anything.

## 3. Features
- F1 — Accept a target directory.
- F2 — Classify files by extension.
- F3 — Show a dry-run plan before changes.
- F4 — Create destination folders only when needed.
- F5 — Move files using `pathlib` or `shutil`.
- F6 — Handle name collisions without overwriting files.
- F7 — Skip directories and optionally hidden files.
- F8 — Produce a summary of moved, skipped, and failed files.

## 4. Suggested structure
```text
file_organizer/
├── main.py
├── file_organizer/
│   ├── __init__.py
│   ├── planner.py
│   └── operations.py
├── tests/
│   └── test_planner.py
└── README.md
```

## 5. Rules
- Never modify files during dry-run mode.
- Do not move a directory into itself.
- Never silently overwrite an existing destination file.
- Test using temporary directories created by `tempfile`.

## 6. Acceptance tests
Test extension grouping, files without extensions, collision handling, empty folders, dry-run safety, and nonexistent directories.

## 7. Stretch goals
Add an undo manifest that records original and new paths.

---

# Project 8 — Inventory and Stock Manager
**Level:** Intermediate  
**Main concepts:** Dictionaries, functions, validation, aggregation, file persistence, invariants.

## 1. The problem
A small shop needs to track products, stock levels, prices, and stock movements to reduce mistakes.

## 2. Your mission
Build an inventory manager that preserves stock consistency through every operation.

## 3. Product fields
- Product ID
- Name
- Unit price
- Quantity in stock
- Reorder threshold

## 4. Features
- F1 — Add, view, update, and remove products.
- F2 — Receive stock.
- F3 — Record sales and reduce stock.
- F4 — Reject sales that exceed available stock.
- F5 — Show low-stock products.
- F6 — Calculate inventory value.
- F7 — Search and sort products.
- F8 — Save and load inventory as JSON.

## 5. Suggested structure
```text
inventory_manager/
├── main.py
├── inventory_manager/
│   ├── __init__.py
│   ├── products.py
│   ├── stock.py
│   └── storage.py
├── tests/
│   ├── test_stock.py
│   └── test_storage.py
└── README.md
```

## 6. Business rules
- Product names cannot be blank.
- Price cannot be negative; quantity and reorder threshold cannot be negative.
- Stock cannot become negative.
- A failed sale must not partially change the inventory.

## 7. Acceptance tests
Test receiving stock, successful and rejected sales, exact-stock sales, low-stock boundaries, inventory valuation, duplicate IDs, and persistence.

## 8. Stretch goals
Add a stock movement history with timestamps using `datetime`.

---

# Project 9 — Student Gradebook
**Level:** Intermediate  
**Main concepts:** Nested data structures, aggregation, sorting, functions, CSV, validation.

## 1. The problem
Teachers need consistent calculations for student scores, averages, grades, and class summaries.

## 2. Your mission
Create a gradebook that records assessments and calculates results according to an explicit grading policy.

## 3. Data model
Each student has an ID, name, and scores for named assessments.

## 4. Features
- F1 — Add and find students.
- F2 — Record and update assessment scores.
- F3 — Validate scores against the configured maximum.
- F4 — Calculate each student's average.
- F5 — Assign letter grades from a documented grading scale.
- F6 — Rank students with clear tie handling.
- F7 — Calculate class averages and highest/lowest scores.
- F8 — Export results to CSV.

## 5. Suggested structure
```text
gradebook/
├── main.py
├── gradebook/
│   ├── __init__.py
│   ├── students.py
│   ├── grading.py
│   └── reports.py
├── tests/
│   ├── test_grading.py
│   └── test_reports.py
└── README.md
```

## 6. Acceptance tests
Test score boundaries, missing assessments, empty classes, average calculations, tied rankings, invalid student IDs, and CSV output.

## 7. Stretch goals
Support weighted assessments and compare results across terms.

---

# Project 10 — Habit Tracker
**Level:** Intermediate  
**Main concepts:** Sets, dictionaries, dates, loops, persistence, date arithmetic.

## 1. The problem
People may record habits inconsistently and struggle to understand whether they are building a regular routine.

## 2. Your mission
Build a local habit tracker that records completion dates and calculates simple consistency metrics.

## 3. Features
- F1 — Create, list, rename, and archive habits.
- F2 — Mark a habit complete for a date.
- F3 — Prevent duplicate completion records for the same habit and date.
- F4 — Show completed habits for a chosen day.
- F5 — Calculate current and longest streaks.
- F6 — Summarize completion over the last 7 or 30 days.
- F7 — Save and reload data as JSON.

## 4. Suggested structure
```text
habit_tracker/
├── main.py
├── habit_tracker/
│   ├── __init__.py
│   ├── habits.py
│   ├── streaks.py
│   └── storage.py
├── tests/
│   ├── test_streaks.py
│   └── test_habits.py
└── README.md
```

## 5. Rules
- Parse dates in one documented format.
- Do not assume every day has a completion.
- Define how a streak behaves when the user has not yet completed today's habit.
- Make date calculations testable by passing a reference date into functions.

## 6. Acceptance tests
Test consecutive dates, a missing day, duplicate completion, future dates, empty history, and streaks across a month boundary.

## 7. Stretch goals
Add recurring habit schedules, such as selected weekdays.

---

# Project 11 — Command-Line To-Do Manager
**Level:** Intermediate  
**Main concepts:** Modules, data modeling, `argparse`, sorting, dates, JSON, exceptions.

## 1. The problem
A long list of tasks becomes difficult to manage without priorities, due dates, status tracking, and filtering.

## 2. Your mission
Build a command-line task manager that supports both menu use and direct commands.

## 3. Task fields
ID, title, description, priority, status, creation date, and optional due date.

## 4. Features
- F1 — Add, view, edit, complete, and delete tasks.
- F2 — Filter by status or priority.
- F3 — Sort by due date and priority.
- F4 — Show overdue tasks.
- F5 — Search task titles.
- F6 — Persist tasks in JSON.
- F7 — Parse command-line options with `argparse`.
- F8 — Return meaningful exit codes for command failures.

## 5. Suggested structure
```text
todo_manager/
├── main.py
├── todo_manager/
│   ├── __init__.py
│   ├── tasks.py
│   ├── commands.py
│   └── storage.py
├── tests/
│   ├── test_tasks.py
│   └── test_commands.py
└── README.md
```

## 6. Acceptance tests
Test CRUD operations, invalid dates, unknown IDs, overdue boundaries, stable sorting, malformed JSON, and CLI argument errors.

## 7. Stretch goals
Add recurring tasks and a command that prints a daily agenda.

---

# Project 12 — Log File Investigator
**Level:** Intermediate  
**Main concepts:** File iteration, string parsing, dictionaries, `datetime`, `collections.Counter`, exceptions.

## 1. The problem
Application logs contain useful diagnostic information, but finding error patterns manually is slow.

## 2. Your mission
Create a tool that parses a documented log format and summarizes events by level, time, and message.

## 3. Features
- F1 — Read a log file line by line.
- F2 — Parse timestamp, level, and message.
- F3 — Count INFO, WARNING, ERROR, and other levels.
- F4 — List the most frequent error messages.
- F5 — Filter events within a time range.
- F6 — Report malformed lines separately.
- F7 — Save a summary report.
- F8 — Support large files without loading every line into memory.

## 4. Suggested structure
```text
log_investigator/
├── main.py
├── log_investigator/
│   ├── __init__.py
│   ├── parser.py
│   └── reports.py
├── sample_data/
│   └── application.log
├── tests/
│   └── test_parser.py
└── README.md
```

## 5. Acceptance tests
Test valid lines, malformed lines, unknown levels, repeated errors, timestamp boundaries, empty files, and large input handled line by line.

## 6. Stretch goals
Compare two log files and identify error messages that appear only in one.

---

# Project 13 — Duplicate File Finder
**Level:** Intermediate  
**Main concepts:** File traversal, binary file reading, hashing, dictionaries, `hashlib`, `pathlib`.

## 1. The problem
Duplicate files consume disk space and create confusion about which copy is authoritative.

## 2. Your mission
Build a scanner that identifies likely exact duplicates without deleting anything automatically.

## 3. Features
- F1 — Recursively scan a selected directory.
- F2 — Group files by size as an initial filter.
- F3 — Calculate a content hash with `hashlib`.
- F4 — Group files with matching hashes.
- F5 — Show file paths and sizes for each duplicate group.
- F6 — Export findings to CSV or JSON.
- F7 — Handle unreadable files and files that disappear during scanning.
- F8 — Include a report-only mode as the default.

## 4. Suggested structure
```text
duplicate_finder/
├── main.py
├── duplicate_finder/
│   ├── __init__.py
│   ├── scanning.py
│   └── reporting.py
├── tests/
│   └── test_scanning.py
└── README.md
```

## 5. Rules
- Do not delete or alter files.
- Equal file sizes alone do not prove that files are duplicates.
- Use temporary directories for tests.
- Report errors rather than silently skipping every failure.

## 6. Acceptance tests
Test identical files, same-size different files, empty files, nested directories, unreadable-file handling where practical, and empty directories.

## 7. Stretch goals
Add an optional comparison step that verifies bytes after hashes match.

---

# Project 14 — Personal Budget Planner
**Level:** Intermediate  
**Main concepts:** Decimal arithmetic, dates, aggregation, validation, JSON, reporting.

## 1. The problem
A person needs to compare planned income and expenses with actual transactions to understand where money is going.

## 2. Your mission
Build a budget planner with categories, monthly budgets, and transaction reports.

## 3. Features
- F1 — Record income and expense transactions.
- F2 — Set a budget limit per category and month.
- F3 — Calculate actual spending by category.
- F4 — Compare spending against the budget.
- F5 — Report remaining budget and overspending.
- F6 — Filter by month and date range.
- F7 — Save and reload transactions and budgets.
- F8 — Export a monthly report to CSV.

## 4. Suggested structure
```text
budget_planner/
├── main.py
├── budget_planner/
│   ├── __init__.py
│   ├── transactions.py
│   ├── budgets.py
│   └── reports.py
├── tests/
│   ├── test_budgets.py
│   └── test_reports.py
└── README.md
```

## 5. Rules
- Use `decimal.Decimal` for monetary calculations rather than binary floating-point arithmetic.
- Keep income and expenses distinguishable.
- Validate date and amount input.
- Define how refunds and transfers are represented before implementation.

## 6. Acceptance tests
Test exact budget boundaries, overspending, no transactions, income exclusion from expense totals, decimal arithmetic, and month transitions.

## 7. Stretch goals
Add recurring transaction templates without automatically duplicating posted transactions.

---

# Project 15 — Library Lending System
**Level:** Intermediate to Advanced  
**Main concepts:** Classes, object relationships, methods, exceptions, data modeling, persistence.

## 1. The problem
A small library needs to track books, members, checkouts, returns, and overdue loans without losing track of available copies.

## 2. Your mission
Design a small object-oriented library system with clear rules for lending and returning books.

## 3. Core objects
- `Book`: book ID, title, author, total copies.
- `Member`: member ID, name, active status.
- `Loan`: loan ID, book ID, member ID, checkout date, due date, return date.

## 4. Features
- F1 — Register books and members.
- F2 — Check out an available copy.
- F3 — Reject checkout for inactive members or unavailable books.
- F4 — Return a loan only once.
- F5 — List active and overdue loans.
- F6 — Search books by title or author.
- F7 — Persist records in JSON.
- F8 — Produce a report of availability and active loans.

## 5. Suggested structure
```text
library_system/
├── main.py
├── library_system/
│   ├── __init__.py
│   ├── models.py
│   ├── library.py
│   └── storage.py
├── tests/
│   ├── test_library.py
│   └── test_storage.py
└── README.md
```

## 6. Acceptance tests
Test checkout and return, unavailable books, duplicate returns, inactive members, due-date boundaries, multiple copies, and save/load integrity.

## 7. Stretch goals
Add a reservation queue for books with no available copies.

---

# Project 16 — Banking Ledger Simulator
**Level:** Advanced  
**Main concepts:** Classes, encapsulation, `Decimal`, invariants, exceptions, transaction history.

## 1. The problem
A banking simulation is useful for learning how to protect balances from invalid operations and maintain a traceable transaction history.

## 2. Your mission
Build a local educational banking simulator. It is not a real banking system and must not handle real credentials or payments.

## 3. Core objects
- `Account`: account ID, owner label, balance, active status.
- `Transaction`: ID, type, amount, timestamp, account references, description.

## 4. Features
- F1 — Create an account.
- F2 — Deposit funds.
- F3 — Withdraw funds when sufficient balance exists.
- F4 — Transfer between two accounts.
- F5 — Show a transaction history.
- F6 — Calculate balances from stored transactions or verify balances against the ledger.
- F7 — Reject invalid amounts and inactive accounts.
- F8 — Save and reload records.

## 5. Suggested structure
```text
banking_simulator/
├── main.py
├── banking_simulator/
│   ├── __init__.py
│   ├── accounts.py
│   ├── transactions.py
│   └── storage.py
├── tests/
│   ├── test_accounts.py
│   └── test_transfers.py
└── README.md
```

## 6. Critical rules
- Use `Decimal` for money.
- Balances must never become negative unless you explicitly implement and test an overdraft policy.
- A transfer must debit and credit consistently; a rejected transfer must not partially update either account.
- Do not store passwords or sensitive real financial data.

## 7. Acceptance tests
Test deposit, withdrawal, insufficient funds, self-transfer policy, transfers between accounts, zero/negative amounts, inactive accounts, and ledger consistency.

## 8. Stretch goals
Add a reconciliation command that detects discrepancies between balances and transaction history.

---

# Project 17 — Text-Based Adventure Game
**Level:** Advanced  
**Main concepts:** Classes, state, dictionaries, sets, functions, branching, serialization.

## 1. The problem
A text adventure gives you a practical way to model a world, player state, inventory, and rule-based interactions.

## 2. Your mission
Create a small interactive adventure in which the player explores locations, collects items, solves a puzzle, and reaches an ending.

## 3. Features
- F1 — Model locations and their connections.
- F2 — Parse and validate player commands.
- F3 — Track health, inventory, and visited locations.
- F4 — Allow items to unlock actions or locations.
- F5 — Implement at least one puzzle.
- F6 — Prevent impossible actions and explain why they failed.
- F7 — Save and restore game state as JSON.
- F8 — Provide a clear win and lose condition.

## 4. Suggested structure
```text
text_adventure/
├── main.py
├── text_adventure/
│   ├── __init__.py
│   ├── world.py
│   ├── player.py
│   ├── commands.py
│   └── saves.py
├── tests/
│   ├── test_world.py
│   └── test_commands.py
└── README.md
```

## 5. Acceptance tests
Test valid and invalid movement, item pickup, locked doors, puzzle success/failure, save/load, and terminal states.

## 6. Stretch goals
Add non-player characters and a turn-based encounter system.

---

# Project 18 — Expression Evaluator
**Level:** Advanced  
**Main concepts:** Strings, tokenization, stacks, recursion or parsing, exceptions, operator precedence.

## 1. The problem
A calculator that accepts unrestricted Python expressions can execute unintended code. Build a small calculator that understands only a defined arithmetic grammar.

## 2. Your mission
Implement an arithmetic expression evaluator without using `eval()` or `exec()`.

## 3. Supported language
Start with numeric literals, parentheses, unary minus, and the operators `+`, `-`, `*`, and `/`. Document operator precedence and associativity.

## 4. Features
- F1 — Tokenize the input string.
- F2 — Reject unsupported characters and malformed numbers.
- F3 — Parse expressions using a documented approach, such as recursive descent.
- F4 — Respect precedence and parentheses.
- F5 — Handle division by zero.
- F6 — Report useful errors with positions where possible.
- F7 — Add an interactive REPL.
- F8 — Keep parsing logic independent of terminal input.

## 5. Suggested structure
```text
expression_evaluator/
├── main.py
├── expression_evaluator/
│   ├── __init__.py
│   ├── tokenizer.py
│   ├── parser.py
│   └── evaluator.py
├── tests/
│   ├── test_tokenizer.py
│   └── test_evaluator.py
└── README.md
```

## 6. Acceptance tests
Test precedence, nested parentheses, unary minus, malformed expressions, empty input, unsupported names, extra closing parentheses, and division by zero.

## 7. Stretch goals
Add exponentiation with a clearly defined precedence and associativity.

---

# Project 19 — Mini Version-Control System
**Level:** Advanced  
**Main concepts:** File operations, hashing, JSON, command parsing, snapshots, data integrity.

## 1. The problem
Version-control tools preserve project history, but their core ideas can be learned by building a small local snapshot system.

## 2. Your mission
Create a local tool that records snapshots of selected files and allows users to inspect and restore earlier versions. It is a learning exercise, not a replacement for Git.

## 3. Features
- F1 — Initialize a repository directory.
- F2 — Track selected files.
- F3 — Create snapshots with unique IDs and timestamps.
- F4 — Store file contents or content-addressed objects.
- F5 — Show snapshot history.
- F6 — Compare a file with an earlier snapshot.
- F7 — Restore a selected snapshot safely.
- F8 — Detect missing or changed files and handle corrupt metadata.

## 4. Suggested structure
```text
mini_vcs/
├── main.py
├── mini_vcs/
│   ├── __init__.py
│   ├── repository.py
│   ├── snapshots.py
│   ├── objects.py
│   └── commands.py
├── tests/
│   ├── test_snapshots.py
│   └── test_restore.py
└── README.md
```

## 5. Critical rules
- Keep repository metadata separate from the user's working files.
- Do not overwrite files during restore without a clear confirmation or safe backup strategy.
- Use hashes to detect content changes.
- Ensure a failed snapshot does not leave metadata claiming that an incomplete snapshot succeeded.

## 6. Acceptance tests
Test initialization, repeated snapshots, unchanged content, changed content, restore, missing files, and malformed metadata.

## 7. Stretch goals
Add a simple diff view and named labels for snapshots.

---

# Project 20 — Document Intelligence CLI
**Level:** Advanced / Capstone  
**Main concepts:** Modules, functions, regular expressions, file handling, validation, reports, CLI design, testing.

## 1. The problem
People who work with collected forms, reports, and text documents often need to identify important values quickly and detect missing or suspicious data.

## 2. Your mission
Build a reusable command-line tool that reads a local text document, extracts selected patterns, validates findings, and creates a report.

## 3. Supported scope
Start with plain-text files. Do not promise reliable extraction from every file format. Add new formats only when you can implement and test their readers using the standard library.

## 4. Features
- F1 — Accept a file path and options through `argparse`.
- F2 — Read text with clear handling for missing, empty, and unreadable files.
- F3 — Extract email-like strings, URLs, phone-like values, dates, money amounts, hashtags, mentions, and IP-address candidates using `re`.
- F4 — Validate extracted values separately from extraction.
- F5 — Report counts and findings with source line numbers where practical.
- F6 — Avoid duplicate findings while preserving useful order.
- F7 — Export reports to JSON or CSV.
- F8 — Provide meaningful errors and exit codes.
- F9 — Keep each extractor independently testable.
- F10 — Include a suite of tests for normal cases, false positives, and edge cases.

## 5. Suggested structure
```text
document_intelligence_cli/
├── main.py
├── docintel/
│   ├── __init__.py
│   ├── cli.py
│   ├── reader.py
│   ├── extractors.py
│   ├── validator.py
│   └── report.py
├── sample_data/
│   └── sample.txt
├── tests/
│   ├── test_reader.py
│   ├── test_extractors.py
│   ├── test_validator.py
│   └── test_report.py
└── README.md
```

## 6. Engineering rules
- Extraction and validation must be separate responsibilities.
- Do not assume that a regex match is automatically a valid real-world value.
- Avoid printing the entire document when only a report is needed.
- Do not overwrite source files.
- Keep the command-line interface separate from the core processing functions.
- Use only Python's standard library.

## 7. Acceptance tests
- Missing and empty files produce clear outcomes.
- Each extractor has positive and negative test cases.
- Invalid values are not reported as validated values.
- Duplicate matches are handled consistently.
- JSON and CSV reports contain the expected data.
- CLI arguments and error paths are tested.
- Running the full test suite does not depend on a user's personal files.

## 8. Stretch goals
Add batch processing for a directory, configurable extraction rules from JSON, and a concise machine-readable summary for other local Python programs.

---

# Suggested progression and skill coverage

| Project | Main learning focus |
|---|---|
| 1. Number Toolkit | Variables, operators, conditions, loops, functions |
| 2. Expense Tracker | Lists, dictionaries, aggregation, validation |
| 3. Quiz Engine | Nested data, randomization, scoring |
| 4. Contact Book | Searching, sorting, JSON |
| 5. Text Analyzer | Files, strings, frequency analysis |
| 6. Password Checker | Boolean logic, policy rules, regex |
| 7. File Organizer | Paths, safe file operations, dry runs |
| 8. Inventory Manager | Business rules, invariants, persistence |
| 9. Gradebook | Nested structures, statistics, CSV |
| 10. Habit Tracker | Sets, dates, streak algorithms |
| 11. To-Do Manager | Modules, `argparse`, CLI design |
| 12. Log Investigator | Streaming file processing, parsing |
| 13. Duplicate Finder | Binary files, hashing, traversal |
| 14. Budget Planner | `Decimal`, date ranges, reports |
| 15. Library System | Classes, relationships, object-oriented design |
| 16. Banking Simulator | Encapsulation, transactions, invariants |
| 17. Text Adventure | State modeling, serialization |
| 18. Expression Evaluator | Tokenization, parsing, stacks/recursion |
| 19. Mini Version Control | Snapshots, hashes, integrity |
| 20. Document Intelligence CLI | Integration, architecture, testing, CLI |

## Final completion standard

A project is complete when:
- The stated requirements work.
- Invalid input is handled deliberately.
- Core logic is testable without interactive input.
- At least 8 meaningful `unittest` tests pass.
- Files are not silently overwritten or corrupted.
- The README explains setup, usage, tests, and limitations.
- You can explain the data structures, algorithms, trade-offs, and tests in your own words.

**Recommended learning rule:** Do not build all 20 projects at once. Finish each project to a reasonable standard, review what you learned, and then move to the next. For the more advanced projects, implement a small working version first and add features incrementally.
