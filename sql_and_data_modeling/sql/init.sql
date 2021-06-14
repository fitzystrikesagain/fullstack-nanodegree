begin;

insert into todo_lists values (1, 'uncategorized') on conflict do nothing;

end;
