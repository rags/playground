import org.hibernate.*;
import org.hibernate.annotations.BatchSize;
import org.hibernate.boot.registry.StandardServiceRegistryBuilder;
import org.hibernate.cfg.Configuration;
import org.hibernate.criterion.Order;
import org.hibernate.criterion.Projection;
import org.hibernate.criterion.ProjectionList;
import org.hibernate.criterion.Projections;
import org.hibernate.transform.DistinctRootEntityResultTransformer;
import org.hibernate.transform.RootEntityResultTransformer;
import org.hibernate.type.Type;

import javax.persistence.*;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.sql.Blob;
import java.sql.Clob;
import java.util.*;

@Entity
class emp {
    @Id
    public int id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "did")
    public dept dept;

    @Override
    public String toString() {
        return "emp{" +
                "id=" + id +
                '}';
    }
}


@Entity
class dept {
    @Id
    public int id;

    @BatchSize(size=2)
    @OneToMany(mappedBy = "dept", fetch = FetchType.LAZY)
    public List<emp> employees;

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        dept dept = (dept) o;

        if (id != dept.id) return false;

        return true;
    }

    @Override
    public int hashCode() {
        return id;
    }
}


/*
mysql> select emp.id as EmpId, dept.id as DeptId from emp, dept where emp.did=dept.id;
+-------+--------+
| EmpId | DeptId |
+-------+--------+
|     1 |      1 |
|     2 |      1 |
|     3 |      1 |
|     4 |      2 |
|     5 |      2 |
|     6 |      3 |
|     7 |      3 |
+-------+--------+
7 rows in set (0.00 sec)

List result
Department: id = 1; Employees =[emp{id=1}, emp{id=2}, emp{id=3}]
Department: id = 2; Employees =[emp{id=4}, emp{id=5}]
Department: id = 3; Employees =[emp{id=7}, emp{id=6}]
********************

Scroll result
Department: id = 1; Employees =[emp{id=1}]
Department: id = 1; Employees =[emp{id=1}] # this should be emp=2
Department: id = 1; Employees =[emp{id=1}] # this should be emp=3

Department: id = 2; Employees =[emp{id=4}]
Department: id = 2; Employees =[emp{id=4}] # this should be emp=5

Department: id = 3; Employees =[emp{id=6}]
Department: id = 3; Employees =[emp{id=6}] # this should be emp=7

Notice 2 things wrong with the scroll:
1. It does not aggregate Employees under a dept.
2. It does not return the right join (Notice all records for dept=1 have emp id=1).
   Emps with ids 2,3,5,7 never show up.
*/


public class Main {


    public static void main(String[] args) {
//        SessionFactory sessionFactory = sessionFactory_mysql();
        SessionFactory sessionFactory = sessionFactory_mssql();
        Session session = session(sessionFactory);

        Criteria depts = criteria(session);
        List<dept> list = depts.list();
        System.out.println("List result");
        for (dept d : list) {
            System.out.println("Department: id = " + d.id + "; Employees =" + d.employees);
        }

        session.clear();
        session.close();
        System.out.println("********************");
        session = session(sessionFactory);
        depts = criteria(session);

        ScrollableResults scroll = depts.scroll();
        //ScrollableResults scroll = new AggregatingScrollableResult(depts.scroll(ScrollMode.FORWARD_ONLY));
        System.out.println("Scroll result");

        while (scroll.next()) {
            dept d = (dept) scroll.get(0);
            System.out.println("Department: id = " + d.id + "; Employees =" + d.employees);
        }
        System.out.println("done");
        session.close();
/*
        System.out.println("********************");
        session = session(sessionFactory);
        depts = criteria(session);
        long count = (Long) criteria(session).setProjection(Projections.count("id")).uniqueResult();
        System.out.println("count = " + count);
        for (long i = 0; i < 7; i += 2) {

            depts.setMaxResults(2);
            depts.setFirstResult((int) i);
            for (dept d : (List<dept>) depts.list()) {
                System.out.println("Department: id = " + d.id + "; Employees =" + d.employees);
            }
        }
        session.close();*/
        sessionFactory.close();
    }

    private static SessionFactory sessionFactory_mssql() {
        return new Configuration()
                    .addAnnotatedClass(emp.class)
                    .addAnnotatedClass(dept.class)
                    .buildSessionFactory(new StandardServiceRegistryBuilder()
                            .applySetting("hibernate.connection.driver_class", "net.sourceforge.jtds.jdbc.Driver")
                            .applySetting("hibernate.connection.url", "jdbc:jtds:sqlserver://192.168.55.184/raghu")
                            .applySetting("hibernate.connection.username", "aconexsql")
                            .applySetting("hibernate.connection.password", "aconexsql")
                            .applySetting("hibernate.dialect", "org.hibernate.dialect.SQLServerDialect")
                            .applySetting("hibernate.show_sql", "true")
                            .build());

    }

