begin;

insert into todo_lists
values (1, 'uncategorized')
on conflict (id) do update
    set id   = 1,
        name = 'uncategorized';

insert into todo_lists
values (2, 'urgent')
on conflict (id) do update
    set id   = 2,
        name = 'urgent';

end;

select * from todo_lists;
select * from todos;