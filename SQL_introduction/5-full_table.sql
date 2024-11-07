--a script that prints the following description of the table first_table from the database hbtn_0c_0 in your MySQL server --
SELECT 
    CONCAT(
        'CREATE TABLE `', table_name, '` (',
        GROUP_CONCAT(
            CONCAT(
                '`', column_name, '` ', column_type,
                CASE 
                    WHEN is_nullable = 'NO' THEN ' NOT NULL'
                    ELSE ''
                END,
                CASE 
                    WHEN column_default IS NOT NULL THEN ' DEFAULT ' 
                        CONCAT('\'', column_default, '\'')
                    ELSE ''
                END
            ) SEPARATOR ', '
        ),
        ', PRIMARY KEY (`id`) ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci'
    ) AS create_statement
FROM information_schema.columns
WHERE table_schema = DATABASE() AND table_name = 'first_table';