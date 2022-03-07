create table t_shops (
    a_id        serial,
    a_name      text     not null,
    a_online    boolean  not null,

   primary key(a_id)
);

create table t_budgets (
    a_id  serial,
    a_shop_id       integer not null,
    a_month         date    not null,
    a_budget_amount numeric not null,
    a_amount_spent  numeric not null,

    primary key(a_id),
    foreign key (a_shop_id) references t_shops(a_id)
);

insert into t_shops(a_name, a_online) values 
    ('Steve McQueen',    '1'),
    ('Fashion Quasar',   '0'),
    ('As Seen On Sale',  '1'),
    ('H&R',              '0'),
    ('Meow Meow',        '1'),
    ('Dole & Cabbage',   '0'),
    ('George Manly',     '1'),
    ('Harrison Ford',    '1');

insert into t_budgets(a_shop_id, a_month, a_budget_amount, a_amount_spent) values
    (1, '2020-06-01', 930.00, 725.67),
    (2, '2020-06-01', 990.00, 886.63),
    (3, '2020-06-01', 650.00, 685.91),
    (4, '2020-06-01', 740.00, 746.92),
    (5, '2020-06-01', 630.00, 507.64),
    (6, '2020-06-01', 640.00, 946.32),
    (7, '2020-06-01', 980.00, 640.16),
    (8, '2020-06-01', 790.00, 965.64),
    (1, '2020-07-01', 960.00, 803.67),
    (2, '2020-07-01', 670.00, 715.64),
    (3, '2020-07-01', 890.00, 580.81),
    (4, '2020-07-01', 590.00, 754.93),
    (5, '2020-07-01', 870.00, 505.12),
    (6, '2020-07-01', 700.00, 912.30),
    (7, '2020-07-01', 990.00, 805.15),
    (8, '2020-07-01', 720.00, 504.25);
