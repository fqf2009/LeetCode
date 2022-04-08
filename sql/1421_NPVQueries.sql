select q.id,
       q.year,
       coalesce(n.npv, 0) npv
  from npv n
 right join queries q
    on q.year = n.year
   and q.id = n.id
   ;