    private static SessionFactory sessionFactory_mysql() {
        return new Configuration()
                    .addAnnotatedClass(emp.class)
                    .addAnnotatedClass(dept.class)
                    .buildSessionFactory(new StandardServiceRegistryBuilder()
                            .applySetting("hibernate.connection.driver_class", "com.mysql.jdbc.Driver")
                            .applySetting("hibernate.connection.url", "jdbc:mysql://localhost:3306/tmp")
                            .applySetting("hibernate.connection.username", "root")
                            .applySetting("hibernate.connection.password", "root")
                            .applySetting("hibernate.dialect", "org.hibernate.dialect.MySQLDialect")
                            .applySetting("hibernate.show_sql", "true")
                            .build());
    }

    private static Criteria criteria(Session session) {
        return session.createCriteria(dept.class)
               // .addOrder(Order.asc("id"))
                //.setFetchSize(2)
                //.setFetchMode("employees", FetchMode.JOIN)
                .setResultTransformer(Criteria.DISTINCT_ROOT_ENTITY);
    }

    private static Session session(SessionFactory sessionFactory) {
        return sessionFactory.openSession();
    }
}


class AggregatingScrollableResult implements ScrollableResults {

    private final ScrollableResults results;

    private Object prev;
    private Object curAgg;
    private final List<Object> agg;
    private int rowNum;


    AggregatingScrollableResult(ScrollableResults results) {
        this.results = results;
        prev = curAgg = null;
        rowNum = 0;
        agg = new ArrayList<Object>();

    }

    public boolean next() {
        while (results.next()) {
            Object cur = results.get(0);
            if (cur.equals(prev) || agg.isEmpty()) {
                agg.add(cur);
                prev = cur;
            } else {
                setCurAgg();
                agg.clear();
                agg.add(cur);
                prev = cur;
                return true;
            }
        }
        if (agg.isEmpty()) {
            return false;
        }
        setCurAgg();
        agg.clear();
        return true;
    }

    private void setCurAgg() {
        curAgg = Criteria.DISTINCT_ROOT_ENTITY.transformList(agg).get(0);
        rowNum++;
    }

    public boolean previous() {
        return false;
    }

    public boolean scroll(int positions) {
        return false;
    }

    public boolean last() {
        return false;
    }

    public boolean first() {
        return false;
    }

    public void beforeFirst() {
        results.beforeFirst();
    }

    public void afterLast() {
        results.afterLast();
    }

    public boolean isFirst() {
        return false;
    }

    public boolean isLast() {
        return false;
    }

    public int getRowNumber() {
        return rowNum;
    }

    public boolean setRowNumber(int rowNumber) {
        return false;
    }

    public void close() {
        results.close();
    }

    public Object[] get() {
        return new Object[]{curAgg};
    }

    public Object get(int i) {
        if (i > 0) {
            throw new IllegalArgumentException(i + " i sout of bounds");
        }
        return curAgg;
    }

    public Type getType(int i) {
        return results.getType(i);
    }

    public Integer getInteger(int col) {
        throw new RuntimeException("Not implemented");
    }

    public Long getLong(int col) {
        throw new RuntimeException("Not implemented");
    }

    public Float getFloat(int col) {
        throw new RuntimeException("Not implemented");
    }

    public Boolean getBoolean(int col) {
        throw new RuntimeException("Not implemented");
    }

    public Double getDouble(int col) {
        throw new RuntimeException("Not implemented");
    }

    public Short getShort(int col) {
        throw new RuntimeException("Not implemented");
    }

    public Byte getByte(int col) {
        throw new RuntimeException("Not implemented");
    }

    public Character getCharacter(int col) {
        throw new RuntimeException("Not implemented");
    }

    public byte[] getBinary(int col) {
        throw new RuntimeException("Not implemented");
    }

    public String getText(int col) {
        throw new RuntimeException("Not implemented");
    }

    public Blob getBlob(int col) {
        throw new RuntimeException("Not implemented");
    }

    public Clob getClob(int col) {
        throw new RuntimeException("Not implemented");
    }

    public String getString(int col) {
        throw new RuntimeException("Not implemented");
    }

    public BigDecimal getBigDecimal(int col) {
        throw new RuntimeException("Not implemented");
    }

    public BigInteger getBigInteger(int col) {
        throw new RuntimeException("Not implemented");
    }

    public Date getDate(int col) {
        throw new RuntimeException("Not implemented");
    }

    public Locale getLocale(int col) {
        throw new RuntimeException("Not implemented");
    }

    public Calendar getCalendar(int col) {
        throw new RuntimeException("Not implemented");
    }

    public TimeZone getTimeZone(int col) {
        throw new RuntimeException("Not implemented");
    }
}