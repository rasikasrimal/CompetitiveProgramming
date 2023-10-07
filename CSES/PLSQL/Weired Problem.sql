SET SERVEROUTPUT ON;

DECLARE
   n NUMBER;
   result VARCHAR2(4000) := '';
BEGIN
   DBMS_OUTPUT.PUT('Enter a value for n: ');
   n := TO_NUMBER(TRIM(TO_CHAR(&n)));

   WHILE n > 1 LOOP
      IF MOD(n, 2) = 0 THEN
         n := n / 2;
      ELSE
         n := 3 * n + 1;
      END IF;

      result := result || n || ' ';
   END LOOP;

   DBMS_OUTPUT.PUT_LINE(result);
END;
/
