Bug Fix: Changing Format Specifier and Database Drop

Issue
The issue was identified in the code where the format specifier was incorrectly set as `%s` instead of `%d` in a particular function. Additionally, there was an omission of a crucial database drop command (`cursor.execute('drop database if exists yyes')`).

Description
-Format Specifier Fix:
  - The incorrect format specifier `%s` has been changed to `%d` in the affected code. This ensures proper handling of the data type and resolves potential runtime errors.

-Database Drop Addition:
  - Added the statement `cursor.execute('drop database if exists yyes')` to address a missing database cleanup step. This ensures that the 'yyes' database is dropped if it exists, preventing unintended issues related to database persistence.

Changes Made
- Modified the format specifier in the affected code from `%s` to `%d`.
- Added the statement `cursor.execute('drop database if exists yyes')` for proper database cleanup.

Reasoning
Format Specifier Fix:
  - The change was necessary to align the format specifier with the expected data type. This prevents potential bugs and improves the overall robustness of the code.

Database Drop Addition:
  - The database drop statement is critical to ensure that the 'yyes' database is properly cleaned up, preventing unintended side effects or conflicts in subsequent executions.

Testing
- The changes have been tested to ensure they do not introduce new issues.
- Specifically, tests have been conducted to verify that the format specifier modification does not affect the functionality, and the database drop statement works as intended.

Related Issues
Link to the original issue or issues that prompted this bug fix.

Checklist
- [ ] The code has been reviewed for adherence to coding standards.
- [ ] Tests have been conducted to validate the bug fix.
- [ ] Documentation has been updated to reflect the changes made.

Additional Notes
Any additional information or considerations that may be relevant.
