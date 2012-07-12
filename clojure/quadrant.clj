(use '[clojure.string :only (split)])
(use '[clojure.test :only (deftest is run-tests use-fixtures testing)])

(def point [:x :y])
(def command [:command :from :to])

(defn parse [input keys] 
      (let [inputs (map read-string (split input #"\s"))]
      	   (zipmap keys inputs)))

(defn accept-input [format]
      (let [n (read-string (read-line))]	
      	    (doall (repeatedly n #(parse (read-line) format)))))

(defn- last-ones [coll from to]
       (take-last (inc (- to from)) coll))

(defn count-quadrants [points from to]
      (defn identify-quadrant [point]
      	    (if (> (:x point) 0) 
	    	(if (> (:y point) 0) [1 0 0 0] [0 0 0 1]) (if (> (:y point) 0) [0 1 0 0] [0 0 1 0])))
      
      (apply map + (map identify-quadrant (last-ones (take to points) from to))))



(defn reflect [points from to axis]
      (let [till-to (take to points) the-rest (drop to points)]      	   
           (concat (take (- from 1) till-to) 
      	    	    (map #(update-in % [axis] -) (last-ones  till-to from to)) 
	    	    the-rest)))


(defmulti process :command)
(defmethod process 'C [command points]
	   (apply prn (count-quadrants points (:from command) (:to command)))
	   points)
(defmethod process 'X [command points]
	   (reflect points (:from command) (:to command) :y))

(defmethod process 'Y [command points]
	   (reflect points (:from command) (:to command) :x))	   


(defn main []
(let [points (accept-input point)
      commands (accept-input command)]
      ;(subvec points 1 3)))
      (reduce #(process %2 %1) points commands)))


(main)

;;Tests;;
(deftest should-parse-points  (is (= {:x 1 :y 3} (parse "1 3" point))))
(deftest should-parse-commands  (is (= {:command 'C :from 1 :to 4} (parse "C 1 4" command))))
(deftest should-count-quadrants (is (= [1 1 1 1] (count-quadrants [{:x 1 :y 1} {:x -1 :y 1} {:x -1 :y -1} {:x 1 :y -1}] 1 4))))
(deftest should-count-quadrants-range (is (= [1 0 0 0] (count-quadrants [{:x 1 :y 1} {:x -1 :y 1} {:x -1 :y -1} {:x 1 :y -1}] 1 1))))
(deftest should-reflect
	 (let [points [{:x 1 :y 1} {:x 2 :y 2} {:x -2 :y -2} {:x 3 :y 3} {:x 1 :y 1} {:x 2 :y 3}]]
	      (testing "should reflect over x"  
	      	        (is (= [{:x 1 :y -1} {:x 2 :y -2} {:x -2 :y 2} {:x 3 :y -3} {:x 1 :y -1} {:x 2 :y -3}] (reflect points 1 6 :y))))
	      (testing "should reflect over y for specified indices"  
	      	        (is (= [{:x 1 :y 1} {:x -2 :y 2} {:x 2 :y -2} {:x -3 :y 3} {:x 1 :y 1} {:x 2 :y 3}] (reflect points 2 4 :x))))))


(run-tests)

(comment

4
1 1
-1 1
-1 -1
1 -1
5
C 1 4
X 2 4
C 3 4
Y 1 2
C 1 3
)