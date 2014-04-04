import org.hibernate.*;
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

    @OneToMany(mappedBy = "dept", fetch = FetchType.LAZY)
    public List<emp> employees;

/*
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
*/
}

public class Main {


    public static void main(String[] args) {
        SessionFactory sessionFactory = new Configuration().addAnnotatedClass(emp.class).addAnnotatedClass(dept.class)
                .setProperty("hibernate.connection.driver_class", "com.mysql.jdbc.Driver")
                .setProperty("hibernate.connection.url", "jdbc:mysql://localhost:3306/tmp")
                .setProperty("hibernate.connection.username", "root")
                .setProperty("hibernate.connection.password", "root")
                .setProperty("hibernate.dialect", "org.hibernate.dialect.MySQLDialect")
                .setProperty("hibernate.show_sql", "true")
                .buildSessionFactory();
        Session session = session(sessionFactory);

        Criteria depts = criteria(session);
        List<dept> list = depts.list();
        //List<dept> list = DistinctRootEntityResultTransformer.INSTANCE.transformList(depts.list());
        System.out.println("list.size() = " + list.size());
        for (dept d : list) {
            System.out.println("d.employees = " + d.employees);
        }

        System.out.println("closing");
        session.clear();
        session.close();
        System.out.println("********************");

        session = session(sessionFactory);
        depts = criteria(session);

        ScrollableResults scroll = depts.scroll();
        //ScrollableResults scroll = new AggregatingScrollableResult(depts.scroll(ScrollMode.FORWARD_ONLY));

        while (scroll.next()) {
            dept d = (dept) scroll.get(0);
            System.out.println("d.employees = " + d.employees);
        }
        System.out.println("done");
        session.close();
/*

        session = session(sessionFactory);
        depts = session.createCriteria(dept.class)
                .add()
                .setResultTransformer(Criteria.ROOT_ENTITY);
*/

        sessionFactory.close();
    }

    private static Criteria criteria(Session session) {
        return session.createCriteria(dept.class)
                .addOrder(Order.asc("id"))
                //.setFetchSize(2)
                .setFetchMode("employees", FetchMode.JOIN)
                //.setResultTransformer(Criteria.DISTINCT_ROOT_ENTITY)
                //.setResultTransformer(Criteria.ROOT_ENTITY)
                ;
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
                prev=cur;
            } else {
                setCurAgg();
                agg.clear();
                agg.add(cur);
                prev=cur;
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
        if (i > 0){
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