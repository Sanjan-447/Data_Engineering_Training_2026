use smart_home_energy;

DELIMITER $$

create procedure total_energy_per_room_per_day(
    in p_room_id int,
    in p_date date
)
begin
    select 
        r.room_id,
        r.room_name,
        date(e.timestamp) as usage_date,
        sum(e.energy_kwh) as total_energy_kwh
    from energy_logs e
    join devices d on e.device_id = d.device_id
    join rooms r on d.room_id = r.room_id
    where r.room_id = p_room_id
      and date(e.timestamp) = p_date
    group by r.room_id, r.room_name, date(e.timestamp);
END $$

DELIMITER ;

call total_energy_per_room_per_day(1, "2026-05-01");