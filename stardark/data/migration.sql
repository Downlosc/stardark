insert into t_budgets(a_shop_id, a_month, a_budget_amount, a_amount_spent) values
    (1, '2021-11-01', 1000.00, 725.67),
    (2, '2021-11-01', 1234.00, 886.63),
    (3, '2021-11-01', 599.00, 685.91),
    (4, '2021-11-01', 500.00, 746.92),
    (5, '2021-11-01', 800.00, 307.64),
    (6, '2021-11-01', 645.00, 946.32),
    (7, '2021-11-01', 950.00, 640.16),
    (8, '2021-11-01', 790.00, 965.64);

alter table t_shops add column a_notified boolean; 
update t_shops set a_online = '1' where a_id >= 1;
update t_shops set a_notified = '0' where a_id >= 1;
