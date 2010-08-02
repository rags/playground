CREATE function Maximum(@x int,@y int)
returns int
as
begin
declare @big int
SELECT @BIG =CASE
                                WHEN @X>@Y THEN  @X
                                ELSE @Y  
                            END
--select @big as 'big'
return @big
end

declare @x as int
select @x=dbo.Maximum(1,2)
print @x


create function padZero(@str varchar(10))
returns varchar(2)
as
begin
if len(@str)=1 
begin
return  '0' + @str
end
else 
begin
return @str
end
return ''
end

CREATE function formatDate(@date datetime)
returns varchar(200)
as
begin
return dbo.padZero(cast(month(@date) as varchar)) +'/' + dbo.padZero(datename(d,@date))  + '/' + datename(yyyy,@date) + ' ' + dbo.padZero(datename(hh,@date)) + ':' + dbo.padZero(datename(n,@date)); 
end



declare @x varchar(200) 
select @x = dbo.formatDate('2003-03-26 19:00:00.000')
print @x

declare @y as datetime
select @y=GETDATE()
select @y,dbo.formatDate(@y)

select dbo.padZero('xx') 