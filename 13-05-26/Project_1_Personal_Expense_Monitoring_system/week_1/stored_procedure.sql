use personal_expense_monitoring;

DELIMITER $$
create procedure  monthly_expense_category(
in p_user_id int,
in p_month int,
in p_year int )
begin 
select c.category_name, sum(e.amount) as total_spent
from expenses e join categories c on c.category_id = e.category_id
where e.user_id = p_user_id and c.category_type = "expense"
and month(e.expense_date) = p_month
and year(e.expense_date) = p_year
group by c.category_name 
order by total_spent desc;
END $$

DELIMITER ;

call monthly_expense_category( 1, 5, 2026);